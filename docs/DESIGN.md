# Design System: BigHammer.ai Databricks Masterclass

Written from the live page (https://amal200496.github.io/bighammer-masterclass/) in the Stitch DESIGN.md format. Brand constraints from the client override the skill's defaults where they conflict; those conflicts are listed in section 8.

## 1. Visual Theme & Atmosphere
A confident, color-blocked event page. Hard-edged, square-cornered surfaces in brand purple, ink and lime, with a single acid-green and yellow accent used for numbers and buttons. Asymmetric split hero (copy left, registration card right), long scroll with one pinned, scroll-driven centerpiece (the framework). Reads like an invoice being audited: meters, ledgers, scans and ticks instead of illustration.
Dials: Variance 7 (offset, asymmetric splits), Motion 7 (fluid CSS plus one scroll-pinned sequence), Density 4 (daily-app balanced, generous section gaps).

## 2. Color Palette & Roles
- **Signal Purple** (#5600EF): hero and framework backgrounds, host portrait offset shadow, links on light.
- **Deep Purple** (#3D00A8): inactive step nodes, depth behind purple surfaces.
- **Ink** (#0D0D14): header, proof strip, case study, team section, footer, dark panels. Never pure black.
- **Off-White Field** (#F2F4FA) and **Mist** (#E9ECF6): light section fills, form inputs, hover fills.
- **Pure Surface** (#FFFFFF): registration card, light sections.
- **Acid Green** (#00FF89): numbers on ink, offset shadows, progress, success.
- **Highlighter Yellow** (#FCFF00): primary button fill (ink text), active step, migration lanes.
- **Alarm Pink** (#FE0079): the problem color (costs, waste, "Seats are limited" tag). Error text uses #B00057 for contrast.
- **Lime** (#B7FF6E): "What you get" band, bonus callout, highlighter under the quote.
- Text: Ink #1C1C1C on light, white at 90% / 75% on dark, Grey #5E5E66 for fine print.

## 3. Typography Rules
- **Display:** Epilogue 700-800, tight tracking (-0.025em to -0.04em), sizes via clamp (hero 40-64px), balanced wrapping.
- **Body:** Poppins 400-600, 16px base, line-height 1.6, 40em maximum on leads.
- **Numbers:** tabular figures on every counter, chart value and countdown.
- **Labels:** one deliberate uppercase kicker in the hero only; everywhere else sentence case.

## 4. Component Stylings
- **Buttons:** square, yellow fill, ink uppercase label. Hover lifts with a hard ink (or green on dark) offset shadow; active presses down 1px with slight scale. Loading state is three pulsing squares.
- **Registration card:** white, square, hard green offset shadow that grows in on load. Two fields only, fine print, bonus callout, one short quote.
- **Inputs:** label above, error below, field-fill background, 3px purple focus ring.
- **Panels:** ink panels with a hard green offset shadow (framework visuals), square corners everywhere.
- **Portraits:** both hosts share one 4:5 frame, grayscale, white background, purple offset shadow, purple duotone on hover.

## 5. Layout Principles
Container 1200px plus fluid gutter. Hero is a two-column grid with named areas (copy, form, hosts) so the form moves above the hosts on mobile. Section layout families vary: split hero, strip, full-width quote, bento-style quote wall, ledger rows, ruled list, pinned two-column stage, timeline plus card, split portraits, marquee. Single column below 900px; framework becomes a swipeable carousel.

## 6. Motion & Interaction
Exponential ease-out (cubic-bezier .16,1,.3,1) throughout. One shared scroll loop drives the progress line, parallax and the pinned framework. Entrances only for content that starts below the fold, and content is visible without JavaScript. Count-ups on figures, digit roll on the countdown, clip-path reveals on portraits, one marquee. Everything collapses to the final state under reduced motion.

## 7. Anti-Patterns (Banned)
No em or en dashes. No emojis. No scroll cues. No pure black. No gradient text. No neon glows. No side-stripe borders. No second marquee. No fake client names or invented numbers (all figures come from the client deck or site).

## 8. Known conflicts with the Stitch skill defaults (client brand wins)
- Purple is the brand color (skill bans purple). Kept, used as flat fills, no glows.
- Five brand accents instead of one. Kept, but each has one job (see section 2).
- Epilogue and Poppins are the client's fonts (skill prefers Geist, Outfit, Satoshi). Kept.
- Square corners everywhere (skill examples use generous rounding). Kept: it is the brand shape rule.
