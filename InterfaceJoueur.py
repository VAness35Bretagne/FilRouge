# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:08:52 2024

@author: Formation
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import CaseClass as CC 
from PyQt5.QtWidgets import QMessageBox
import compteur as comp
from PyQt5.QtWidgets import QLabel, QVBoxLayout

class Fenetre(QWidget):
    
    def __init__(self, niveau='débutant'):
        super().__init__()
      
        self.setWindowTitle(f"Demineur - Niveau {niveau.capitalize()}")
        
        # Création du layout principal
        layout_principal = QVBoxLayout()
        
        # Ajoute le label du compteur
        self.label_compteur = QLabel("Temps : 0 s")
        layout_principal.addWidget(self.label_compteur)
        
        self.compteur = comp.Compteur(self.label_compteur)  # Initialisation du compteur
        self.compteur.start()  # Démarrage du chrono
        
        # Initialisation des attributs
        self.niveau = niveau
        self.grille = None
        self.boutons = []
        self.premier_clic = True  # Attribut pour vérifier le premier clic

        # Layout pour la grille des boutons
        self.grid_layout = QGridLayout()
        layout_principal.addLayout(self.grid_layout)  # Ajoute la grille dans le layout principal
        
        self.setLayout(layout_principal)
        
        # Appel initial pour créer la grille
        self.grille = CC.Case(self.niveau)
        self.setup_bouton()  # Crée les boutons, même si ils sont vides au départ

        
    def setup_bouton(self):
        """
        Crée et initialise les boutons pour chaque case de la grille du Démineur.
    
        Pour chaque cellule de la grille, cette fonction crée un bouton de taille 
        fixe (40x40 pixels) et le place dans une grille d'affichage (QGridLayout). 
        Chaque bouton est connecté à la méthode `reveler_case`, qui est appelée lorsqu'un
        bouton est cliqué. Les boutons sont stockés dans une liste.
    
        Attributs modifiés:
        -------------------
        - self.boutons : Liste contenant les boutons de la grille du Démineur.
        - self.grid_layout : Grille d'affichage qui ajoute chaque bouton à la fenêtre de jeu.
        
        """
        self.boutons = []
        for i in range(self.grille.lignes):
            row = []
            for j in range(self.grille.colonnes):
                bouton = QPushButton("")  # Crée un bouton vide
                bouton.setFixedSize(40, 40)  # Taille du bouton
                # Connecte le bouton à une méthode qui révèle la case
                bouton.clicked.connect(lambda _, x=i, y=j: self.reveler_case(x, y))
                self.grid_layout.addWidget(bouton, i, j)  # Ajoute le bouton au layout
                row.append(bouton)
            self.boutons.append(row)
            

    def reveler_case(self, x, y):
        
        """
        Révèle la case spécifiée par ses coordonnées (x, y) et met à jour l'affichage.
    
        Lors du premier clic, la fonction génère la grille avec des bombes, 
        en veillant à ne pas en placer autour de la case initialement cliquée.
        Ensuite, la fonction révèle le contenu de la case cliquée :
        - Si c'est une bombe, elle affiche une icône de bombe.
        - Sinon, elle affiche le nombre de mines adjacentes.
        Si la case contient un "0", la fonction appelle récursivement `reveler_case`
        pour révéler les cases adjacentes.
    
        Paramètres:
        -----------
        - x (int) : Coordonnée x de la case cliquée (ligne).
        - y (int) : Coordonnée y de la case cliquée (colonne).
    
        Attributs modifiés:
        -------------------
        - self.grille : Initialisée lors du premier clic (si `premier_clic` est True).
        - self.boutons : Mise à jour de l'affichage du texte des boutons, en fonction
                         du contenu des cases (bombe ou nombre de mines adjacentes).
        """
        
        if self.premier_clic:
            
            self.grille.placer_bombe_aleatoirement((x,y))  # Assure-toi que cette méthode ne place pas de bombes autour de (x, y)
            self.grille.calculer_mines_adjacentes()
            
            self.premier_clic = False  # Change l'état après le premier clic
        
        # Vérifie si la case est une bombe
        if self.grille.grille[x][y] == -1:
            # Révèle toutes les bombes en appelant la méthode All_bombes() de la classe CaseClass
            positions_bombes = self.grille.All_bombes()  # Récupère la liste des positions des bombes
            for (i, j) in positions_bombes:
                self.boutons[i][j].setText("💣")  # Affiche une bombe sur les boutons des cases où il y a une bombe
            # Affiche un message de défaite
            self.afficher_message_defaite()
            
            # Arrête le chrono
            self.compteur.stop()
            return

        self.boutons[x][y].setText(str(self.grille.grille[x][y])) #affiche le numero de la case forcément differents de 1
        
        if self.grille.grille[x][y] == 0:
            
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1), (1, 0), (1, 1)]
            
            for dx, dy in directions :
                nx, ny = x + dx, y + dy
                # Vérifie que nous ne sortons pas des limites de la grille
                if 0 <= nx < self.grille.lignes and 0 <= ny < self.grille.colonnes:
                # Révèle la case adjacente
                    
                    if self.boutons[nx][ny].text() == "":
                        self.reveler_case(nx, ny)  # Appel récursif pour révéler les cases adjacentes

    
    def afficher_message_defaite(self):
        """Affiche un message indiquant que la partie est perdue."""
        msg = QMessageBox()
        msg.setWindowTitle("Défaite")
        msg.setText("Vous avez perdu ! Toutes les bombes ont été révélées.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
    
    # def mousePressEvent(self,event):
    #     if event.button() == Qt.LeftButton:
    #         print("appui bouton gauche")
    #         print("position = " + str(event.x()) + " " + str(event.y()))
        
    #     if event.button() == Qt.RightButton:
    #         print("appui bouton droite")
    #         print("position = " + str(event.x()) + " " + str(event.y()))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre('intermédiaire')  # Tu peux choisir 'débutant', 'intermédiaire', ou 'difficile'
    fenetre.show()
    sys.exit(app.exec_())