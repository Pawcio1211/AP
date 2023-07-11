import sys
import requests
import json
import os
from datetime import datetime
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QLabel)
from PySide6 import QtCore, QtGui

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        # Create widgets
        self.text = QLabel("Wpisz miasto ;)",
                                     alignment=QtCore.Qt.AlignCenter)
        self.edit = QLineEdit("")
        self.button = QPushButton("Show Greetings")
        
        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(self.layout)
        
        # Add button signal to greetings slot
        self.button.clicked.connect(self.loaddata)




    def T_C(self,zmienna):
        return round((zmienna -32)/2,2)
        
    def loaddata(self):
        my_API_Kay = "KL54EKVPQVU3DR8FJCE9TN6NW"
        J_dock_name = "wyniki"
        #if not os.path.exists(f"D:\windowAP\AP\{J_dock_name}.json"):
        try:
            r =requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{self.edit.text()}/?key={my_API_Kay} ").json()
            miasto = r["address"]
            with open(f"{J_dock_name}.json","w") as f:
                json.dump(r,f)

            self.loadJson(f"{J_dock_name}.json")
        except:
            self.text.setText("Błąd w nazwie spróbuj ponownie")

    def loadJson(self, patch):
        with open(patch,'r') as f:
            data = json.load(f)

        now = datetime.now().strftime("%H:00:00")
        for i in data["days"][0]["hours"]:
            if i["datetime"] == now:
                tekst = f"""Temperatura dzisiaj: {self.T_C(i["temp"])}"""
                self.text.setText(tekst)
    



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.resize(400,300)
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())