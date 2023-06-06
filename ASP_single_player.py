#akmens šķēres papīrīts ar ascii art
#izveidoja Marts Mercs DP 1-1

import random
from time import sleep
from os import system

def spele1():
    turns = ["akmens", "papīrs", "šķēres"]

    uzvaras = 0
    while True : 
        human_turn = input("Ievadi akmens, šķēres, papīrs vai exit: ")
        computer_turn = random.choice(turns)
        if human_turn == 'exit' :
            print('Tu uzvarēji', uzvaras,'reizes')
            break
        system('cls')
        print("""    
        _______                                     _______           
    ---'   ____)                                   (____   '---
          (_____)                                 (_____)
          (_____)                                 (_____)
          (____)                                   (____)
    ---.__(___)                                     (___)__.---""")
        sleep(0.7)
        system('cls')
        print("""
            
        
        _______                                     _______           
    \--'   ____)                                   (____   '--/
          (_____)                                 (_____)
          (_____)                                 (_____)
          (____)                                   (____)
    \--.__(___)                                     (___)__.--/
    """)
        sleep(0.7)
        system('cls')
        print("""   
        _______                                     _______           
    ---'   ____)                                   (____   '---
          (_____)                                 (_____)
          (_____)                                 (_____)
          (____)                                   (____)
    ---.__(___)                                     (___)__.---""")
        sleep(0.7)
        system('cls')
        if human_turn == "akmens" and computer_turn == "akmens" : #1
            print("""    
        _______                                     _______           
    ---'   ____)                                   (____   '---
          (_____)                                 (_____)
          (_____)                                 (_____)
          (____)                                   (____)
    ---.__(___)                                     (___)__.---
                        Neizšķirts!
                        """)
        elif human_turn == "akmens" and computer_turn == "papīrs": #2
            print("""
        _______                                    ________
    ---'    ____)                             ____(____    '---
           (_____)                           (______
           (_____)                           (_______
           (____)                             (_______
    ---.___(___)                                (__________'---
                        Dators uzvar!
                        """)
        elif human_turn == "akmens" and computer_turn == "šķēres" : #3
            print("""
        _______                                    ________
    ---'    ____)                             ____(____    '---
           (_____)                           (______
           (_____)                          (________
           (____)                                  (___
    ---.___(___)                                    (______'---
                        Tu uzvari!
                        """)
            uzvaras=uzvaras+1
        elif human_turn == "papīrs" and computer_turn == "papīrs" : #4
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
              _______)                       (_______
             _______)                         (_______
    ---.__________)                             (__________'---
                        Neizšķirts!
                        """)  
        elif human_turn == "papīrs" and computer_turn == "šķēres": #5
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
              _______)                      (________
             _______)                              (___
    ---.__________)                                 (______'---
                        Dators uzvar!
                        """)
        elif human_turn == "papīrs" and computer_turn == "akmens" : #6
            print("""
        _______                                    ________
    ---'    ____)____                             (____    '---
               ______)                           (_____)
              _______)                           (_____)
             _______)                             (____)
    ---.__________)                                (___)___'---
                        Tu uzvari!
                        """)
            uzvaras=uzvaras+1
        elif human_turn == "šķēres" and computer_turn == "šķēres" : #7
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
              ________)                     (_________
            ___)                                  (___
    ---.______)                                     (______'---
                        Neizšķirts!
                        """)
        elif human_turn == "šķēres" and computer_turn == "akmens" : #8
            print("""
        _______                                    ________
    ---'    ____)____                             (____    '---
               ______)                           (_____)
              ________)                          (_____)
             ___)                                 (____)
    ---.______)                                    (___)___'---
                        Dators uzvar!
                        """)
        elif human_turn == "šķēres" and computer_turn == "papīrs" : #9
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
              ________)                      (_______
             ___)                             (_______
    ---.______)                                 (_________'---
                        Tu uzvari!
                        """)
            uzvaras=uzvaras+1
        else :
            print('Ievadīts nepareizi, mēģiniet atkal.')
