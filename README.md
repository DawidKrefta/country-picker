# Country Picker

A simple PyQt6 application for selecting and displaying country names, with asynchronous data loading and MVC architecture.

## Features

- Fetches and displays a sorted list of countries from an online API
- Responsive GUI using background threading
- MVC-inspired code structure
- Command-line option to pre-select a country
- Unit tests for API integration

## Requirements

- Tested with Python 3.12.10
- See [requirements.txt](requirements.txt) for dependencies

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/country-picker.git
    cd country-picker
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the application:
```sh
python -m country_picker
```

Optionally, pre-select a country:
```sh
python -m country_picker --select Germany
```

## Project Structure

```
country-picker/
├── country_picker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── api.py
│   ├── controller.py
│   ├── loader.py
│   ├── main.py
│   └── ui.py
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```

- `country_picker/` – Application source code
- `tests/` – Unit tests

## Testing

Run all tests with:
```sh
python -m pytest
```

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Dawid Krefta
