# Créatop, de la fenêtre principale et de la zone de texte
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class PyEditor:
    def __init__(self, master):
        self.master = master
        self.filename = None


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
        if len(self.textarea.get(1.0, END + '-1c')) > 0:
            message_save = messagebox.askyesno("ENREGISTRER",
                                               "L'éditeur va quitter le document ouvert, voulez-vous l'enregistrer avant d'ouvrir un autre document?")

            if message_save >0:
                self.save()
        self.textarea.delete(1.0, END)




    # Faire une fonction pour ouvrir un document
    def open_document(self):
        if len(self.textarea.get(1.0, END+ '-1c')) >0:
            message_save = messagebox.askyesno("ENREGISTRER", "L'éditeur va quitter le document ouvert, voulez-vous l'enregistrer avant d'ouvrir un autre document?")

            # Si on appuie sur yes alors on déclenche le processure d'enregistrement
            if message_save >0:
                self.save()
            # Dès qu'on enregistre notre travail, la page devient vide
            self.textarea.delete(1.0, END)

        self.filename = filedialog.askopenfilename(initialdir = "C", title = "Ouvrir un document",
                                               defaultextension = ".txt",
                                               filetypes = [("Fichier texte", "*.text"),
                                                            ("Script Python", "*.py"),
                                                            ("Script html", "*.html"),
                                                            ("Scrit Javascript", "*.js"),
                                                            # Permet de mettre une extensions pas reconnue
                                                            ("Tous fichiers", "*.*")

                                               ])


        # Si l'utilisateur a déjà choisi d'ouvrir un document
        if self.filename:
            try:
                # Ouvrir le document
                file = open(self.filename, "r")
                # Lire le contenu
                fr = file.read()
                # Fermer le document
                file.close()
                # Insérer son contenu dans la zone de text
                self.textarea.insert("1.0", fr)


            except Exception as e:
                (messagebox.showerror("Ouvrir document", e))



    # Faire une fonction pour enregistrer sous
    def save_as(self):

        try:
            file = filedialog.asksaveasfilename(initialdir = "C", title = "Enregistrer sous",
                                               initialfile = "Inserer un nom",
                                               defaultextension = ".txt",
                                               filetypes = [("Fichier texte", "*.text"),
                                                            ("Script Python", "*.py"),
                                                            ("Script html", "*.html"),
                                                            ("Scrit Javascript", "*.js"),
                                                            # Permet de mettre une extensions pas reconnue
                                                            ("Tous fichiers", "*.*")

                                               ])

            # Récupérer le contenu dans la zone du text et le mettre dans une variable (depuis le premier caractère jusqu'à la fin)
            content_file =  self.textarea.get(1.0, END)
            if file:
                # Ouvre le fichier choisi en mode écriture (il peut écraser un contenu existant s'il y a déjà un fichier au même endroit avec le même nom)
                f = open(file, "w")
                # Écrit dans le fichier le contenu récupéré de textarea
                f.write(content_file)
                # Ferme le fichier après l'avoir écrit
                f.close()
                # Met à jour une variable interne pour indiquer que le fichier est sauvegardé
                self.filename = file




        except Exception as e:
            messagebox.showerror("Exception", e)



    # Faire une fonction pour enregistrer
    def save(self):
        # Si le document enregistré a déjà un nom alors :
        if self.filename:

            try:
                # Récupère le contenu de la zone de texte (textarea) depuis la première ligne jusqu'à la fin.
                content_file = self.textarea.get(1.0, END)
                # Ouvre le fichier avec le nom donné (self.filename) en mode écriture ("w").
                # Si le fichier existe déjà, son contenu sera remplacé.
                with open(self.filename, "w") as f:
                    # Écrit le contenu récupéré dans le fichier.
                    f.write(content_file)
            # Si une erreur se produit lors de l'enregistrement, affiche un message d'erreur avec la boîte de dialogue messagebox.
            except Exception as e:
                messagebox.showerror("Exception", e)
        # Si le fichier n'a pas encore de nom (self.filename est vide ou None),
        # appelle une autre méthode (save_as) pour demander à l'utilisateur de spécifier un nom de fichier.
        else:
            self.save_as()


    # Faire une fonction pour fermer
    def close_document(self):
        if len(self.textarea.get(1.0, END+ '-1c')) >0:
            message_save = messagebox.askyesno("ENREGISTRER", "L'éditeur va quitter le document ouvert, voulez-vous l'enregistrer avant d'ouvrir un autre document?")

            # Si il n'y a pas de contenu, alors on ferme directement la page
            if save <= 0:
                self.textarea.quit()
            # Si il y a du contenu, on demande si on veut enregistrer le travail et après on quitte
            else:
                self.save()
                self.textarea.quit()


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
        filesMenu.add_command(label = "Ouvrir", accelerator="Ctrl+O", command = self.open_document)
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
