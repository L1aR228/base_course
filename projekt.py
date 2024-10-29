import sys
import numpy as np
from PIL import Image, ImageFilter
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog,
    QLabel, QVBoxLayout, QWidget, QPushButton,
    QHBoxLayout
)
from PyQt6.QtGui import QPixmap, QImage, QColor
from PyQt6.QtCore import Qt

class PhotoEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Фоторедактор")  # Название окна
        self.setGeometry(100, 100, 800, 600)  # Размеры окна

        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.initUI()  # Инициализация интерфейса
        self.image = None  # Переменная для хранения изображения
        self.history = []  # Стек для хранения истории изменений

    def initUI(self):
        # Меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Файл")
        stylesMenu = menubar.addMenu("Стили")

        # Действие открытия файла
        openAction = QAction("Открыть", self)
        openAction.triggered.connect(self.openImage)
        fileMenu.addAction(openAction)

        # Действие сохранения файла
        saveAction = QAction("Сохранить", self)
        saveAction.triggered.connect(self.saveImage)
        fileMenu.addAction(saveAction)

        # Действие выхода
        exitAction = QAction("Выход", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Действие для выделения контуров
        contourAction = QAction("Контур", self)
        contourAction.triggered.connect(self.applyContour)
        stylesMenu.addAction(contourAction)

        contourAction1 = QAction("Тиснение", self)
        contourAction1.triggered.connect(self.EMBOSS)
        stylesMenu.addAction(contourAction1)

        contourAction6 = QAction("Инверсия цветов", self)
        contourAction6.triggered.connect(self.invertColors)
        stylesMenu.addAction(contourAction6)

        contourAction7 = QAction("Черно белый", self)
        contourAction7.triggered.connect(self.black_white)
        stylesMenu.addAction(contourAction7)

        contourAction2 = QAction("Гладкость", self)
        contourAction2.triggered.connect(self.SMOOTH1)
        stylesMenu.addAction(contourAction2)
        # Основной макет
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.imageLabel)

        contourAction5 = QAction("Повышенная гладкость", self)
        contourAction5.triggered.connect(self.SMOOTH2)
        stylesMenu.addAction(contourAction5)

        contourAction9 = QAction("Стереопара", self)
        contourAction9.triggered.connect(self.makeAnaglyph)
        stylesMenu.addAction(contourAction9)


        # Основной макет
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.imageLabel)

        contourAction3 = QAction("Четкость", self)
        contourAction3.triggered.connect(self.EDGE_EHNACE_MORE1)
        stylesMenu.addAction(contourAction3)

        contourAction4 = QAction("Повышанная четкость", self)
        contourAction4.triggered.connect(self.EDGE_EHNACE_MORE1)
        stylesMenu.addAction(contourAction4)
        # Основной макет
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.imageLabel)

        # Кнопки
        buttonLayout = QHBoxLayout()


        btnRotateLeft = QPushButton("Повернуть влево")
        btnRotateLeft.clicked.connect(self.rotateLeft)  # Поворот влево

        btnRotateRight = QPushButton("Повернуть вправо")
        btnRotateRight.clicked.connect(self.rotateRight)  # Поворот вправо

        btnUndo = QPushButton("Отмена")
        btnUndo.clicked.connect(self.come_back)  # Отмена изменений

        buttonLayout.addWidget(btnRotateLeft)
        buttonLayout.addWidget(btnRotateRight)
        buttonLayout.addWidget(btnUndo)  # Добавление кнопки отмены

        mainLayout.addLayout(buttonLayout)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)
    def makeAnaglyph(self):
        """Создание анаглифа из изображения."""
        if self.image is not None:
            self.saveState()
            try:
                pil_image = self.qimageToPIL(self.image)
                delta = 10  # смещение для создания анаглифа
                anaglyph_image = self.createAnaglyph(pil_image, delta)
                self.image = self.PILtoQImage(anaglyph_image)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            except Exception as e:
                print(f"Ошибка при создании анаглифа: {e}")

    def createAnaglyph(self, image, delta):
        """Создание анаглифа с использованием PIL."""
        x, y = image.size
        result_image = Image.new('RGB', (x, y))  # Создаем новое изображение для анаглифа
        pixels = image.load()
        result_pixels = result_image.load()

        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j][:3]  # Извлекаем RGB
                if i < delta:
                        result_pixels[i, j] = (0, g, b)  # Заменяем R на 0
                else:
                        # Переносим красный цвет с учетом смещения
                    r_shifted = pixels[i - delta, j][0] if i - delta >= 0 else 0
                    result_pixels[i, j] = (r_shifted, g, b)

        return result_image



    def openImage(self):
        # Открытие изображения
        fileName, _ = QFileDialog.getOpenFileName(self, "Открыть файл изображения")
        if fileName:  # Проверяем, что файл был выбран
            self.image = QImage(fileName)
            self.history.clear()  # Очистка истории при открытии нового изображения
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))

    def applyContour(self):
        # Применение фильтра контура
        self.saveState()
        if self.image is not None:
            try:
                pil_image = self.qimageToPIL(self.image)
                contoured_image = pil_image.filter(ImageFilter.CONTOUR)
                self.image = self.PILtoQImage(contoured_image)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            except Exception as e:
                print(f"Ошибка при применении фильтра: {e}")
    def EMBOSS(self):
        # Применение фильтра контура
        self.saveState()
        if self.image is not None:
            try:
                pil_image = self.qimageToPIL(self.image)
                contoured_image = pil_image.filter(ImageFilter.EMBOSS)
                self.image = self.PILtoQImage(contoured_image)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            except Exception as e:
                print(f"Ошибка при применении фильтра: {e}")

    def SMOOTH1(self):
        # Применение фильтра контура
        self.saveState()
        if self.image is not None:
            try:
                pil_image = self.qimageToPIL(self.image)
                contoured_image = pil_image.filter(ImageFilter.SMOOTH)
                self.image = self.PILtoQImage(contoured_image)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            except Exception as e:
                print(f"Ошибка при применении фильтра: {e}")
    def SMOOTH2(self):
        # Применение фильтра контура
        self.saveState()
        if self.image is not None:
            try:
                pil_image = self.qimageToPIL(self.image)
                contoured_image = pil_image.filter(ImageFilter.SMOOTH_MORE)
                self.image = self.PILtoQImage(contoured_image)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            except Exception as e:
                print(f"Ошибка при применении фильтра: {e}")
    def EDGE_EHNACE_MORE1(self):
        # Применение фильтра контура
        self.saveState()
        if self.image is not None:
            try:
                pil_image = self.qimageToPIL(self.image)
                contoured_image = pil_image.filter(ImageFilter.EDGE_ENHANCE)
                self.image = self.PILtoQImage(contoured_image)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            except Exception as e:
                print(f"Ошибка при применении фильтра: {e}")
    def EDGE_EHNACE_MORE2(self):
        # Применение фильтра контура
        self.saveState()
        if self.image is not None:
            try:
                pil_image = self.qimageToPIL(self.image)
                contoured_image = pil_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
                self.image = self.PILtoQImage(contoured_image)
                self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
            except Exception as e:
                print(f"Ошибка при применении фильтра: {e}")

    def saveImage(self):
        # Сохранение изображения
        if self.image is not None:
            fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить файл изображения")
            if fileName:
                self.image.save(fileName)

    def saveState(self):
        # Сохранение текущего состояния изображения в историю
        if self.image is not None:
            self.history.append(self.image.copy())

    def come_back(self):
        # Отмена последнего изменения
        if self.history:
            self.image = self.history.pop()  # Извлечение последнего состояния
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))

    def invertColors(self):
        # Инвертирование цветов изображения
        self.saveState()  # Сохранение текущего состояния
        if self.image is not None:
            for x in range(self.image.width()):
                for y in range(self.image.height()):
                    color = self.image.pixelColor(x, y)
                    invertedColor = QColor(255 - color.red(), 255 - color.green(), 255 - color.blue())
                    self.image.setPixelColor(x, y, invertedColor)
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))

    def black_white(self):
        # Перевод изображения в градации серого
        self.saveState()  # Сохранение текущего состояния
        if self.image is not None:
            for x in range(self.image.width()):
                for y in range(self.image.height()):
                    color = self.image.pixelColor(x, y)
                    gray = (color.red() + color.green() + color.blue()) // 3
                    grayColor = QColor(gray, gray, gray)
                    self.image.setPixelColor(x, y, grayColor)
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))

    def rotateLeft(self):
        # Поворот влево на 90
        self.saveState()
        if self.image is not None:
            width = self.image.width()
            height = self.image.height()
            new_image = QImage(height, width, self.image.format())

            for x in range(width):
                for y in range(height):
                    new_image.setPixelColor(height - y - 1, x, self.image.pixelColor(x, y))

            self.image = new_image
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))


    def rotateRight(self):
        self.saveState()
        if self.image is not None:
            img = self.image
            width = img.width()
            height = img.height()
            new_image = QImage(height, width, img.format())

            for x in range(width):
                for y in range(height):
                    new_image.setPixelColor(y, width - x - 1, img.pixelColor(x, y))

            self.image = new_image
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))

    def qimageToPIL(self, img):
        """Конвертация QImage в PIL.Image."""
        img = img.convertToFormat(QImage.Format.Format_RGBA8888)
        width = img.width()
        height = img.height()
        ptr = img.bits()
        ptr.setsize(img.sizeInBytes())
        img_arr = np.array(ptr).reshape(height, width, 4)
        return Image.fromarray(img_arr, 'RGBA')

    def PILtoQImage(self, image):
        """Конвертация PIL.Image в QImage."""
        image = image.convert('RGBA')
        width, height = image.size
        data = image.tobytes()
        return QImage(data, width, height, QImage.Format.Format_RGBA8888)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhotoEditor()
    ex.show()
    sys.exit(app.exec())