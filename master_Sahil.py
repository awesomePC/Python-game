import requests
import sys
import threading
import os
import time
import subprocess
import webbrowser
# import pyautogui

command_to_play_game = f"nohup nestopia 1.nes -f & echo $! > 1.txt"
os.system(command_to_play_game)

html_list = ['list']
html_list.append('/home/sahil/Desktop/Code/arcade/html/contra.html')
html_list.append('/home/sahil/Desktop/Code/arcade/html/packman.html')
html_list.append('/home/sahil/Desktop/Code/arcade/html/mario.html')
html_list.append('/home/sahil/Desktop/Code/arcade/html/tetris.html')

html_home_page = '/home/sahil/Desktop/Code/arcade/html/index.html'

nes = ['list']
nes.append('/home/sahil/Desktop/Code/arcade/nes/Contra.nes')
nes.append('/home/sahil/Desktop/Code/arcade/nes/Pac-Man.nes')
nes.append('/home/sahil/Desktop/Code/arcade/nes/Super-Mario.nes')
nes.append('/home/sahil/Desktop/Code/arcade/nes/Tetris.nes')
pid_file_path = "/home/sahil/Desktop/Code/arcade/pid.txt"
machine_id = 2
payment_check_url = f"https://takepayments.tk/check.php?machine_id={machine_id}"
time_for_each_play = 60
kill_command = "sh /home/sahil/Desktop/Code/arcade/kill.sh"
time_to_check_payment  = 30
sudoPassword = '9pbq'
                
while(1):
    try:
        game_status = int(requests.get(url=payment_check_url).text)
    except:
        err_msg_1 = "Payment Link Down Exiting the system!"
        sys.exit(err_msg_1)

    ## This means that payment is in!! 
    ## and we need to play the game

    if(game_status != 0):
        print(f"Game Status = {game_status}")
        ## Status = # 1= contra ; # 2=mario ; # 3=packman  ; # 4=tetris
        try:
            game_to_play = nes[int(game_status)]
            html_to_open = html_list[int(game_status)]
        except:
            err_msg_2 = "Unwanted Game from the list being called"
            sys.exit(err_msg_2)

        print(f"Lets Play {game_to_play}")

        ## Start Game in another Thread and Store the PID in a File!
        command_to_play_game = f"nohup nestopia {game_to_play} -f & echo $! > {pid_file_path}"
        os.system(command_to_play_game)

        
        ## Sleeping for sometime to let player play :P
        time_diff2 = 0
        time_start2 = time.time()
        ## Code will remain inside this loop till time_to_check_payment
         
        while(True):
            time.sleep(time_for_each_play)

            ## Extract PID of the game from th file!
            with open(pid_file_path,"r") as read_file:
                pid_of_game = read_file.read()

            pause_command = f"kill -STOP {pid_of_game}"
            resume_command = f"kill -CONT {pid_of_game}"

            ## Time to pause the game
            subprocess.call(pause_command, shell=True)

            ## time to open the Browser
            webbrowser.open(html_to_open)

            ## Checking Payment for 30 Seconds
            time_diff = 0
            time_start = time.time()
            ## Code will remain inside this loop till time_to_check_payment
            
            while(time_diff < time_to_check_payment):
                try:
                    payment_status = int(requests.get(url=payment_check_url+f"&game_id={game_status}").text)
                except:
                    err_msg_3 = "Payment Check Failure Exitting Out and Killing the Game"
                    os.system(kill_command)
                    sys.exit(err_msg_3)

                if(payment_status == 0):    
                    time.sleep(1)
                    time_now = time.time()
                    time_diff = time_now - time_start
                else:
                    ## Payment Recieved Break Out
                    break
            print(payment_status)
            print(game_status)
            ## Check Payment Status and taking Action
            if(payment_status == 0):
                ## Payment Not Recieved which means
                ## We will close the game and Open the browser!

                p = os.system('echo %s|sudo -S %s' % (sudoPassword, kill_command))

                #os.system(kill_command)
                webbrowser.open(html_home_page)
                break

            elif(int(payment_status) == int(game_status)):
                ##Payment made for the same Game
                # Will Unpause the game and play
                print("Lets Play The Game")
                pyautogui.keyDown('alt')
                pyautogui.press('tab') 
                pyautogui.keyUp('alt')   
                time.sleep(1)
                subprocess.call(resume_command, shell=True)
                print("Put 0 to the file")
                time.sleep(30)
        
    else:
        print("No Payment will Sleep now!")
        time.sleep(1)
        continue        

            



    #nohup nestopia '/home/sahil/Desktop/Code/arcade/nes/Contra.nes' 2>devnul & 
