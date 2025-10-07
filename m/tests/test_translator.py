from src.components.translator import translate


def test_translate_simple():
    assert "translated" in translate("hello", "en", "es")
