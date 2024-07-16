s = float(input('Qual é o salário do funcionário? R$'))
a = s*15/100
n = s + a
print('O sálario deste funcionário teve um aumento de 15%, passará de {:.2f} para {:.2f}.'.format(s,n))