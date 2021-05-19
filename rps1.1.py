#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random


# Three different moves the player can make
moves = ['rock', 'paper', 'scissor']


# Function for who wins and loses
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Function to choose a random move
class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))


# Function asks the Player to choose a move
class HumanPlayer(Player):
    def move(self):
        your_move = input('Choose your move: (rock / paper / scissors)\n')
        if your_move == "rock":
            print("You chose rock.")
        elif your_move == "paper":
            print("You chose paper.")
        elif your_move == "scissors":
            print("You chose scissors.")
        else:
            print("Try again!")
            self.move()
        return your_move

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.moves_number = len(moves)
        self.next_move_index = random.randrange(self.moves_number)

    # Randomly selects the move and restarts when it reaches rock
    def move(self):
        next_move = moves[self.next_move_index]
        self.next_move_index = (
            self.next_move_index + 1) % self.moves_number
        return next_move

    # Recalls the players last move
    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 Move: {move1}  Player 2 Move: {move2}")
        if beats(move1, move2) is True:
            print("Player One Wins")
            self.score1 += 1
            print(f"score: player1: {self.score1} , player2: {self.score2} \n")
        elif beats(move2, move1) is True:
            print("Player Two Wins")
            self.score2 += 1
            print(f"score: player1: {self.score1} , player2: {self.score2} \n")
        else:
            print("It's a Tie")
            print(f"score: player1: {self.score1} , player2: {self.score2} \n")
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)

    def play_game(self):
        print("Game has started!")
        self.rounds = 3
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        print("\nEnd of Game")
        print(f"""Total Points\nPlayer One Points: {self.score1} """
              f""" Player Two Points: {self.score2}""")
        if self.score1 > self.score2:
            print("Player One Wins\n")
        elif self.score1 < self.score2:
            print("Player Two Wins\n")
        else:
            print("It's a Tie\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
