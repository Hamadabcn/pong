# Pong Game

Welcome to **Pong by Hamadabcn**! This is a simple Pong game implemented in Python. The game features classic Pong gameplay with paddle controls, scoring, and sound effects.

## Table of Contents

- [About the Game](#about-the-game)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Controls](#game-controls)
- [Gameplay](#gameplay)
- [License](#license)

## About the Game

This Pong game is a basic implementation using Python's `turtle` module for graphics and `pygame` for sound effects. The game is designed for beginners to understand game development basics and to have some fun!

## Requirements

To run this game, you'll need:

- Python 3.x
- Pygame
- winsound

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Hamadabcn/snake.git

2. Navigate to the project directory:

   ```bash
    cd pong

Install the required Python packages:

3. You can install Pygame using pip:

   ```bash
    pip install pygame
    The winsound module is included with Python on Windows, so no additional installation is needed for it.

## How to Run
Make sure you have the required files:

Ensure that bounce.wav and game_over.wav sound files are in the same directory as main.py.

Run the game:
    ```bash
    python main.py

## Game Controls
Paddle A (Player X):

Move Up: W
Move Down: S
Paddle B (Player Y):

Move Up: Up Arrow
Move Down: Down Arrow

## Gameplay
The game starts with both paddles and a ball in their initial positions.
Players control their paddles to keep the ball in play and try to score by getting the ball past the opponent's paddle.
The first player to reach the maximum score wins the game.
The game ends when one player reaches the target score, and a "Game Over" message is displayed.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
