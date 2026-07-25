# MIC NSW — Ready to Publish

This folder is a complete, self-contained static website. Upload it as-is.

## What's inside
```
index.html                    → Homepage (all sections + Packages)
build-your-renovation.html    → Kitchen & Bathroom Design Studio (configurator)
sitemap.xml                   → Submit this to Google Search Console
robots.txt                    → Already configured to allow indexing
```

## How to publish (pick one)

**Option A — Your existing hosting (cPanel / FTP / SiteGround etc.)**
1. Connect via FTP or the File Manager.
2. Go to `public_html/` (the web root).
3. Upload all 4 files from this folder directly into `public_html/` — keep them together, don't put them in a subfolder, so the links between the two pages keep working.
4. Visit `https://mic-nsw.com.au/` to confirm it loads, then click every nav link and the "Design Yours" button to confirm both pages connect correctly.

**Option B — Netlify / Vercel (drag-and-drop, free, fastest)**
1. Go to netlify.com (or vercel.com) → "Add new site" → "Deploy manually".
2. Drag this whole folder into the upload box.
3. It goes live instantly on a temporary URL — then connect your `mic-nsw.com.au` domain in the site settings (DNS instructions provided by whichever host you choose).

**Option C — Replacing the current WordPress site**
If MIC NSW currently runs on WordPress and you want to fully replace it with this static site, you'll need to either point the domain's DNS at a static host (Option B) instead of the WordPress hosting, or ask your host to serve these files as the site root instead of WordPress. This is a bigger step — happy to walk through it if that's the direction you take.

## Before you go live — final checklist
- [ ] Confirm the phone, email, licence (393630C) and ABN shown are current
- [ ] Confirm real package pricing with MIC NSW (current prices are estimates)
- [ ] Confirm which supplier brands MIC NSW can actually source (shown as examples)
- [ ] Connect the contact form to a real inbox — right now it only shows an on-screen "message sent" confirmation and does not actually email anyone. The easiest fix is a free form backend like Formspree or Web3Forms: sign up, get an endpoint URL, and change the `<form id="contactForm">` action to POST there instead of the current JavaScript-only handler.
- [ ] Submit `sitemap.xml` in Google Search Console once live
- [ ] Connect Google Analytics if you want visitor tracking
- [ ] Test on an actual phone, not just browser resize
- [ ] Consider self-hosting the logo image instead of linking to the old site, in case that gets taken down later
