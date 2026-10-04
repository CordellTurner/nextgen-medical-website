# NeXtGen Medical website

A responsive static website for NeXtGen Medical built with plain HTML, CSS, and JavaScript. No framework or package installation is required.

## Preview locally

Open `index.html` in a browser, or serve this directory with any static web server.

## Pages

- `index.html` — homepage, provider information, pricing, FAQs, patient review, and location
- `services.html` — categorized service overview
- `services/` — individual pages for weight management, hormone care, peptide therapy, vitamins, regenerative medicine, rheumatology, and lab services
- `sitemap.xml` and `robots.txt` — search engine discovery and crawl guidance
- The homepage includes the local business structured data and embedded Google Map; appointment links point to the practice's existing online scheduler.
- `styles.min.css` and `script.min.js` — production assets generated from the readable sources with `python scripts/minify_assets.py`

Regenerate the minified assets after editing `styles.css` or `script.js`.

## Before launch

- Confirm that the online booking link, published fees, services, and clinic details are still current.
- Confirm `https://www.nextgenmedicalllc.com/` is the preferred public domain; canonical URLs, social metadata, and the sitemap use it.
- Replace the sample Unsplash clinic photo with approved NeXtGen Medical photography if available.
- Add patient review excerpts only after the practice confirms permission and attribution; the homepage links to public Google reviews until approved excerpts are supplied.
- Deploy the files to the hosting provider configured for `www.nextgenmedicalllc.com`.
