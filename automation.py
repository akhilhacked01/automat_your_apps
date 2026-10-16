import webbrowser
import sys
import time
import subprocess
import os

GREEN  = "\033[32m"

visit_website = input(GREEN + "visit my website for python projects y/n : ")

if visit_website == "y":
    webbrowser.open("https://akhilhacked01.github.io/ATD.web/")
    
if visit_website == "n":
    print("Thank you")    
    
def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
                

RESET = "\033[0m"

BLACK  = "\033[30m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA = "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"

typewriter(BLUE + "////////////////////////////////////////////\n")
#typewriter(YELLOW + "type 8 for list dir\n")
typewriter(BLUE + "///////////////////////////////////////////\n")

typewriter(GREEN + "//////////////////////////////////////////////\n")

typewriter(MAGENTA + "this is a best automation tool, youtube\nfacebook\ninstagram\ngithub\nakhiltechdev\nPOWERD-BY AKHIL TECH DEVELOPER\n")

typewriter(GREEN + "//////////////////////////////////////////////\n")


typewriter(RED + "///////////////////////////////////////\n")
typewriter(RED + "type (1) for open youtube\n")
typewriter(BLUE + "type (2) for  open facebook\n")
typewriter(RED + "type (3) for  open instagram\n")
typewriter(CYAN + "type (4) for  open github\n")
typewriter(CYAN + "type (5) for  open akhiltechdev\n")
typewriter(GREEN + "type (6) for open hackertyper\n")
typewriter(BLUE + "type (7) for make dir\n")
typewriter(YELLOW + "type (8) for list dir\n")
# typewriter(GREEN + "type (9) for open file manager")
typewriter(YELLOW + "type (9) to open google\n")
typewriter(RED + "///////////////////////////////////////\n")


YouTube = "https://youtube.com"
FaceBook = "https://facebook.com"
Instagram = "https://instagram.com"
github = "https://github.com"
akhiltechdev = "https://github.com/akhil-tech-dev.git"
hackertyper = "https://hackertyper.net"


opening = int(input("enter your opening number : "))


if opening == 1:
    webbrowser.open(YouTube)
    
if opening == 2:
     webbrowser.open(FaceBook)
     
if opening == 3:
    webbrowser.open(Instagram)
    
if opening == 4:
    webbrowser.open(github)
    
if opening == 5:
    webbrowser.open(akhiltechdev)
    
if opening == 6:
    webbrowser.open(hackertyper)
    
if opening == 7:
    dir_name = input(GREEN + "enter dir name : ")
    os.mkdir(f"{dir_name}")
    
if opening == 8:
    subprocess.run("ls")
    subprocess.run("pwd")
    
if opening == 9:
       webbrowser.open("https://google.com")    
       
else:
    print("please enter valid number : ")                                                                                                                    