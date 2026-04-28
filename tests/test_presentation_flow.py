from pathlib import Path

TEXT = (Path(__file__).resolve().parents[1] / "index.html").read_text()


def assert_contains(snippet: str) -> None:
    assert snippet in TEXT, f"missing snippet: {snippet[:120]}"


def assert_before(a: str, b: str) -> None:
    assert TEXT.index(a) < TEXT.index(b), f"expected {a[:60]!r} before {b[:60]!r}"


# Hero / visual treatment
assert_contains('.hero-globe-wrap {')
assert_contains('class="hero-globe-visual hero-globe-static" src="assets/globe-bg.png"')
assert '<video id="globe-fallback-video"' not in TEXT

# Phone previews no longer zoom/crop and all eight use mobile-style regenerated assets.
assert_contains('@keyframes phone-scroll-calibrated')
assert_contains('.phone-frame-mobile img { --phone-scale: 1.00; }')
assert_contains('.phone-frame-large.is-live-ready iframe {')
assert_contains("frame.classList.add('is-live', 'is-live-ready')")
assert_contains('setTimeout(restoreStaticPreview, 5000)')
for tab in ['overview', 'camera', 'screen', 'hardware', 'power', 'events', 'uptime', 'settings']:
    assert_contains(f'data-live-tab="{tab}"')
for asset in [
    'assets/overview-tab-mobile.png',
    'assets/camera-tab-mobile.png',
    'assets/screen-tab-mobile.png',
    'assets/hardware-tab-mobile.png',
    'assets/power-tab-mobile.png',
    'assets/events-tab-mobile.png',
    'assets/uptime-tab-mobile.png',
    'assets/settings-tab-mobile.png',
]:
    assert_contains(asset)

# Early context and Konstruktiv framing.
assert_before('The portal network operates almost completely in the dark.', 'The old controller touched one layer. Scope covers the installation.')
assert_contains('Recovery starts in Splashtop and a buggy app, not in a real operating layer.')
assert_contains('We usually find out from a visitor or local operator.')
assert_contains("A daily Splashtop check is not monitoring. It's hoping.")
assert_contains('The old controller touched one layer. Scope covers the installation.')
assert_contains('The tools we had covered only narrow slices of the installation.')
assert_before('The old controller touched one layer. Scope covers the installation.', 'The shift is from controlling a cabinet to operating the whole installation.')
assert_contains('Little visibility into VW, NovaStar, WAN, UPS, AC, or screenshots')
assert_contains('What the old controller mostly was')
assert_contains('What <span class="scope-brand">Scope</span> becomes instead')
assert_contains('The controller proved the value of a remote surface. <span class="scope-brand">Scope</span> turns that idea into an operating layer for the whole installation.')

# Scope / coverage / architecture order.
assert_before('An operational system for electronic art installations. Not just another dashboard.', '<span class="scope-brand">Scope</span> sees what an installation actually is.')
assert_before('<h2><span class="scope-brand">Scope</span> sees what an installation actually is.</h2>', '<h2><span class="scope-brand">Scope</span> architecture.</h2>')
assert_contains('the core product and IP can support future Portals, Augmentl, and other installation deployments too')

# Dashboard section now has a separate intro slide and three screenshot slides with contain framing.
assert_contains('The dashboard is the fleet and project layer around the controller.')
assert_contains('assets/dashboard-ops-attached.png')
assert_contains('assets/dashboard-portals-attached.png')
assert_contains('assets/dashboard-project-attached.png')
assert_contains('preview-dashboard-frame contain')
assert_contains('The Augmentl Dashboard is the fleet and operations layer around every portal.')
assert_contains('The same system can expose a dedicated portals dashboard without the rest of the Augmentl workspace.')
assert_contains('The dashboard adds project and install context that the controller app should not have to carry.')
assert_before('The capability already exists. The decision is how far to take it.', 'The dashboard is the fleet and project layer around the controller.')
assert_before('The dashboard is the fleet and project layer around the controller.', 'The Augmentl Dashboard is the fleet and operations layer around every portal.')
assert_before('The Augmentl Dashboard is the fleet and operations layer around every portal.', 'The same system can expose a dedicated portals dashboard without the rest of the Augmentl workspace.')
assert_before('The same system can expose a dedicated portals dashboard without the rest of the Augmentl workspace.', 'The dashboard adds project and install context that the controller app should not have to carry.')


# Operating loop framing is explicit.
assert_contains('Observe. Diagnose. Act. Learn.')
assert_contains('Diagnose across layers')

# App preview tabs remain in order and surface the uptime proof point.
for title in [
    'Live status at a glance.',
    'Camera setup, virtual tilt, lens correction, presence detection, and per-installation profiles.',
    'Full LED display control.',
    'Deep hardware visibility.',
    'Power, UPS state, and operating cost in one tab.',
    'An operational timeline, not a mystery.',
    'Audience-visible uptime, separated from raw process uptime.',
    'Portal settings and hardware identity in one place.',
]:
    assert_contains(title)
assert_contains('Raw process uptime still visible')
assert_contains('This is already answering a real Portals question in a measurable way.')

# Commercial framing and ask are clearer and less adversarial.
assert_contains('What changes when Portals funds a dedicated operating layer.')
assert_contains('Current baseline: manual support around Video Window')
assert_contains('With Augmentl <span class="scope-brand">Scope</span>: €500/portal/month')
assert_contains('Separate operating layer, not overflow support.')
assert_contains('<strong>€500 per portal per month ongoing.</strong> That is the same budget level Portals was already prepared to allocate.')
assert_contains('Formalise <span class="scope-brand">Scope</span> as a separate operating capability for the portal network, with a roadmap and rollout plan.')
assert_contains('Fund ongoing product development, monitoring, and support on a separate operating budget instead of folding it into the existing monthly arrangement.')
assert_contains('If procurement needs another commercial shape, use a higher separate operating retainer')
assert_contains('If Portals is funding an operating layer, fund the one already built from the real installations and incentivised to keep hardening them.')

# Future work covers client-facing views and the PC-side installation layer.
assert_contains('Limited client-facing portal views')
assert_contains('A future scoped client view can let each site or stakeholder see only its own portal status, health summary, and a tightly limited set of permitted actions.')
assert_contains('Better PC-side install and runtime management')
assert_contains('Scoped actions like blank or blur for their own screen only')

# Ending business framing is partnership/governance aware.
assert_contains("Access, hosting, and data handling can be structured to fit Portals' needs.")
assert_contains('class="slide slide-centered-stage">')
assert_contains('class="slide slide-centered-stage ask-slide">')
assert_contains('partner-managed, or otherwise agreed')
assert_contains('Per-portal command permissions can be scoped per user, so Portals can decide who sees what and who can act.')
assert_contains('Video Window can stay in a narrower playback and first-line support role without inheriting the whole operating layer or getting the Scope/IP value for free')
assert_contains("Adopt <span class=\"scope-brand\">Scope</span> as the portal network's shared operating layer, developed in partnership.")
assert_contains('Why adopting <span class="scope-brand">Scope</span> is strategically stronger for Portals.')
assert_contains('Agree the operating model: hosting, access, portal-owned versus partner-managed layers, and where Video Window stays in a narrower playback/support role.')

# End slide and smooth transitions remain present.
assert_contains('id="end-globe-static"')
assert_contains('id="end-globe-frame"')
assert_contains('class="end-panel"')
assert_contains("scrollIntoView({ behavior: 'smooth', block: 'start' })")
assert_contains("document.addEventListener('wheel'")

print('presentation flow assertions passed')
