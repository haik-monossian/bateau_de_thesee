import tkinter as tk
from tkinter import messagebox

class ShipGUI:
    def __init__(self, root, ship):
        self.root = root
        self.ship = ship
        self.root.title("Le Paradoxe de Thésée - Gestion Complète")
        
        # Titre
        tk.Label(root, text=f"Navire : {ship.name}", font=("Arial", 14, "bold")).pack(pady=10)

        # Liste des pièces
        tk.Label(root, text="Sélectionnez une pièce ci-dessous :").pack()
        self.listbox = tk.Listbox(root, width=50, height=6)
        self.listbox.pack(pady=5)
        
        # Zone de saisie pour le matériau
        tk.Label(root, text="Nouveau matériau :").pack()
        self.entry_material = tk.Entry(root)
        self.entry_material.pack(pady=5)

        # Boutons d'action
        # Modifier par référence (change le matériau de l'objet existant)
        tk.Button(root, text="Modifier Matériau (Référence)", command=self.modify_material, bg="#e1f5fe").pack(fill="x", padx=20)
        
        # Séparateur visuel
        tk.Label(root, text="").pack()
        
        tk.Button(root, text="Événement Aléatoire", command=self.trigger_event, bg="#fff9c4").pack(fill="x", padx=20)
        tk.Button(root, text="Afficher l'Historique", command=self.show_history).pack(fill="x", padx=20, pady=5)

        self.update_list()

    def update_list(self):
        """Met à jour la liste affichée à l'écran"""
        self.listbox.delete(0, tk.END)
        for part_name, part_obj in self.ship.get_parts().items():
            self.listbox.insert(tk.END, f"{part_name} : {part_obj.material}")

    def get_selected_part_name(self):
        """Récupère le nom de la pièce sélectionnée dans la Listbox"""
        try:
            selection = self.listbox.get(self.listbox.curselection())
            return selection.split(" : ")[0]
        except:
            messagebox.showwarning("Attention", "Veuillez sélectionner une pièce dans la liste !")
            return None

    def modify_material(self):
        """Modifie le matériau de la pièce sélectionnée"""
        part_name = self.get_selected_part_name()
        new_mat = self.entry_material.get()
        
        if part_name and new_mat:
            self.ship.change_part(part_name, new_mat)
            self.update_list()
            self.entry_material.delete(0, tk.END)
        elif not new_mat:
            messagebox.showwarning("Erreur", "Veuillez entrer un matériau.")

    def trigger_event(self):
        msg = self.ship.random_event()
        messagebox.showwarning("Alerte Tempête", msg)
        self.update_list()

    def show_history(self):
        h = "\n".join(self.ship.history) if self.ship.history else "Aucune modification enregistrée."
        messagebox.showinfo("Suivi Historique", h)