import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QTextEdit,
)


class MacroPEapp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MacroPE - Ana Ekran")
        self.resize(800, 600)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1100, 800)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.create_file_selection()
        self.create_basic_info()
        self.create_feature_grid()
        self.create_log_area()

        with open("assets/style.qss", "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def create_file_selection(self):
        self.top_layout = QHBoxLayout()

        label = QLabel("Dosya Adı: ")
        self.top_layout.addWidget(label)

        self.dosya_yolu = QLineEdit()
        self.dosya_yolu.setReadOnly(True)
        self.top_layout.addWidget(self.dosya_yolu)

        buton = QPushButton("📁 Dosya Seç")
        self.top_layout.addWidget(buton)
        buton.clicked.connect(self.browse_file)

        self.main_layout.addLayout(self.top_layout)

    def create_basic_info(self):

        self.info_layout = QHBoxLayout()

        label = QLabel("Dosya Tipi: ")
        self.info_layout.addWidget(label)

        self.dosya_tipi = QLineEdit()
        self.dosya_tipi.setReadOnly(True)
        self.info_layout.addWidget(self.dosya_tipi)

        label2 = QLabel("Dosya Boyutu: ")
        self.info_layout.addWidget(label2)

        self.dosya_boyutu = QLineEdit()
        self.dosya_boyutu.setReadOnly(True)
        self.info_layout.addWidget(self.dosya_boyutu)

        label3 = QLabel("Entry Point: ")
        self.info_layout.addWidget(label3)

        self.entry_point = QLineEdit()
        self.entry_point.setReadOnly(True)
        self.info_layout.addWidget(self.entry_point)

        self.main_layout.addLayout(self.info_layout)

    def create_feature_grid(self):
        self.grid_layout = QGridLayout()

        btn_info = QPushButton("Dosya Bilgisi")
        btn_hex = QPushButton("Hex Görünümü")
        btn_strings = QPushButton("Dizgeler")
        btn_imports = QPushButton("İçe Aktarılanlar")

        self.grid_layout.addWidget(btn_info, 0, 0)
        self.grid_layout.addWidget(btn_hex, 0, 1)
        self.grid_layout.addWidget(btn_strings, 1, 0)
        self.grid_layout.addWidget(btn_imports, 1, 1)

        self.main_layout.addLayout(self.grid_layout)

    def create_log_area(self):
        self.log_ekrani = QTextEdit()
        self.log_ekrani.setReadOnly(True)

        self.main_layout.addWidget(self.log_ekrani)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "PE Dosyası Seç", "", "Çalıştırılabilir Dosyalar (*.exe *.dll)"
        )

        if file_path:
            self.dosya_yolu.setText(file_path)
            self.log_ekrani.append(f"Seçilen dosya: {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MacroPEapp()
    window.show()
    sys.exit(app.exec())
