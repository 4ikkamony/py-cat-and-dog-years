import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("cat", "dog"),
        (1, "dog"),
        ("cat", 1),
        (2.3, 4.3),
        (1, 10.2),
        (4.3, 1),
        (None, None),
        (1, None),
        (None, 1),
    ]
)
def test_should_raise_type_error_when_arguments_are_not_integers(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 1),
        (1, -1),
        (-1, -1),
        (-10, 1),
        (1, -10),
        (-10, -10)
    ]
)
def test_should_raise_value_error_with_negative_arguments(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (0, 1),
        (1, 0),
        (0, 0),
    ]
)
def test_should_raise_value_error_when_arguments_are_0(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (1, 1),
        (3, 10),
        (13, 3),
        (1, 14),
        (14, 1),
        (14, 14),
    ]
)
def test_human_years_should_be_0_for_animal_age_below_15(
    cat_age: int,
    dog_age: int
) -> None:
    cat_to_human, dog_to_human = get_human_age(cat_age, dog_age)
    assert cat_to_human == 0 and dog_to_human == 0, (
        "Human years must be 0 for animal ages < 15"
    )


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15, 15),
        (18, 22),
        (23, 16),
        (15, 23),
        (23, 15),
        (23, 23),
    ]
)
def test_human_years_should_be_1_for_animal_ages_from_15_to_24(
    cat_age: int,
    dog_age: int
) -> None:
    cat_to_human, dog_to_human = get_human_age(cat_age, dog_age)
    assert cat_to_human == 1 and dog_to_human == 1, (
        "Human years must be 0 for animal ages < 24"
    )


@pytest.mark.parametrize(
    "dog_age,expected",
    [
        (24, 2),
        (27, 2),
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (98, 16),
        (99, 17),
    ]
)
def test_dog_to_human_years_calculation_age_24_and_after(
    dog_age: int, expected: int
) -> None:
    _, dog_to_human = get_human_age(1, dog_age)
    assert dog_to_human == expected, (
        "Every 5 years after dog age == 24 should count as a human year"
    )


@pytest.mark.parametrize(
    "cat_age,expected",
    [
        (24, 2),
        (27, 2),
        (28, 3),
        (31, 3),
        (32, 4),
        (33, 4),
        (99, 20),
        (100, 21),
    ]
)
def test_cat_to_human_years_calculation_age_24_and_after(
    cat_age: int,
    expected: int
) -> None:
    cat_to_human, _ = get_human_age(cat_age, 1)
    assert cat_to_human == expected, (
        "Every 4 years after cat age == 24 should count as a human year"
    )
