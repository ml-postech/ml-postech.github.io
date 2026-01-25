# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static GitHub Pages website for the Machine Learning Lab (MLLab) at POSTECH. It uses a single-page application pattern with jQuery-based tab navigation.

- **Live site**: ml.postech.ac.kr
- **Stack**: HTML5, CSS3, vanilla JavaScript, Bootstrap 3.4.0, jQuery 3.2.1

## Development

**No build system required.** This is a pure static site.

To test locally, open `index.html` directly in a browser. All dependencies load from CDNs or local files.

## Architecture

### Tab-Based SPA Pattern

`index.html` serves as the main container and loads content dynamically:
```javascript
$("#home").load("home.html");
$("#people").load("people.html");
// etc.
```

Hash-based routing (`/#home`, `/#people`, `/#publication`, `/#contact`, `/#research_participate`) triggers Bootstrap tab switching.

### Key Files

| File | Purpose |
|------|---------|
| `index.html` | SPA container, navigation, tab loading logic |
| `home.html` | News and announcements |
| `people.html` | Faculty and student directory |
| `pub.html` | Publication browser (uses bibtex-js) |
| `pub.bib` | BibTeX bibliography database |
| `contact.html` | Location and contact info |
| `research_participate.html` | Undergraduate research opportunities |
| `static/mlpostech.css` | Custom styling |
| `scripts/bibtex_js.js` | Local bibtex-js fallback |

### Publications System

Publications are stored in `pub.bib` as BibTeX entries. The `bibtex-js` library parses and renders them client-side in `pub.html`. Conference abbreviations are defined as `@STRING` at the top of `pub.bib`.

## Common Tasks

**Add news**: Edit `home.html`, update the news section (look for badge elements with dates)

**Add/update people**: Edit `people.html`. Profile images go in `/img/` directory

**Add publications**: Add BibTeX entries to `pub.bib`. Use existing `@STRING` definitions for conference names

**Update styling**: Modify `/static/mlpostech.css`. Primary accent color is `#ebb810` (gold)

## Deployment

Push to GitHub triggers automatic GitHub Pages deployment. The `CNAME` file configures the custom domain.
