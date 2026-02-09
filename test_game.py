import tkinter as tk
from tkinter import messagebox
import random

class ConnectionsGame:
    def __init__(self, words, solution):
        self.words = set(words)
        self.solution = solution
        self.solved_groups = []
        self.mistakes_left = 4

    def guess(self, selected_words):
        if self.is_game_over():
            return "Game over."

        selected_words = set(selected_words)

        if len(selected_words) != 4:
            return "You must select exactly 4 words."

        for group in self.solution:
            if (
                selected_words == group["words"]
                and group not in self.solved_groups
            ):
                self.solved_groups.append(group)
                self.words -= group["words"]
                return f"✅ Correct! ({group['color']} {group['category']})"

        self.mistakes_left -= 1

        if self.mistakes_left == 0:
            return "❌ Game Over!"

        return f"❌ Incorrect. Mistakes left: {self.mistakes_left}"

    def reveal_solution(self):
        reveal_text = "🔍 SOLUTION:\n\n"
        for group in self.solution:
            reveal_text += (
                f"{group['color']} {group['category']}\n"
                f"{', '.join(sorted(group['words']))}\n\n"
            )
        return reveal_text

    def is_game_over(self):
        return self.mistakes_left == 0 or len(self.solved_groups) == 4

words = [
    "CANNIBAL",
    "MAKO",
    "PANTHERIAN",
    "HELIX",
    "SHAMBHALA",
    "EXPEDITION GEFORCE",
    "HANGTIME",
    "SHIVERING TIMBERS",
    "PANTHEON",
    "VOYAGE",
    "APOLLO'S CHARIOT",
    "WILDCAT'S REVENGE",
    "DIAMONDBACK",
    "ALPENFURY",
    "FONIX",
    "OLYMPIA LOOPING"
]

solution = [
    {
        "color": "🟨",
        "category": "B&M HYPERS",
        "words": {"MAKO", "DIAMONDBACK", "APOLLO'S CHARIOT", "SHAMBHALA"}
    },
    {
        "color": "🟩",
        "category": "OPENED IN THE 2020s",
        "words": {"PANTHEON", "ALPENFURY", "WILDCAT'S REVENGE", "FONIX"}
    },
    {
        "color": "🟦",
        "category": "TALLEST COASTER IN RESPECTIVE U.S. STATE",
        "words": {"CANNIBAL", "PANTHERIAN", "SHIVERING TIMBERS", "VOYAGE"}
    },
    {
        "color": "🟪",
        "category": "NAMES CONTAIN COASTER TERMINOLOGY",
        "words": {"HANGTIME", "HELIX", "OLYMPIA LOOPING", "EXPEDITION GEFORCE"}
    }
]

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎢 Coaster Connections")
        self.root.geometry("900x700")
        
        self.game = ConnectionsGame(words, solution)
        self.selected = []
        self.word_buttons = {}
        
        # Title
        title = tk.Label(root, text="🎢 COASTER CONNECTIONS 🎢", font=("Arial", 20, "bold"))
        title.pack(pady=10)
        
        # Status
        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
        self.status_label.pack(pady=5)
        self.update_status()
        
        # Buttons frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.create_buttons()
        
        # Control buttons
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)
        
        tk.Button(control_frame, text="Submit", command=self.submit, font=("Arial", 12), bg="green", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Clear", command=self.clear, font=("Arial", 12), bg="orange", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Shuffle", command=self.shuffle, font=("Arial", 12), bg="blue", fg="white", width=10).pack(side=tk.LEFT, padx=5)
    
    def create_buttons(self):
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        
        words_list = list(self.game.words)
        random.shuffle(words_list)
        
        self.word_buttons = {}
        for word in words_list:
            btn = tk.Button(
                self.buttons_frame,
                text=word,
                font=("Arial", 11, "bold"),
                width=25,
                height=2,
                bg="lightgray",
                command=lambda w=word: self.toggle(w)
            )
            btn.pack(pady=5)
            self.word_buttons[word] = btn
    
    def toggle(self, word):
        if word in self.selected:
            self.selected.remove(word)
            self.word_buttons[word].config(bg="lightgray")
        else:
            if len(self.selected) < 4:
                self.selected.append(word)
                self.word_buttons[word].config(bg="lightyellow")
            else:
                messagebox.showwarning("Limit", "Select exactly 4!")
    
    def submit(self):
        if len(self.selected) != 4:
            messagebox.showwarning("Error", "Select exactly 4 coasters!")
            return
        
        result = self.game.guess(self.selected)
        messagebox.showinfo("Result", result)
        
        for word in self.selected:
            if word in self.word_buttons:
                self.word_buttons[word].destroy()
        
        self.selected = []
        self.create_buttons()
        self.update_status()
        
        if self.game.is_game_over():
            if len(self.game.solved_groups) == 4:
                messagebox.showinfo("Victory!", "🎉 YOU WON! 🎉")
            else:
                messagebox.showinfo("Game Over", self.game.reveal_solution())
            self.root.quit()
    
    def clear(self):
        for word in self.selected:
            if word in self.word_buttons:
                self.word_buttons[word].config(bg="lightgray")
        self.selected = []
    
    def shuffle(self):
        self.create_buttons()
    
    def update_status(self):
        text = f"❌ Mistakes: {self.game.mistakes_left}/4  |  ✅ Groups: {len(self.game.solved_groups)}/4"
        self.status_label.config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GameGUI(root)
    root.mainloop()
