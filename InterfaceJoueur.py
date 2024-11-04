# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:08:52 2024

@author: Formation
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

from PyQt5.QtWidgets import QMessageBox
import compteur as comp
from PyQt5.QtWidgets import QLabel, QVBoxLayout
import CaseClass as CC

class Interfacejoueur(QWidget):
    
    def __init__(self, niveau='débutant'):
        super().__init__()
      
        self.niveau=niveau
        self.setWindowTitle(f"Demineur - Niveau {niveau.capitalize()}")
        
        # Création de l'interface utilisateur
        layout_principal = QVBoxLayout()
        self.label_compteur = QLabel("Temps : 0 s")
        layout_principal.addWidget(self.label_compteur)
        
        self.compteur = comp.Compteur(self.label_compteur)  # Initialisation du compteur
        self.compteur.start()  # Démarrage du chrono
        
        self.grille = CC.Case(niveau)
        self.boutons = []
        self.drapeaux = [[False for _ in range(self.grille.nb_colonnes)] for _ in range(self.grille.nb_lignes)]
        
        self.premier_clic = True  # Attribut pour vérifier le premier clic

        # Layout pour la grille des boutons
        self.grid_layout = QGridLayout()
        layout_principal.addLayout(self.grid_layout)  # Ajoute la grille dans le layout principal
        
        self.setLayout(layout_principal)
        self.setup_bouton()  # Crée les boutons, même si ils sont vides au départ
        
        #Comptage des drapeaux
        self.label_drapeaux = QLabel(f"Drapeaux restants : {self.grille.nombre_de_bombes}")
        layout_principal.addWidget(self.label_drapeaux)  # Ajoute le label dans le layout principal

        
    def setup_bouton(self):
        """
        Crée et initialise les boutons pour chaque case de la grille du Démineur.
    
        
        """
        for i in range(self.grille.nb_lignes):
            row = []
            for j in range(self.grille.nb_colonnes):
                bouton = QPushButton("")  # Crée un bouton vide
                bouton.setFixedSize(40, 40)  # Taille du bouton
                # Connecte le bouton à une méthode qui révèle la case
                bouton.clicked.connect(lambda _, x=i, y=j: self.reveler_case(x, y))
                bouton.setContextMenuPolicy(Qt.CustomContextMenu)
                bouton.customContextMenuRequested.connect(lambda pos, x=i, y=j: self.poser_drapeau(x, y))
                
                self.grid_layout.addWidget(bouton, i, j)  # Ajoute le bouton au layout
                row.append(bouton)
            self.boutons.append(row)
            
    
    def poser_drapeau(self, x, y):
        if self.drapeaux[x][y]:
            self.drapeaux[x][y] = False
            self.boutons[x][y].setText("")
            self.grille.nb_bombes += 1  # Restauration du compteur de drapeaux
        else:
            self.drapeaux[x][y] = True
            self.boutons[x][y].setText("🚩")
            self.grille.nombre_de_bombes -= 1  # Décrémentation du compteur de drapeaux
            
        # Met à jour le label pour refléter le nombre de drapeaux restants
        self.label_drapeaux.setText(f"Drapeaux restants : {self.grille.nombre_de_bombes}")
        
    # Vérifiez si le joueur a gagné
        if self.grille.nombre_de_bombes == 0:
            self.afficher_message_victoire()  

    def reveler_case(self, x, y):
        
        """
        Révèle la case spécifiée par ses coordonnées (x, y) et met à jour l'affichage.
    
        """
        #Actualisation de la grille pour le premier clique
        if self.premier_clic:
            self.grille.placer_bombe_aleatoirement((x,y)) 
            self.grille.calculer_mines_adjacentes()
            self.premier_clic = False  # Change l'état après le premier clic
        
        # Situation où la case est une bombe
        if self.grille.grille[x][y] == -1:
            positions_bombes = self.grille.All_bombes() 
            for (i, j) in positions_bombes:
                self.boutons[i][j].setText("💣")  
            self.compteur.stop()    
            self.afficher_message_defaite()
            return
            
        mines_adjacentes = self.grille.grille[x][y]
        self.boutons[x][y].setText(str(mines_adjacentes))
        
        # Appliquer la couleur en fonction du nombre de mines adjacentes
        self.appliquer_couleur(x, y, mines_adjacentes)
        
        #Cas particulier lorsque l'on révèle un 0
        if self.grille.grille[x][y] == 0:
            
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1), (1, 0), (1, 1)]
            
            for dx, dy in directions :
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.grille.nb_lignes and 0 <= ny < self.grille.nb_colonnes:
                    if self.boutons[nx][ny].text() == "":
                        self.reveler_case(nx, ny)  



    #Méthode pour l'esthétique et la compréhension du jeu
    def appliquer_couleur(self, x, y, mines_adjacentes):
            """Applique une couleur au bouton en fonction du nombre de mines adjacentes."""
            couleurs = {
                1: "blue",
                2: "green",
                3: "red",
                4: "darkblue",
                5: "darkred",
                6: "cyan",
                7: "magenta",
                8: "gray",
            }
            self.boutons[x][y].setStyleSheet(f"color: {couleurs.get(mines_adjacentes, 'black')};")
    
        
    
    def afficher_message_defaite(self):
        """Affiche un message indiquant que la partie est perdue."""
        msg = QMessageBox()
        msg.setWindowTitle("Défaite")
        msg.setText("Vous avez perdu ! Toutes les bombes ont été révélées.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        
    def afficher_message_victoire(self):
        """Affiche un message indiquant que la partie est gagné."""
        msg = QMessageBox()
        msg.setWindowTitle("Victoire")
        msg.setText("Vous avez gagné ! Toutes les bombes ont été trouvées.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
    
    

if __name__ == "__main__":
    niveau_choisi = input("Choisissez un niveau (débutant, intermédiaire, difficile) : ").lower()

    app = QApplication(sys.argv)
    interface = Interfacejoueur(niveau_choisi)  # Tu peux choisir 'débutant', 'intermédiaire', ou 'difficile'
    interface.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    