import pandas as pd
series_obj = pd.Series([4, 7, 9, 8, -2], index = ['alfa', 'beta', 'teat', 'gama'])
series_obj

disciplinas = {'cursos' : ['Estatística', 'Economia', 'Cálculo', 'Geometria'], 'créditos' : [90, 60, 90, 40], 'requisito' : [True, False, True, False]}

data = pd.DataFrame(disciplinas)
data