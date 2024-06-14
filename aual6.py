#dicionarios e estrutura de dados

lista_linguagens=['php', 'js', 'python', 'java']

salarios=[2500, 2800, 5000, 4000]
#dicionario

dic_linguagens={'php':2500 , 'js': 2800, 'python': 5000, 'java':4000}
#ver
#print(dic_linguagens["php"])

#editar
#dic_linguagens["php"]=dic_linguagens["php"]*4.9
#print(dic_linguagens["php"])

#print(len(dic_linguagens))

for salario in dic_linguagens:
    novo_salario=dic_linguagens[salario]*2.1
    dic_linguagens[salario]=novo_salario
print(dic_linguagens)
