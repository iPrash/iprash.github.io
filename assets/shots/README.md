# assets/shots

Screenshots for the project cards on the landing page.

Name each file after the project's `slug` in `_build/projects.json`, lowercase or uppercase
exactly as the slug is written there:

    assets/shots/FIFA26.png

The build checks for the file at build time. When it exists the card shows it; when it does
not, the card falls back to a generated tile built from the project's `glyph` and `accent`.
Either way the page renders complete, so a missing screenshot is never a broken card.

Roughly 16:10 suits the card frame. About 1200px wide is plenty, and anything much larger is
wasted bytes on a page that is otherwise a few kilobytes. PNG or JPG both work; the card is
`object-fit: cover` anchored to the top of the image, so put the interesting part up there.

Run `python _build\build.py --landing` after adding one.

This README exists so the folder is tracked by git. Git does not track empty directories.
