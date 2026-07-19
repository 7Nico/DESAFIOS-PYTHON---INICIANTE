#Vou criar um programa que lê o valor de um produto e calcule qual vai ser o valor se pagar a vista (terá 7% de desconto).
#E parcelado irá aumentar 2% no valor original do produto (juros) a partir da quinta parcela

produto = float(input('Digite o valor do produto: R$'))
print('-'*150)
vista = produto - (produto*7/100)
print(f'O valor do produto caso seja pago á vista no pix é de R${vista:.2f}')
print()
print('Caso deseje parcelar, segue abaixo os valor do produto e de cada parcela, com um aumento de 2% da quinta parcela em diante: ')
print(f'2x  de R${produto/2:.2f} = R${produto:.2f} \n3x  de R${produto/3:.2f} = R${produto:.2f} \n4x  de R${produto/4:.2f} = R${produto:.2f} ')
print(f'5x  de R${(produto + produto*2/100)/5:.2f} = R${produto + (produto*2/100):.2f} \n6x  de R${(produto + produto*4/100)/6:.2f} = R${produto + produto*4/100:.2f} ')
print(f'7x  de R${(produto + produto*6/100)/7:.2f} = R${produto + produto*6/100:.2f} \n8x  de R${(produto + produto*8/100)/8:.2f} = R${produto + produto*8/100:.2f} ')
print(f'9x  de R${(produto + produto*10/100)/9:.2f} = R${produto + produto*10/100:.2f} \n10x de R${(produto + produto*12/100)/10:.2f} = R${produto + produto*12/100:.2f}')
print(f'11x de R${(produto + produto*14/100)/11:.2f} = R${produto + produto*14/100:.2f} \n12x de R${(produto + produto*16/100)/12:.2f} = R${produto + produto*16/100:.2f}')
print('-'*150)