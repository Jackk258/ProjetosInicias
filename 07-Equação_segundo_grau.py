a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))
c = int(input('Digite o valor de C:'))

delta = b**2 -4*a*c

print('O valor de delta é igual a:',delta)
#x = (-b +- raiz(delta))/2a

x1 =(-b - delta**0.5) / (2*a)
x2 =(-b + delta**0.5) / (2*a)

print('O valor de x1 é igual a:',x1)
print('O valor de x2 é igual a:',x2)