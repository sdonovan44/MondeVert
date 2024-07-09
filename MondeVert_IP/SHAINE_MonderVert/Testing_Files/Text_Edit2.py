logo = r"A:\Amini Amor\SHAINE\Requests\Beta\Audio Transcript\Extracted images\2024-02-15\Shane Show\Best\1111.png"
# dynamic_gui.py
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame

class DynamicGUI(QMainWindow):
    def __init__(self, window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setWindowFlags(window_type | Qt.WindowTitleHint)
        self.setStyleSheet("background-color: lightgray;")
        self.resize(window_size[0], window_size[1])

        self.internal_frame_widgets = {}
        self.frame_data = {}

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(QLabel("Main Buttons: " + ", ".join(main_buttons)))
        main_layout.addWidget(QLabel("Main Checkboxes: " + ", ".join(main_checkboxes)))

        # Add logo image
        logo_label = QLabel()
        logo_pixmap = QPixmap(logo)
        logo_label.setPixmap(logo_pixmap)
        main_layout.addWidget(logo_label)

        for frame_config in internal_frames:
            frame_widget = self.create_frame(frame_config)
            main_layout.addWidget(frame_widget)

        continue_button = QPushButton("Continue")
        continue_button.clicked.connect(self.close_window)
        main_layout.addWidget(continue_button)

        self.setCentralWidget(main_widget)

    def create_frame(self, frame_config):
        frame_title, frame_text, frame_buttons, frame_checkboxes, frame_color = frame_config

        frame_widget = QFrame()
        frame_widget.setStyleSheet(f"background-color: {frame_color};")

        frame_layout = QVBoxLayout(frame_widget)
        frame_layout.addWidget(QLabel(frame_title))

        if frame_text:
            frame_layout.addWidget(QLabel(frame_text))

        for button_text in frame_buttons:
            button = QPushButton(button_text)
            button.clicked.connect(lambda _, btn_text=button_text: self.update_status_bar(btn_text))
            frame_layout.addWidget(button)

        for checkbox in frame_checkboxes:
            frame_layout.addWidget(QLabel(checkbox))

        self.internal_frame_widgets[frame_title] = frame_widget
        self.frame_data[frame_title] = {"frame_title": frame_title,
                                        "frame_text": frame_text,
                                        "frame_buttons": frame_buttons,
                                        "frame_checkboxes": frame_checkboxes,
                                        "frame_color": frame_color}

        return frame_widget

    def update_frame_data(self, frame_title, frame_title_new=None, frame_text=None, frame_buttons=None, frame_checkboxes=None, frame_color=None):
        frame_data = self.frame_data.get(frame_title, {})
        if frame_data:
            if frame_title_new is not None:
                frame_data["frame_title"] = frame_title_new

            if frame_text is not None:
                frame_data["frame_text"] = frame_text

            if frame_buttons is not None:
                frame_data["frame_buttons"] = frame_buttons

            if frame_checkboxes is not None:
                frame_data["frame_checkboxes"] = frame_checkboxes

            if frame_color is not None:
                frame_data["frame_color"] = frame_color

            self.frame_data[frame_title] = frame_data

    def get_frame_data(self, frame_title):
        return self.frame_data.get(frame_title, {})

    def update_status_bar(self, button_text):
        status_bar = QLabel(f"Button '{button_text}' Pressed")
        self.statusBar().addWidget(status_bar)

    def close_window(self):
        self.close()
# worker.py
from PyQt5.QtCore import QThread


class Worker(QThread):
    def __init__(self, window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames):
        super().__init__()
        self.window_title = window_title
        self.window_type = window_type
        self.window_size = window_size
        self.main_buttons = main_buttons
        self.main_checkboxes = main_checkboxes
        self.internal_frames = internal_frames
        self.dynamic_gui = None

    def run(self):
        app = QApplication([])
        self.dynamic_gui = DynamicGUI(self.window_title, self.window_type, self.window_size, self.main_buttons, self.main_checkboxes, self.internal_frames)
        self.dynamic_gui.show()
        app.exec_()

    def update_frame_data(self, frame_title, frame_title_new=None, frame_text=None, frame_buttons=None, frame_checkboxes=None, frame_color=None):
        if self.dynamic_gui:
            self.dynamic_gui.update_frame_data(frame_title, frame_title_new, frame_text, frame_buttons, frame_checkboxes, frame_color)

    def get_frame_data(self, frame_title):
        if self.dynamic_gui:
            return self.dynamic_gui.get_frame_data(frame_title)

    def close_window(self):
        if self.dynamic_gui:
            self.dynamic_gui.close()


# main.py
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    window_title = "Dynamic GUI"
    window_type = Qt.Window
    window_size = (600, 400)
    main_buttons = ["Button 1", "Button 2", "Continue"]
    main_checkboxes = ["Checkbox 1", "Checkbox 2"]
    internal_frames = [
        ("Internal Frame 1", "Some text for Frame 1", ["Frame 1 Button 1", "Frame 1 Button 2"], ["Frame 1 Checkbox 1", "Frame 1 Checkbox 2"], "lightblue"),
        ("Internal Frame 2", "Some text for Frame 2", ["Frame 2 Button 1", "Frame 2 Button 2"], ["Frame 2 Checkbox 1", "Frame 2 Checkbox 2"], "lightgreen")
    ]

    app = QApplication([])
    worker = Worker(window_title, window_type, window_size, main_buttons, main_checkboxes, internal_frames)
    worker.start()
    sys.exit(app.exec_())
