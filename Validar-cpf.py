import re

cpf = input()

padrao = r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}-?[0-9]{2}$'



def verifica_dv(numero):
  peso = len(numero)
  soma = 0

  for i in range(len(numero) -1):
      soma += int(numero[i]) * peso
      peso -= 1

  dv = 11 - soma%11

  if dv >= 10:
      dv = 0
  
  return dv == int(numero[-1])
      
      

if re.match(padrao, cpf):
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')
    print(verifica_dv(cpf) and verifica_dv(cpf[:-1]) and cpf[0]*11 != cpf)
      
else:
    print(False)
