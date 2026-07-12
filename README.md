# tanmaygambhir37-design.github.io

Personal website. Everything below can be done directly on github.com (press `.` or just click a file → pencil icon) — no local setup needed.

## How to update things

| What | How |
|---|---|
| **Substack article** | Nothing. Publishes automatically — the site pulls your latest 3 posts from the Substack feed. |
| **GitHub project** | Nothing. Any public repo with a description shows up automatically. Add a description + topics to the repo for a nicer card. |
| **CV** | Replace `cv.pdf` with the new version (same filename). |
| **Investment memo** | 1) Upload the PDF to the `memos/` folder. 2) Edit `memos.json`: set the entry's `"live": true` and `"file": "memos/your-file.pdf"`, or add a new entry. |
| **Text/sections** | Edit `index.html` — experience, about, skills are plain HTML near the top of `<body>`. |

Changes go live ~1 minute after committing.
