# Créatop, de la fenêtre principale et de la zone de texte
from tkinter import *

class PyEditor:
    def __init__(self, master):
        self.master = master

    def create_window(self):
        self.master.title("Nouveau document - Editeur de texte")
