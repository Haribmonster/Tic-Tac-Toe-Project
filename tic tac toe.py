import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.scores = {"X": 0, "O": 0}  # Win counters for each player
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        
    def create_widgets(self):
        # Dark theme colors
        self.bg_color = "#2B2B2B"
        self.button_color = "#3C3C3C"
        self.text_color = "#FFFFFF"
        self.x_color = "#FF6F61"
        self.o_color = "#61C0FF"
        
        # Configure main window background
        self.window.configure(bg=self.bg_color)
        
        # Create the scoreboard label
        self.score_label = tk.Label(
            self.window,
            text=f"Player X: {self.scores['X']} | Player O: {self.scores['O']}",
            font=("Helvetica", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.score_label.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=10)
        
        # Create the player turn label
        self.turn_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s Turn",
            font=("Helvetica", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.turn_label.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=10)
        
        # Create the game grid buttons
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=("Arial Rounded MT Bold", 24),
                    width=6,
                    height=2,
                    bg=self.button_color,
                    fg=self.text_color,
                    relief="flat",
                    bd=0,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row + 2, column=col, padx=5, pady=5)
                button.configure(highlightbackground=self.bg_color, highlightthickness=2)
                self.buttons[row][col] = button
    
    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(
                text=self.current_player,
                fg=self.x_color if self.current_player == "X" else self.o_color
            )
            
            if self.check_winner():
                self.scores[self.current_player] += 1
                self.update_scoreboard()
                self.turn_label.config(text=f"Player {self.current_player} Wins!", fg="#FFD700")
                self.window.after(2000, self.reset_game)  # Reset after 2 seconds
            elif self.is_draw():
                self.turn_label.config(text="It's a Draw!", fg="#FFA500")
                self.window.after(2000, self.reset_game)  # Reset after 2 seconds
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s Turn")
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        
        return False
    
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text="", state=tk.NORMAL, fg=self.text_color)
        self.turn_label.config(text=f"Player {self.current_player}'s Turn", fg=self.text_color)
    
    def update_scoreboard(self):
        self.score_label.config(text=f"Player X: {self.scores['X']} | Player O: {self.scores['O']}")
    
    def run(self):
        self.window.mainloop()

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
