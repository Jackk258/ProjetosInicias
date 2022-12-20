ficha = []
while True:
    nome =str(input('Insira o Nome do aluno:'))
    sexo =str(input('Insira o Sexo [M/F]:'))

    nota01 =floar(input('Insira a nota 01:'))
    while nota01 < 0 or nota1>10:
        print('Nota inválida,insira uma nota entre 0 à 10:')
        nota01 = float(input('Insira a nota 01:'))

nota02= float(input('Insira a nota 02:'))
while nota02 <0 or nota2 > 10:
    print('Nota inválida,insira uma nota entre 0 à 10:')
    nota02= float(input('Insira a nota 02:'))

nota03 = float(input('Insira a nota 03:'))
while nota03 <0 or nota03 >10:
    print('Nota inválida,insira uma nota entre 0 à 10:')
    nota03 = float(input('Insira a nota 03:'))

media =(nota01 + nota02 + nota03 )/3
if media >= 7:
    status = "Aprovado"
elif media < 7 and media >= 4:
    status = "Exame"
else:
    status = 'Reprovado'

ficha.append([nome, sexo, [nota01, nota02, nota03,],media, status])

reposta = str(input('Quer continuar? [S/N]'))
if resposta in 'Nn':
    break

tx_aprovado = 0
tx_exame = 0
tx_reprovados = 0

m_aprovado = 0
f_aprovado = 0
m_exame = 0
f_exame = 0
m_reprovado = 0
f_reprovado = 0

for i in range(0, len(ficha), 1):
    if ficha[i][4] == "Reprovado":
        tx_reprovados+= 1
        if ficha[i][1] in 'Ff':
            f_reprovado += 1
        else:
            m_reprovado += 1

    elif ficha [i][4] == 'Exame':
        tx_exame += 1
        if ficha[i][1] in "Ff":
            f_exame += 1 
        else:
            m_exame += 1

    elif ficha[i][4] =="Aprovado":
        tx_aprovado += 1
        if ficha[i][1] in "Ff":
            f_aprovado += 1
        else:
            m_aprovado += 1


print('Taxas de Status: ')
print(f"Alunos aprovados:"  {(tx_aprovado/len(ficha))*100}%')
print(f"Alunos para exame:" {(tx_exame/len(ficha))*100}%')
print(f"Alunos reprovados:" {(tx_reprovado/len(ficha))*100}%')

print('-' *45)

print('Visualização por sexo:')
print(f'alunas aprovadas: {f_aprovado}')
print(f'alunas exame: {f_exame}')
print(f'alunas reprovadas: {f_reprovado}')

print('')

print('Visualização por sexo:')
print(f'alunos aprovados: {m_aprovado}')
print(f'alunos exame: {m_exame}')
print(f'alunos reprovados: {m_reprovado}')