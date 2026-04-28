# Scope Pitch Presenter Notes

Audience: Portals / stakeholders evaluating Scope as the portal network operating layer.

Use this as an off-screen script. The slides should carry the structure and proof. The spoken delivery should carry most of the detail.

## Overall delivery notes
- Keep the pace brisk through the problem, contrast, and system slides.
- Do not read bullets verbatim.
- Let the embedded controller pages function as the live demo block.
- Keep Konstruktiv before the Scope controller demo. It sets the contrast.
- Show the embedded controller demo block before the dashboard slides. The controller is the first concrete proof of the product.
- Use the dashboard after the controller to widen the frame from one portal to the whole network.
- Reuse three anchor phrases:
  - "The network is operationally blind."
  - "Scope turns support work into an operating layer."
  - "This already exists. The question is how far to formalise it."

---

## Slide 0 - Opening stage
**Key message**
Every installation. Fully in view.

**Talk track**
- Open on ambition, not detail.
- This is about making electronic artworks operable like serious infrastructure.
- The portal network is the proving ground, not the limit of the product.

## Slide 1 - Hero
**Key message**
One operational surface for installations in the field.

**Talk track**
- Scope is the operating surface around the installation, not just a dashboard.
- It comes from the work already being done to keep these portals running.
- This is why it fits the reality of the network.

## Slide 2 - The problem
**Key message**
The network is still mostly dark until a human notices something is wrong.

**Talk track**
- Lead with the visitor-report point. That is the emotional and operational failure.
- The problem is not just incident frequency. It is that diagnosis starts blind.
- Splashtop belongs here. Say it once, clearly: remote desktop is not monitoring.
- The deeper problem is that the operating model lives in one person's head.

**Likely question**
How often does this happen?

**Answer direction**
The point is less the raw count and more the fact that when it happens, response quality depends too much on memory, luck, and manual inspection.

## Slide 3 - Konstruktiv controller context
**Key message**
The old app showed that a mobile surface was valuable, but it only touched one layer.

**Talk track**
- Be fair to it. It proved the need.
- Then state the limit: it never became a full operating layer.
- Emphasise no display reasoning, no full-stack diagnostics, no integrated visibility.

## Slide 4 - Transition
**Key message**
The shift is from controlling a cabinet to operating the whole installation.

**Talk track**
- This is the conceptual hinge of the deck.
- Konstruktiv gave button access. Scope gives operational understanding.
- The important move is from intervention tool to operating layer.

## Slide 5 - What Scope is
**Key message**
Scope is an operational system for electronic art installations.

**Talk track**
- Distinguish it from generic monitoring and from a pure control app.
- It models the installation the way it actually works: compute, display, environment, network, and camera.
- The portal network is where it is furthest along today.

## Slide 6 - Already in use
**Key message**
This is already live, already useful, and already solving operator problems.

**Talk track**
- Treat this as the credibility slide.
- Say clearly: this is not a concept deck for an idea that does not exist yet.
- Use the uptime example as the cleanest proof that the system answers real operator questions.

**Likely question**
What is still left to build?

**Answer direction**
Productising, access scoping, rollout hardening, and making the operating layer easier for more people to use.

## Slide 7 - Coverage
**Key message**
Scope sees the installation as it actually is.

**Talk track**
- Do not read every item.
- Sweep across the four quadrants: visual state, display control, hardware layer, commissioning.
- End with: this is why the product can diagnose, not just observe.

## Slide 8 - System diagram
**Key message**
The stack is coherent: controller, dashboard, alerts, and portal-side runtime all connect into one operational picture.

**Talk track**
- Keep this moving.
- Show the cloud layer, the bridge on the portal PC, and the separate Controllino path.
- Mention outbound-only connections here if needed, but do not over-explain yet.

## Slide 9 - Operating loop
**Key message**
Observe. Diagnose. Act. Learn.

**Talk track**
- This is the operating model in one slide.
- Observe: one retained operational picture.
- Diagnose: correlate layers before guessing.
- Act: scoped controls and automation.
- Learn: event history and patterns improve future operations.

## Slide 10 - Dashboard intro
**Key message**
The dashboard is the fleet and project layer around the deep per-portal controller.

**Talk track**
- If the room feels controller-first, keep this short and move quickly.
- The dashboard matters because the network is more than one portal and more than runtime telemetry.
- It is where shared operational context lives.

## Slide 11 - Augmentl dashboard
**Key message**
This is the broad operations workspace.

**Talk track**
- Fleet view, tasks, planning, project context.
- Distinguish it from the controller: controller is deep action on one portal, dashboard is network-wide visibility and coordination.

## Slide 12 - Portals-only dashboard
**Key message**
The same backend can expose a narrower portal-team surface.

**Talk track**
- This is not another product.
- It is a scoped view of the same system.
- That matters politically and operationally.

## Slide 13 - Project workspaces
**Key message**
Project context belongs around the runtime, not inside the controller UI.

**Talk track**
- Install notes, deployment timing, documents, and operational memory live here.
- This is how context survives the current operator.

## Slide 14 - Monitoring + alerts
**Key message**
Monitoring only matters if it reaches the operator with enough context to act.

**Talk track**
- Alerts should arrive with probable cause, not just noise.
- The workflow stays where people already work: chat.
- The thread becomes the narrative of the incident and the recovery.

## Slide 15 - Commercial framing
**Key message**
Funding Scope changes the network from reactive support to a dedicated operating layer.

**Talk track**
- Say clearly that this is not overflow support folded into a retainer.
- It funds telemetry, alerting, uptime logic, diagnostics, and recovery paths as product infrastructure.
- The strongest line here is: same monthly magnitude, very different operational outcome.

**Likely question**
What exactly is included in the €500?

**Answer direction**
Treat it as the dedicated operating layer: product development, monitoring, alerting, telemetry, and support for that layer, separate from playback support.

---

# Embedded controller demo block

## Delivery note for slides 16-23
These slides are the live demo, just presented inside the deck. Keep your spoken copy lighter here. Narrate what matters and what an operator learns from each page.

## Slide 16 - Overview tab
**Key message**
This is the fastest way to understand whether the portal is actually healthy.

**Talk track**
- Two visual feeds, stream state, system telemetry, and recovery actions in one place.
- Say: this is the page I would open first if something looked wrong.

## Slide 17 - Camera tab
**Key message**
Commissioning and camera health are built into the same controller.

**Talk track**
- Framing, exposure, white balance, correction.
- Emphasise this is not another disconnected tool.

## Slide 18 - Screen tab
**Key message**
Display control is first-class, not bolted on.

**Talk track**
- Brightness, blanking, thermal state, and reasoning all in one place.
- This is a strong contrast moment versus the old app.

## Slide 19 - Hardware tab
**Key message**
The cabinet and infrastructure layer are visible without a remote desktop.

**Talk track**
- Controllino, WAN, temperatures, PC state, hardware health.
- This is where the product stops being a viewer and becomes an operating surface.

## Slide 20 - Power tab
**Key message**
Power events and operating cost become observable instead of anecdotal.

**Talk track**
- UPS state, input power, and cost context.
- Good place to mention this matters for diagnosing faults that are not software faults.

## Slide 21 - Events tab
**Key message**
Incidents become timelines instead of mysteries.

**Talk track**
- Explain this as the narrative layer.
- Not just that something failed, but when, in what order, and what followed.

## Slide 22 - Uptime tab
**Key message**
Audience-visible uptime is different from raw process uptime.

**Talk track**
- This is one of the strongest proof points in the whole deck.
- Clarify that uptime here means what the audience actually experiences.

## Slide 23 - Settings tab
**Key message**
Portal identity and configuration live in one place.

**Talk track**
- This matters for rollout, consistency, and making future scaling less chaotic.

---

## Slide 24 - Growth vision
**Key message**
The real opportunity is moving from person-dependent recovery to a reproducible operating network.

**Talk track**
- Walk the stages quickly.
- Mention NixOS here as deployment discipline, not as the product itself.
- The point is reproducibility, rollback, and safer scaling.

## Slide 25 - Next layer
**Key message**
The next worthwhile expansions are already obvious.

**Talk track**
- Scoped client views.
- Better PC-side deployment discipline.
- Deeper project workspaces.
- Keep this short. It is a roadmap teaser, not the core ask.

## Slide 26 - Security
**Key message**
Security and hosting can be structured to fit Portals' needs.

**Talk track**
- Encrypted transport.
- No direct hardware exposure.
- Authenticated access and scoped permissions.
- Deployment-chosen infrastructure.
- Do not over-explain unless asked.

**Likely question**
Where does the data live?

**Answer direction**
On infrastructure chosen for the deployment model: portal-owned, partner-managed, or another agreed arrangement.

## Slide 27 - Why this matters
**Key message**
Adopting Scope is operationally useful and strategically stronger for Portals.

**Talk track**
- Faster diagnosis and fewer blind recoveries.
- Stronger baseline for current and future portals.
- Clearer separation between Video Window playback/support and the operating layer.

## Slide 28 - The ask
**Key message**
Formalise Scope as the shared operating layer for the portal network.

**Talk track**
- Ask 1: formalise the capability.
- Ask 2: agree the operating model and ownership boundaries.
- Ask 3: fund it on a separate operating budget.
- Pause between each ask.

## Slide 29 - End
**Key message**
Return to the opening: every installation, fully in view.

**Talk track**
- End cleanly.
- Take questions.

---

## Questions to expect
- Why is this separate from Video Window support?
- What exactly is included in the operating layer fee?
- How much of this is already live today?
- What would rollout look like beyond Portal 5?
- Who hosts the data and who gets access?
- What does Portals get as a dedicated view versus what stays in Augmentl's broader workspace?

## Suggested rehearsal emphasis
If time is tight, protect these beats:
1. Problem
2. Konstruktiv contrast
3. What Scope is
4. Already in use
5. Embedded controller demo block
6. Commercial framing
7. The ask
