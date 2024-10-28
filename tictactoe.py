'''

tic-tac-toe game!
author: hannah wasson
course: practical python
date: 8/18/2024

description: this game was created for a practical python course taken during my MS in Analytics.

'''

import numpy as np 

counter = 2 

playing = True 

empty = np.array([['A1', 'B1', 'C1'],
                  ['A2', 'B2', 'C2'],
                  ['A3', 'B3', 'C3']])

def is_x_o(value): 
     
     if value == 'X' or value == 'X': 
          raise ValueError("Please input valid positions only.")
     if value == 'O' or value == 'o': 
          raise ValueError("Please input valid positions only.")

def create_board(board, position):

    arr = board.copy()
    arr_x = arr.flatten().tolist()
    arr_o = arr_x
    
    if (counter % 2 == 0): 
            idx_x = arr_x.index(position)
            arr_x[idx_x] = "X"
            arr_x = np.array(arr_x).reshape(-1,3)
            return arr_x

    if(counter % 2 != 0):

            idx_o = arr_o.index(position)
            arr_o[idx_o] = "O"
            arr_o = np.array(arr_o).reshape(-1,3)
            return arr_o

def check_win_cond(current):
    
    check = current.flatten().tolist()
    idx_0, idx_1, idx_2, idx_3, idx_4 = check[0], check[1], check[2], check[3], check[4]
    idx_5, idx_6, idx_7, idx_8 = check[5], check[6], check[7], check[8]

    r1 = idx_0 + idx_1 + idx_2 
    r2 = idx_3 + idx_4 + idx_5
    r3 = idx_6 + idx_7 + idx_8
    c1 = idx_0 + idx_3 + idx_6
    c2 = idx_1 + idx_4 + idx_7
    c3 = idx_2 + idx_5 + idx_8
    d1 = idx_0 + idx_4 + idx_8
    d2 = idx_2 + idx_4 + idx_6  

    conditions = ["XXX" == r1,
                  "OOO" == r1,
                  "XXX"  == r2,
                  "OOO"  == r2,
                  "XXX"  == r3,
                  "OOO"  == r3, 
                  "XXX"  == c1,
                  "OOO"  == c1,
                  "XXX"  == c2,
                  "OOO"  == c2,
                  "XXX"  == c3,
                  "OOO"  == c3,
                  "XXX"  == d1,
                  "OOO"  == d1,
                  "XXX"  == d2,
                  "OOO"  == d2]

    if True in conditions: 
        return True
    else: 
        return False

def check_draw(current): 

    positions = np.array([['A1', 'B1', 'C1'],
                          ['A2', 'B2', 'C2'],
                          ['A3', 'B3', 'C3']])

    if positions in current: 
        return False
    else:
        return True
    

print("Welcome to the game of Tic-Tac-Toe!!")
input("Please press enter to start game.")
print(empty)

board = empty 

while playing == True: 
    
    if counter % 2 == 0: 

        input_x = input("Player X, please select a position: ").upper()

        try: 
            is_x_o(input_x)

            board = create_board(board, input_x)

            if (check_win_cond(board) == False): 

                if (check_draw(current=board) == False): 
                    print(board)
                else: 
                    print("Draw!")
                    print(board)
                    break

            else:
                print(board)
                print("Player X Won!")
                print("Thanks for Playing Tic-Tac-Toe!")
                break

        except ValueError: 
                print("Please select a valid position.")
                counter -= 1 

        counter += 1 

    else: 

        input_o = input("Player O, please select a position: ").upper()

        try:
            is_x_o(input_o)

            board = create_board(board, input_o)

            if (check_win_cond(board) == False): 
                if(check_draw(board) == False):
                    print(board)

                else: 
                    print("Draw!")
                    print(board)
                    break

            else:

                print(board)
                print("Player O Won!")
                print("Thanks for Playing Tic-Tac-Toe!")
                break
            

        except (ValueError):
            print("Please select a valid position.")
            counter -= 1
        
        counter += 1
    
        
