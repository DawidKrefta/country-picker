from PyQt6.QtWidgets import (
    QWidget, QLabel, QComboBox, QVBoxLayout, QMainWindow, QSizePolicy
)
from PyQt6.QtSvgWidgets import QSvgWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Country Picker")
        self._init_ui()

    def _init_ui(self):
        self.combo_box = QComboBox()
        self.flag_label = QSvgWidget()
        self.flag_label.setMinimumHeight(64)
        self.flag_label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.flag_label)
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)