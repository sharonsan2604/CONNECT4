import tkinter as tk
from tkinter import messagebox

# Constants
ROWS = 6
COLS = 7
EMPTY = ""
PLAYERS = ["X", "O", "A", "B"]
WINNING_LENGTH = 4

class Move:
    def __init__(self, player, column, row):
        self.player = player
        self.column = column
        self.row = row

class Node:
    def __init__(self, move):
        self.move = move
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, move):
        self.root = self._insert(self.root, move)

    def _insert(self, node, move):
        if node is None:
            return Node(move)

        if move.column < node.move.column:
            node.left = self._insert(node.left, move)
        else:
            node.right = self._insert(node.right, move)

        return node

class ConnectFourGame:
    def __init__(self, num_players):
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.current_player_index = 0
        self.move_history_bst = BST()
        self.num_players = num_players

    def make_move(self, column):
        row = self.get_next_empty_row(column)
        if row is not None:
            player = PLAYERS[self.current_player_index]
            self.board[row][column] = player
            move = Move(player, column, row)
            self.move_history_bst.insert(move)
            return True
        return False

    def get_next_empty_row(self, column):
        for row in range(ROWS-1, -1, -1):
            if self.board[row][column] == EMPTY:
                return row
        return None

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % self.num_players

    def check_winner(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (self.check_row(row) or
                    self.check_column(col) or
                    self.check_diagonal(row, col)):
                    return True
        return False

    def check_row(self, row):
        count = 0
        for col in range(COLS):
            if self.board[row][col] == PLAYERS[self.current_player_index]:
                count += 1
                if count == WINNING_LENGTH:
                    return True
            else:
                count = 0
        return False

    def check_column(self, col):
        count = 0
        for row in range(ROWS):
            if self.board[row][col] == PLAYERS[self.current_player_index]:
                count += 1
                if count == WINNING_LENGTH:
                    return True
            else:
                count = 0
        return False

    def check_diagonal(self, row, col):
        # Check diagonal from top-left to bottom-right
        count = 0
        for i in range(min(row, col), min(ROWS, COLS)):
            if self.board[i][i] == PLAYERS[self.current_player_index]:
                count += 1
                if count == WINNING_LENGTH:
                    return True
            else:
                count = 0

        # Check diagonal from top-right to bottom-left
        count = 0
        for i in range(min(row, COLS - col - 1), min(ROWS, COLS)):
            if self.board[i][COLS - i - 1] == PLAYERS[self.current_player_index]:
                count += 1
                if count == WINNING_LENGTH:
                    return True
            else:
                count = 0

        return False

class ConnectFourGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")
        self.root.attributes('-fullscreen', True)  # Set to full-screen mode

        # Brown and cream color combination
        bg_color = "#8B735B"
        fg_color = "#FFF5E1"

        self.start_frame = tk.Frame(self.root, bg=bg_color)
        self.start_frame.pack(pady=self.root.winfo_screenheight() / 4)  # Adjust the padding to center vertically

        tk.Label(self.start_frame, text="Connect Four", font=("Helvetica", 30, "bold"), fg=fg_color, bg=bg_color).pack(pady=20)
        tk.Label(self.start_frame, text="Select the number of players:", font=("Helvetica", 16), fg=fg_color, bg=bg_color).pack(pady=10)

        self.player_count_var = tk.StringVar()
        self.player_count_var.set("2")  # Default value
        player_count_menu = tk.OptionMenu(self.start_frame, self.player_count_var, "2", "3", "4")
        player_count_menu.config(font=("Helvetica", 14), fg=bg_color, bg=fg_color)
        player_count_menu.pack(pady=20)

        start_button = tk.Button(self.start_frame, text="Start Game", command=self.show_game, font=("Helvetica", 16), fg=fg_color, bg=bg_color)
        start_button.pack(pady=20)

        self.game_frame = tk.Frame(self.root, bg=bg_color)

        self.connect_four_game = None
        self.canvas = None
        self.buttons = []

        self.root.bind("<Escape>", self.exit_game)  # Bind Esc key to exit the game

        self.root.mainloop()

    def show_game(self):
        player_count = int(self.player_count_var.get())
        if 2 <= player_count <= 4:
            self.connect_four_game = ConnectFourGame(player_count)
            self.create_game_widgets()
            self.start_frame.pack_forget()
            self.game_frame.pack()
        else:
            messagebox.showwarning("Invalid Input", "Please select a valid number of players (2-4).")

    def create_game_widgets(self):
        for col in range(COLS):
            button = tk.Button(self.game_frame, text=str(col + 1), command=lambda c=col: self.make_move(c), font=("Helvetica", 16), fg="#000", bg="#D2B48C")
            button.grid(row=0, column=col, sticky="nsew")
            self.buttons.append(button)

        # Create canvas for the game grid
        self.canvas = tk.Canvas(self.game_frame, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg="#D2B48C")
        self.canvas.grid(row=1, column=0, columnspan=COLS, rowspan=ROWS)

    def make_move(self, column):
        if self.connect_four_game.make_move(column):
            self.draw_board()
            if self.connect_four_game.check_winner():
                self.show_winner()
            else:
                self.connect_four_game.switch_player()

    def draw_board(self):
        self.canvas.delete("all")

        cell_width = self.root.winfo_screenwidth() / COLS
        cell_height = self.root.winfo_screenheight() / ROWS

        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height

                self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFF5E1", outline="#8B735B")

                player = self.connect_four_game.board[row][col]
                if player != EMPTY:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=player, font=("Arial", int(min(cell_width, cell_height) / 2)), fill="#8B735B")

    def show_winner(self):
        winner = self.connect_four_game.current_player_index + 1
        messagebox.showinfo("Game Over", f"The winner is Player {winner}!")
        self.exit_game()

    def exit_game(self, event=None):
        self.root.destroy()

ConnectFourGUI()
