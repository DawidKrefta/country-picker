import requests
from typing import List
import traceback


def fetch_sorted_country_names() -> List[str]:
    """
    Fetches country names from the API and returns them sorted alphabetically.

    Returns:
        List[str]: A list of country names.

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

    country_names = [country.get("name") for country in data if "name" in country]
    return sorted(country_names)