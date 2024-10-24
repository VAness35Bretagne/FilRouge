# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:35:08 2024

@author: Formation
"""

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel

class Compteur:
    def __init__(self, label: QLabel):
        self.timer = QTimer()
        self.time_elapsed = 0
        self.label = label  # Référence au QLabel qui affichera le temps
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.time_elapsed = 0
        self.timer.start(1000)  # Met à jour le chrono toutes les secondes
        self.update_label()  # Met à jour l'affichage dès le début

    def stop(self):
        self.timer.stop()

    def update_time(self):
        self.time_elapsed += 1
        self.update_label()  # Met à jour l'affichage à chaque seconde

    def update_label(self):
        self.label.setText(f"Temps : {self.time_elapsed} s")