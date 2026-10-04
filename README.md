# NeXtGen Medical website

A responsive static website for NeXtGen Medical built with plain HTML, CSS, and JavaScript. No framework or package installation is required.

## Preview locally

Open `index.html` in a browser, or serve this directory with any static web server.

## Pages

- `index.html` — homepage, provider information, pricing, FAQs, public Google reviews, and location
- `services.html` — categorized service overview
- `about.html` — provider background, credentials, and practice approach
- `contact.html` — Lake Wylie address, hours, phone, map, directions, and booking
- `faq.html` — dedicated answers about appointments, services, labs, payment, and office location
- `services/` — individual pages for weight management, hormone care, peptide therapy, vitamins, regenerative medicine, rheumatology, and lab services
- `sitemap.xml` and `robots.txt` — search engine discovery and crawl guidance
- `.github/workflows/deploy-pages.yml` — publishes the static site to GitHub Pages on each push to `main`
- The homepage includes the local business structured data and embedded Google Map; appointment links point to the practice's existing online scheduler.
- The supplied NeXtGen logo is used throughout the site, with the blue/aqua theme sampled from its artwork. The homepage hero uses a locally relevant Lake Wylie lakeside photo by Karolina Bobek via Unsplash, credited and linked on the page.
- `styles.min.css` and `script.min.js` — production assets generated from the readable sources with `python scripts/minify_assets.py`

Regenerate the minified assets after editing `styles.css` or `script.js`.

## Before launch

- Confirm that the online booking link, published fees, services, and clinic details are still current.
- Confirm `https://www.nextgenmedicalllc.com/` is the preferred public domain; canonical URLs, social metadata, and the sitemap use it.
- Replace the blank homepage hero placeholder with approved NeXtGen Medical photography if desired.
- Add patient review excerpts only after the practice confirms permission and attribution; the homepage links to public Google reviews until approved excerpts are supplied.
- The GitHub Pages preview is separate from the Wix production domain `www.nextgenmedicalllc.com`.
