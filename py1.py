#           UNDER APACHE 2.0 LICENSE
#   LICENSED TO LUNAR
#   USE ONLY WITH PERMISSION
#   ILLEGAL COPIES ARE DISALLOWED

import os
from sys import platform
import time

enc = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
       'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
       'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': 'SPACE'}
dec = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
       '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
       '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
       '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', 'SPACE': ' '}


def whichSystem():
    if platform == "linux" or platform == "linux2":  # linux
        return 'linux'
    elif platform == "darwin":  # OS X
        return 'mac-os'
    elif platform == "win32":  # Windows...
        return 'windows'


def encrypt(SentenseToEncrypt):
    res = ''
    for i in SentenseToEncrypt:
        res += enc[i] + ' '
    return res


def decrypt(SentenseToDecrypt):
    res = ''
    SentenseToDecrypt = SentenseToDecrypt.split()
    for i in SentenseToDecrypt:
        if i in dec.keys():
            res += dec[i]
    return res


def clearScreen():
    if whichSystem() == 'linux' or whichSystem() == 'mac-os':
        os.system('clear')
    elif whichSystem() == 'windows':
        os.system('cls')


def printDONE():
    print('''
        o__ __o            o__ __o        o          o    o__ __o__/_ 
         <|     v\          /v     v\      <|\        <|>  <|    v      
         / \     <\        />       <\     / \\o      / \  < >          
         \o/       \o    o/           \o   \o/ v\     \o/   |           
          |         |>  <|             |>   |   <\     |    o__/_       
         / \       //    \\           //   / \    \o  / \   |           
         \o/      /        \         /     \o/     v\ \o/  <o>          
          |      o          o       o       |       <\ |    |           
         / \  __/>          <\__ __/>      / \        < \  / \  _\o__/_
         
          
    ''')


def UserInterface():
    clearScreen()
    print("""
             __    __  ________  __        __         ______  
            /  |  /  |/        |/  |      /  |       /      \ 
            $$ |  $$ |$$$$$$$$/ $$ |      $$ |      /$$$$$$  |
            $$ |__$$ |$$ |__    $$ |      $$ |      $$ |  $$ |
            $$    $$ |$$    |   $$ |      $$ |      $$ |  $$ |
            $$$$$$$$ |$$$$$/    $$ |      $$ |      $$ |  $$ |
            $$ |  $$ |$$ |_____ $$ |_____ $$ |_____ $$ \__$$ |
            $$ |  $$ |$$       |$$       |$$       |$$    $$/ 
            $$/   $$/ $$$$$$$$/ $$$$$$$$/ $$$$$$$$/  $$$$$$/  
            """)
    time.sleep(1)
    clearScreen()
    print('''
        Note : Highly recommend to run this code from console or terminal!
        Welcome to morse encryption program, what we will do today? (press 1 or 2)
        1: encrypt
        2: decrypt
    ''')
    print('your answer: ', end='')
    inp = ''
    while True:
        inp = input()
        if inp == '1' or inp == '2':
            print('ok')
            time.sleep(0.2)
            clearScreen()
            break
        else:
            clearScreen()
            print('sorry, try again, put 1 or 2 here: ', end='')
    # //////
    if inp == '1':
        print('insert string for encrypt: ', end='')
        inp = input()
        time.sleep(0.2)
        printDONE()
        print(encrypt(inp.upper()))
    if inp == '2':
        print('insert string for decrypt: ', end='')
        inp = input()
        time.sleep(0.2)
        printDONE()
        print(decrypt(inp))


UserInterface()
