import pandas as pd

series_objeto = pd.Series([1, 7, 9, 13, 17, 99])
print(series_objeto)

series_objeto2 = pd.Series([4, 7, 8, -2], index=['alfa', 'beta', 'teta', 'gama'])
print(series_objeto2)

disciplinas = {'cursos' : ['Estatística', 'Economia', 'Cálculo', 'Geometria'], 'créditos' : [90, 60, 90, 40], 'requisito' : [True, False, True, False]}
data = pd.DataFrame(disciplinas)
print(data)

nome_cidade = pd.Series(['Maringá', 'Itabira', 'Uberlândia'])
populacao = pd.Series([ 403.063, 120.904, 699.097])
cidade = pd.DataFrame({"Cidade": nome_cidade, "População": populacao})
print(cidade)

cidades = ['Maringá', 'Itabira', 'Uberlândia', 'Salvador', 'Fortaleza']
populacoes = [403.063, 120.904, 699.097, 2.886698, 2.686612]

populacao_cidades = dict(zip(cidades, populacoes))
print(populacao_cidades)

print(type(populacao_cidades))
print(populacao_cidades['Uberlândia'])
print('Maringá' in populacao_cidades)
print('São Carlos' in populacao_cidades)

populacao_cidades['Vitória'] = 365.855
print(populacao_cidades)