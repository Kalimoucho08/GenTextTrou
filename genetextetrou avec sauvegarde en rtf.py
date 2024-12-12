import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import spacy
import random

# Charger le modèle français de spaCy
nlp = spacy.load("fr_core_news_sm")

class TexteATrousApp:
    def __init__(self, master):
        self.master = master
        master.title("Générateur de Texte à Trous")
        master.geometry("700x700")

        # Créer un cadre principal pour contenir les barres de défilement
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Créer des barres de défilement
        self.canvas = tk.Canvas(self.main_frame)
        self.scroll_y = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scroll_x = ttk.Scrollbar(self.main_frame, orient="horizontal", command=self.canvas.xview)

        # Créer un cadre pour le contenu
        self.content_frame = ttk.Frame(self.canvas)

        # Configurer la barre de défilement
        self.content_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Ajouter le cadre au canvas
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Pack les éléments
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configuration des barres de défilement
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)

        # Zone de texte
        self.text_label = ttk.Label(self.content_frame, text="Entrez votre texte :")
        self.text_label.pack(pady=10)
        self.text_entry = scrolledtext.ScrolledText(self.content_frame, height=10)
        self.text_entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Nombre de mots à supprimer
        self.num_words_label = ttk.Label(self.content_frame, text="Nombre de mots à supprimer :")
        self.num_words_label.pack(pady=5)
        self.num_words_entry = ttk.Entry(self.content_frame, width=10)
        self.num_words_entry.pack()

        # Types de mots à supprimer
        self.types_frame = ttk.Frame(self.content_frame)
        self.types_frame.pack(pady=10)

        self.type_vars = {
            'Noms': tk.BooleanVar(),
            'Verbes': tk.BooleanVar(),
            'Adjectifs': tk.BooleanVar(),
            'Pronoms Personnels': tk.BooleanVar(),
            'Articles/Déterminants': tk.BooleanVar(),
            'Prépositions': tk.BooleanVar()
        }

        # Disposition des cases à cocher en 2 colonnes
        row, col = 0, 0
        for word_type, var in self.type_vars.items():
            cb = ttk.Checkbutton(self.types_frame, text=word_type, variable=var)
            cb.grid(row=row, column=col, padx=5, pady=2, sticky='w')
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Sélection de la police
        self.font_label = ttk.Label(self.content_frame, text="Choisissez une police :")
        self.font_label.pack(pady=5)

        self.font_var = tk.StringVar(value="Calibri")
        self.font_menu = ttk.Combobox(self.content_frame, textvariable=self.font_var)
        self.font_menu['values'] = ["Calibri", "Arial", "Times New Roman", "Courier New"]
        self.font_menu.pack()

        # Sélection de la taille des caractères
        self.size_label = ttk.Label(self.content_frame, text="Choisissez une taille de police :")
        self.size_label.pack(pady=5)

        self.size_var = tk.IntVar(value=22)  # Taille par défaut (22 points)
        self.size_menu = ttk.Combobox(self.content_frame, textvariable=self.size_var)
        self.size_menu['values'] = [10, 12, 14, 16, 18, 20, 22, 24]
        self.size_menu.pack()

        # Bouton de génération
        self.generate_button = ttk.Button(self.content_frame, text="Générer Texte à Trous", command=self.generate_texte_a_trous)
        self.generate_button.pack(pady=10)

        # Zone de résultat
        self.result_label = ttk.Label(self.content_frame, text="Texte à trous :")
        self.result_label.pack(pady=5)

        self.result_text = scrolledtext.ScrolledText(self.content_frame, height=10)
        self.result_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Bouton de sauvegarde en RTF
        self.save_button = ttk.Button(self.content_frame, text="Sauvegarder en RTF", command=self.save_to_rtf)
        self.save_button.pack(pady=10)

    def generate_texte_a_trous(self):
        text = self.text_entry.get("1.0", tk.END).strip()

        if not text:
            messagebox.showerror("Erreur", "Veuillez entrer un texte.")
            return

        try:
            num_words = int(self.num_words_entry.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide de mots à supprimer.")
            return

        selected_types = [t for t, var in self.type_vars.items() if var.get()]

        if not selected_types:
            messagebox.showerror("Erreur", "Veuillez sélectionner au moins un type de mot à supprimer.")
            return

        doc = nlp(text)

        type_mapping = {
            'Noms': ['NOUN', 'PROPN'],
            'Verbes': ['VERB', 'AUX'],
            'Adjectifs': ['ADJ'],
            'Pronoms Personnels': ['PRON'],
            'Articles/Déterminants': ['DET'],
            'Prépositions': ['ADP']
        }

        eligible_tokens = [token for token in doc if any(token.pos_ == pos for type in selected_types for pos in type_mapping[type])]

        if num_words > len(eligible_tokens):
            num_words = len(eligible_tokens)

        tokens_to_remove = random.sample(eligible_tokens, num_words)

        result_words = []

        # Remplacement des mots par des trous proportionnels sans césure
        for token in doc:
            if token in tokens_to_remove:
                gap_length = max(1, len(token.text) * 2)  # Trou doublement proportionnel
                gap = '_' * gap_length
                result_words.append(gap)
            else:
                result_words.append(token.text)

        result_text = " ".join(result_words)

        # Afficher le texte à trous dans la zone de résultat
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result_text)

    def save_to_rtf(self):
        content = self.result_text.get("1.0", tk.END).strip()

        if not content:
            messagebox.showerror("Erreur", "Aucun texte à trous n'a été généré.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".rtf",
                                                 filetypes=[("Fichier RTF", "*.rtf")])

        if file_path:
            try:
                font_name = self.font_var.get()
                font_size = int(self.size_var.get())

                with open(file_path, 'w', encoding='utf-8') as file:
                    rtf_content = "{\\rtf1\\ansi\\ansicpg1252\\deff0\\nouicompat\\deflang1036\n"
                    rtf_content += f"{{\\fonttbl{{\\f0\\fnil {font_name};}}}}\n"
                    rtf_content += f"\\viewkind4\\uc1\\pard\\sa200\\sl276\\slmult1\\f0\\fs{font_size * 2} "

                    for char in content:
                        if ord(char) < 128:  # Caractères ASCII standard
                            rtf_content += char
                        else:  # Caractères spéciaux (accents)
                            rtf_content += f"\\u{ord(char)}?"

                    rtf_content += "\\par\n}"
                    file.write(rtf_content)

                messagebox.showinfo("Succès", f"Le fichier a été sauvegardé avec succès à l'emplacement :\n{file_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur est survenue lors de la sauvegarde :\n{str(e)}")

# Exécution de l'application
root = tk.Tk()
app = TexteATrousApp(root)
root.mainloop()
