from random import *
import pyperclip
import time
CHARACTERS = {
    "letters": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers": "0123456789",
    "symbols": "!@#$%^&*()_-+=<>?/|~"
}

def new_psw():
    psw=''
    chosen = choice(list(CHARACTERS.keys()))
    while True:
        psw+=choice(CHARACTERS[chosen])
        if len(psw) >= 13:
            break
    website = input('website?').lower()
    with open("psw.txt", "a") as f:
        f.write(f"\n{website} {psw}")
def retrieve_psw():
    with open("psw.txt", "r") as f:
        lines = f.readlines()
        psw_dict = {element.split(' ')[0]:element.split(' ')[1] for element in lines}
    pyperclip.copy(psw_dict[input('website which you want password for?').lower()])
    time.sleep(8)
    pyperclip.copy('dummypsw')

try:
    with open("psw.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("psw.txt", "w") as f:
        pass

menu = {'add':new_psw, 'retrieve':retrieve_psw}
menu[input('add/retrieve:\n').lower()]()