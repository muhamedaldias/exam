"""Expose LANG / RTL / T to every template (student pages use them)."""
from .lang import STRINGS, get_lang


def language(request):
    code = get_lang(request)
    path = request.path or "/"
    # Language toggle is scoped to student-facing pages.
    show_toggle = not (
        path.startswith("/teacher")
        or path.startswith("/accounts")
        or path.startswith("/admin")
        or path.startswith("/static")
    )
    return {
        "LANG": code,
        "RTL": code == "ar",
        "T": STRINGS[code],
        "SHOW_LANG_TOGGLE": show_toggle,
    }
