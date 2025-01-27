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


    # Faire une fonction pour copier
    def copy(self):
        pass


    # Faire une fonction pour couper
    def cut(self):
        pass


    # Faire une fonction pour coller
    def paste(self):
        pass


    def selectAll(self):
        pass

    # Faire une fonction pour ajouter un menu
    def add_menu(self):

        # Créer une barre de menu
        barMenu = Menu(self.master)

        # Configurer la barre menu et la mettre à jour dans la fenêtre principale
        self.master.config(menu = barMenu)

        # La barre de menu qui aura comme police ubuntu et en 14px (tearoff false permet que le menu ne soit plus détaché (--------------)
        filesMenu = Menu(barMenu, font=("ubuntu", 14), tearoff=False)

        # Afficher dans le menu les onglets :
        filesMenu.add_command(label = "Nouveau document", accelerator="Ctrl+N", command = self.new_document)
        filesMenu.add_command(label = "Ouvrir document", accelerator="Ctrl+O", command = self.open_document)
        # Ajouter une ligne pour séparer entre "ouvrir document" et "enregistrer sous"
        filesMenu.add_separator()
        filesMenu.add_command(label = "Enregistrer sous", accelerator="Ctrl+Shift+S", command = self.save_as)
        filesMenu.add_command(label = "Enregistrer", accelerator="Ctrl+S", command = self.save)
        filesMenu.add_separator()
        filesMenu.add_command(label = "Fermer", accelerator="Ctrl+F", command = self.close_document)

        # Créer un nouveau menu de type hiérarchique en associant un menu donné à un menu parent (permet d'afficher "fichier" comme onglet)
        barMenu.add_cascade(label = "Fichier", menu = filesMenu)


        # Menu Edition (tearoff false permet que le menu ne soit plus détaché (--------------)
        editionMenu = Menu(barMenu, font=("ubuntu", 14), tearoff=False )

        editionMenu.add_command(label="Copier", accelerator="Ctrl+C", command=self.copy)
        editionMenu.add_command(label="Couper", accelerator="Ctrl+X", command=self.cut)
        # Ajouter une ligne pour séparer entre "ouvrir document" et "enregistrer sous"
        editionMenu.add_separator()
        editionMenu.add_command(label="Coller", accelerator="Ctrl+V", command=self.paste)
        editionMenu.add_separator()
        editionMenu.add_command(label="Selectionner tout", accelerator="Ctrl+A", command=self.selectAll)


        # Permet d'afficher "edition" comme onglet
        barMenu.add_cascade(label = "Edition", menu = editionMenu)




# Condition spéciale utilisée pour contrôler l'exécution d'un script
if __name__ == "__main__":
    master = Tk()
    editor = PyEditor(master)
    editor.create_window()
    # Permet d'écrire sur la fenêtre
    editor.create_textarea()
    # Permet d'afficher la barMenu
    editor.add_menu()


    master.mainloop()
