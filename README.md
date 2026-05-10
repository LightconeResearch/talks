# talks

Slides for presentations from Lightcone Research.

## Layout

```
.
├── theme/                      brand-level theme assets (shared across talks)
│   ├── lightcone.css           Reveal.js theme
│   ├── Primary Logo.svg        wordmark — title slides + corner brand mark
│   ├── Secondary Logo_Gold.svg square mark — section dividers
│   ├── Secondary Logo_Blue.svg square mark — closing / "over to X" slides
│   └── mt-corcoran.jpg         Bierstadt painting — default title backdrop
├── assets/                     per-talk assets — plots, screenshots, data
├── template.html               starter file — copy this for each new talk
└── README.md
```

## Starting a new talk

```sh
cp template.html my-talk.html
```

Then edit:

- The `<title>` in `<head>`
- The title slide (eyebrow, hero title, subtitle, date)
- The body sections (each `<section>` is one slide)

Reference any plots/images you need from `assets/` (e.g.
`<img src="assets/my-plot.png">`). Don't put per-talk assets in `theme/` —
that folder is reserved for brand-level material shared across decks.

The cheat-sheet comment block at the top of `template.html` lists the
available colour tokens, font tokens, and reusable classes
(`.card-glow`, `.section-label`, `.hero-title`, `.pill`, etc).

## Local preview

```sh
python3 -m http.server 8000
# then open http://localhost:8000/my-talk.html
```

A static server is required so that the asset paths resolve (Reveal won't
load `data-background-image` over `file://`).
