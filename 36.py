reta1= int(input('Digite o valor da primeira reta'))
reta2= int(input('Digite o valor da segunda reta'))
reta3= int(input('Digite o valor da terceira reta'))
if reta1 < (reta2 + reta3):
   print('Os seguimentos acima formam um triângulo')
elif reta2 < (reta1 + reta3):
   print('Os seguimentos acima pode forman um triângulo')
elif reta3 < (reta1 + reta2):
   print('Os seguimentos acima formam um triângulo')
else: print('Os seguimentos acima não podem formar um triângulo')
