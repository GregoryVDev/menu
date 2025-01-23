# Créatop, de la fenêtre principale et de la zone de texte
from tkinter import *

from PIL.ImageOps import expand


class PyEditor:
    def __init__(self, master):
        self.master = master

    def create_window(self):
        self.master.title("Nouveau document - Editeur de texte")
        self.master.geometry("1200x700")

    def create_textarea(self):
        self.textarea = Text(self.master, font=("ubuntu", 18))
        # Mettre un pack pour activer la zone de text (expand permet d'étaler le texte sur toute la fenêtre et fill BOTH pour dire verticalement et horizontalement)
        self.textarea.pack(side=LEFT, expand = True, fill= BOTH)


# Condition spéciale utilisée pour contrôler l'exécution d'un script
if __name__ == "__main__":
    master = Tk()
    editor = PyEditor(master)
    editor.create_window()
    # Permet d'écrire sur la fenêtre
    editor.create_textarea()


    master.mainloop()
