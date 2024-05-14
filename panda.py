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

del populacao_cidades['Fortaleza']
print(populacao_cidades)

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães Rosa']
Livro = ['A Arte da guerra', 'Poesias Selecionadas', 'A Montanha mágica', 'Primeiras estórias']
Ano = [2000, 2004, 2015, 2017]

dados = {'Autor':Autor, 'Livro':Livro, 'Ano':Ano}
autores = pd.DataFrame(dados)
print(type(autores))
df = pd.DataFrame(autores)
print(df)

df.to_csv("autores.csv")

autores = pd.read_csv('autores.csv', index_col=0)
print(autores)
print(autores.info())
print(autores.columns)
print(autores.index)

