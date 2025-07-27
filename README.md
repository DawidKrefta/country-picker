# Country Picker

**Release: v1.1.0**

A simple PyQt6 application for selecting and displaying country names and flags, with asynchronous data loading, logging, and MVC architecture.

## Features

- Fetches and displays a sorted list of countries from an online API
- Displays country flags (SVG) from local assets
- Responsive GUI using background threading
- MVC-inspired code structure
- Command-line option to pre-select a country
- Release version and current date displayed in the UI
- Centralized logging to file and console
- Customizable application style via `style.qss`
- Unit tests for API integration

## Requirements

- Tested with Python 3.12.10
- See [requirements.txt](requirements.txt) for dependencies

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DawidKrefta/country-picker.git
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
├── assets/
│   └── flags/                # SVG flag files
├── country_picker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── api.py
│   ├── controller.py
│   ├── loader.py
│   ├── logger.py
│   ├── main.py
│   ├── style.qss             # Qt stylesheet for UI
│   ├── ui.py
│   └── logs/
│       └── country_picker.log
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```

- `assets/flags/` – SVG flag images
- `country_picker/` – Application source code
- `country_picker/style.qss` – Application stylesheet (colors, fonts, etc.)
- `country_picker/logs/` – Log files (created at runtime)
- `tests/` – Unit tests

## Logging

- All important events and errors are logged to `country_picker/logs/country_picker.log` and the console.
- Logging is configured in [`country_picker/logger.py`](country_picker/logger.py).

## Style Customization

- UI appearance (font, color, etc.) can be customized in [`country_picker/style.qss`](country_picker/style.qss).

## Release Version

- The current release version is tracked in [`country_picker/__init__.py`](country_picker/__init__.py) and displayed in the application window.

## Testing

Run all tests with:
```sh
python -m pytest
```

## License

This project is licensed under the [MIT License](LICENSE).

## Author

Dawid Krefta
