/* Frontier Engineer → Principal — shared behaviour
   Copied from the aigov site engine and adapted: storage keys renamed to this site's own
   "fe." namespace (each site's assets are independent, but localStorage is shared across
   the whole iprash.github.io origin, so key names must not collide between sites), and the
   aigov-specific renewal calculator removed since this site doesn't have one. Everything
   else (theme, TOC, read-tracking, checklist items, scroll-spy) is the same engine. */
(function () {
  'use strict';

  /* ---------- theme ---------- */
  var KEY_THEME = 'fe.theme';
  var root = document.documentElement;
  function applyTheme(t) {
    root.setAttribute('data-theme', t);
    var b = document.getElementById('themeBtn');
    if (b) {
      b.textContent = t === 'dark' ? '☀' : '☾';
      b.setAttribute('aria-label', t === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    }
  }
  var saved = null;
  try { saved = localStorage.getItem(KEY_THEME); } catch (e) {}
  applyTheme(saved || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
  document.addEventListener('click', function (e) {
    if (!e.target.closest || !e.target.closest('#themeBtn')) return;
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    try { localStorage.setItem(KEY_THEME, next); } catch (err) {}
  });

  /* ---------- store helpers ---------- */
  function load(key) {
    try { return JSON.parse(localStorage.getItem(key) || '{}'); } catch (e) { return {}; }
  }
  function save(key, obj) {
    try { localStorage.setItem(key, JSON.stringify(obj)); } catch (e) {}
  }

  /* ---------- back to top ---------- */
  var top = document.querySelector('.totop');
  if (top) {
    window.addEventListener('scroll', function () {
      top.classList.toggle('show', window.scrollY > 700);
    }, { passive: true });
    top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }

  /* ---------- document pages: TOC + read tracking ---------- */
  var doc = document.querySelector('.doc');
  var docId = doc && doc.dataset.doc;
  if (doc && docId) {
    var KEY_READ = 'fe.read.' + docId;
    var read = load(KEY_READ);
    var tocEl = document.getElementById('toc');
    var heads = Array.prototype.slice.call(doc.querySelectorAll('h1[id]:not(.doctitle), h2[id], h3[id]'));

    /* build TOC */
    if (tocEl) {
      var frag = document.createDocumentFragment();
      heads.forEach(function (h) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent.replace(/\s*—\s*/g, ' — ');
        a.dataset.target = h.id;
        if (h.tagName === 'H3') a.className = 'lvl3';
        if (h.tagName === 'H1') a.className = 'lvl1';
        li.appendChild(a);
        frag.appendChild(li);
      });
      tocEl.appendChild(frag);
    }

    /* mark-read buttons on every part and section heading */
    var h2s = heads.filter(function (h) { return h.tagName === 'H1' || h.tagName === 'H2'; });
    h2s.forEach(function (h) {
      var row = document.createElement('div');
      row.className = h.tagName === 'H1' ? 'h2row h1row' : 'h2row';
      h.parentNode.insertBefore(row, h);
      row.appendChild(h);
      var btn = document.createElement('button');
      btn.className = 'markread';
      btn.type = 'button';
      btn.dataset.section = h.id;
      btn.innerHTML = '<span class="box"></span><span class="lbl">Mark read</span>';
      btn.setAttribute('aria-pressed', read[h.id] ? 'true' : 'false');
      if (read[h.id]) btn.querySelector('.lbl').textContent = 'Read';
      btn.addEventListener('click', function () {
        var on = btn.getAttribute('aria-pressed') === 'true';
        btn.setAttribute('aria-pressed', on ? 'false' : 'true');
        btn.querySelector('.lbl').textContent = on ? 'Mark read' : 'Read';
        if (on) { delete read[h.id]; } else { read[h.id] = 1; }
        save(KEY_READ, read);
        paint();
      });
      row.appendChild(btn);
    });

    function paint() {
      var done = h2s.filter(function (h) { return read[h.id]; }).length;
      var pct = h2s.length ? Math.round((done / h2s.length) * 100) : 0;
      var n = document.getElementById('progNum');
      var b = document.getElementById('progBar');
      if (n) n.textContent = done + ' / ' + h2s.length;
      if (b) b.style.width = pct + '%';
      var p = document.getElementById('progPct');
      if (p) p.textContent = pct + '%';
      if (tocEl) {
        Array.prototype.forEach.call(tocEl.querySelectorAll('a'), function (a) {
          a.classList.toggle('read', !!read[a.dataset.target]);
        });
      }
      try { localStorage.setItem('fe.pct.' + docId, String(pct)); } catch (e) {}
    }
    paint();

    var resetBtn = document.getElementById('resetProg');
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        if (!confirm('Clear reading progress for this document?')) return;
        read = {};
        save(KEY_READ, read);
        Array.prototype.forEach.call(doc.querySelectorAll('.markread'), function (b) {
          b.setAttribute('aria-pressed', 'false');
          b.querySelector('.lbl').textContent = 'Mark read';
        });
        paint();
      });
    }

    /* TOC filter */
    var search = document.getElementById('tocSearch');
    if (search && tocEl) {
      search.addEventListener('input', function () {
        var q = search.value.trim().toLowerCase();
        Array.prototype.forEach.call(tocEl.querySelectorAll('a'), function (a) {
          a.parentNode.classList.toggle('hidden', q && a.textContent.toLowerCase().indexOf(q) === -1);
        });
      });
    }

    /* scroll spy */
    if (tocEl && 'IntersectionObserver' in window) {
      var links = {};
      Array.prototype.forEach.call(tocEl.querySelectorAll('a'), function (a) { links[a.dataset.target] = a; });
      var current = null;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          var a = links[en.target.id];
          if (!a || a === current) return;
          if (current) current.classList.remove('active');
          a.classList.add('active');
          current = a;
          var box = tocEl.getBoundingClientRect();
          var lb = a.getBoundingClientRect();
          if (lb.top < box.top || lb.bottom > box.bottom) {
            tocEl.scrollTop += lb.top - box.top - box.height / 2;
          }
        });
      }, { rootMargin: '-80px 0px -72% 0px' });
      heads.forEach(function (h) { io.observe(h); });
    }

    /* checklist items rendered from "- [ ]" markdown */
    var KEY_CHK = 'fe.chk.' + docId;
    var chk = load(KEY_CHK);
    Array.prototype.forEach.call(doc.querySelectorAll('li'), function (li) {
      var t = li.textContent || '';
      if (!/^\s*\[[ xX]\]/.test(t)) return;
      var id = 'c' + Math.abs(hash(t.slice(0, 90)));
      var label = li.innerHTML.replace(/^\s*\[[ xX]\]\s*/, '');
      li.className = 'checkitem';
      li.innerHTML = '<input type="checkbox" id="' + id + '"><span>' + label + '</span>';
      var input = li.querySelector('input');
      input.checked = !!chk[id];
      li.classList.toggle('done', input.checked);
      input.addEventListener('change', function () {
        if (input.checked) { chk[id] = 1; } else { delete chk[id]; }
        li.classList.toggle('done', input.checked);
        save(KEY_CHK, chk);
      });
    });
  }

  function hash(s) {
    var h = 0, i;
    for (i = 0; i < s.length; i++) { h = ((h << 5) - h + s.charCodeAt(i)) | 0; }
    return h;
  }

  /* ---------- index page: progress readouts on the document cards ---------- */
  ['roadmap', 'resources'].forEach(function (id) {
    var el = document.getElementById('pct-' + id);
    if (!el) return;
    var v = null;
    try { v = localStorage.getItem('fe.pct.' + id); } catch (e) {}
    el.textContent = (v ? v : '0') + '% read';
  });
})();
