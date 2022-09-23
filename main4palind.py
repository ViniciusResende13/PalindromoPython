pn= input('Digite a palavra ou número')
pn=pn.replace(' ','')
pnReverse= pn[::-1]

if pn==pnReverse:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

