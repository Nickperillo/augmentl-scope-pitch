from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / 'index.html'
TEXT = HTML.read_text()


def test_logo_animation_waits_until_auth_is_complete():
    assert 'function initLogoReplay()' in TEXT
    assert 'if (!isAuthed()) showAuthOverlay();\n      else {\n        initGlobe();\n        initLocalLivePreviews();\n        initLogoReplay();\n      }' in TEXT
    assert "overlay.remove();\n          initGlobe();\n          initLocalLivePreviews();\n          initLogoReplay();" in TEXT


def test_hero_globe_uses_shared_bigger_softer_masked_style():
    assert '.hero-globe-visual {' in TEXT
    assert 'right: 72px;' in TEXT
    assert 'width: 1260px;' in TEXT
    assert 'height: 1260px;' in TEXT
    assert 'mask-image: radial-gradient(circle at 54% 50%, rgba(0,0,0,0.98) 28%, rgba(0,0,0,0.96) 42%, rgba(0,0,0,0.88) 56%, rgba(0,0,0,0.62) 70%, rgba(0,0,0,0.22) 84%, transparent 100%);' in TEXT
    assert '<img id="globe-static" class="hero-globe-visual hero-globe-static"' in TEXT
    assert '<iframe id="globe-frame" class="hero-globe-visual"' in TEXT
    assert 'style="position:absolute;right:-60px;top:50%;transform:translateY(-50%);width:860px;height:860px;' not in TEXT
