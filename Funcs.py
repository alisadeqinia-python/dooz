from random import *

## این تابع یک جدول 3*3 با شماره ردیف و ستون می کشه و برمیگردونه
def create_board():
    board=[
        ["  ","1 ","2 ","3 "],
        ["1 ","_ ","_ ","_ "],
        ["2 ","_ ","_ ","_ "],
        ["3 ","_ ","_ ","_ "]
        ]
    return board

## این تابع برد رو میگیره و اون رو نشون میده
def show_board(board):
    for i in range(4):
        print("".join(board[i]),end="\n")

## این تابع بازیکن رو اول بازی انتخاب میکنه
def first_player():
    a=['O ','X ']
    player=choice(a)
    return player


##این تابع صحت ورودی را چک میکند
def input_check(board,row,col):
    if row<4 and col<4:
        cell=board[row][col]
        if cell=="_ ":
            return True
        else:
            return False
    else:
        return False


## این تابع بورد رو بر اساس ورودی بازیکن آپدیت میکنه
def update_board(board,row,col,player):
    board[row][col]=player
    return board


## تغییر بازیکن
def player_change(player):
    p=['O ','X ']
    p.remove(player)
    player=p[0]
    return player


## آیا برنده شده است؟
def is_win(board,row,col,player):
    m=0
    for i in range(1,4):
        if board[row][i]==player:
            m+=1
        if m==3:
            return True
    m=0
    for i in range(1,4):
        if board[i][col]==player:
            m+=1
        if m==3:
            return True
    m=0
    if row==col:
        for i in range(1,4):
            if board[i][i]==player:
               m+=1
        if m==3:
            return True
    m=0
    if row+col==4:
        if board[1][3]==player:
               m+=1
        if board[2][2]==player:
            m+=1
        if board[3][1]==player:
            m+=1
        if m==3:
            return True
    return False


