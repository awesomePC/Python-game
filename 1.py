import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = tk.Tk()
print(123)


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


import requests
import sys
import threading
import os
import time
import subprocess
import webbrowser
# import pyautogui


def open_game(id):
    if id == 1:
        command_to_play_game = f"nohup nestopia MarioBros.nes -f & echo $! > 1.txt"
        os.system(command_to_play_game)
    # pass
    else:
        command_to_play_game = f"nohup nestopia Contra.nes -f & echo $! > 1.txt"
        os.system(command_to_play_game)

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Fullscreen without toolbar
# window.attributes('-fullscreen',True)

# Fullscreen with toolbar
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open1 = tk.Button(frm_buttons, text="Open game1", command=lambda: open_game(1))
btn_open2 = tk.Button(frm_buttons, text="Open game2", command=lambda: open_game(2))
btn_open3 = tk.Button(frm_buttons, text="Open game3", command=lambda: open_game(3))
btn_open4 = tk.Button(frm_buttons, text="Open game4", command=lambda: open_game(4))
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)

btn_open1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open2.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_open3.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_open4.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=5, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
# window.title("Simple Text Editor")
window.mainloop()


# while(1):
#     try:
#         game_status = int(requests.get(url=payment_check_url).text)
#     except:
#         err_msg_1 = "Payment Link Down Exiting the system!"
#         sys.exit(err_msg_1)

#     ## This means that payment is in!! 
#     ## and we need to play the game

#     if(game_status != 0):
#         print(f"Game Status = {game_status}")
#         ## Status = # 1= contra ; # 2=mario ; # 3=packman  ; # 4=tetris
#         try:
#             game_to_play = nes[int(game_status)]
#             html_to_open = html_list[int(game_status)]
#         except:
#             err_msg_2 = "Unwanted Game from the list being called"
#             sys.exit(err_msg_2)

#         print(f"Lets Play {game_to_play}")

#         ## Start Game in another Thread and Store the PID in a File!
#         command_to_play_game = f"nohup nestopia {game_to_play} -f & echo $! > {pid_file_path}"
#         os.system(command_to_play_game)

        
#         ## Sleeping for sometime to let player play :P
#         time_diff2 = 0
#         time_start2 = time.time()
#         ## Code will remain inside this loop till time_to_check_payment
         
#         while(True):
#             time.sleep(time_for_each_play)

#             ## Extract PID of the game from th file!
#             with open(pid_file_path,"r") as read_file:
#                 pid_of_game = read_file.read()

#             pause_command = f"kill -STOP {pid_of_game}"
#             resume_command = f"kill -CONT {pid_of_game}"

#             ## Time to pause the game
#             subprocess.call(pause_command, shell=True)

#             ## time to open the Browser
#             webbrowser.open(html_to_open)

#             ## Checking Payment for 30 Seconds
#             time_diff = 0
#             time_start = time.time()
#             ## Code will remain inside this loop till time_to_check_payment
            
#             while(time_diff < time_to_check_payment):
#                 try:
#                     payment_status = int(requests.get(url=payment_check_url+f"&game_id={game_status}").text)
#                 except:
#                     err_msg_3 = "Payment Check Failure Exitting Out and Killing the Game"
#                     os.system(kill_command)
#                     sys.exit(err_msg_3)

#                 if(payment_status == 0):    
#                     time.sleep(1)
#                     time_now = time.time()
#                     time_diff = time_now - time_start
#                 else:
#                     ## Payment Recieved Break Out
#                     break
#             print(payment_status)
#             print(game_status)
#             ## Check Payment Status and taking Action
#             if(payment_status == 0):
#                 ## Payment Not Recieved which means
#                 ## We will close the game and Open the browser!

#                 p = os.system('echo %s|sudo -S %s' % (sudoPassword, kill_command))

#                 #os.system(kill_command)
#                 webbrowser.open(html_home_page)
#                 break

#             elif(int(payment_status) == int(game_status)):
#                 ##Payment made for the same Game
#                 # Will Unpause the game and play
#                 print("Lets Play The Game")
#                 pyautogui.keyDown('alt')
#                 pyautogui.press('tab') 
#                 pyautogui.keyUp('alt')   
#                 time.sleep(1)
#                 subprocess.call(resume_command, shell=True)
#                 print("Put 0 to the file")
#                 time.sleep(30)
        
#     else:
#         print("No Payment will Sleep now!")
#         time.sleep(1)
#         continue        

            



#     #nohup nestopia '/home/sahil/Desktop/Code/arcade/nes/Contra.nes' 2>devnul & 













# Frame.py

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import * 
from tkinter import TclError, ttk
from tkinter.messagebox import showwarning
from PIL import Image,ImageTk
import requests
import sys
import threading
import os
import time
import subprocess
import webbrowser
#global variable to show selected game.
gbl_game_id = 0

def left_frame(container):

    frame = tk.Frame(container, width= container.winfo_screenwidth(), height=container.winfo_screenheight(), bg="#181515")
    
    # define grid columns
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    # define grid rows
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)
    frame.rowconfigure(5, weight=4)
    frame.rowconfigure(6, weight=1)

    # Define content
    # Left side Title
    text = tk.Label(frame, text='CHOOSE GAME',bg='#181515', fg='#FFF', font=50)
    text.config(font=('Helvetica bold',80))
    text.grid(column=0, row=0, columnspan=2, ipady=40, sticky=tk.EW)


    # Game list 
    tk.Button(frame, text='PAC MAN', bg='#181515', fg='orange', command=lambda: select_game(1)).grid(column=0, row=1)
    tk.Button(frame, text='SUPER MARIO BROS',bg='#181515', fg='orange', command=lambda: select_game(2)).grid(column=0, row=2)
    tk.Button(frame, text='CONTRAA', bg='#181515', fg='orange', command=lambda: select_game(3)).grid(column=0, row=3)
    tk.Button(frame, text='TETRIS', bg='#181515', fg='orange', command=lambda: select_game(4)).grid(column=0, row=4)
    #Bottom buttons
    tk.Button(frame, text='SELECT').grid(column=0, row=6)
    tk.Button(frame, text='PLAY', command=lambda: start_game()).grid(column=1, row=6,sticky=tk.W)
    # for widget in frame.winfo_children():
    #     widget.grid(padx=5, pady=5)

    return frame

def right_frame(container):

    frame = tk.Frame(container, width=container.winfo_screenwidth()/2, height=2000, bg="#181515")
    # define grid columns
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    # define grid rows
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=4)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)

    # Right sied Title
    text_top = tk.Label(frame, text='TRIPLE',bg='#181515', fg='#FFF', font=50)
    text_top.config(font=('Helvetica bold',30))
    text_top.grid(column=1, row=0, sticky=tk.SE)
    
    text_bottom = tk.Label(frame, text='ARCADE',bg='#181515', fg='red', font=50)
    text_bottom.config(font=('Helvetica bold',30))
    text_bottom.grid(column=1, row=1, sticky=tk.NE)
    # Define canvas to display image.
    global canvas
    canvas = tk.Canvas(frame, width=600, height=600, bg='white')
    # select image
    img= ImageTk.PhotoImage(Image.open("1.jpg"))
 
    canvas.create_image(400,400,image=img)
    canvas.image = img
    
    canvas.grid(column=0, row=2, columnspan=2, sticky=tk.N)
    
    return frame

# Define a function to display the message
def key_press(e):

    if e.keycode == 116:
        print("below")
    elif e.keycode == 111:
        print("above")
#    label.config(text="Welcome to TutorialsPoint")

def key_released(e):
#    label.config(text="Press any Key...")
    pass

def create_main_window():

    window = tk.Tk()
    window.title('Game Menu')
    width= window.winfo_screenwidth()               
    height= window.winfo_screenheight()               
    window.geometry("%dx%d" % (width, height))
    window.configure(bg='#181515')
    # window.resizable(0, 0)
    # try:
    #     # windows only (remove the minimize/maximize button)
    #     window.attributes('-toolwindow', True)
    # except TclError:
    #     print('Not supported on your platform')

    # layout on the window window
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)

    frame_1 = left_frame(window)
    frame_1.grid(column=0, row=0, sticky='nsew')

    frame_2 = right_frame(window)
    frame_2.grid(column=1, row=0, sticky='nsew')

    # Bind the Mouse button event
    window.bind('<KeyPress>',key_press)
    window.bind('<KeyRelease>',key_released )

    window.mainloop()

def select_game(game_id):
    global gbl_game_id
    gbl_game_id = game_id
    # if gbl_game_id == 1:
    #     # select image
    #     img= ImageTk.PhotoImage(Image.open("1.png"))
    #     canvas.create_image(200,200,image=img)
    #     canvas.image = img
    #     # pass
    # else:
    #      # select image
    #     img= ImageTk.PhotoImage(Image.open("2.png"))
    #     canvas.create_image(200,200,image=img)
    #     canvas.image = img
    #     # pass

    match (gbl_game_id):
        case 1: 
            img= ImageTk.PhotoImage(Image.open("1.png"))
            canvas.create_image(200,200,image=img)
            canvas.image = img
        case 2:
            img= ImageTk.PhotoImage(Image.open("2.png"))
            canvas.create_image(200,200,image=img)
            canvas.image = img
        case 3:
            img= ImageTk.PhotoImage(Image.open("1.jpg"))
            canvas.create_image(200,200,image=img)
            canvas.image = img
        case _:
            img= ImageTk.PhotoImage(Image.open("6.jpg"))
            canvas.create_image(200,200,image=img)
            canvas.image = img

def start_game():
    global gbl_game_id
    if gbl_game_id == 0:
        # pass
        showwarning(title='Warning', message='Please select a game to play.')
    elif gbl_game_id == 1:
        command_to_play_game = f"nohup nestopia MarioBros.nes -f & echo $! > 1.txt"
        os.system(command_to_play_game)
    # pass
    else:
        command_to_play_game = f"nohup nestopia Contra.nes -f & echo $! > 1.txt"
        os.system(command_to_play_game)

if __name__ == "__main__":
    create_main_window()


