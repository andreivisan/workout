#!/usr/bin/env python3

from typing import List

def n_queens(n: int) -> List[List[str]]:
    return backtrack(n, [], [])

def backtrack(n: int, row: List[str], board: List[List[str]]) -> List[List[str]]:
    if len(board) == n:
        return board
    
    if len(row) == n:
        board.append(row)
        return board   

    for i in range(n):
        if is_valid(n, i, board):
            row[i] = 'Q'
            backtrack(n, row, board)
            row[i] = '.'
        else:
            row[i] = '.'

def is_valid(n: int, pos: int, board: List[List[str]]) -> bool:
    if not board:
        return True
    for i in range(n):
        if board[i] and board[i][pos]:
            return False
        
