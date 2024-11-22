# CONNECT4
#python#connectfour#game
### Connect Four Game Description for GitHub

#### **Project Title:** Connect Four Game with GUI

#### **Description:**
This project implements the classic **Connect Four game** in Python using the **Tkinter library** for the graphical user interface (GUI). The game supports **2 to 4 players** and features a **binary search tree (BST)** to track move history. Players take turns dropping their markers into columns, and the first to form a horizontal, vertical, or diagonal line of four markers wins the game.

The GUI is designed with a visually appealing **brown and cream color scheme** and includes:
- A start screen to select the number of players.
- A full-screen game interface.
- Interactive buttons and a dynamically updated game board.

#### **How the Code Works:**

1. **Game Logic:**
   - The `ConnectFourGame` class manages the game board, turn-based player switching, and win condition checks. 
   - Moves are tracked in a custom **Binary Search Tree (BST)** for potential extensions, such as analyzing the game's history.
   - Win conditions are verified by checking rows, columns, and diagonals for a sequence of four consecutive markers of the current player.

2. **Move Tracking:**
   - Each move is encapsulated in a `Move` object containing the player's marker, column, and row. These moves are stored in the BST.

3. **Graphical User Interface:**
   - The `ConnectFourGUI` class handles the GUI components:
     - A **start frame** lets users choose the number of players.
     - A **game frame** displays the grid and column buttons.
     - The game board is rendered dynamically using a **canvas**, and player markers are drawn as text.
   - Players interact with the game by clicking buttons corresponding to columns.

4. **Winning and Exiting:**
   - When a player wins, a pop-up message announces the winner, and the game closes upon confirmation.
   - The game can also be exited at any time using the **Escape (Esc)** key.

This implementation combines **structured game logic** and an **intuitive GUI** to create an enjoyable gaming experience. It’s a great demonstration of Python programming concepts, including object-oriented design and GUI development.
