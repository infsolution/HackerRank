# -*- coding : utf8 -*-

"""
     #
    ##
   ###
  ####
 #####
######

"""

altura = int(input("Altura da figura: "))

nao_preenchidos = altura - 1
preenchidos = 1

for i in range(altura):
	print( (nao_preenchidos - i)*" " + (preenchidos + i)*"#")