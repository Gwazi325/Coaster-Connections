import tkinter as tk
from tkinter import messagebox

class CoasterSelection:
    def __init__(self, root):
        self.root = root
        self.root.title('Coaster Selection')

        self.coasters = [
            'Coaster 1', 'Coaster 2', 'Coaster 3', 'Coaster 4',
            'Coaster 5', 'Coaster 6', 'Coaster 7', 'Coaster 8',
            'Coaster 9', 'Coaster 10', 'Coaster 11', 'Coaster 12',
            'Coaster 13', 'Coaster 14', 'Coaster 15', 'Coaster 16'
        ]
        self.selected_coasters = []

        self.create_buttons()

    def create_buttons(self):
        for index, coaster in enumerate(self.coasters):
            button = tk.Button(self.root, text=coaster, command=lambda c=coaster: self.select_coaster(c))
            button.grid(row=index // 4, column=index % 4, padx=10, pady=10, sticky='nsew')
            self.root.grid_rowconfigure(index // 4, weight=1)
            self.root.grid_columnconfigure(index % 4, weight=1)

    def select_coaster(self, coaster):
        if coaster not in self.selected_coasters:
            self.selected_coasters.append(coaster)
        else:
            self.selected_coasters.remove(coaster)

        messagebox.showinfo('Selection', f'Selected Coasters: {self.selected_coasters}')

if __name__ == '__main__':
    root = tk.Tk()
    app = CoasterSelection(root)
    root.mainloop()