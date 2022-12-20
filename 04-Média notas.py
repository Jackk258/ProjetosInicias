print('Média final')
nota01 =int(input('Digite a primeira nota:'))
nota02 =int(input('Digite a segunda nota:'))
nota03 =int(input('Digite a terceira nota:'))
nota04 =int(input('Digite a quarta nota:'))
media=(nota01+nota02+nota03+nota04)/4

print('A nota do primeiro bimestre foi:',nota01)
print('A nota do segundo bimestre foi:',nota02)
print('A nota do terceiro bimestre foi:',nota03)
print('A nota do terceiro bimestre foi:',nota04)
print('A média final foi :',media)

if media >= 6:
    print('O status do aluno é: APROVADO')
else:
    print('O Status do aluno é:REPROVADO')