import requests
from typing import List
import traceback


def fetch_sorted_countries() -> list[tuple[str, str]]:
    """
    Fetches country names from the API and returns them sorted alphabetically.

    Returns:
        List of (country_name, alpha2_code), sorted alphabetically by name.

    Raises:
        requests.RequestException: If the HTTP request fails.
        ValueError: If the JSON structure is not as expected.
    """
    url = "https://www.apicountries.com/countries"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        traceback.print_exc()
        print(f"Exception message: {e}")
        raise

    if not isinstance(data, list):
        raise ValueError("Unexpected JSON structure: expected a list")

    result = []
    for country in data:
        name = country.get("name")
        alpha2 = country.get("alpha2Code")
        if name and alpha2:
            result.append((name, alpha2.lower()))

    return sorted(result, key=lambda x: x[0])
