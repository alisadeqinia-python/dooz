from Funcs import *

board=create_board()
player=first_player()
while True:
    show_board(board)
    order=input(f"It's {player}turn! input cell number in row column format: ")
    row=int(order[0])
    col=int(order[2])
    ch=input_check(board,row,col)
    if not ch:
        print("Please Enter correct cell number!", end="\n")
        continue
    board=update_board(board,row,col,player)
    w=is_win(board,row,col,player)
    if w:
        break
    player=player_change(player)
print(f"Player:{player} is winner! SHIRINI YADET NARE :)))", end="\n")


