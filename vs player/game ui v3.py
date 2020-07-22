from tkinter import *
from tkinter import ttk

app=Tk()
app.geometry("326x373")
app.title("Tic Tac Toe")
app.configure(background="white")

turn1=True

def reset(restart):
    global turn1
    turn1=True
    turn_label["text"]="Player 1's turn (X)"
    turn_label.config(bg="white")
    app.config(bg="white")
    restart.destroy()
    button_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for btn in button_list:
        btn["text"]=''
        btn["state"]=ACTIVE

def disp_win():
    global turn1
    if not turn1:
        turn_label.config(bg="#50d890")
        app.config(bg="#50d890")
        turn_label["text"]="Player 1 (X) wins!"
    elif turn1:
        turn_label.config(bg="#ed8240")
        app.config(bg="#ed8240")
        turn_label["text"]="Player 2 (O) wins!"
    button_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for btn in button_list:
        btn["state"]=DISABLED
    restart_btn()

def restart_btn():
    restart=ttk.Button(app,text="Restart",command=lambda:reset(restart))
    restart.grid(row=3,column=2,sticky=E,padx=5)

def check_win():
    #rows
    if(b1["text"]==b2["text"]==b3["text"] and (b1["text"]=='X' or b1["text"]=='O')):
        disp_win()
    elif(b4["text"]==b5["text"]==b6["text"] and (b4["text"]=='X' or b4["text"]=='O') ):
        disp_win()
    elif(b7["text"]==b8["text"]==b9["text"] and (b7["text"]=='X' or b7["text"]=='O')):
        disp_win()
    #columns
    elif(b1["text"]==b4["text"]==b7["text"] and (b1["text"]=='X' or b1["text"]=='O')):
        disp_win()
    elif(b2["text"]==b5["text"]==b8["text"] and (b2["text"]=='X' or b2["text"]=='O') ):
        disp_win()
    elif(b3["text"]==b6["text"]==b9["text"] and (b3["text"]=='X' or b3["text"]=='O')):
        disp_win()
    #diagonals
    elif(b1["text"]==b5["text"]==b9["text"] and (b1["text"]=='X' or b1["text"]=='O') ):
        disp_win()
    elif(b3["text"]==b5["text"]==b7["text"] and (b3["text"]=='X' or b3["text"]=='O')):
        disp_win()
    elif(b1["state"]==b2["state"]==b3["state"]==b4["state"]==b5["state"]==b6["state"]==b7["state"]==b8["state"]==b9["state"]==DISABLED):
        restart_btn()
        turn_label["bg"]="yellow"
        turn_label["text"]="Draw!"
        app.config(bg="yellow")    

def toggle_turn(btn):
    global turn1
    if turn1:
        btn["text"]='X'
        turn_label["text"]="Player 2's turn (O)"
        turn1=False
    else:
        btn["text"]='O'
        turn_label["text"]="Player 1's turn (X)"
        turn1=True
    btn["disabledforeground"]='black'
    btn["state"]=DISABLED
    check_win()

b1=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b1))
b1.grid(row=0,column=0,sticky=W)
b2=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b2))
b2.grid(row=0,column=1,sticky=W)
b3=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b3))
b3.grid(row=0,column=2,sticky=W)
b4=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b4))
b4.grid(row=1,column=0,sticky=W)
b5=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b5))
b5.grid(row=1,column=1,sticky=W)
b6=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b6))
b6.grid(row=1,column=2,sticky=W)
b7=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b7))
b7.grid(row=2,column=0,sticky=W)
b8=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b8))
b8.grid(row=2,column=1,sticky=W)
b9=Button(app,text="",height = 1, width = 3,font=("verdana","40"),command=lambda:toggle_turn(b9))
b9.grid(row=2,column=2,sticky=W)

turn_label=Label(app,text="Player 1's turn (X)",font=("verdana","15"),bg="white",fg="#202125")
turn_label.grid(row=3,column=0,columnspan=3,sticky=W,padx=5)

app.mainloop()