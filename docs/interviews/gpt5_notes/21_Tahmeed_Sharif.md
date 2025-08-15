# HajjGuide Interview Analysis — 21. Tahmeed Sharif

> Automated first-pass extraction from uploaded transcripts. Pains and hypotheses are heuristic; ambiguous fiqh items are flagged for scholar review.

### 1) Interview metadata
- **Interviewee type:** Agent
- **Origin market and language(s):** BD, UK, KSA; Arabic, Bangla, English
- **Trip type and timing:** Hajj + Umrah + Ramadan season
- **Group composition:** Group
- **Tech comfort:** Medium
- **Any special needs:** None mentioned
- **Interview date/context:** [Not provided]

### 2) Executive summary
- **Top pains**: Facility wayfinding, Transport price opacity, Permit/route constraints
- **Biggest opportunities aligned with HajjGuide**: Offline map & lap counter; fixed-fare vetted transport; wheelchair/accessibility marketplace; merchant discovery; agency bundle onboarding.
- **Willingness to pay**: 10 Riyal, 400 Riyal, 500 Riyal, 15 Riyal, 30 Riyal
- **Risks/constraints flagged**: Permit/compliance; on-site transport legality; map accuracy; data/privacy (location/voice).
- **Overall signal strength for PMF**: **High**

### 3) Pain inventory by stage and persona

| Stage | Pain (short name) | Description & evidence (keywords) | Severity (1–5) | Frequency (1–5) | Current workaround | Time/Money spent | Emotion | Related H# | Confidence |
|---|---|---|---:|---:|---|---|---|---|---|
| In-trip | Facility wayfinding | Detected terms: zamzam | 4 | 1 | Asking locals/agency, ad-hoc tools | Varies | Stress | H6,H7 | Med |
| In-trip | Transport price opacity | Detected terms: fare, taxi | 4 | 3 | Asking locals/agency, ad-hoc tools | Varies | Stress | H2,H8 | High |
| In-trip | Permit/route constraints | Detected terms: nusuk | 4 | 2 | Asking locals/agency, ad-hoc tools | Varies | Stress | H5,H7 | Med |
| In-trip | Language barrier | Detected terms: arabic, english | 3 | 5 | Asking locals/agency, ad-hoc tools | Varies | Frustration | H6 | High |
| In-trip | Discovery near Haram (food/shops) | Detected terms: expensive, shop, where to buy | 3 | 5 | Asking locals/agency, ad-hoc tools | Varies | Frustration | H1 | High |
| Pre-trip | Connectivity & SIM | Detected terms: data, sim | 2 | 5 | Agency research / DIY forums | Varies | Concern | H6,H9 | High |

### 4) Jobs-To-Be-Done
- When I enter a crowded Haram, I want to find toilets/ablution and re-entry paths, so I can maintain wudu and finish rituals calmly.
- When I land with luggage, I want fixed-fare vetted transport, so I can avoid haggling and last-mile stress.
- When routes are blocked or timed, I want compliant route/timing guidance, so I can reach safely without fines.
- When I shop or need help, I want simple Arabic phrases and translation, so I can communicate confidently.

### 5) Journey snapshot
- **Pre-trip**
  - *Tasks*: Research, visa/permits, booking
  - *Pain points*: Trust in providers, clarity on permits
  - *Workarounds*: Agents, WhatsApp/YouTube
  - *Opportunities*: Cohort training, permit explainer (AI Concierge)
- **In-trip**
  - *Tasks*: Arrival, check-in, rituals, transport, meals
  - *Pain points*: Wayfinding, price opacity, language, accessibility
  - *Workarounds*: Ask staff, haggle, manual counters
  - *Opportunities*: Offline map, lap counter, fixed-fare rides, wheelchair marketplace, phrasebook
- **Post-trip**
  - *Tasks*: Reflection, referrals, planning next Umrah
  - *Pain points*: Momentum fades; scattered media
  - *Opportunities*: Journaling & community; referrals

### 6) Alternatives and workarounds
- **Tools referenced**: Facebook groups, Google Maps, Nusuk
- **Pros**: Familiar, low learning curve; social proof via groups
- **Cons**: Opaque pricing; unreliable availability; fragmented info
- **Switching costs & trust anchors**: Mosque/imam endorsements; agency bundles; refundable escrow

### 7) Willingness to pay and value exchange
- **Explicit prices mentioned**: 10 Riyal, 400 Riyal, 500 Riyal, 15 Riyal, 30 Riyal
- **Inferred price tolerance**: One-off add-on within $10–30 or ৳500–1,000 if value is immediate (Low–Med confidence)
- **Payer**: Pilgrim; potential agency-bundled upsell
- **Expected ROI**: Time saved, stress reduction, scam avoidance

### 8) Hypothesis scoreboard
| Hypothesis (H#) | Support / Contradict / Unclear | Confidence | Notes |
|---|---|---|---|
| H1 | Support | Med | Auto-derived from pains/tools |
| H2 | Support | Med | Auto-derived from pains/tools |
| H3 | Unclear | Low | Auto-derived from pains/tools |
| H4 | Support | Med | Auto-derived from pains/tools |
| H5 | Support | Med | Auto-derived from pains/tools |
| H6 | Support | Med | Auto-derived from pains/tools |
| H7 | Support | Med | Auto-derived from pains/tools |
| H8 | Support | Med | Auto-derived from pains/tools |
| H9 | Support | Med | Auto-derived from pains/tools |
| H10 | Unclear | Low | Auto-derived from pains/tools |
| H11 | Unclear | Low | Auto-derived from pains/tools |
| H12 | Unclear | Low | Auto-derived from pains/tools |

### 9) Feature implications and priority
| Feature/Capability | Pain addressed | Module | Must/Should/Could | Rationale & acceptance criteria |
|---|---|---|---|---|
| Offline Hajj Map | Facility wayfinding | AI Concierge | Must | Offline, nearest facility in ≤2 taps; accuracy ≥90% |
| Fixed-fare rides + escrow | Transport price opacity | Marketplace | Must | Quote→book in ≤3 taps; on-time ≥90% |
| Compliant route/timing | Permit/route constraints | AI Concierge | Should | Route avoids restricted areas |
| Phrasebook + translate | Language barrier | Guides | Should | 50 phrases with audio |

### 10) Supply-side insights
- **Demand patterns**: Referral heavy; seasonality peaks
- **Pricing/margins**: Prefers fixed payouts; wary of no-shows
- **Licensing/permits**: Critical; wants platform help tracking rules
- **Platform expectations**: Payout reliability, escrow, review fairness

### 11) Distribution and partnerships
- **Channels**: Mosque/imam endorsements; diaspora FB/WhatsApp groups; agency bundles
- **Messaging**: No haggling, no getting lost, pray with focus
- **Referral behaviors**: Group leaders as affiliates

### 12) Risks, constraints, and compliance notes
- Route/permit compliance must be enforced in UX.
- Driver legality and insurance must be verified.

### 13) Quotes repository (verbatim)
- - Muhammad: “If you could share which year you performed Hajj, then we can start, insha'Allah. Could you please repeat? First, please introduce yourself, and if you could share which year you…”
- Tahmeed Sharif: “I am currently the founder of [brown dike - inaudible/best guess: probably a company name like Brown Dike, or it could be "brown diggi"], I am a software engineer previously. I…”
- Tahmeed Sharif: “Yes, brother, can you hear me now?”
- Tahmeed Sharif: “Okay, brother, is the audio better now?”
- Tahmeed Sharif: “Yes, brother, I performed Hajj in 2024.”
- Tahmeed Sharif: “My journey was 40 days. And regarding choosing, when I was in software, a brother shared a Facebook post about it. I saw it there, and then he suggested registering while there…”
- Tahmeed Sharif: “It was a challenge initially, even for submitting my documents, especially during Ramadan. And I later found out that their Chittagong partners were [Gojiyara - inaudible/best…”
- Tahmeed Sharif: “Yes, online.”
- Tahmeed Sharif: “Yes, the classes were effective, but I think they could have been a bit more interactive.”
- Tahmeed Sharif: “Yes, I think this would be beneficial because currently, people's attention spans are very short. So, if large courses of two, three, or four hours are given, it might be…”

### 14) Contradictions, unknowns, follow-ups
- Validate price bands for key services (taxis, wheelchairs)
- Measure map accuracy and latency in crowded zones
- Clarify willingness to pay and who pays (pilgrim vs. agent)

### 15) Recommended next experiments
- **E1**: Transport MVP (airport⇄hotel) with escrow; target on-time ≥90%
- **E2**: Offline map + lap counter usability test; success ≥95% finish without errors
- **E3**: Wheelchair marketplace pilot; fill rate ≥85%

### 16) Coding for cross-interview analysis
- **Persona**: Agent-SME
- **Stage tags**: PreTrip, InTrip, PostTrip
- **Pain tags**: CrowdStress, LanguageBarrier, Payment, PermitConfusion
- **Channel tags**: Facebook
- **Region tags**: ID, IN, MY, NG, PK, SA, UK, US
- **Feature tags**: Escrow, Reroute

---
