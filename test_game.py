import tkinter as tk
from tkinter import messagebox

class CoasterConnections:
    def __init__(self, master):
        self.master = master
        master.title("Coaster Connections")

        self.coasters = ["Coaster A", "Coaster B", "Coaster C", "Coaster D"]
        self.selected_coasters = []

        self.instructions = tk.Label(master, text="Select a coaster and submit your guess!")
        self.instructions.pack()

        self.buttons = []
        for coaster in self.coasters:
            button = tk.Button(master, text=coaster, command=lambda c=coaster: self.select_coaster(c))
            button.pack(pady=5)
            self.buttons.append(button)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=20)

    def select_coaster(self, coaster):
        if coaster not in self.selected_coasters:
            self.selected_coasters.append(coaster)
            messagebox.showinfo("Selected", f"You selected {coaster}!")
        else:
            self.selected_coasters.remove(coaster)
            messagebox.showinfo("Deselected", f"You deselected {coaster}!")

    def submit_guess(self):
        if not self.selected_coasters:
            messagebox.showwarning("No Selection", "Please select at least one coaster.")
            return
        messagebox.showinfo("Your Guess", f"You guessed: {', '.join(self.selected_coasters)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = CoasterConnections(root)
    root.mainloop()