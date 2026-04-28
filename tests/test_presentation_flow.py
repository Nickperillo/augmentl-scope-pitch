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
assert_contains('.phone-frame-large.is-live iframe {')
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
assert_before('The portal network operates almost completely in the dark.', 'We did have a remote-management app, but it only touched the control hardware layer.')
assert_contains('Recovery means logging into Splashtop and attempting a restart through a buggy app.')
assert_contains('Reports from the audience or client are a last resort and should not be necessary at all.')
assert_contains('Splashtop is a remote desktop, not a monitoring solution, and should be a last resort')
assert_contains('The only remote-management layer we had was Konstruktiv, which covered a narrow control layer and is being retired as we transition to the new system')
assert_before('We did have a remote-management app, but it only touched the control hardware layer.', 'The shift is from controlling a cabinet to operating the whole installation.')
assert_contains('Some AC controls, but weak in practice')
assert_contains('What the old controller mostly was')
assert_contains('What <span class="scope-brand">Scope</span> becomes instead')
assert_contains('The controller was a narrow intervention tool. <span class="scope-brand">Scope</span> becomes the operational layer around the whole installation.')

# Scope / coverage / architecture order.
assert_before('An operational system for electronic art installations. Not just another dashboard.', '<span class="scope-brand">Scope</span> sees what an installation actually is.')
assert_before('<h2><span class="scope-brand">Scope</span> sees what an installation actually is.</h2>', '<h2><span class="scope-brand">Scope</span> architecture.</h2>')
assert_contains('the core product and IP can support future Portals, Augmentl, and other installation deployments too')

# Dashboard section now has a separate intro slide and three screenshot slides with contain framing.
assert_contains('The controller is not the whole operating surface. The dashboard is the layer around the portals.')
assert_contains('assets/dashboard-ops-attached.png')
assert_contains('assets/dashboard-portals-attached.png')
assert_contains('assets/dashboard-project-attached.png')
assert_contains('preview-dashboard-frame contain')
assert_contains('Augmentl Dashboard matters because the app is not the whole operating surface.')
assert_contains('The same system can expose a dedicated portals dashboard without the rest of the Augmentl workspace.')
assert_contains('The dashboard adds project and install context that the controller app should not have to carry.')
assert_before('The capability already exists. The decision is how far to take it.', 'The controller is not the whole operating surface. The dashboard is the layer around the portals.')
assert_before('The controller is not the whole operating surface. The dashboard is the layer around the portals.', 'Augmentl Dashboard matters because the app is not the whole operating surface.')
assert_before('Augmentl Dashboard matters because the app is not the whole operating surface.', 'The same system can expose a dedicated portals dashboard without the rest of the Augmentl workspace.')
assert_before('The same system can expose a dedicated portals dashboard without the rest of the Augmentl workspace.', 'The dashboard adds project and install context that the controller app should not have to carry.')

# Operating loop framing is explicit.
assert_contains('Observe. Diagnose. Act. Learn.')
assert_contains('Diagnose across layers')

# App preview tabs remain in order.
for title in [
    'Live status at a glance.',
    'Camera setup and monitoring, built into the controller.',
    'Full LED display control.',
    'Deep hardware visibility.',
    'Power, UPS state, and operating cost in one tab.',
    'An operational timeline, not a mystery.',
    'Audience-visible uptime, separated from raw process uptime.',
    'Portal settings and hardware identity in one place.',
]:
    assert_contains(title)

# Future work covers client-facing views and the PC-side installation layer.
assert_contains('Limited client-facing portal views')
assert_contains('A future scoped client view can let each site or stakeholder see only its own portal status, health summary, and a tightly limited set of permitted actions.')
assert_contains('More reproducible portal-side runtime')
assert_contains('Scoped actions like blank or blur for their own screen only')

# Ending business framing is partnership/governance aware.
assert_contains("Access, hosting, and data handling can be structured to fit Portals' needs.")
assert_contains('class="slide slide-centered-stage">')
assert_contains('class="slide slide-centered-stage ask-slide">')
assert_contains('partner-managed, or otherwise agreed')
assert_contains('Adopt <span class="scope-brand">Scope</span> for the portal network as a shared operational platform, developed and operated in partnership.')
assert_contains('Why adopting <span class="scope-brand">Scope</span> is strategically stronger for Portals.')
assert_contains('Agree the operating model: who hosts what, who manages access, and which layers stay portal-owned versus partner-managed')

# End slide and smooth transitions remain present.
assert_contains('id="end-globe-static"')
assert_contains('id="end-globe-frame"')
assert_contains('class="end-panel"')
assert_contains("scrollIntoView({ behavior: 'smooth', block: 'start' })")
assert_contains("document.addEventListener('wheel'")

print('presentation flow assertions passed')
