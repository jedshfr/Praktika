import os
from PySide6.QtWidgets import  QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QLineEdit, QComboBox, QFormLayout
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from database import Address, TypePartner, Partner, session

# Класс для окна добавления нового партнера
class AddPartnerWindow(QDialog):

    # Инициализация окна добавления партнера
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Добавление партнера")
    
        icon_path = os.path.expanduser("D:\icon.ico")  # Путь к иконке
        self.setWindowIcon(QIcon(icon_path))

        # Поля ввода
        self.name_input = QLineEdit()
        self.name_input.setFont(QFont("Segoe UI", 12))
        self.name_input.setStyleSheet("color: #67BA80;")
        self.name_input.setMaxLength(200)  # Ограничение на длину (200 символов)
        
        self.type_combo = QComboBox()
        self.type_combo.addItems(["ОАО", "ООО", "ПАО", "ЗАО"])
        self.type_combo.setFont(QFont("Segoe UI", 12))
        self.type_combo.setStyleSheet("color: #67BA80;")
        
        self.phone_input = QLineEdit()
        self.phone_input.setFont(QFont("Segoe UI", 12))
        self.phone_input.setStyleSheet("color: #67BA80;")
        self.phone_input.setMaxLength(10)  # Ограничение на длину (10 символов)

        self.email_input = QLineEdit()
        self.email_input.setFont(QFont("Segoe UI", 12))
        self.email_input.setStyleSheet("color: #67BA80;")
        self.email_input.setMaxLength(40)  # Ограничение на длину (40 символов)
        
        self.rating_input = QLineEdit()
        self.rating_input.setFont(QFont("Segoe UI", 12))
        self.rating_input.setStyleSheet("color: #67BA80;")
        
        self.director_input = QLineEdit()
        self.director_input.setFont(QFont("Segoe UI", 12))
        self.director_input.setStyleSheet("color: #67BA80;")
        self.director_input.setMaxLength(200)  # Ограничение на длину (200 символов)

        # Поля для адреса
        self.index_input = QLineEdit()
        self.index_input.setFont(QFont("Segoe UI", 12))
        self.index_input.setStyleSheet("color: #67BA80;")
        
        self.region_input = QLineEdit()
        self.region_input.setFont(QFont("Segoe UI", 12))
        self.region_input.setStyleSheet("color: #67BA80;")
        self.region_input.setMaxLength(100)  # Ограничение на длину (100 символов)
        
        self.country_input = QLineEdit()
        self.country_input.setFont(QFont("Segoe UI", 12))
        self.country_input.setStyleSheet("color: #67BA80;")
        self.country_input.setMaxLength(100)  # Ограничение на длину (100 символов)
        
        self.street_input = QLineEdit()
        self.street_input.setFont(QFont("Segoe UI", 12))
        self.street_input.setStyleSheet("color: #67BA80;")
        self.street_input.setMaxLength(100)  # Ограничение на длину (100 символов)
        
        self.house_input = QLineEdit()
        self.house_input.setFont(QFont("Segoe UI", 12))
        self.house_input.setStyleSheet("color: #67BA80;")

        # Кнопки
        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.save_partner)
        save_button.setFont(QFont("Segoe UI", 12))
        save_button.setStyleSheet("background-color: #67BA80; color: white;")
        
        back_button = QPushButton("Вернуться назад")
        back_button.clicked.connect(self.close)
        back_button.setFont(QFont("Segoe UI", 12))
        back_button.setStyleSheet("background-color: #67BA80; color: white;")

        # Макет формы
        form_layout = QFormLayout()
        form_layout.addRow("Наименование партнера", self.name_input)
        form_layout.addRow("Тип партнера", self.type_combo)
        form_layout.addRow("ФИО директора", self.director_input)
        form_layout.addRow("Телефон", self.phone_input)
        form_layout.addRow("Email", self.email_input)
        form_layout.addRow("Рейтинг", self.rating_input)
        form_layout.addRow("Индекс", self.index_input)
        form_layout.addRow("Регион", self.region_input)
        form_layout.addRow("Город", self.country_input)
        form_layout.addRow("Улица", self.street_input)
        form_layout.addRow("Дом", self.house_input)
        
        # Макет кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(back_button)
        button_layout.addWidget(save_button)

        # Общий макет
        main_layout = QVBoxLayout(self)
        header_label = QLabel("<h2>Добавление партнера</h2>")
        header_label.setFont(QFont("Segoe UI", 18))
        header_label.setStyleSheet("color: #67BA80;")
        header_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(header_label)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    # Метод для сохранения данных партнера
    def save_partner(self):
        # Получение данных из полей ввода
        name = self.name_input.text()
        type_partner_text = self.type_combo.currentText()
        phone = self.phone_input.text()
        email = self.email_input.text()
        rating = self.rating_input.text()
        director = self.director_input.text()
        index = self.index_input.text()
        region = self.region_input.text()
        country = self.country_input.text()
        street = self.street_input.text()
        house = self.house_input.text()

        # Проверка на корректность данных
        if len(phone) != 10:
            # Выводим предупреждение, если длина номера телефона не 10 символов
            print("Номер телефона должен содержать 10 цифр")
            return
        
        if not rating.isdigit() or not index.isdigit() or not house.isdigit():
            # Проверка, что рейтинг, индекс и дом являются цифрами
            print("Рейтинг, индекс и дом должны быть числами")
            return
        
        rating = int(rating)
        index = int(index)
        house = int(house)

        # Получение или создание типа партнера
        type_partner = session.query(TypePartner).filter_by(type_partners=type_partner_text).first()
        if not type_partner:
            type_partner = TypePartner(type_partners=type_partner_text)
            session.add(type_partner)
            session.commit()

        # Проверка на существующий адрес
        existing_address = session.query(Address).filter_by(
            index=index, region=region, country=country, street=street, house=house
        ).first()

        if existing_address:
            address = existing_address  # Используем существующий адрес
        else:
            # Создание и сохранение нового адреса
            address = Address(index=index, region=region, country=country, street=street, house=house)
            session.add(address)
            session.commit()

        # Создание и сохранение партнера
        partner = Partner(
            type_partners=type_partner.id_type_partners,
            name_partners=name,
            director=director,
            phone=phone,
            email=email,
            rating=rating,
            address=address.id_address
        )
        session.add(partner)
        session.commit()

        # Обновление списка партнеров в главном окне
        self.main_window.update_partners()
        self.close()
