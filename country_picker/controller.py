from .ui import MainWindow
from .loader import CountryLoader


class AppController:
    def __init__(self, window: MainWindow):
        self.window = window
        self._connect_signals()
        self._start_background_load()

    def _connect_signals(self):
        self.window.combo_box.currentTextChanged.connect(
            self._on_country_selected
        )

    def _on_country_selected(self, country_name: str):
        self.window.label.setText(f"{country_name}")

    def _start_background_load(self):
        self.loader = CountryLoader()
        self.loader.countries_loaded.connect(self._on_countries_loaded)
        self.loader.error_occurred.connect(self._on_loading_error)
        self.loader.start()

    def _on_countries_loaded(self, countries: list[str]):
        self.window.combo_box.addItems(countries)
        self.window.combo_box.setCurrentIndex(-1)
        self.window.label.setText("")

    def _on_loading_error(self, message: str):
        self.window.label.setText(f"Failed to load countries: {message}")
