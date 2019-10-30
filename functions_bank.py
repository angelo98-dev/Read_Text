###################################
# Functions_Banks                 #
# Author(s) : @ngelo ELijah, 2019 #
# Profession                      #
###################################



def question(annonce='Yes or No ?, please : '):

    """function to ask the user a Yes or No question"""
    reponse = input(annonce)
    if(reponse in ('y','Y','Yes','YES','YeS','yES','yeS','YEs','yEs')):
    	return 1
    if(reponse in ('n','N','No','NO','nO')):
    	return 0




