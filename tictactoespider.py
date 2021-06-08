tictactoeList = ['-','-','-','-','-','-','-','-','-']

# board layout
def board():
    print(tictactoeList[0]+'|'+tictactoeList[1]+'|'+tictactoeList[2])
    print(tictactoeList[3]+'|'+tictactoeList[4]+'|'+tictactoeList[5])
    print(tictactoeList[6]+'|'+tictactoeList[7]+'|'+tictactoeList[8])
    
    
#handle play
player = 'X'
def handle_play():
    global player
    print(f'{player} playing...')
    valid = False
    while not valid:
        position = input('Enter a position between 1-9: ')
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Enter a position between 1-9: ')
        parse_position = int(position)
        if tictactoeList[parse_position-1] == '-':
            tictactoeList[parse_position-1] = player
            valid = True
        else:
            print('You cant move there! Go again')
    board()
    
#check win or tie
game_over = False
def check_win():
    global game_over
    tie_game = check_tie()
    row_winner = check_rows()
    column_winner = check_columns()
    diagonals_winner = check_diagonals()
    
    if row_winner or column_winner or diagonals_winner or tie_game:
        game_over = True
    if row_winner:
        print(f'{check_rows()} won')
    elif column_winner:
        print(f'{check_columns()} won')
    elif diagonals_winner:
        print(f'{check_diagonals()} won')
    elif tie_game:
        print(f'{check_tie()}')
    else:
        game_over = False


#check win on rows 
winner = None
def check_rows():
    global winner
    row1 = tictactoeList[0] == tictactoeList[1] == tictactoeList[2] != '-'
    row2 = tictactoeList[3] == tictactoeList[4] == tictactoeList[5] != '-'
    row3 = tictactoeList[6] == tictactoeList[7] == tictactoeList[8] != '-'
    if row1:
        winner = tictactoeList[0]
    elif row2:
        winner = tictactoeList[3]
    elif row3:
        winner = tictactoeList[6]
    else:
        winner = None
    return winner


#check win on columns
def check_columns():
    global winner
    column1 = tictactoeList[0] == tictactoeList[3] == tictactoeList[6]  != '-'
    column2 = tictactoeList[1] == tictactoeList[4] == tictactoeList[7]  != '-'
    column3 = tictactoeList[2] == tictactoeList[5] == tictactoeList[8]  != '-'
    if column1:
        winner = tictactoeList[0]
    elif column2:
        winner = tictactoeList[1]
    elif column3:
        winner = tictactoeList[2]
    else:
        winner = None
    return winner


#check win on diagonals
def check_diagonals():
    global winner
    diagonal1 = tictactoeList[0] == tictactoeList[4] == tictactoeList[8] != '-'
    diagonal2 = tictactoeList[2] == tictactoeList[4] == tictactoeList[6] != '-'
    if diagonal1:
        winner = tictactoeList[0]
    elif diagonal2:
        winner = tictactoeList[2]
    else:
        winner = None
    return winner
        
#check for tie
def check_tie():
    if winner == None and '-' not in tictactoeList:
        return 'Tie'
    
    
#switch player
def switch_player():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'

def play_tictactoe():
        board()
        while not game_over:
            handle_play()
            check_win()
            switch_player()
            
play_tictactoe()
