from src.components.localizer import localize


def test_localize_simple():
    assert "localized" in localize("time", "en_US")
