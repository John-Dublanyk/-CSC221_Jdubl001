import pytest
from city_functions import city_country

@pytest.mark.parametrize('city', [
    'Montreal',
    'Boston',
])
def test_city_country(city):
    expected_country = {
        'Montreal': 'Canada',
        'Boston': 'USA',
    }

    result = city_country(city, expected_country[city])
    assert result == f"{city}, {expected_country[city]}", f"Expected result: {city}, {expected_country[city]}, but got {result} for city: '{city}'" 


