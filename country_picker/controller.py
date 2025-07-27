from .ui import MainWindow
from .loader import CountryLoader


class AppController:
    def __init__(self, window: MainWindow, selected_country: str | None = None):
        self.window = window
        self.selected_country = selected_country
        self._connect_signals()
        self._start_background_load()

    def _connect_signals(self):
        self.window.combo_box.currentTextChanged.connect(self._on_country_selected)

    def _on_country_selected(self, country_name: str):
        self.window.label.setText(country_name)

    def _start_background_load(self):
        self.loader = CountryLoader()
        self.loader.countries_loaded.connect(self._on_countries_loaded)
        self.loader.error_occurred.connect(self._on_loading_error)
        self.loader.start()

    def _on_countries_loaded(self, countries: list[tuple[str, str]]):
        self.window.combo_box.clear()
        # countries: list of (name, alpha2)
        country_names = [name for name, _ in countries]
        self.window.combo_box.addItems(country_names)
        self.window.combo_box.setCurrentIndex(-1)
        self.window.label.setText("")

        if self.selected_country:
            index = self.window.combo_box.findText(self.selected_country)
            if index >= 0:
                self.window.combo_box.setCurrentIndex(index)
            else:
                self.window.label.setText(f'Country "{self.selected_country}" not found.')

    def _on_loading_error(self, message: str):
        self.window.label.setText(f"Failed to load countries: {message}")
