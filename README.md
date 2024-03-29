# Pong
Pong is a two-dimensional sports game that simulates table tennis. The player controls an in-game paddle by moving it vertically across the left or right side of the screen. They can compete against another player controlling a second paddle on the opposing side. Players use the paddles to hit a ball back and forth. The goal is for each player to reach eleven points before the opponent; points are earned when one fails to return the ball to the other.

## Game Rules
Pong is played according to the following rules.
Players can move paddle up and down. Player one moves using the A and Z keys. Player two moves using the K and M keys. Each player moves their paddle up and down to hit the ball back to the opposite side. If a player fails to return the ball to the other player, the opponent earns a point. First player to score 11 points wins the set. Game is over when a player wins 2 sets. 

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 pong 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.
```
## Project Structure
---
The project files and folders are organized as follows:

root                    (project root folder)
+-- pong                (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)


## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Heidi Munson  (mun21014@byui.edu)
* Kelly Nebeker (bnknebeker@gmail.com)
* Armando Martinez (mar21095@byui.edu)
