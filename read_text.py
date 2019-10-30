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



###################################
# Main programme's body


chemin = input("Indiquer le chemin du fichier :")
try:
	with open(chemin, 'r') as fichier:
		contenu = fichier.read()
		print(contenu)
except FileNotFoundError as e:
	print("Le fichier n'existe pas !")
except IsADirectoryError as e:
	print("Vous n'avez pas indiqué un fichier !")

#os.system("pause")            #for windows user
