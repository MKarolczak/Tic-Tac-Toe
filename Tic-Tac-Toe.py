import tkinter as tk
from tkinter import messagebox, colorchooser

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        # Default player colors
        self.player_x_color = "light blue"
        self.player_o_color = "light green"
        
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create menu to allow players to change colors
        self.create_menu()
        
        # Create the Tic-Tac-Toe board
        self.create_board()

    # Create the Tic-Tac-Toe board using buttons
    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font=('Arial', 40), width=5, height=2, bg="white",
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    # Handle button click
    def on_click(self, row, col):
        if self.board[row][col] == " " and not self.check_win() and not self.check_draw():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Change button color based on the player
            if self.current_player == "X":
                self.buttons[row][col].config(bg=self.player_x_color)
            else:
                self.buttons[row][col].config(bg=self.player_o_color)

            if self.check_win():
                self.highlight_winner()
            elif self.check_draw():
                self.display_draw()
            else:
                self.switch_player()

    # Switch player
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    # Check for a win and return the winning combination (if any)
    def check_win(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winning_combination = [(row, 0), (row, 1), (row, 2)]
                return True
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winning_combination = [(0, col), (1, col), (2, col)]
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winning_combination = [(0, 0), (1, 1), (2, 2)]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winning_combination = [(0, 2), (1, 1), (2, 0)]
            return True
        return False

    # Check for a draw
    def check_draw(self):
        return all(self.board[row][col] != " " for row in range(3) for col in range(3))

    # Highlight the winning cells
    def highlight_winner(self):
        for (row, col) in self.winning_combination:
            self.buttons[row][col].config(bg="yellow")
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.reset_game()

    # Display draw message
    def display_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    # Reset the game
    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", bg="white")

    # Create a settings menu to allow players to choose their colors
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        settings_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Set Player X Color", command=self.set_player_x_color)
        settings_menu.add_command(label="Set Player O Color", command=self.set_player_o_color)

    # Function to set Player X's color and update board
    def set_player_x_color(self):
        color = colorchooser.askcolor(title="Choose Player X's color")
        if color[1] is not None:  # If a valid color is chosen
            self.player_x_color = color[1]
            self.update_board_colors()

    # Function to set Player O's color and update board
    def set_player_o_color(self):
        color = colorchooser.askcolor(title="Choose Player O's color")
        if color[1] is not None:  # If a valid color is chosen
            self.player_o_color = color[1]
            self.update_board_colors()

    # Update the board colors for already placed marks
    def update_board_colors(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "X":
                    self.buttons[row][col].config(bg=self.player_x_color)
                elif self.board[row][col] == "O":
                    self.buttons[row][col].config(bg=self.player_o_color)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()