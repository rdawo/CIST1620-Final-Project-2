import tkinter as tk
from tkinter import messagebox
from logic import ConnectFourGame

class ConnectFourApp:
    # builds board and programs each button/square to complete appropriate tasks
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")
        self.root.resizable(False, False)
        self.game = ConnectFourGame()
        self.buttons = []
        self.labels = []

        for col in range(7):
            # builds top row of buttons to act as drops for x's and o's
            button = tk.Button(self.root, text="Drop", command=lambda c=col: self.on_click(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)

        # builds bottom row of boxes to be drops for x's and o's
        for row in range(6):
            row_labels = []
            for col in range(7):
                label = tk.Label(self.root, text=" ", width=4, height=2, font=("Arial", 20), borderwidth=1, relief="solid")
                label.grid(row=row+1, column=col)
                row_labels.append(label)
            self.labels.append(row_labels)

    def on_click(self, column):
        try:
            row, player = self.game.make_move(column)
            color = "red" if player == "X" else "blue"
            self.labels[row][column].config(text=player, fg=color)
            # uses logic file to check if player wins in any direction
            if self.game.check_winner(row, column):
                messagebox.showinfo("Winner", f"Player {player} wins!")
                self.disable_buttons()
            elif self.game.is_draw():
                messagebox.showinfo("Draw", "The game is a draw.")
                self.disable_buttons()

        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def run(self):
        self.root.mainloop()
