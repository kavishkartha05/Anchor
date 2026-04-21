from __future__ import annotations

import pytest

from anchor.decomposer import Decomposer


@pytest.fixture
def decomposer() -> Decomposer:
    # _normalize() does not call the model, so a no-op model_fn is fine.
    return Decomposer(model_fn=lambda _messages: "")


# ---------------------------------------------------------------------------
# numbered prefixes
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_normalize_strips_dot_numbered_prefix(decomposer: Decomposer) -> None:
    assert decomposer._normalize("1. question") == "question"


@pytest.mark.unit
def test_normalize_strips_paren_numbered_prefix(decomposer: Decomposer) -> None:
    assert decomposer._normalize("2) question") == "question"


# ---------------------------------------------------------------------------
# bullet prefixes
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_normalize_strips_hyphen_bullet(decomposer: Decomposer) -> None:
    assert decomposer._normalize("- question") == "question"


@pytest.mark.unit
def test_normalize_strips_asterisk_bullet(decomposer: Decomposer) -> None:
    assert decomposer._normalize("* question") == "question"


# ---------------------------------------------------------------------------
# already-normalized and no-op cases
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_normalize_preserves_plain_text(decomposer: Decomposer) -> None:
    assert decomposer._normalize("plain question") == "plain question"


@pytest.mark.unit
def test_normalize_trims_surrounding_whitespace(decomposer: Decomposer) -> None:
    assert decomposer._normalize("   plain question   ") == "plain question"


@pytest.mark.unit
def test_normalize_handles_padded_prefix(decomposer: Decomposer) -> None:
    # The helper strips the outer whitespace first, then the list prefix.
    assert decomposer._normalize("   2) padded query  ") == "padded query"


# ---------------------------------------------------------------------------
# blank / whitespace-only input
# ---------------------------------------------------------------------------


@pytest.mark.unit
@pytest.mark.parametrize("blank", ["", " ", "   ", "\t", "\n", "\t\n  "])
def test_normalize_returns_empty_string_for_blank_input(
    decomposer: Decomposer, blank: str
) -> None:
    assert decomposer._normalize(blank) == ""
