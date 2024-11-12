import sys, os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func
from database import Partner, PartnerProduct, session
from new import AddPartnerWindow
from edit import EditPartnerWindow
from history import HistoryWindow

# Функция для расчета скидки партнера
def calculate_discount(partner_id):
    total_sales = (
        session.query(func.sum(PartnerProduct.count_product))
        .filter(PartnerProduct.id_partner == partner_id)
        .scalar()
    ) or 0  
    if total_sales < 10000:
        return 0
    elif 10000 <= total_sales < 50000:
        return 5
    elif 50000 <= total_sales < 300000:
        return 10
    else:
        return 15
    
# Класс для создания карточки партнера
class PartnerWidget(QWidget):
    def __init__(self, main_window, partner_type, name, director, phone, rating, discount, partner_id):
        super().__init__()
        self.main_window = main_window  
        self.partner_id = partner_id  

        # Настройка стилей для виджета
        self.setStyleSheet("""
            background-color: #F4E8D3; 
            border: 1px solid #CCCCCC; 
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        """)

        layout = QVBoxLayout(self)
        # Заголовок с типом и именем партнера
        title_label = QLabel(f"{partner_type} | {name}")
        title_label.setFont(QFont("Segoe UI", 12))
        title_label.mousePressEvent = self.open_history_window  # Открытие окна истории по клику

        # Информация о партнере
        director_label = QLabel(f"Директор: {director}")
        phone_label = QLabel(phone)
        rating_label = QLabel(f"Рейтинг: {rating}")
        discount_label = QLabel(f"Скидка: {discount}%")
        discount_label.setStyleSheet("color: #67BA80;")

        # Кнопка для редактирования партнера
        edit_button = QPushButton("Редактировать")
        edit_button.setFont(QFont("Segoe UI", 10))
        edit_button.clicked.connect(self.open_edit_window)

        top_layout = QHBoxLayout()
        top_layout.addWidget(title_label)
        top_layout.addStretch()
        top_layout.addWidget(discount_label)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(edit_button, alignment=Qt.AlignRight)

        # Добавляем компоненты в layout
        layout.addLayout(top_layout)
        layout.addWidget(director_label)
        layout.addWidget(phone_label)
        layout.addWidget(rating_label)
        layout.addLayout(bottom_layout)

    # Открытие окна истории продаж по ID партнера   
    def open_history_window(self, event):
        history_window = HistoryWindow(self.partner_id)
        history_window.exec()

    # Открытие окна редактирования партнера
    def open_edit_window(self):
        edit_window = EditPartnerWindow(self.main_window, self.partner_id)
        edit_window.exec()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список партнеров")
        main_layout = QVBoxLayout(self)

        # Заголовок
        header_label = QLabel("Список партнеров")
        header_label.setFont(QFont("Segoe UI", 18))
        header_label.setStyleSheet("color: #67BA80;")
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)

        # Устанавливаем иконку окна
        icon_path = os.path.expanduser("D:\icon.ico")
        self.setWindowIcon(QIcon(icon_path))

        # Логотип
        logo_path = os.path.expanduser("D:\icon.ico")
        self.logo_label = QLabel()
        logo_pixmap = QPixmap(logo_path).scaled(40, 40, Qt.KeepAspectRatio)
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.logo_label)

        # Прокручиваемая область для списка партнеров
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        self.partners_layout = QVBoxLayout(content_widget)
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

        # Кнопка добавления партнера
        add_partner_button = QPushButton("Добавить партнера")
        add_partner_button.setFont(QFont("Segoe UI", 12))
        add_partner_button.setStyleSheet("background-color: #67BA80; color: white;")
        add_partner_button.clicked.connect(self.open_add_partner_window)
        main_layout.addWidget(add_partner_button)

        # Обновление списка партнеров
        self.update_partners()  
        
    # Открытие окна добавления нового партнера
    def open_add_partner_window(self):
        self.add_partner_window = AddPartnerWindow(self)
        self.add_partner_window.exec_()
        
    # Обновление списка партнеров
    def update_partners(self):
        for i in reversed(range(self.partners_layout.count())):  # Удаляем старые карточки
            widget = self.partners_layout.takeAt(i).widget()
            if widget:
                widget.deleteLater()
                
        # Получаем всех партнеров
        partners = session.query(Partner).options(joinedload(Partner.type_partner)).all()  
        for partner in partners:
            
            # Рассчитываем скидку для каждого партнера
            discount = calculate_discount(partner.id_partners)  
            partner_widget = PartnerWidget(
                self,
                partner.type_partner.type_partners,
                partner.name_partners,
                partner.director,
                partner.phone,
                partner.rating,
                discount,
                partner.id_partners
            )
            # Добавляем карточку партнера
            self.partners_layout.addWidget(partner_widget)  

        # Настройка ширины окна
        self.setMinimumWidth(450)
        self.setMaximumWidth(500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
