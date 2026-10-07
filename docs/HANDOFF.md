# Handoff: go-live build (co-host refresh)

This commit is the go-live version of the masterclass page. One file, `index.html`, fully self-contained (images are embedded).

## What changed in this commit
- New host portraits for Srinath Reddy and Richard Lawrence. Both are black and white on white, 4:5, 800x1000, with the same face size and eye line, so they read as a matched pair.
  - Srinath: re-cut from the original BigHammer studio photo (higher resolution than the old crop).
  - Richard: from his Kie.ai avatar set (half-body studio pose), background removed and toned to match.
- The images live in two CSS variables, `--photo-s` and `--photo-r`. They feed both places portraits appear: the hero host strip and the "Your hosts" section.
- Both people are now presented as co-hosts: "Host" label on both, "Your hosts" heading, the "Joined by" tag removed, same size and position for both cards, designations shown under each name.
- Hero lead line and social description now name both hosts.

## Second pass (polish and content)
- Richard's portrait replaced with a new Kie.ai pose from his avatar set: light closed-mouth smile, black blazer and tee on white, matching Srinath's photo.
- Both host cards now have three pointers under the designation (Richard's quote removed so the cards match). Richard's pointers are role-level; confirm the wording with him.
- "What you get" rebuilt from the masterclass deck: four modules with detail (business problems, six waste patterns, healthcare teardown numbers, assess/migrate/monitor), the live Q&A, and the two ways to run the free assessment.
- Free bonus under the form is a highlighted card; the form testimonial now has Anushka's photo (from bighammer.ai) in a small circle.
- Removed: footer (privacy and terms links), the recording promise under the button and in the final CTA, the scan line that crossed the workload labels.
- Fixes found in the visual pass: headline no longer shows "0%" while counting, proof numbers share one size, mobile proof strip no longer overflows, "Re-assess" label no longer clipped, pattern 05 graphic ends on the tiny-files grid, host cards line up.

## Still to do before going live
1. **CRM / lead form.** Search `index.html` for `FORM_ENDPOINT` (near the bottom script). It is `null`, so nothing is sent yet. Set it to the CRM form or webhook URL. Each submit POSTs JSON with the signup fields plus UTM and timezone data.
2. **Hosting.** Upload `index.html` as the site root on the live domain. Consider adding `og:url`, `og:image` and a `canonical` link in the `<head>` once the final URL is known (none are set yet).
3. Submit a test signup and confirm it lands in the CRM.
