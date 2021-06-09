board_size = int(input("please enter board size: "))
board = [["-" for i in range(board_size)] for i in range(board_size)]
max_turn = board_size*board_size

user = True # when true it refers to x, otherwise o
turns = 0

def current_user(user):
    if user:
        return "x"
    else:
        return "o" 

def print_board(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()


def quit(user_input):
    if user_input.lower() == 'q':
        print("Thanks for playning")   
        return True
    else:
        return False 

def check_input(user_input):
    try:
      user_input = int(user_input)
      if user_input >= 1 and user_input <= max_turn:
        return True
      else:
        print("please enter valid number")  
        return False
    except ValueError:
        print("did you enter number")
        return False
    except Exception as e:
        print(str(e))
        print("pls enter valid number")
        return False 

def coordinates(user_input):
    row = int(user_input / board_size)
    col =  user_input
    if col > 2:
        col = int(col % board_size) 
    return (row, col) 

def isTaken(coords, board):
    row = coords[0]
    col = coords[1] 
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else:
        return False  

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user 

def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diag_shape1(board):
        return True
    if check_diag_shape2(board):
        return True    
    return False            

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False

def check_col(user, board):
    for col in range(board_size):
        complete_col = True
        for row in range(board_size):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False

def check_diag_shape1(board): 
    
    diags = []

    for ix in range(len(board)):
        diags.append(board[ix][ix])
            
    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (\\)")
        return True

    return False  


def check_diag_shape2(board):

    diags = []

    for idx, reverse_idx in enumerate(reversed(range(len(board)))):
        diags.append(board[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        return True
    return False

def all_same(diags):

    if diags.count(diags[0]) == len(diags) and diags[0] != "-":
        return True
    else:
        return False          

while turns < max_turn:
    active_user = current_user(user)
    print_board(board) 
    user_input = input(f"Please enter a position between 1 to {max_turn} or enter 'q' to quit: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    print(coords)
    if isTaken(coords, board):
        print("please try again")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        print_board(board)
        break


    turns += 1
    if turns == max_turn: 
        print("Tie!")
    user = not user    

