#!/usr/bin/env python

def isSafe(board, n, col): #this function is completely broken
  for i in range(0, n):
    if(board[i][col] == '*'):
      return False
  return True

def placepiece(board, n, k, start=0, count=0):
  if(k == count):
    return 1
  if(n == start):
    return 0
  solutions = 0
  for i in range(0,n):
    if(board[start][i] == '#' and isSafe(board, n, i)): #fix the isSafe function call
      board[start][i] = '*'
      solutions += placepiece(board, n, k, start+1, count+1)
      board[start][i] = '#'
      
  solutions += placepiece(board, n, k, start+1, count)
  return solutions

def main():
    n, k = (int(x) for x in input().split())
    board = [list(input()) for _ in range(n)]
    
    print(placepiece(board, n, k))

if __name__ == "__main__":
    main()