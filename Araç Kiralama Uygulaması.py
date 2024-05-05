import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QListWidget, QCalendarWidget, QTimeEdit
from PyQt6.QtCore import QDateTime

class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kullanıcı Girişi")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label_username = QLabel("Kullanıcı Adı:")
        layout.addWidget(self.label_username)

        self.entry_username = QLineEdit()
        layout.addWidget(self.entry_username)

        self.label_password = QLabel("Şifre:")
        layout.addWidget(self.label_password)

        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.entry_password)

        self.button_login = QPushButton("Giriş Yap")
        self.button_login.clicked.connect(self.login)
        layout.addWidget(self.button_login)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QLabel {
                color: #ecf0f1;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #bdc3c7;
                color: #34495e;
                font-size: 14px;
                border: 1px solid #34495e;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #3498db;
                color: #ecf0f1;
                font-size: 14px;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

    def login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        # Kullanıcı adı ve şifrenin doğruluğu kontrol ediliyor (örnek olarak sadece "admin" ve "password" kabul ediliyor)
        if username == "admin" and password == "password":
            QMessageBox.information(None, "Başarılı", "Giriş başarılı!")
            self.close()  # Giriş ekranını kapat
            self.kiralama_sistemi = KiralamaSistemiUI()  # Ana uygulamayı başlat
            self.kiralama_sistemi.show()
        else:
            QMessageBox.critical(None, "Hata", "Kullanıcı adı veya şifre hatalı!")

class Araç:
    def __init__(self, araç_id, model):
        self.araç_id = araç_id
        self.model = model
        self.kiralama_durumu = {}  # Tarihleri depolamak için bir sözlük kullanıyoruz

    def araç_durumu_güncelle(self, tarih, durum):
        self.kiralama_durumu[tarih] = durum

    def tarih_durumu_kontrol(self, tarih):
        return self.kiralama_durumu.get(tarih, "Müsait")

class KiralamaSistemiUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Araç Kiralama Sistemi")
        self.setGeometry(100, 100, 400, 400)

        self.selected_date = None
        self.selected_time = None

        layout = QVBoxLayout()

        self.label_araç = QLabel("Araçlar:")
        layout.addWidget(self.label_araç)

        self.list_widget_araçlar = QListWidget()
        layout.addWidget(self.list_widget_araçlar)

        self.calendar_widget = QCalendarWidget()
        self.calendar_widget.clicked.connect(self.select_date)
        layout.addWidget(self.calendar_widget)

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.timeChanged.connect(self.select_time)
        layout.addWidget(self.time_edit)

        self.button_kiralama = QPushButton("Kiralama Yap")
        self.button_kiralama.clicked.connect(self.make_reservation)
        layout.addWidget(self.button_kiralama)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QLabel {
                color: #ecf0f1;
                font-size: 14px;
            }
            QListWidget {
                background-color: #bdc3c7;
                color: #34495e;
                font-size: 14px;
                border: 1px solid #34495e;
                border-radius: 5px;
            }
            QCalendarWidget {
                background-color: #bdc3c7;
                color: #34495e;
                font-size: 14px;
                border: 1px solid #34495e;
                border-radius: 5px;
            }
            QTimeEdit {
                background-color: #bdc3c7;
                color: #34495e;
                font-size: 14px;
                border: 1px solid #34495e;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #3498db;
                color: #ecf0f1;
                font-size: 14px;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)

        # Araçları ekleyelim
        self.araçlar = {
            "001": Araç("001", "Toyota Corolla"),
            "002": Araç("002", "Renault Clio"),
            "003": Araç("003", "Honda Civic")
        }

        for araç_id, araç in self.araçlar.items():
            self.list_widget_araçlar.addItem(f"{araç_id}: {araç.model}")

    def select_date(self, date):
        self.selected_date = date

    def select_time(self):
        self.selected_time = self.time_edit.time()

    def make_reservation(self):
        if self.selected_date is None:
            QMessageBox.critical(None, "Hata", "Lütfen bir tarih seçin!")
            return

        if self.selected_time is None:
            QMessageBox.critical(None, "Hata", "Lütfen bir saat seçin!")
            return

        if self.list_widget_araçlar.currentItem() is None:
            QMessageBox.critical(None, "Hata", "Lütfen bir araç seçin!")
            return

        araç_id = self.list_widget_araçlar.currentItem().text().split(":")[0]
        araç = self.araçlar[araç_id]

        selected_date_str = self.selected_date.toString("yyyy-MM-dd")
        selected_datetime_str = f"{selected_date_str} {self.selected_time.toString('HH:mm')}"

        # Seçilen aracın seçilen tarih ve saatte kiralanabilir olduğunu kontrol et
        if araç.tarih_durumu_kontrol(selected_date_str) == "Kiralandı":
            QMessageBox.critical(None, "Hata", "Seçilen araç zaten bu tarihte kiralanmış!")
            return

        # Kiralama işlemini gerçekleştir
        araç.araç_durumu_güncelle(selected_date_str, "Kiralandı")

        QMessageBox.information(None, "Başarılı", f"{selected_datetime_str} tarihinde {araç.model} aracı kiralandı!")

        # Başka bir kiralama yapmak isteyip istemediğini sor
        reply = QMessageBox.question(None, "Kiralama", "Başka bir kiralama yapmak ister misiniz?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.selected_date = None
            self.selected_time = None
            self.list_widget_araçlar.clearSelection()
            self.calendar_widget.setSelectedDate(QDateTime.currentDateTime().date())
            self.time_edit.setTime(QDateTime.currentDateTime().time())
        else:
            sys.exit()  # Programı kapat

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())
