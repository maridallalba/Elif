print('Escolha o que comprar:')
print('1. Maçãs')
print('2. Laranjas')
print('3. Bananas')

x = int(input('Qual?'))
y = int(input('Quantas?'))

if(x == 1):
  valor = y * 2,3
  print('Você comprou {} maçãs. O valor é de {} reais.' .format(y, valor))
elif(x == 2):
  valor = y * 3,6
  print('Você comprou {} laranjas. O valor é de {} reais.' .format(y, valor))
elif(x == 3):
  valor = y * 1,85
  print('Você comprou {} bananas. O valor é de {} reais.' .format(y, valor))