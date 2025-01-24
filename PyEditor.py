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
        self.textarea.pack(side = LEFT, expand = True, fill= BOTH)
        # Afficher le scrollbar sur la fenêtre master verticalement
        self.scroll = Scrollbar(self.master, command = self.textarea.yview())
        self.textarea.configure(yscrollcommand = self.scroll.set)
        # Permet de l'afficher à droite en vertical
        self.scroll.pack(side = RIGHT, fill = Y)


    # Faire une fonction pour créer un nouveau document
    def new_document(self):
        pass


    # Faire une fonction pour ouvrir un document
    def open_document(self):
        pass


    # Faire une fonction pour enregistrer sous
    def save_as(self):
        pass


    # Faire une fonction pour enregistrer
    def save(self):
        pass


    # Faire une fonction pour fermer
    def close_document(self):
        pass

    def add_menu(self):

        # Créer une barre de menu
        barMenu = Menu(self.master)

        # Configurer la barre menu et la mettre à jour dans la fenêtre principale
        self.master.config(menu = barMenu)

        # La barre de menu qui aura comme police ubuntu et en 14px
        filesMenu = Menu(barMenu, font=("ubuntu", 14))

        # Afficher dans le menu les onglets :
        filesMenu.add_command(label = "Nouveau document", command = self.new_document)
        filesMenu.add_command(label = "Ouvrir document", command = self.open_document)
        filesMenu.add_command(label = "Enregistrer sous", command = self.save_as)
        filesMenu.add_command(label = "Enregistrer", command = self.save)
        filesMenu.add_command(label = "Fermer", command = self.close_document)

        # Créer un nouveau menu de type hiérarchique en associant un menu donné à un menu parent
        barMenu.add_cascade(label = "Fichier", menu = filesMenu)

# Condition spéciale utilisée pour contrôler l'exécution d'un script
if __name__ == "__main__":
    master = Tk()
    editor = PyEditor(master)
    editor.create_window()
    # Permet d'écrire sur la fenêtre
    editor.create_textarea()


    master.mainloop()
