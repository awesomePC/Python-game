import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import * 
from tkinter import TclError, ttk
from tkinter.messagebox import showwarning, askokcancel, WARNING
from PIL import Image,ImageTk
import requests
import sys
import threading
import os
import time
import subprocess
import webbrowser
import time
import threading
import razorpay

#global variable to show selected game.
gbl_game_id = 0
# Is Alt-F4 pressed?
pressed_f4 = False 
pid_file_path = "1.txt"
game_images = ["Contra.jpg", "DK.jpg", "Excite bike.png", "fighter.jpg", "metroid.jpg", "NES_01.gif", "pac.jpg", "road.png", "SuperMarioBro.jpg", "tetris.jpg", "zelda.jpg"]
game_sources = ["Contras.nes", "Donkey_Kong.nes", "Excitebike.nes", "Kung_Fu.nes", "Metroid.nes", "Street_Fighter.nes", "Man-Pac.nes", "Road_Fighter.nes", "Super_Mario_Bros.nes", "Tetris.nes", "Legend_of_Zelda.nes"]
game_names = ["Contra", "Donkey kong", "Excite Bike", "Street Fighter", "Metroid", "Sparta X", "Pac Man", "Road Fighter", "Super Mario Bros", "Tetris", "Legend of Zelda"]

def left_frame(container):
    global leftside_frame
    leftside_frame = tk.Frame(container, width= container.winfo_screenwidth(), height=container.winfo_screenheight(), bg="#181515")
    
    # define grid columns
    leftside_frame.columnconfigure(0, weight=1)
    leftside_frame.columnconfigure(1, weight=1)
    leftside_frame.columnconfigure(2, weight=1)
    leftside_frame.columnconfigure(3, weight=1)

    # define grid rows
    leftside_frame.rowconfigure(0, weight=2)
    leftside_frame.rowconfigure(1, weight=1)
    leftside_frame.rowconfigure(2, weight=1)
    leftside_frame.rowconfigure(3, weight=1)
    leftside_frame.rowconfigure(4, weight=1)
    leftside_frame.rowconfigure(5, weight=4)
    leftside_frame.rowconfigure(6, weight=1)

    # Define content
    # Left side Title
    global text
    text = tk.Label(leftside_frame, text='CHOOSE GAME',bg='#181515', fg='#FFF', font=50)
    text.config(font=('Helvetica bold',80))
    text.grid(column=0, row=0, columnspan=4, padx=40, sticky=tk.W)


    # 
    canvas = Canvas(leftside_frame, height=400, highlightthickness=0,  bg="#181515") # a canvas in the parent object
    frame = Frame(canvas, bg="#181515") # a frame in the canvas

    # define grid columns
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)

    # define grid rows
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)
    frame.rowconfigure(5, weight=1)
    frame.rowconfigure(6, weight=1)
    frame.rowconfigure(7, weight=1)
    frame.rowconfigure(8, weight=1)
    frame.rowconfigure(9, weight=1)
    frame.rowconfigure(10, weight=1)
    # a scrollbar in the parent
    scrollbar = Scrollbar(leftside_frame, orient="vertical", command=canvas.yview)
    # connect the canvas to the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    # scrollbar.grid(column=0, row=1, columnspan=1, sticky=tk.N)
    # scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    canvas.grid(column=0, row=2, columnspan=4, sticky=tk.EW)
    # canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
   
    # bind the frame to the scrollbar
    frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    container.bind_all("<Down>", lambda x: canvas.yview_scroll(1, 'units')) # bind "Down" to scroll down
    container.bind_all("<Up>", lambda x: canvas.yview_scroll(-1, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    # leftside_frame.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))

    # labels = [Label(frame, text=str(i)) for i in range(20)] # make some Labels
    # for l in labels: l.pack() # pack them

    global labels
    labels = []
    for i in range(11):
        label = tk.Label(frame, text=f'  {game_names[i]}', bg='#181515', fg='orange')
        label.config(font=('Helvetica bold',30))
        labels.append(label)
    for i in range(11): 
        labels[i].grid(column=0, row=i+1, columnspan=2, padx= 80, pady= 5, sticky=tk.W)
        # l.pack() # pack them



    # Game list
    # global game_1, game_2, game_3, game_4
    # #game_1 label
    # game_1 = tk.Label(leftside_frame, text='>PAC MAN', bg='#181515', fg='orange')
    # game_1.config(font=('Helvetica bold',30))
    # game_1.grid(column=0, row=1, columnspan=2, padx= 40, sticky=tk.W)
    # #game_2 label
    # game_2 = tk.Label(leftside_frame, text='   SUPER MARIO BROS', bg='#181515', fg='orange')
    # game_2.config(font=('Helvetica bold',30))
    # game_2.grid(column=0, row=2, columnspan=2, padx= 40, sticky=tk.W)
    # #game_3 label
    # game_3 = tk.Label(leftside_frame, text='   CONTRAA', bg='#181515', fg='orange')
    # game_3.config(font=('Helvetica bold',30))
    # game_3.grid(column=0, row=3, columnspan=2, padx= 40, sticky=tk.W)
    # #game_4 label
    # game_4 = tk.Label(leftside_frame, text='   TETRIS', bg='#181515', fg='orange')
    # game_4.config(font=('Helvetica bold',30))
    # game_4.grid(column=0, row=4, columnspan=2, padx= 40, sticky=tk.W)

    #game_slect label
    select = tk.Label(leftside_frame, text='SELECT', bg='#181515', fg='orange')
    select.config(font=('Helvetica bold',30))
    select.grid(column=0, row=6, padx= 10, sticky=tk.E)
    #game_slect icon
    im = Image.open("select.png")
    im = im.resize((40,30))
    img= ImageTk.PhotoImage(im)
 
    select_img = tk.Label(leftside_frame, image=img)
    select_img.grid(column=1, row=6, sticky=tk.W)
    select_img.image = img
    #play label
    global play
    play = tk.Label(leftside_frame, text='PLAY', bg='#181515', fg='orange')
    play.config(font=('Helvetica bold',30))
    play.grid(column=2, row=6, padx= 10, sticky=tk.E)
    #game_play label
    im = Image.open("play.png")
    im = im.resize((40,30))
    img= ImageTk.PhotoImage(im)
 
    play_img = tk.Label(leftside_frame, image=img)
    play_img.grid(column=3, row=6, padx= 0, sticky=tk.W)
    play_img.image = img

    return leftside_frame

def right_frame(container):
    global rightside_frame
    rightside_frame = tk.Frame(container, width=container.winfo_screenwidth()/2, height=2000, bg="#181515")
    # define grid columns
    rightside_frame.columnconfigure(0, weight=1)
    rightside_frame.columnconfigure(1, weight=1)
    # define grid rows
    rightside_frame.rowconfigure(0, weight=1)
    rightside_frame.rowconfigure(1, weight=1)
    rightside_frame.rowconfigure(2, weight=4)
    rightside_frame.rowconfigure(3, weight=1)
    rightside_frame.rowconfigure(4, weight=1)

    # Right sied Title
    text_top = tk.Label(rightside_frame, text='TRIPLE',bg='#181515', fg='#FFF', font=50)
    text_top.config(font=('Helvetica bold',30))
    text_top.grid(column=1, row=0, sticky=tk.S)
    
    text_bottom = tk.Label(rightside_frame, text='ARCADE',bg='#181515', fg='red', font=50)
    text_bottom.config(font=('Helvetica bold',30))
    text_bottom.grid(column=1, row=1, sticky=tk.N)
    # Define canvas to display image.
    global canvas_right
    canvas_right = tk.Canvas(rightside_frame, width=600, height=600, bg='white')
    # select image
    img= ImageTk.PhotoImage(Image.open("man.png").resize((600, 600)))
 
    canvas_right.create_image(300,300,image=img)
    canvas_right.image = img
    canvas_right.grid(column=0, row=2, columnspan=2, sticky=tk.N)
    
    return rightside_frame

# Define a function to receive keyevent
def key_press(e):
    # print(e.keycode)
    global gbl_game_id
    #down or right key -> below
    if e.keycode == 116:
        if gbl_game_id != 10:
            gbl_game_id += 1
            select_game()

    #up or left key -> up
    elif e.keycode == 111:
        if gbl_game_id != 0:
            gbl_game_id -= 1
            select_game()

    # s key -> start game
    elif e.keycode == 39:
        start_game()

def key_released(e):
#    label.config(text="Press any Key...")
    pass

#create main window function
def create_main_window():
    global window
    window = tk.Tk()
    window.title('Game Menu')
    #window width, height define
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight()  
            
    window.geometry("%dx%d" % (width, height))
    window.configure(bg='#181515')
    #window gird column, row define 
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)

     # Bind the key event
    window.bind('<KeyPress>',key_press)
    window.bind('<KeyRelease>',key_released )

    frame_1 = left_frame(window)
    frame_1.grid(column=0, row=0, sticky='nsew')

    frame_2 = right_frame(window)
    frame_2.grid(column=1, row=0, sticky='nsew')

    # gamepad configuration
    # command_to_gamepad_config = f"antimicrox --hidden --profile config.amgp"
    # os.system(command_to_gamepad_config)

    #Keycomb to close gamelist app.
    window.bind('<Alt-F4>', alt_f4)
    # window.bind('<Escape>', close)
    window.protocol("WM_DELETE_WINDOW",do_exit)

    # Bind the key event
    window.bind('<KeyPress>',key_press)
    window.bind('<KeyRelease>',key_released )
    #start mainwindow
    window.mainloop()

def do_exit():

    global pressed_f4
    print('Trying to close application')

    answer = askokcancel(
            title='Confirmation',
            message='Closing will cause you to restart game.',
            icon=WARNING)
    if answer is False:
        pass
    # if pressed_f4:  # Deny if Alt-F4 is pressed
    #     print('Denied!')
    #     showwarning(title='Warning', message='Please select a game to play.')
    #     pressed_f4 = False  # Reset variable
    else:
        close()     # Exit application

def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    print('Alt-F4 pressed')
    pressed_f4 = True

def close(*event):  # Exit application
    window.destroy()

# select game to play.
def select_game():
    global gbl_game_id, labels, canvas_right
    global game_1, game_2, game_3, game_4
    img= ImageTk.PhotoImage(Image.open(f"10_ROMGames/Images/{game_images[gbl_game_id]}").resize((600, 600)))
    canvas_right.create_image(300,300,image=img)
    canvas_right.image = img
    for i in range(11):
        labels[i]["text"] = f"  {game_names[i]}"
    labels[gbl_game_id]["text"] = f">{game_names[gbl_game_id]}"

#clear frames
def clear_frames():
    global leftside_frame, rightside_frame
    #clear frame
    for widgets in leftside_frame.winfo_children():
      widgets.destroy()

    for widgets in rightside_frame.winfo_children():
      widgets.destroy()

#Pay screen generate function
def pay_screen():
    #left side
    global leftside_frame
    
    # define grid columns
    leftside_frame.columnconfigure(0, weight=1)
    leftside_frame.columnconfigure(1, weight=1)
    leftside_frame.columnconfigure(2, weight=1)
    leftside_frame.columnconfigure(3, weight=1)

    # define grid rows
    leftside_frame.rowconfigure(0, weight=2)
    leftside_frame.rowconfigure(1, weight=1)
    leftside_frame.rowconfigure(2, weight=1)
    leftside_frame.rowconfigure(3, weight=1)
    leftside_frame.rowconfigure(4, weight=1)
    leftside_frame.rowconfigure(5, weight=4)
    leftside_frame.rowconfigure(6, weight=1)

    # Define content
    # Left side Title
    global text
    text = tk.Label(leftside_frame, text='SCAN & PAY',bg='#181515', fg='#FFF', font=50)
    text.config(font=('Helvetica bold',80))
    text.grid(column=0, row=0, columnspan=4, padx=40, sticky=tk.W)

    # Game list
    global game_1, game_2, game_3, game_4
    #game_1 label
    game_1 = tk.Label(leftside_frame, text='>RS 10 FOR 10MINUTES PLAY', bg='#181515', fg='orange')
    game_1.config(font=('Helvetica bold',30))
    game_1.grid(column=0, row=1, columnspan=2, padx= 40, sticky=tk.W)

    #game_slect label
    global count_time
    count_time = tk.Label(leftside_frame, text='30 SECS LEFT...', bg='#181515', fg='orange')
    count_time.config(font=('Helvetica bold',30))
    count_time.grid(column=0, row=6, padx= 10, sticky=tk.E)

    #right side
    global rightside_frame
   
    # define grid columns
    rightside_frame.columnconfigure(0, weight=1)
    rightside_frame.columnconfigure(1, weight=1)
    # define grid rows
    rightside_frame.rowconfigure(0, weight=1)
    rightside_frame.rowconfigure(1, weight=1)
    rightside_frame.rowconfigure(2, weight=4)
    rightside_frame.rowconfigure(3, weight=1)
    rightside_frame.rowconfigure(4, weight=1)

    # Right side Title
    text_top = tk.Label(rightside_frame, text='TRIPLE',bg='#181515', fg='#FFF', font=50)
    text_top.config(font=('Helvetica bold',30))
    text_top.grid(column=1, row=0, sticky=tk.S)
    
    text_bottom = tk.Label(rightside_frame, text='ARCADE',bg='#181515', fg='red', font=50)
    text_bottom.config(font=('Helvetica bold',30))
    text_bottom.grid(column=1, row=1, sticky=tk.N)
    # Define canvas to display image.
    global canvas
    canvas = tk.Canvas(rightside_frame, width=600, height=600, bg='white')
    # select image
    img= ImageTk.PhotoImage(Image.open("QR_CODE.png").resize((600, 600)))
 
    canvas.create_image(300,300,image=img)
    canvas.image = img
    canvas.grid(column=0, row=2, columnspan=2, sticky=tk.N)

#Pay screen generate function
def pay_screen_time():
    #left side
    global leftside_frame
    
    # define grid columns
    leftside_frame.columnconfigure(0, weight=1)
    leftside_frame.columnconfigure(1, weight=1)
    leftside_frame.columnconfigure(2, weight=1)
    leftside_frame.columnconfigure(3, weight=1)

    # define grid rows
    leftside_frame.rowconfigure(0, weight=2)
    leftside_frame.rowconfigure(1, weight=1)
    leftside_frame.rowconfigure(2, weight=1)
    leftside_frame.rowconfigure(3, weight=1)
    leftside_frame.rowconfigure(4, weight=1)
    leftside_frame.rowconfigure(5, weight=4)
    leftside_frame.rowconfigure(6, weight=1)

    # Define content
    # Left side Title
    global text
    text = tk.Label(leftside_frame, text='TIMES UP!',bg='#181515', fg='#FFF', font=50)
    text.config(font=('Helvetica bold',80))
    text.grid(column=0, row=0, columnspan=4, padx=40, sticky=tk.W)

    # Game list
    global game_1, game_2, game_3, game_4
    #game_1 label
    game_1 = tk.Label(leftside_frame, text='>TO CONTINUE PLAYING', bg='#181515', fg='orange')
    game_1.config(font=('Helvetica bold',30))
    game_1.grid(column=0, row=1, columnspan=2, padx= 40, sticky=tk.W)
     #game_1 label
    game_2 = tk.Label(leftside_frame, text='SCAN & PAYRS 10 FOR 10MINUTES PLAY', bg='#181515', fg='orange')
    game_2.config(font=('Helvetica bold',30))
    game_2.grid(column=0, row=2, columnspan=2, padx= 80, sticky=tk.W)

    #game_slect label
    global count_time
    count_time = tk.Label(leftside_frame, text='30 SECS LEFT...', bg='#181515', fg='orange')
    count_time.config(font=('Helvetica bold',30))
    count_time.grid(column=0, row=6, padx= 10, sticky=tk.E)

    #right side
    global rightside_frame
   
    # define grid columns
    rightside_frame.columnconfigure(0, weight=1)
    rightside_frame.columnconfigure(1, weight=1)
    # define grid rows
    rightside_frame.rowconfigure(0, weight=1)
    rightside_frame.rowconfigure(1, weight=1)
    rightside_frame.rowconfigure(2, weight=4)
    rightside_frame.rowconfigure(3, weight=1)
    rightside_frame.rowconfigure(4, weight=1)

    # Right side Title
    text_top = tk.Label(rightside_frame, text='TRIPLE',bg='#181515', fg='#FFF', font=50)
    text_top.config(font=('Helvetica bold',30))
    text_top.grid(column=1, row=0, sticky=tk.S)
    
    text_bottom = tk.Label(rightside_frame, text='ARCADE',bg='#181515', fg='red', font=50)
    text_bottom.config(font=('Helvetica bold',30))
    text_bottom.grid(column=1, row=1, sticky=tk.N)
    # Define canvas to display image.
    global canvas
    canvas = tk.Canvas(rightside_frame, width=600, height=600, bg='white')
    # select image
    img= ImageTk.PhotoImage(Image.open("QR_CODE.png").resize((600, 600)))
 
    canvas.create_image(300,300,image=img)
    canvas.image = img
    canvas.grid(column=0, row=2, columnspan=2, sticky=tk.N)


#Game menu screen
def gamemenu_screen():
    global gbl_game_id
    #left side
    global leftside_frame, window
    
    # define grid columns
    leftside_frame.columnconfigure(0, weight=1)
    leftside_frame.columnconfigure(1, weight=1)
    leftside_frame.columnconfigure(2, weight=1)
    leftside_frame.columnconfigure(3, weight=1)

    # define grid rows
    leftside_frame.rowconfigure(0, weight=2)
    leftside_frame.rowconfigure(1, weight=1)
    leftside_frame.rowconfigure(2, weight=1)
    leftside_frame.rowconfigure(3, weight=1)
    leftside_frame.rowconfigure(4, weight=1)
    leftside_frame.rowconfigure(5, weight=4)
    leftside_frame.rowconfigure(6, weight=1)

    # Define content
    # Left side Title
   # Left side Title
    global text
    text = tk.Label(leftside_frame, text='CHOOSE GAME',bg='#181515', fg='#FFF', font=50)
    text.config(font=('Helvetica bold',80))
    text.grid(column=0, row=0, columnspan=4, padx=40, sticky=tk.W)


    # 
    canvas = Canvas(leftside_frame, height=400, highlightthickness=0,  bg="#181515") # a canvas in the parent object
    frame = Frame(canvas, bg="#181515") # a frame in the canvas

    # define grid columns
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)

    # define grid rows
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)
    frame.rowconfigure(5, weight=1)
    frame.rowconfigure(6, weight=1)
    frame.rowconfigure(7, weight=1)
    frame.rowconfigure(8, weight=1)
    frame.rowconfigure(9, weight=1)
    frame.rowconfigure(10, weight=1)
    # a scrollbar in the parent
    scrollbar = Scrollbar(leftside_frame, orient="vertical", command=canvas.yview)
    # connect the canvas to the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    # scrollbar.grid(column=0, row=1, columnspan=1, sticky=tk.N)
    # scrollbar.pack(side="right", fill="y") # comment out this line to hide the scrollbar
    canvas.grid(column=0, row=2, columnspan=4, sticky=tk.EW)
    # canvas.pack(side="left", fill="both", expand=True) # pack the canvas
    # make the frame a window in the canvas
    canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
   
    # bind the frame to the scrollbar
    frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    window.bind_all("<Down>", lambda x: canvas.yview_scroll(1, 'units')) # bind "Down" to scroll down
    window.bind_all("<Up>", lambda x: canvas.yview_scroll(-1, 'units')) # bind "Up" to scroll up
    # bind the mousewheel to scroll up/down
    # leftside_frame.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))

    # labels = [Label(frame, text=str(i)) for i in range(20)] # make some Labels
    # for l in labels: l.pack() # pack them

    global labels
    labels = []
    for i in range(11):
        label = tk.Label(frame, text=f'  {game_names[i]}', bg='#181515', fg='orange')
        label.config(font=('Helvetica bold',30))
        labels.append(label)
    for i in range(11): 
        labels[i].grid(column=0, row=i+1, columnspan=2, padx= 80, pady= 5, sticky=tk.W)
    #highligth selected game
    labels[gbl_game_id]['text'] = f">{game_names[gbl_game_id]}"

    #game_slect label
    select = tk.Label(leftside_frame, text='SELECT', bg='#181515', fg='orange')
    select.config(font=('Helvetica bold',30))
    select.grid(column=0, row=6, padx= 10, sticky=tk.E)
    #game_slect icon
    im = Image.open("select.png")
    im = im.resize((40,30))
    img= ImageTk.PhotoImage(im)
 
    select_img = tk.Label(leftside_frame, image=img)
    select_img.grid(column=1, row=6, sticky=tk.W)
    select_img.image = img
    #play label
    play = tk.Label(leftside_frame, text='PLAY', bg='#181515', fg='orange')
    play.config(font=('Helvetica bold',30))
    play.grid(column=2, row=6, padx= 10, sticky=tk.E)
    #game_play label
    im = Image.open("play.png")
    im = im.resize((40,30))
    img= ImageTk.PhotoImage(im)
 
    play_img = tk.Label(leftside_frame, image=img)
    play_img.grid(column=3, row=6, padx= 0, sticky=tk.W)
    play_img.image = img


    #right side

    global rightside_frame
    
    # define grid columns
    rightside_frame.columnconfigure(0, weight=1)
    rightside_frame.columnconfigure(1, weight=1)
    # define grid rows
    rightside_frame.rowconfigure(0, weight=1)
    rightside_frame.rowconfigure(1, weight=1)
    rightside_frame.rowconfigure(2, weight=4)
    rightside_frame.rowconfigure(3, weight=1)
    rightside_frame.rowconfigure(4, weight=1)

    # Right sied Title
    text_top = tk.Label(rightside_frame, text='TRIPLE',bg='#181515', fg='#FFF', font=50)
    text_top.config(font=('Helvetica bold',30))
    text_top.grid(column=1, row=0, sticky=tk.S)
    
    text_bottom = tk.Label(rightside_frame, text='ARCADE',bg='#181515', fg='red', font=50)
    text_bottom.config(font=('Helvetica bold',30))
    text_bottom.grid(column=1, row=1, sticky=tk.N)
    # Define canvas to display image.
    global canvas_right
    canvas_right = tk.Canvas(rightside_frame, width=600, height=600, bg='white')
    # select image
    img= ImageTk.PhotoImage(Image.open(f"10_ROMGames/Images/{game_images[gbl_game_id]}").resize((600, 600)))
 
    canvas_right.create_image(300,300,image=img)
    canvas_right.image = img
    canvas_right.grid(column=0, row=2, columnspan=2, sticky=tk.N)


#display pay screen
def display_pay_screen():
   
    #clear screen
    clear_frames()
    pay_screen()
    #scan payment
    
def thread_function():

    global count_time
    total_time = 30

    #check payment status
        
    with open('pay_info.txt') as f:
        pay_info = f.readlines()

    merchant_id = pay_info[0].split(":")[1]
    qr_id = pay_info[1].split(":")[1]
    webhook_url = pay_info[2].split(":")[1]
    your_id = pay_info[3].split(":")[1]
    your_secret = pay_info[4].split(":")[1]

    while total_time > 0:

        time.sleep(1)
        total_time = total_time - 1
        # display_pay_screen()
        count_time['text'] = f"{total_time} SECS LEFT..."

        # payment_status = int(requests.get(url=payment_check_url+f"&game_id={game_status}").text)
        
        client = razorpay.Client(auth=(your_id, your_secret))

        # result = client.qrcode.fetch_all_payments(qr_id)
        result = 1
        global text
        if result == 1 and total_time == 0:
            text["text"] = "PROCESSING..."
            time.sleep(2)
            # text["text"] = "PAYMENT SUCCESSFUL"
            # time.sleep(2)
            print("here")
            if result == 1:
                #start game
                print("111111")
                global gbl_game_id
                if gbl_game_id == 0:
                    # pass
                    showwarning(title='Warning', message='Please select a game to play.')
            
                else:
                    global second_win
                    second_win = Toplevel()
                    second_win.title("timer")
                    second_win.geometry("400x100")
                    second_win.overrideredirect(True)
                    second_win.attributes('-topmost',True)
                    second_win.rowconfigure(0, weight=1)
                    second_win.columnconfigure(0, weight=1)
                    global text_time
                    text_time = tk.Label(second_win, text='3:00',bg='#181515', fg='#FFF', font=50)
                    text_time.config(font=('Helvetica bold',40))
                    text_time.grid(column=0, row=0, sticky=tk.EW)

                    timer = threading.Thread(target=thread_timer, args=())
                    timer.start()
                    print(1)
                    command_to_play_game = f"nohup nestopia 10_ROMGames/{game_sources[gbl_game_id]} -f & echo $! > 1.txt"
                    os.system(command_to_play_game)
                    global window
                    window.withdraw()
                    

                x2 = threading.Thread(target=thread_function2, args=())
                x2.start()
                print(2)
            elif result == 0:
                print("jere")
                text["text"] = "FAILED! TRY AGAIN"
                time.sleep(5)
                clear_frames()
                gamemenu_screen()
        #     result = False
        # elif result is False and total_time == 21:
        #     time.sleep(2)
        #     text["text"] = "FAILED! TRY AGAIN"
        #     time.sleep(2)
        # print(result)
        
    
def thread_timer():

    total_time = 180
    while total_time > 0:

        time.sleep(1)
        total_time = total_time - 1
        minute = total_time//60
        second = total_time%60
        # display_pay_screen()
        if second < 10:
            text_time['text'] = f"{minute}:0{second}"
        else:
            text_time['text'] = f"{minute}:{second}"
    
#start game selected by user.
def start_game():

    #disply pay screen
    display_pay_screen()
    
    x = threading.Thread(target=thread_function, args=())
    x.start()
    print(1)
    
def thread_function_repay():

    global count_time
    total_time = 30

    #check payment status
        
    with open('pay_info.txt') as f:
        pay_info = f.readlines()

    merchant_id = pay_info[0].split(":")[1]
    qr_id = pay_info[1].split(":")[1]
    webhook_url = pay_info[2].split(":")[1]
    your_id = pay_info[3].split(":")[1]
    your_secret = pay_info[4].split(":")[1]

    while total_time > 0:

        time.sleep(1)
        total_time = total_time - 1
        # display_pay_screen()
        count_time['text'] = f"{total_time} SECS LEFT..."
    

def thread_function2():
    time.sleep(20)
     ## Extract PID of the game from th file!
    with open(pid_file_path,"r") as read_file:
        pid_of_game = read_file.read()
    pause_command = f"kill -STOP {pid_of_game}"
    resume_command = f"kill -CONT {pid_of_game}"

    ## Time to pause the game
    subprocess.call(pause_command, shell=True)
    # https://unix.stackexchange.com/questions/280860/how-to-hide-a-specific-process
    # os.system(f"mount -o bind /empty/dir /proc/{pid_of_game}")
    
    print("stop")
    global window
    window.deiconify()
    showwarning(title='Warning', message='Please pay again to play.')
    clear_frames()
    pay_screen_time()
    x = threading.Thread(target=thread_function_repay, args=())
    x.start()
    global second_win
    second_win.withdraw()
    time.sleep(30)
    window.withdraw()
    subprocess.call(resume_command, shell=True)

#main function
if __name__ == "__main__":
    create_main_window()
