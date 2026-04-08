import pytest

from calculator import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
        (-10, 4.5, -5.5),
        (1000000, 2000000, 3000000),
    ],
)
def test_add_returns_correct_result_for_multiple_numeric_cases(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b",
    [
        ("2", 3),
        (None, 1),
        ([1, 2], 5),
        ({"x": 1}, 2),
        (True, 7),
        (3, False),
    ],
)
def test_add_raises_type_error_for_invalid_arguments(a, b):
    with pytest.raises(TypeError, match="must be int or float"):
        add(a, b)


def test_add_handles_floating_point_precision_correctly():
    result = add(0.1, 0.2)
    assert result == pytest.approx(0.3, rel=1e-9, abs=1e-12)
