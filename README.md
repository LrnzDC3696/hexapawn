# HexaPawn

# What is HexaPawn?

Hexapawn is a deterministic two-player game invented by Martin Gardner. It is played on a rectangular
board of variable size, for example on a 3×3 board or on a chessboard. On a board of size n×m, each player
begins with m pawns, one for each square in the row closest to them.
The goal of each player is to advance one of their pawns to the opposite end of the board or to prevent
the other player from moving.

Hexapawn on the 3×3 board is a solved game; with perfect play, white will always lose in 
3 moves: (1.b2 axb2 2.cxb2 c2 3.a2 c1#). Indeed, Gardner specifically constructed it as a game
with a small game tree, in order to demonstrate how it could be played by a heuristic AI implemented
by a mechanical computer based on Donald Michie's Matchbox Educable Noughts and Crosses Engine.

![image](https://user-images.githubusercontent.com/95162875/198818692-bd7c9f88-0e60-425d-b88d-c912c5cf3525.png)


## Rules
As in chess, each pawn may be moved in two different ways: it may be moved one square forward, or it
may capture a pawn one square diagonally ahead of it. A pawn may not be moved forward if there is a
pawn in the next square. Unlike chess, the first move of a pawn may not advance it by two spaces. 
A player loses if they have no legal moves or the other player reaches the end of the board with a pawn.
