 ####Import####
import tkinter
###KEY###
# -1 = O
# 1 = X
# 0 = none
#Values of x or o list
moves = {
    'tl': 0,
    'tm': 0,
    'tr': 0,
    'ml': 0,
    'mm': 0,
    'mr': 0,
    'bl': 0,
    'bm': 0,
    'br': 0
}
#Paths that are possibilities of winning
paths = [
  ['tl', 'tm', 'tr'],
  ['ml', 'mm', 'mr'],
  ['bl', 'bm', 'br'],
  ['tl', 'ml', 'bl'], 
  ['tm', 'mm', 'bm'], 
  ['tr', 'mr', 'br'],
  ['tl', 'mm', 'br'], 
  ['tr', 'mm', 'bl']
  ]
#Numver of moves
numXMoves = 0
#The score of x
xScore = 0
#The score of o
oScore = 0

#Tkinter window creation
root = tkinter.Tk()
root.title("Tic-Tac-Toe")
root.geometry("200x100")
#--------------------
#####TOP BUTTONS#####
tl = tkinter.Button()
tm = tkinter.Button()
tr = tkinter.Button()
#--------------------
####MIDDLE BUTTONS###
ml = tkinter.Button()
mm = tkinter.Button()
mr = tkinter.Button()
lbel = tkinter.Label()
pAgain = tkinter.Button(text='Play Again')
xoScore = tkinter.Label(text='X: ' + str(xScore) + ' - ' + 'O: ' + str(oScore))
#--------------------
####BOTTOM BUTTONS###
bl = tkinter.Button()
bm = tkinter.Button()
br = tkinter.Button()

board = {
    'tl': tl,
    'tm': tm,
    'tr': tr,
    'ml': ml,
    'mm': mm,
    'mr': mr,
    'bl': bl,
    'bm': bm,
    'br': br
}


#-------------------------------------------------------
#####Functions######
def restartBoard():
    global numXMoves
    numXMoves = 0
    for m in moves:
        moves[m] = 0
    for b in board:
        board[b].config(text='', state='normal')
    lbel.config(text='')
    pAgain.place_forget()
    xoScore.config(text='X: ' + str(xScore) + ' - ' + 'O: ' + str(oScore))
    xoScore.place(x=110, y=2)


#Returns true if x won, and returns false if not
def xWon():
    global xScore
    for p in paths:
        if moves[p[0]] + moves[p[1]] + moves[p[2]] == 3:
            lbel.config(text='X won')
            for b in board:
                board[b].config(state='disabled')
            xScore += 1
            xoScore.place(x=110, y=35)
            xoScore.config(text='X: ' + str(xScore) + ' - ' + 'O: ' +
                           str(oScore))
            pAgain.place(x=100, y=65)
            return True
    return False


#Returns true if o won, and returns false if not
def oWon():
    global oScore
    for p in paths:
        if moves[p[0]] + moves[p[1]] + moves[p[2]] == -3:
            lbel.config(text='O won')
            for b in board:
                board[b].config(state='disabled')
            oScore += 1
            xoScore.config(text='X: ' + str(xScore) + ' - ' + 'O: ' +
                           str(oScore))
            xoScore.place(x=110, y=35)
            pAgain.place(x=100, y=65)
            return True
    return False


#oMove finds the first available position in path p, and record o's moves
def oMove(p):
    for x in p:
        if moves[x] == 0:
            board[x].config(text='O', state='disabled')
            moves[x] = -1
            oWon()
            return


# x is the player, and o is the computer on the game board UI
# in the moves list 1 represents player x, and -1 represents player o
# in the moves list 0 represents an empty position on the game board
# the paths list stores the possible ways of winning
# each path in the paths list is a combination of 3 positions
# if a path sums up to 3 then x won, and if a path sums to -3 then o won
def nextMove():
    if xWon():
        return
    if numXMoves == 5:
        lbel.config(text='Draw')
        xoScore.place(x=110, y=35)
        pAgain.place(x=100, y=65)
        return
    for p in paths:
        ##O can win##
        if moves[p[0]] + moves[p[1]] + moves[p[2]] == -2:
            oMove(p)
            return
        ##X can win##
        if moves[p[0]] + moves[p[1]] + moves[p[2]] == 2:
            oMove(p)
            return
    ##Next available##
    for p in paths:
        if moves[p[0]] == 0 or moves[p[1]] == 0 or moves[p[2]] == 0:
            oMove(p)
            return


#Button configurations with functions
#Top Buttons
def tlXO():
    global numXMoves
    tl.config(text='X', state='disabled')
    numXMoves += 1
    moves['tl'] = 1
    nextMove()


def tmXO():
    global numXMoves
    tm.config(text='X', state='disabled')
    numXMoves += 1
    moves['tm'] = 1
    nextMove()


def trXO():
    global numXMoves
    tr.config(text='X', state='disabled')
    numXMoves += 1
    moves['tr'] = 1
    nextMove()


#Middle Buttons
def mlXO():
    global numXMoves
    ml.config(text='X', state='disabled')
    numXMoves += 1
    moves['ml'] = 1
    nextMove()


def mmXO():
    global numXMoves
    mm.config(text='X', state='disabled')
    numXMoves += 1
    moves['mm'] = 1
    nextMove()


def mrXO():
    global numXMoves
    mr.config(text='X', state='disabled')
    numXMoves += 1
    moves['mr'] = 1
    nextMove()


#Bottom Buttons
def blXO():
    global numXMoves
    bl.config(text='X', state='disabled')
    numXMoves += 1
    moves['bl'] = 1
    nextMove()


def bmXO():
    global numXMoves
    bm.config(text='X', state='disabled')
    numXMoves += 1
    moves['bm'] = 1
    nextMove()


def brXO():
    global numXMoves
    br.config(text='X', state='disabled')
    numXMoves += 1
    moves['br'] = 1
    nextMove()


#----------------------------------------------------
#Button configurations with button clicks
def config():
    tl.config(command=lambda: tlXO())
    tm.config(command=lambda: tmXO())
    tr.config(command=lambda: trXO())

    ml.config(command=lambda: mlXO())
    mm.config(command=lambda: mmXO())
    mr.config(command=lambda: mrXO())

    bl.config(command=lambda: blXO())
    bm.config(command=lambda: bmXO())
    br.config(command=lambda: brXO())
    pAgain.config(command=lambda: restartBoard())
    #Button and label placment
    tl.place(x=3, y=2)
    tm.place(x=30, y=2)
    tr.place(x=57, y=2)
    lbel.place(x=125, y=2)

    ml.place(x=3, y=32)
    mm.place(x=30, y=32)
    mr.place(x=57, y=32)

    bl.place(x=3, y=62)
    bm.place(x=30, y=62)
    br.place(x=57, y=62)


config()
#loops the window being shown / allows for the window to be shown until terminated
root.mainloop()