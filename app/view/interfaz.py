import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QLineEdit, QPushButton,
                            QTabWidget, QComboBox, QTimeEdit, QMessageBox,
                            QTableWidget, QTableWidgetItem, QGroupBox, QFormLayout)
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtGui import QFont, QIcon
from datetime import datetime, time
from app.model.study import Estudio, Usuario, GrupoDeEstudio

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.estudio = Estudio()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sistema de Estudio')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QTabWidget {
                background-color: white;
            }
            QTabWidget::pane {
                border: 1px solid #cccccc;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #e0e0e0;
                padding: 8px 20px;
                margin: 2px;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: none;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
                min-width: 250px;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
            QLabel {
                color: #333333;
                font-size: 14px;
                font-weight: bold;
            }
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #ddd;
                border-radius: 8px;
                margin-top: 1ex;
                padding: 15px;
            }
            QComboBox {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
                min-width: 250px;
            }
            QTimeEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
                min-width: 250px;
            }
        """)

        # Widget central y layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Crear pestañas
        tabs = QTabWidget()
        tabs.addTab(self.crear_tab_registro(), "Registro de Estudiante")
        tabs.addTab(self.crear_tab_grupos(), "Grupos de Estudio")
        tabs.addTab(self.crear_tab_calendario(), "Calendario")

        layout.addWidget(tabs)

    def crear_tab_registro(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Grupo de registro
        grupo_registro = QGroupBox("Registro de Estudiante")
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        # Campos de entrada con etiquetas
        self.nombre_input = QLineEdit()
        self.correo_input = QLineEdit()
        self.id_input = QLineEdit()
        self.carrera_input = QLineEdit()
        self.semestre_input = QLineEdit()

        # Añadir campos al layout con sus etiquetas
        form_layout.addRow("Nombre completo:", self.nombre_input)
        form_layout.addRow("Correo electrónico:", self.correo_input)
        form_layout.addRow("ID:", self.id_input)
        form_layout.addRow("Carrera:", self.carrera_input)
        form_layout.addRow("Semestre actual:", self.semestre_input)

        # Botón de registro en un contenedor horizontal para centrarlo
        btn_container = QHBoxLayout()
        btn_registrar = QPushButton("Registrar")
        btn_registrar.clicked.connect(self.registrar_estudiante)
        btn_container.addStretch()
        btn_container.addWidget(btn_registrar)
        btn_container.addStretch()

        form_layout.addRow(btn_container)

        grupo_registro.setLayout(form_layout)
        layout.addWidget(grupo_registro)
        layout.addStretch()
        tab.setLayout(layout)
        return tab

    def crear_tab_grupos(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Grupo de creación de grupos
        grupo_crear = QGroupBox("Crear Grupo de Estudio")
        form_layout = QFormLayout()
        form_layout.setSpacing(15)

        self.nombre_grupo_input = QLineEdit()
        self.tematica_input = QLineEdit()
        self.modalidad_combo = QComboBox()
        self.modalidad_combo.addItems(["Presencial", "Virtual", "Híbrido"])
        self.horario_input = QTimeEdit()

        # Añadir campos al layout con sus etiquetas
        form_layout.addRow("Nombre del grupo:", self.nombre_grupo_input)
        form_layout.addRow("Temática:", self.tematica_input)
        form_layout.addRow("Modalidad:", self.modalidad_combo)
        form_layout.addRow("Horario:", self.horario_input)

        # Botón de crear grupo
        btn_container = QHBoxLayout()
        btn_crear_grupo = QPushButton("Crear Grupo")
        btn_crear_grupo.clicked.connect(self.crear_grupo)
        btn_container.addStretch()
        btn_container.addWidget(btn_crear_grupo)
        btn_container.addStretch()

        form_layout.addRow(btn_container)

        grupo_crear.setLayout(form_layout)
        layout.addWidget(grupo_crear)
        layout.addStretch()
        tab.setLayout(layout)
        return tab

    def crear_tab_calendario(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Grupo del calendario
        grupo_calendario = QGroupBox("Calendario de Eventos")
        calendario_layout = QVBoxLayout()

        # Aquí puedes agregar la implementación del calendario
        label = QLabel("Próximos eventos")
        label.setAlignment(Qt.AlignCenter)
        calendario_layout.addWidget(label)

        grupo_calendario.setLayout(calendario_layout)
        layout.addWidget(grupo_calendario)
        layout.addStretch()
        tab.setLayout(layout)
        return tab

    def registrar_estudiante(self):
        try:
            nombre = self.nombre_input.text()
            correo = self.correo_input.text()
            id_estudiante = int(self.id_input.text())
            carrera = self.carrera_input.text ()
            semestre = int(self.semestre_input.text())

            if self.estudio.registrar_estudiante(nombre, id_estudiante, correo, carrera, semestre):
                QMessageBox.information(self, "Éxito", "Estudiante registrado correctamente")
                # Limpiar campos
                for widget in [self.nombre_input, self.correo_input, self.id_input,
                             self.carrera_input, self.semestre_input]:
                    widget.clear()
            else:
                QMessageBox.warning(self, "Error", "No se pudo registrar el estudiante")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, verifica los datos ingresados")

    def crear_grupo(self):
        try:
            nombre = self.nombre_grupo_input.text()
            tematica = self.tematica_input.text()
            modalidad = self.modalidad_combo.currentText()
            horario = self.horario_input.time().toPyTime()

            if self.estudio.registrar_grupo_de_estudio(nombre, tematica, modalidad, horario):
                QMessageBox.information(self, "Éxito", "Grupo creado correctamente")
                # Limpiar campos
                self.nombre_grupo_input.clear()
                self.tematica_input.clear()
            else:
                QMessageBox.warning(self, "Error", "No se pudo crear el grupo")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al crear el grupo: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())