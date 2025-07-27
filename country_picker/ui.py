from PyQt6.QtWidgets import (
    QWidget, QLabel, QComboBox, QVBoxLayout, QMainWindow, QSizePolicy
)
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from . import __version__
from datetime import datetime


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

        info_text = f"Version: {__version__} | Date: {datetime.now().strftime('%Y-%m-%d')}"
        self.info_label = QLabel(info_text)
        self.info_label.setObjectName("info_label")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.flag_label)
        layout.addWidget(self.label)
        layout.addWidget(self.info_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)