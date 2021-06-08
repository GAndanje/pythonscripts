#chess_board = ['[' for x in range(64) '_' for y in range(64) ']' for z in range(64):]
chess_board = list()
for x in range(64):
    chess_board.append('[')
    chess_board.append('_')
    chess_board.append(']')

chess_board[1:24:3] = 'R','N','B','K','Q','B','N','R'
chess_board[25:48:3] = 'p','p','p','p','p','p','p','p'
chess_board[145:168:3] = 'p','p','p','p','p','p','p','p'
chess_board[169:192:3] = 'R','N','B','Q','K','B','N','R'
#chess_board[1],chess_board[2],chess_board[3],chess_board[4],chess_board[5],chess_board[6],chess_board[7] = 'Ro','Kn','Bi','Ki','Qu','Bi','Kn','Ro'
def chessboard():
    print(''.join(chess_board[:24]))
    print(''.join(chess_board[24:48]))
    print(''.join(chess_board[48:72]))
    print(''.join(chess_board[72:96]))
    print(''.join(chess_board[96:120]))
    print(''.join(chess_board[120:144]))
    print(''.join(chess_board[144:168]))
    print(''.join(chess_board[168:192]))
    return
chessboard()




#print(chess_board)
