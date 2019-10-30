###################################
# Program's name  Read file       #
# Author(s) : @ngelo ELijah, 2019 #
# Profession                      #
###################################
#!/usr/local/bin/python3.7
# -*-coding:utf-8 *-

###################################
# External functions importation
#import os

###################################
# Local functions definition
from functions_bank import*


###################################
# Main programme's body

again = 1

while again:

	chemin = input("Indiquer le chemin du fichier :")
	try:
		with open(chemin, 'r') as fichier:
			contenu = fichier.read()
			print(contenu)
	except FileNotFoundError as e:
		print("Le fichier n'existe pas !")
	except IsADirectoryError as e:
		print("Vous n'avez pas indiqué un fichier !")

	again = question("Lire un autre fichier ? (yes, no) : ")


#os.system("pause")            #for windows user
