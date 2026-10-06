# BigHammer Masterclass: Motion & Visual Design Spec (v3)

Build target for the next pass. Everything here is vanilla HTML/CSS/JS on top of the current page. No new libraries.

**Source of truth**
- Current page source (artifact form, no doctype): `scratchpad/template5.html`
- Outputs written on every build:
  - `scratchpad/bighammer-masterclass.html` (publish as the artifact, same file path keeps the same URL)
  - `GC TASK/bighammer-landing.html` (standalone, doctype wrapper added)
  - `scratchpad/gh/index.html` (commit and push to `amal200496/bighammer-masterclass`, GitHub Pages)
- Copy rules: no em dashes or en dashes anywhere, short plain sentences, no new marketing filler. Do not change copy except where this spec gives new copy.

---

## 1. Concept: "The bill, audited"

The page reads like a Databricks invoice being taken apart line by line. Every visual device comes from that world: meters, line items, gauges, scans, checkmarks, a running cost counter. No decorative blobs or generic illustrations.

**One bold moment:** the pinned framework section. Everything else is restrained: short reveals, count-ups, small data graphics. If something competes with the framework for attention, tone it down.

---

## 2. Motion system (build this first)

### Tokens (add to `:root`)
```
--ease-out: cubic-bezier(.16,1,.3,1);   /* already exists */
--ease-in-out: cubic-bezier(.65,0,.35,1);
--t-fast: 180ms;  --t-med: 480ms;  --t-slow: 800ms;
--stagger: 70ms;
```

### Shared JS utilities (one script block, top of the IIFE)
1. **`onEnter(el, fn, {threshold, once})`**: one shared IntersectionObserver. Calls `fn(el)` once when the element enters.
2. **`countUp(el)`**: reads `data-count-to`, `data-prefix`, `data-suffix`, `data-decimals`. Animates from 0 over 1100ms with ease-out cubic. Final text must equal the original static text exactly, so the no-JS state is correct.
3. **`scrollLoop`**: a single `requestAnimationFrame` loop driven by a passive scroll listener (already exists for the framework). Extend it to also drive the header progress bar and the host parallax. One loop only.
4. **`motionOK`**: `matchMedia('(prefers-reduced-motion: no-preference)')`. Every effect below checks it. With reduced motion, everything renders in its final state with no animation.

### Rules
- **Visible at rest.** Content is fully visible without JS. JS only adds a pending class to elements *below the fold at load*, then animates them in. Never leave content at `opacity:0` waiting for an observer.
- Animate only `transform`, `opacity`, `clip-path`, `stroke-dashoffset` and `background-size`. Never animate width, height, top or left (the existing `.scan` uses `left`: switch it to `transform: translateX()` against a wrapper of known width).
- Each section gets one entrance treatment that fits its content (see per-section notes). Do not reuse the same fade-up everywhere.

---

## 3. Global elements

### 3.1 Header reading-progress line
```
┌───────────────────────────────────────────────────────────┐
│ [logo]            Free live masterclass  Thu...  [SAVE]   │
├███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░┤ <- 2px green, scaleX(progress)
```
- 2px bar pinned to the bottom edge of the header, `transform-origin:left`, `scaleX(scrollY / (docHeight - innerHeight))`.
- Color `--green`. Hidden with reduced motion.

### 3.2 Header countdown hand-off
- When the main countdown (proof strip) scrolls out of view, the header event chip swaps its text to a compact live countdown: `Starts in 13d 04h 22m`. When the strip is visible again, it swaps back.
- Crossfade 180ms. Desktop only (the chip is already hidden under 900px).

### 3.3 Sticky mobile CTA
- Label becomes `Save my seat · 13 days left` (live days value). Keep one middle dot only.
- Existing hide/show logic stays.

---

## 4. Section by section

### 4.1 Hero

```
┌──────────────────────────────────────┬──────────────────────────┐
│ [FREE LIVE MASTERCLASS FOR DATA...]  │  ┌ SEATS ARE LIMITED ┐   │
│                                      │  Save your free seat     │
│ Cut your Databricks                  │  ...form...              │
│ bill by up to 75%.   <- 0%→75%       │                          │
│                                      │  [ SAVE MY SEAT → ]      │
│ See where Databricks spend leaks...  │  +1 Free bonus...        │
│ ──────────────────────────────────── │                          │
│ Thursday, October 15, 2026           └──────────────────────────┘
│ 12:00 PM ET / 45 min + live Q&A          ▲ hard green shadow
│ 9:00 AM Pacific  5:00 PM UK ...            "drops" in on load
│ ──────────────────────────────────────
│ ┌ IDLE CLUSTER METER ──────────────┐
│ │ $0.37 billed since you arrived   │  <- ticks every 100ms
│ │ One idle all-purpose cluster at  │
│ │ $X/hr. Illustrative.             │
│ └──────────────────────────────────┘
│ [photo] [photo]
│ Srinath   Richard
└──────────────────────────────────────
```

**Load choreography (total about 1.2s, then stop):**
| t (ms) | Element | Motion |
|---|---|---|
| 0 | Kicker chip | clip-path reveal left to right, 400ms |
| 80 | Headline line 1 | rise 22px + fade, 700ms |
| 160 | Headline line 2 | rise + fade; `75%` counts up from `0%` over 900ms |
| 300 | Lead | fade, 500ms |
| 380 | Date block | fade; the two hairlines draw `scaleX(0→1)` from the left |
| 450 | Form card | slides in 24px from the right; the green hard shadow grows from `0 0` to `12px 12px` over 500ms, 200ms after the card lands |
| 600 | Host portraits | clip-path `inset(100% 0 0 0)` to `inset(0)`, bottom-up, 70ms stagger |

**New element: idle cluster meter** (the one "interesting" hero device)
- Small ink card (`--ink-900`, white text, green number), placed between the date block and the hosts.
- Copy: **`$0.00`** (large, tabular figures) + `billed by one idle cluster since you opened this page` + footnote `Based on $X.XX/hr. Illustrative.`
- JS: `start = performance.now()`; every 100ms set `value = rate * elapsedHours`, two decimals.
- **Blocker:** the hourly rate must come from BigHammer. Until it is confirmed, do not ship this element; leave it behind a flag `const IDLE_RATE = null;` and render nothing when null.

**Hosts in hero**
- Hover (pointer devices only): the grayscale photo gets a purple duotone (an overlay `::after` with `background: var(--purple); mix-blend-mode: screen; opacity 0 → .55`), and the offset shadow shifts from `6px 6px` to `10px 10px`. 240ms.

**Form micro-interactions**
- Focused field: background goes white and the label turns purple (existing border ring stays).
- Submit: button shows a 3-square loader (three 6px squares pulsing in sequence, brand colors) for 600ms, then the success state.
- Success: the tick is an inline SVG polyline drawn with `stroke-dashoffset` (400ms). The pink "Seats are limited" flag flips (rotateX 90° out, new flag in) to a green flag reading `Seat saved`.

### 4.2 Proof strip + countdown
- Countdown digits: when a digit changes, the old digit slides up and out and the new one slides up in (`translateY(-100%)` → `0`), 280ms. Each cell needs `overflow:hidden` and two stacked spans.
- Facts (`$3M+`, `>400%`, `60%`): `countUp` when the strip enters. `$3M+` counts 0 to 3 with the prefix `$` and suffix `M+`.

### 4.3 Customer quote (Anushka)
- On enter: the quote words appear in 3 chunks (split at the commas and periods), 120ms apart.
- After the text lands, a lime highlighter sweeps under **"in months"**: `background-image: linear-gradient(var(--lime), var(--lime)); background-size: 0% 40%` → `100% 40%`, positioned bottom, 600ms.

### 4.4 Sound familiar? (quotes + problems)
- Quote cards enter in masonry order with stagger. The big purple Ferrari card enters first with a slight scale (`.96 → 1`).
- Desktop only: the Ferrari card drifts 30px slower than the page (parallax) while the section is in view. Drive it from the shared scroll loop. No parallax on mobile.
- Problems panel: the three columns reveal left to right. The vertical dividers draw top to bottom (`scaleY(0→1)`).

### 4.5 Six patterns → "itemized bill" with live micro-graphics

Biggest content upgrade. Each pattern row gets a small data graphic on its right that animates when the row enters. The graphics are 120×44px, drawn with CSS (or tiny inline SVG for shapes), colored from the tokens.

```
01  Always-on clusters                     CPU [█░░░░░░░░░] 2%
    Run 24/7 at 1-2% peak CPU...

02  Photon on everything                   DBU rate  1x ──► 2x
    2x DBU premium on simple ETL...

03  Failed-run leakage                     [██████░░░░] 57-63%
    No timeouts. Failed jobs burn...

04  Spin-up overhead                       [▒▒▒▒▒▒▒███] start | run
    Micro-batch jobs spend 65-75%...

05  Small-file drag                        ▪▪▪▪▪▪▪▪▪▪▪▪ → ■
    Tiny Delta files slow reads...

06  No guardrails                          ☐ tags ☐ alerts ☐ policies
    No tags, alerts or policies...
```

| # | Graphic | Animation on enter |
|---|---|---|
| 01 | Horizontal gauge, label `CPU` | Fill rises to 2% and stops; the empty track briefly pulses pink once (what you pay for) |
| 02 | Chip `1x` with an arrow to a chip `2x` | `1x` appears, arrow draws, `2x` pops (scale .8 → 1) in pink |
| 03 | Pink bar | Fills from 0 to 60%; label counts up to `57-63%` |
| 04 | Split bar, hatched grey "start" segment + purple "run" segment | Hatched segment grows to 70%, then the run segment fills the rest |
| 05 | 24 tiny squares | Squares collapse into one block (each moves via transform to the block position), 600ms |
| 06 | Three empty checkboxes with labels | Boxes appear one by one; they stay empty (that is the point) |

- Number column (`01`...`06`) stays pink. On enter, each number slides up from a mask (clip-path).
- Mobile: graphic moves under the text, full width.
- The lime CTA bar below the list: when it enters, its button does one subtle nudge (`translateX 0 → 4px → 0`). Once, never repeating.

### 4.6 Case study (ink)
- `~50%` counts up.
- Chart: bars grow (already built) with count-up values (`$2.74M`, `$315K`, `$308K`).
- Add a thin baseline axis under the bars with tick labels `$0` and `$2.74M`. The scale must match the bar widths.
- The purple radial glow behind the section moves with scroll (parallax 0.2) on desktop.

### 4.7 Framework: the bold moment (desktop pinned, mobile carousel)

```
┌──────────────────────────────────────────────────────────────┐
│ Assess. Migrate. Monitor.                Scroll to step through│
│ (1)━━━━━━━━━━━━━(2)─ ─ ─ ─ ─ ─ ─ ─ ─ ─(3)                     │
│                                                              │
│   0 2   <- giant outlined numeral, behind, 30% opacity       │
│ ┌─────────────────────┐  ┌────────────────────────────────┐  │
│ │ Migrate             │  │ Dual-run       Same inputs     │  │
│ │ Prove it before     │  │ [Databricks]═▪══▪═▪═[EMR]      │  │
│ │ cutover.            │  │ Wave 1 ══▪═══▪══               │  │
│ │ Move in waves...    │  │ Wave 2 ═══▪════                │  │
│ │ Output: cutover...  │  │ ☑ Row counts  ☑ Data hashes    │  │
│ └─────────────────────┘  │ ☑ Quality     ☐ Key metrics    │  │
│                          │ ☐ SLA         ☐ Cost           │  │
│                          │ [ Parity confirmed. Cut over. ]│  │
│                          └────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

Keep the existing pin, rail and `--sp` / `data-at` system. Add:

1. **Giant step numeral**: `01` / `02` / `03` in Epilogue 800, about 28vw, outlined (`-webkit-text-stroke: 2px var(--w-20)`, transparent fill), positioned behind the copy column. On step change, the old numeral slides up 40px and fades out, and the new one slides in from below. Drive it with `--p` so it is scroll-linked, not timed.
2. **Step transition via clip-path**: the outgoing visual panel wipes out with `clip-path: inset(0 0 0 100%)` while the new one wipes in from `inset(0 100% 0 0)` to `inset(0)`. 500ms, `--ease-in-out`. The copy column keeps its crossfade.
3. **Assess**: the scan line uses `transform` (see section 2). Add a live counter in the visual header: `0 / 16 classified`, which increments as cells turn `.on`.
4. **Migrate**: add data packets. 6 small squares per lane, positioned with `transform: translateX(calc(var(--sp) * <lane width> * k))` so they move with scroll. Ticks draw (SVG check, stroke-dashoffset) instead of instantly filling.
5. **Monitor**: replace the loop chips row with a **ring**: an SVG circle (r = 70) with 4 labelled nodes at 12, 3, 6 and 9 o'clock (Detect, Act, Improve, Re-assess). A green arc draws around the ring with `stroke-dashoffset` bound to `--sp`; each node lights as the arc passes it. The tiles sit to the left of the ring on desktop and above it on mobile.
6. **Rail**: the active node pulses once (scale 1 → 1.15 → 1.12) when it becomes active.

**Mobile (< 900px): horizontal scroll-snap carousel** instead of the long stack.
- `.fw-steps { display:grid; grid-auto-flow:column; grid-auto-columns:88%; overflow-x:auto; scroll-snap-type:x mandatory; gap:16px }`, each step `scroll-snap-align:center`.
- Three square dots under it show the active step. Use IntersectionObserver on the steps with `root` set to the carousel, threshold .6.
- Each step's visual plays its `--sp` 0 → 1 tween (already built) the first time it becomes the active card.
- This alone cuts roughly 1,500px of mobile scroll.

### 4.8 What you get (lime)

```
 0 ────────────────── 30 ───────── 45 min
 [███ Masterclass ███][ Live Q&A ]
```
- Add a horizontal **45-minute timeline bar** above the two agenda rows: two segments sized 30:15 (purple and ink), labels under the ticks `0`, `30`, `45 min`.
- On enter the segments fill left to right in order: 700ms, then 350ms.
- **Assessment card "7"**: under the big `7`, add a row of 7 small squares labelled `Q1`...`Q7`. They light green one at a time (90ms apart) on enter.

### 4.9 Hosts
- Portraits reveal with clip-path bottom-up (same as the hero, so the two moments rhyme).
- Desktop parallax: Srinath's portrait moves at 0.94x scroll speed and Richard's at 1.06x while the section is in view. The offset is small (max ±24px) and comes from the shared scroll loop.
- Hover duotone (same as the hero).
- Names: reveal from a mask (text slides up from `translateY(100%)` inside an `overflow:hidden` line wrapper).

### 4.10 Marquee + final CTA (pink)

```
▸ THU OCT 15  ▸ 12:00 PM ET  ▸ FREE  ▸ LIVE  ▸ 45 MIN  ▸ THU OCT 15 ...   <- ink strip, scrolls left
┌──────────────────────────────────────────────────────────────┐
│ Thursday, October 15, 12:00 PM ET                             │
│ Find out how much of your                    [ SAVE MY SEAT → ]│
│ Databricks bill is waste.                                     │
│ Free seat. Free assessment. Recording included.               │
└──────────────────────────────────────────────────────────────┘
```
- **The page's one marquee**: an ink strip directly above the pink section, uppercase Epilogue 700, about 20px, green `▸` separators. CSS `@keyframes` translateX loop, 30s. Pause on hover. Static (no animation) with reduced motion. Duplicate the content once for a seamless loop and mark the duplicate `aria-hidden`.
- Headline: on enter, each line rises from a mask, 90ms apart.
- Button: idle "breathing" is banned. Instead, the hard shadow appears on hover only (already built).

### 4.11 Footer
- No change beyond the existing links. The 4-color bottom bar segments draw left to right when the footer enters (scaleX, 80ms stagger).

---

## 5. Accessibility and performance checklist

- [ ] Reduced motion: every effect above is off, all values are final, the marquee is static, the framework is not pinned and the carousel has no auto-tween.
- [ ] No JS: the page is complete and readable (count-up targets are already in the HTML text).
- [ ] Only one `requestAnimationFrame` scroll loop and one shared IntersectionObserver (plus the carousel observer).
- [ ] Animated properties are limited to transform, opacity, clip-path, stroke-dashoffset and background-size.
- [ ] Count-ups use `font-variant-numeric: tabular-nums` so the layout does not jitter.
- [ ] The countdown digit roll keeps `role="timer"` and stays readable by screen readers (update a visually hidden full string, not each animated span).
- [ ] Marquee: `aria-hidden="true"` (the same info is in the final CTA).
- [ ] No horizontal page scroll at 375px (the carousel scrolls inside its own container).
- [ ] Zero em or en dashes in visible text.
- [ ] Check pinned framework at 1280×800 and 1440×900; check carousel at 375×812.

## 6. Build order (for the next pass)

1. Motion utilities + header progress line + scan-line transform fix.
2. Six-pattern micro-graphics (biggest visible win).
3. Framework additions (numeral, clip-path transitions, packets, ring) + mobile carousel.
4. Count-ups, countdown roll, quote highlighter.
5. Timeline bar, 7-query squares, hosts parallax/duotone, marquee, final CTA mask reveal.
6. Form micro-interactions (loader, tick draw, flag flip).
7. Idle cluster meter, only once BigHammer confirms the hourly rate.
8. Rebuild all three outputs, republish the artifact, push to GitHub Pages.

## 7. Open inputs (from the client)
- Hourly rate for the idle cluster meter, or approval to cut that element.
- ~~Whether "Seats are limited" is real~~ Confirmed by the client: seats are limited. Keep the pink "Seats are limited" flag on the form, and add `Seats are limited.` as the last sentence of the final CTA lead (`Free seat. Free assessment. Recording included. Seats are limited.`).
- A real baseline-versus-now cost figure for the Monitor tile (optional).
- A higher-resolution photo of Srinath.
