# BigHammer Databricks masterclass landing page: project report

Live page: https://amal200496.github.io/bighammer-masterclass/
Event: Thursday, October 15, 2026, 12:00 PM ET. Free, seats limited.

## What was built
- Copy rewritten from the Masterclass V3 deck and bighammer.ai: short, plain, no filler, no em or en dashes.
- Design in BigHammer brand colours, fonts and square corners, with the concept "the bill, audited" (meters, ledgers, scans, ticks).
- Srinath Reddy leads as host, Richard Lawrence joins. Both portraits share one 4:5 frame and size.
- New expertise section: "Tools show the bill. Experience explains it."
- Real proof only: healthcare case ($3M+ avoided, >400% ROI, $2.74M / $315K / $308K), Anushka (SBC Labs) quote, Privacy and Terms links.
- Scroll-driven motion: pinned Assess / Migrate / Monitor framework, count-ups, countdown roll, per-pattern graphics, one marquee. Content is visible without JavaScript and respects reduced motion.
- Removed: FAQ, Srinath's email, repeated URL and logo.

## Conversion work
- Signup reduced to name and email. Company, role and phone are an optional step after signup.
- Calendar buttons (Google, .ics), visitor's own-timezone time, event tracking hooks and UTM capture.
- Phone order: headline, lead, one-line date, form, then hosts. Form and Save button fit on the first phone screen.
- "What you get" moved up. Spring easing, no overlaps, no equal three-column rows (Stitch audit).

## Conversion simulation (friction model, not a forecast)
- 100 simulated visitors across 9 types, checked against measured page geometry at 375x812 and 1280x720.
- Visitor mix and patience are assumptions. Page measurements are real.
- Before: 36 of 100 visitors hit friction (22 could not register without scrolling on phones, 6 could not see their own timezone early, 8 found no named customers).
- After: 8 of 100, all of them skeptics wanting named customers.
- Run it: `py simulation/sim.py simulation/facts_before.json` and `facts_after.json`.
- Limit: no real traffic or baseline rate exists, so this finds friction and does not predict sign-up rates.

## Open items
- Connect the form to the lead tool (set FORM_ENDPOINT in the page script).
- Add an analytics ID so form views, starts and submits are recorded.
- Client logos or a second named quote.
- Higher-resolution photo of Srinath.
- BigHammer to confirm: "agents run on a context engine built around that domain knowledge".
