from art import *
import random
import os
import math
from functools import reduce
from hangman import HANGMAN_PICS

def replace_letter_in_word(word):
    attemps_limit = len(word)
    word_as_list = list(word.lower())
    
    hide_word = ["_" for letter in word]
    
    for i in range(attemps_limit * 2):
        if word_as_list != hide_word:
            count = attemps_limit * 2 - i
            
            tprint("Hangman".center(50))
            tprint("Game".center(50))
            
            show_hangman(HANGMAN_PICS, count, attemps_limit * 2)
            
            print("¡BIENVENIDO A UN NUEVO JUEGO! \nLas siguientes son las reglas para ganar la partida".center(50))
            print("1. Debes elegir una letra a la vez entre la A y la Z".center(50))
            print("2. No está permitido el ingreso de números".center(50))
            print(f'Tienes {count} intentos restantes...'.center(50))
            
            for space in range(len(hide_word)):
                print(hide_word[space], end=" ")
            
            try:
                entry = input("\n\nIngresa una letra... ")
                if entry.isalpha() != True:
                    raise ValueError('Oops! ha ocurrido un error...')
                if len(entry) > 1:
                    raise Exception('Oops! ha ocurrido un error...')
            
                for i in range(len(word_as_list)):
                    if entry == word_as_list[i]:
                        hide_word[i] = entry
                os.system("clear")
            except ValueError as ve:
                print('\nNo es una letra')
                print(ve)
            except Exception as e:
                print("\nSolo puedes ingresar una letra")
                print(e)
        else:
            break
    return False if "_" in hide_word else True

def show_hangman(mans: list, attemps: int, attemps_n: int):
    p_attemps = attemps / attemps_n
    if p_attemps == 1.0:
        print(mans[-1])
    elif p_attemps >= 0.85:
        print(mans[-2])
    elif p_attemps >= 0.70:
        print(mans[-3])
    elif p_attemps >= 0.55:
        print(mans[-4])
    elif p_attemps >= 0.40:
        print(mans[-5])
    elif p_attemps >= 0.25:
        print(mans[-6])
    else:
        print(mans[-7])

def attemps():
    word_in_game = choose_word()
    result = replace_letter_in_word(word_in_game)
    ganaste = f"Felicidades ! ganaste la palabra escondida es {word_in_game}"
    perdiste = f"Has perdido! la palabra escondida era {word_in_game}"
    fin = f"{ganaste} :D" if result == True else f"{perdiste} :c"
    print(fin)
        
def choose_word():
    file = "./archivos/data.txt"
    with open(file, mode="r", encoding="utf-8") as f:
        words = [line for line in f]
    word_rand = random.choice(words)
    score["played"] = list()
    score["played"].append(word_rand[:len(word_rand)-1])    
    return word_rand[:len(word_rand)-1]
    
def new_game():
    attemps()
    
def main():
    
    new_game()
    
if __name__ == '__main__':
    score = dict()
    main()