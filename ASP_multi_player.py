#akmens šķēres papīrīts ar ascii art
#izveidoja Marts Mercs DP 1-1

from time import sleep
from os import system

def spele2():
    uzvaras1=0
    uzvaras2=0
    while True : 
        human_turn1 = input("Ievadi akmens, šķēres, papīrs vai exit: ")
        human_turn2 = input("Ievadi akmens, šķēres, papīrs vai exit: ")
        if human_turn1 == 'exit' :
            print('Pirmais spēlētājs uzvarēja', uzvaras1,'reizes')
            print('Otrais spēlētājs uzvarēja', uzvaras2,'reizes')
            break
        elif human_turn2 == 'exit' :
            print('Pirmais spēlētājs uzvarēja', uzvaras1,'reizes')
            print('Otrais spēlētājs uzvarēja', uzvaras2,'reizes')
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
        if human_turn1 == "akmens" and human_turn2 == "akmens" : #1
            print("""    
        _______                                     _______           
    ---'   ____)                                   (____   '---
          (_____)                                 (_____)
          (_____)                                 (_____)
          (____)                                   (____)
    ---.__(___)                                     (___)__.---
                        Neizšķirts!
                        """)
        elif human_turn1 == "akmens" and human_turn2 == "papīrs": #2
            print("""
        _______                                    ________
    ---'    ____)                             ____(____    '---
           (_____)                           (______
           (_____)                           (_______
           (____)                             (_______
    ---.___(___)                                (__________'---
                        Uzvar 2. spēlētājs!
                        """)
            uzvaras2=uzvaras2+1
        elif human_turn1 == "akmens" and human_turn2 == "šķēres" : #3
            print("""
        _______                                    ________
    ---'    ____)                             ____(____    '---
           (_____)                           (______
           (_____)                          (________
           (____)                                  (___
    ---.___(___)                                    (______'---
                        Uzvar 1. spēlētājs!
                        """)
            uzvaras1=uzvaras1+1
        elif human_turn1 == "papīrs" and human_turn2 == "papīrs" : #4
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
              _______)                       (_______
             _______)                         (_______
    ---.__________)                             (__________'---
                        Neizšķirts!
                        """)  
        elif human_turn1 == "papīrs" and human_turn2 == "šķēres": #5
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
              _______)                      (________
             _______)                              (___
    ---.__________)                                 (______'---
                        Uzvar 2. spēlētājs!
                        """)
            uzvaras2=uzvaras2+1
        elif human_turn1 == "papīrs" and human_turn2 == "akmens" : #6
            print("""
        _______                                    ________
    ---'    ____)____                             (____    '---
               ______)                           (_____)
              _______)                           (_____)
             _______)                             (____)
    ---.__________)                                (___)___'---
                        Uzvar 1. spēlētājs!
                        """)
            uzvaras1=uzvaras1+1
        elif human_turn1 == "šķēres" and human_turn2 == "šķēres" : #7
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
             ________)                     (_________
             ___)                                  (___
    ---.______)                                     (______'---
                        Neizšķirts!
                        """)
        elif human_turn1 == "šķēres" and human_turn2 == "akmens" : #8
            print("""
        _______                                    ________
    ---'    ____)____                             (____    '---
               ______)                           (_____)
              ________)                          (_____)
             ___)                                 (____)
    ---.______)                                    (___)___'---
                        Uzvar 2. spēlētājs!
                        """)
            uzvaras2=uzvaras2+1
        elif human_turn1 == "šķēres" and human_turn2 == "papīrs" : #9
            print("""
        _______                                    ________
    ---'    ____)____                         ____(____    '---
               ______)                       (______
              ________)                      (_______
             ___)                             (_______
    ---.______)                                 (_________'---
                        Uzvar 1. spēlētājs!
                        """)
            uzvaras1=uzvaras1+1
        else :
            print('Ievadīts nepareizi, mēģiniet atkal.')
