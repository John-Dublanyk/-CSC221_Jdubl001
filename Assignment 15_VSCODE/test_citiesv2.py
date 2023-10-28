import pytest
from city_functionsv2 import city_country

@pytest.mark.parametrize('city, expected_country, expected_population', [
    ('Montreal', 'Canada', 36991981),
    ('Boston', 'USA', 335618149),
])
def test_city_country(city, expected_country, expected_population):
    result = city_country(city, expected_country, expected_population)
    expected_result = f"{city}, {expected_country} - population {expected_population}"
    assert result == expected_result, f"Expected result: {expected_result}, but got {result} for city: '{city}'"
