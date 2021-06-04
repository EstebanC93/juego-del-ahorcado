# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 07:43:38 2021

@author: Esteban Henao
"""
import os
from random import choice


def main():
    lista = []
    underline = [] 

    
    with open(r'C:\Users\Esteban Henao\Desktop\python\python intermedio\archivos\data.txt',
              "r", encoding="utf-8") as f:
        for i in f:
            i=i.rstrip("\n")
            lista.append(i)
        word = choice(lista)
        new_word = word.maketrans('áéíóú','aeiou')
        word = word.translate(new_word)
        #print(word)
        word.split()
        
        for j in range(len(word)):
            underline.append("_")
        print(underline)
        
        cont = 0
        aux=0
        
        for x in range(1000):
            try:
                letter = input("Ingrese una letra: ")
                position = word.index(letter)
                #print(position)
                if letter in word:
                    if letter !="":
                        for index, value in enumerate(word):
                            
                            if value == letter:
                                underline[index] = letter
                                aux +=1
                        if aux == len(word):
                            print("Felicidades has ganado!!!!")
                            os.system("exit")
                        print(underline)
                if letter == "":
                    print("Debe de Ingresar una letra")
            except ValueError:
                cont +=1
                print(f"Intentos sin exito: {cont}")
            if cont == 6:
                print("Ha alcanzado la cantidad maxima de intentos fallidos")
                print("GAME OVER!!!")
                os.system("exit")
                                       
        

if __name__ == '__main__':
    
    print("Bienvenido al juego del Ahorcado\n"
          "Adivina la palabra!\n")
    main()
    os.system("cls")