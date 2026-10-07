# Handoff: go-live build (co-host refresh)

This commit is the go-live version of the masterclass page. One file, `index.html`, fully self-contained (images are embedded).

## What changed in this commit
- New host portraits for Srinath Reddy and Richard Lawrence. Both are black and white on white, 4:5, 800x1000, with the same face size and eye line, so they read as a matched pair.
  - Srinath: re-cut from the original BigHammer studio photo (higher resolution than the old crop).
  - Richard: from his Kie.ai avatar set (half-body studio pose), background removed and toned to match.
- The images live in two CSS variables, `--photo-s` and `--photo-r`. They feed both places portraits appear: the hero host strip and the "Your hosts" section.
- Both people are now presented as co-hosts: "Host" label on both, "Your hosts" heading, the "Joined by" tag removed, same size and position for both cards, designations shown under each name.
- Hero lead line and social description now name both hosts.

## Still to do before going live
1. **CRM / lead form.** Search `index.html` for `FORM_ENDPOINT` (near the bottom script). It is `null`, so nothing is sent yet. Set it to the CRM form or webhook URL. Each submit POSTs JSON with the signup fields plus UTM and timezone data.
2. **Hosting.** Upload `index.html` as the site root on the live domain. Consider adding `og:url`, `og:image` and a `canonical` link in the `<head>` once the final URL is known (none are set yet).
3. Submit a test signup and confirm it lands in the CRM.
