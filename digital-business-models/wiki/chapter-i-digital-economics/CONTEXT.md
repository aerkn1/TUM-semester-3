# Ubiquitous Language: Digital Economics

Source note: [chapter-i-digital-economics.md](chapter-i-digital-economics.md). Discovery sources: [Chapter i](../../raw/Lecture%20-%20Chapter%20i.pdf), all pages; [Exercise 1](../../raw/Exercise%201.pdf) where stated. Reconciled 2026-10-20. PDF page references are canonical; after PDF p. 13 printed labels are one higher.

## Canonical terms and aliases

| Term | Definition / provenance | Avoid |
|---|---|---|
| Direct network effect | Same-group participation increases participant value [local pp. 2–3] | lower server cost |
| Indirect network effect | One side's participation increases another side's value; cross-side network effect [local p. 4] | every new seller helps existing sellers |
| Economies of scale | Increasing volume lowers average cost [local p. 6] | demand-side network effect |
| Critical mass | Sufficient relevant network for further adoption without continuing external incentives [local p. 3] | universal registration threshold or guaranteed profit |
| Chicken-and-egg problem | Each side awaits participation on the other [local; Exercise Q4] | all launch costs |
| Penguin problem | Individual users delay adoption to avoid being stranded [Exercise Q4] | multihoming or high development cost |
| Launch strategy | Initial market side, scope/density and investment choice [local pp. 8–12] | a one-time credit |
| Limited consumer-side opening | Selected consumer group, often invitations/eligibility, before expansion [local p. 12] | broad two-sided launch |
| Limited seller-side opening | Start with selected suppliers/tools, then consumer marketplace [local p. 12] | proof of consumer critical mass |
| Start small | Concentrate useful supply/demand within a niche before expansion [local pp. 9–12] | a scattered small headcount |
| Hell-bent strategy | Fund rapid coordinated two-sided launch [local p. 8; Exercise Q8] | more advertising only on one side |
| Piggybacking | Access an established platform's audience [local p. 11] | independent network from scratch |
| Seeding | Supply initial platform content/activity [local p. 13] | signup cash subsidy |
| Marquee users | Prominent participants whose presence attracts others [local p. 13] | every early user |
| Fringe benefits | Useful standalone functionality independent of network size [local p. 13] | temporary payment |
| Subsidizing | Financial reduction in joining/participation cost [local p. 13] | network effect itself |
| Onboarding | Reduce setup complexity/effort [local p. 13] | a geographic strategy |
| Knowledge transfer | Training/best practices; course groups with cost-decreasing tactics [local p. 8; Exercise Q6] | classifying it as value-increasing in this MC item |
| Tipping | Adoption concentrates through feedback; possible, not guaranteed [local p. 15] | network effects prove monopoly |
| Search cost | Finding and comparing options/partners [local p. 17] | assessing truth alone |
| Verification cost | Assessing reliability/trustworthiness/quality [local p. 17] | production cost |
| Long tail | Many low-selling niche items collectively contribute demand [local p. 19; wording enriched] | each niche product is a bestseller |
| Reputation system | Visible history/signals supporting informed trust and incentives [local p. 21] | average rating guarantees quality |
| Information asymmetry | Participants differ in relevant knowledge about quality/reliability [local term; definition enriched] | all parties know equally much |
| WTP | Maximum monetary price a user pays for a particular offer [local p. 27] | revenue already collected |
| Experience good | Quality learned through use/consumption [local p. 28; wording enriched] | low objective quality |
| Bundling | Offer multiple goods as one package [local p. 25; definition enriched] | identical tastes |
| Subscription | Charge for access over a period [local p. 25; definition enriched] | necessarily a permanent purchase |
| Freemium | Free basic tier, paid enhancements [local p. 26; definition enriched] | every service with ads |
| Advertising model | Advertiser pays for audience access; user gives attention and possibly data [local pp. 26, 29] | zero price means no payer or cost |

## Cost notation, formulas and units

Algebra is **standard enrichment**, with numerical applications from Exercise 1. It is not a transcription of a supplied formula sheet.

| Symbol | Meaning and unit |
|---|---|
| `q` | Units/downloads/users served within a defined period |
| `F` | Fixed cost, € for that same period |
| `c` / `MC` | Constant marginal cost, €/unit in the linear model |
| `TC(q)` | Total cost, € |
| `ATC(q)` | Total cost per unit, €/unit |
| `p` | Uniform monetary price, €/unit |
| `R` | Revenue, € |
| `π` | Profit, € |
| `q_BE` | Break-even quantity, units |

`TC=F+cq`; `MC=dTC/dq=c` for the linear differentiable model; `ATC=TC/q=F/q+c` for `q>0`; `R=pq`; `π=(p−c)q−F`; `q_BE=F/(p−c)` only if `p>c` (round up for indivisible units). Q3 uses `ΔTC/Δq` over an interval; do not claim that identifies every derivative outside the interval.

Price at MC implies `π=−F` when all users pay the same price in this model. More volume lowers ATC but never makes `p=c` cover positive `F`. Model prices/costs must share a period and unit. WTP for a one-off song cannot be compared with a monthly price without stating a conversion/offer.

## Causal relationships and visual intuition

Same-side/cross-side participation → value → further adoption. Strategies concentrate or fund participation; tactics raise value/lower joining cost → critical mass → self-sustaining feedback, with possible tipping. Network density and competitor alternatives change the threshold.

Search reduction branches into price competition and niche discovery. Verification reduction changes quality information and behavior incentives. Reputation must distinguish reliable sellers, encourage good behavior and deter unreliable participation. Low MC plus high `F` gives a flat-ish TC line and falling ATC; low MC plus offsetting valuations supports bundling.

Cost-chart intercept is fixed cost; slope is MC. Cost-versus-cost intersection is not business break-even. Revenue-versus-cost intersection is break-even. The tipping lines are illustrative. Bundle totals may be closer while individual tastes remain different.

## Constructed example dialogue

> Student: “More users reduce cost, so that is a direct network effect?”
> Coach: “That describes scale economies. For a direct effect, explain why a participant's value rises because more relevant people on the same side use it.”

> Student: “MC is €1, so charging €1 breaks even?”
> Coach: “At 25,000 users revenue is €25,000. Compare it with the supplied €135,000 total cost before concluding.”

> Student: “Bundling makes everyone like the same songs?”
> Coach: “No. Add each consumer's valuations. The total can match while their preferred songs differ.”

## Ambiguities and exam traps

- p. 8 names “policy distinction” without explanation; retain the source label and uncertainty instead of inventing a definition.
- p. 10's Facebook/Facemash naming appears questionable; use dense-community intuition without claiming corrected history.
- `P=MC=0` is a competitive zero-MC benchmark; actual digital costs/prices need not equal zero.
- Knowledge transfer can affect multiple outcomes; the course's classification is cost-decreasing.
- p. 29 supplies a privacy/price choice, not a measured universal privacy preference.
- Fixed annual licensing in Q12 is local to that exercise. Large bundles do not automatically average perfectly correlated tastes.
- No observed weak spots yet. Check prerequisite overview, ask for mechanism/calculation before explaining, then record actual errors.
