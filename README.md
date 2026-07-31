# tanmaygambhir37-design.github.io

Personal website. Everything below can be done directly on github.com (press `.` or just click a file → pencil icon) — no local setup needed.

## How to update things

| What | How |
|---|---|
| **Substack article** | Nothing. `.github/workflows/substack.yml` refreshes `posts.json` every morning and the newest three posts appear on the site. To publish one immediately, run the workflow by hand from the Actions tab. |
| **Project card** | Edit the `PROJECTS` array near the top of the `<script>` block in `index.html`. Each entry takes `badge`, `title`, `desc`, `tags`, and `links`; set `featured: true` to give it the wide card. |
| **CV** | Replace `cv.pdf` with the new version (same filename). |
| **Investment memo** | Edit `memos.json`: set the entry's `"live": true` and point `"file"` at the page or PDF. A hosted write-up is a path like `investment-research/dust/`; a PDF goes in the `memos/` folder and is referenced as `memos/your-file.pdf`. |
| **Link preview image** | Replace `og-image.png` (1200 × 630). This is what LinkedIn and WhatsApp show when the site is shared. |
| **Text/sections** | Edit `index.html` — experience, about, and skills are plain HTML near the top of `<body>`. |

Changes go live ~1 minute after committing.

## What updates itself

- **`posts.json`** — written daily by `.github/scripts/fetch_substack.py`, run from GitHub Actions. The page reads it from this origin, so the Substack section renders with the page rather than waiting on a third-party CORS proxy. If the file is missing or empty, the section falls back to a single link to the Substack.
- **`memos.json`** — read by the page at load; edit it directly, no build step.

Project cards do **not** update themselves. They were a live GitHub API listing once; that was replaced with the hand-written `PROJECTS` array so each card says what the work actually is.
