#!/usr/bin/env python

def isSafe(position, start, piece): #this function is completely broken
  for i in range(0, start):
    if(position[i] == piece):
      return False

def placepiece(board, n, k, start, count):
    # Complete this function
    if(k == count):
      return 1
    if(n == start):
      return 0
    solutions = 0
    for i in range(0,n):
      if(board[start][start] == '#' and isSafe(board[start][i], start, '*')): #fix the isSafe function call
        board[start][start] = '*'
        solutions += placepiece(board, n, k, start+1, count+1)
        board[start][start] = '#'
    solutions += placepiece(board, n, k, start+1, count)
    return solutions

def main():
    n, k = (int(x) for x in input().split())
    board = [list(input()) for _ in range(n)]
    print(placepiece(board, n, k, 0, 0))

if __name__ == "__main__":
    main()