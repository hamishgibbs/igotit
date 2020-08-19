#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:22:23 2020

@author: hamishgibbs

"""

import sys
import random

class igotit():
    
    def __init__(self):
        self.solutions = [set([0, 1, 2, 3, 4]),
                          set([5, 6, 7, 8, 9]),
                          set([10, 11, 12, 13, 14]),
                          set([15, 16, 17, 18, 19]),
                          set([20, 21, 22, 23, 24]),
                          set([0, 5, 10, 15, 20]),
                          set([1, 6, 11, 16, 21]),
                          set([2, 7, 12, 19, 22]),
                          set([3, 8, 13, 18, 23]),
                          set([4, 9, 14, 19, 24]),
                          set([0, 6, 12, 18, 24]),
                          set([4, 8, 12, 16, 20])]
        
        self.player_history = {}
        
    def check_solution(self, solution: list):
                
        return(sum([len(set(x).difference(solution)) == 0 for x in self.solutions]) > 0)
    
    def throw(self, player_id):
        
        x = random.randint(0, 24)
        
        try:
            while x in self.player_history[player_id]:
                
                x = random.randint(0, 24)
            
            return(x)    
        except:
            return(x)
    
    def record_throw(self, player_id: int):
            
        if player_id not in self.player_history.keys():
            self.player_history[player_id] = [self.throw(player_id)]
        else:
            self.player_history[player_id].append(self.throw(player_id))
    
    def create_board(self, player_id):
                
        board = [' '] * 25
        
        for i in self.player_history[player_id]:
            board[i] = 'X'
            
        board = [board[i:i + 5] for i in range(0, len(board), 5)]
            
        return(board)
    
    def print_board(self, board):
        
        print('- - - - - - -')
        
        for b in board:
            print('| ' + ' '.join(b) + ' |')
        
        print('- - - - - - -')
    
    def print_winning_player(self, winning_player, human_id):
        
        if len(winning_player) > 1:
            
            if human_id in winning_player:
            
                print('{} won!'.format(' and '.join(['You'] + ['Player ' + str(x) for x in [x for x in winning_player if x != human_id]])))
            
            else:
                
                print('Players {} won.'.format(' and '.join([str(x) for x in winning_player])))
        else:
                        
            if human_id in winning_player:
                
                print('You won!')
            
            else:
                            
                print('Player {} won.'.format(winning_player[0]))

    def compete(self, n_players = 10):
        
        human_id = random.randint(0, n_players)
                
        print('Competing against {} players.'.format(n_players))
        
        player_success = []
        
        i = 1
        
        while sum(player_success) == 0:
            
            for player_id in range(0, n_players + 1):
                
                if player_id == human_id:
    
                    input('Toss in ball {}...'.format(i))
                    
                    self.record_throw(player_id)
                
                    self.print_board(self.create_board(player_id))      
    
                else:
    
                    self.record_throw(player_id)
                
            player_success = [self.check_solution(self.player_history[x]) for x in range(0, n_players + 1)]
            
            i += 1
            

        winning_player = [i for i, x in enumerate(player_success) if x]
        
        self.print_winning_player(winning_player, human_id)
                
    
def main():
        
    try:
        n_players = int(sys.argv[1])
    except:
        n_players = 10

    game = igotit()
    
    game.compete(n_players = n_players)

if __name__ == '__main__':

    main()
       