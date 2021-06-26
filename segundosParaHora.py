# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#entrada da quantidade em segundos
tempo = int(input("Digite a hora em segundos: "))


if tempo <= 60:
    print(" A hora é de: ",tempo, "segundos")
    

#quando o segundos indicados forem maiores que 60 e menores que 3600s
elif tempo > 60 and tempo <= 2599:
        minuto = tempo // 60
        segundo = tempo - 60
        print("A minuto é: ",minuto)
        print("O Segundo é: ", segundo)
    
#quando o segundos indicados forem maiores que 3600s
else: 
    hora = tempo // 3600
    minuto = int(((tempo / 3600)- hora) * 60)
    segundo = tempo - (hora * 3600) - (minuto * 60)
    print("A hora é: ",hora)
    print("O minuto é: ",minuto)
    print("O segundo é: ", segundo)