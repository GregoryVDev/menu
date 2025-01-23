# Créatop, de la fenêtre principale et de la zone de texte
from tkinter import *

class PyEditor:
    def __init__(self, master):
        self.master = master

    def create_window(self):
        self.master.title("Nouveau document - Editeur de texte")
        self.master.geometry("1200x700")

    def create_textarea(self):
        self.textarea = Text(self.master, font=("ubuntu", 18))


# Condition spéciale utilisée pour contrôler l'exécution d'un script
if __name__ == "__main__":
    master = Tk()
    editor = PyEditor(master)
    editor.create_window()


    master.mainloop()
