import csv
def read_csv(filepath):
    table = list()  # Tabela é uma lista de linhas
    with open(filepath) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            table.append(row)

    return table

titanic_tbl = read_csv("train.csv")
titanic_tbl
soma_idade = 0
soma_idade_vivos = 0
soma_idade_mortos = 0
contados = 0
contados_vivos = 0
contados_mortos = 0
idades = 0
idades_vivos = 0
idedes_mortos = 0
"""
for passg in titanic_tbl:
  try:
      soma_idade += float(passg["Age"])
      if (passg["Survived"]=="1"):
          soma_idade_vivos += float(passg["Age"])
          contados_vivos +=1
      else:
          soma_idade_mortos += float(passg["Age"])
          contados_mortos +=1
      contados +=1
  except(ValueError):
      pass
"""
def is_float(x):
    try:
        float(x)
        return True
    except:
        return False

idades = [float(passg["Age"])for passg in titanic_tbl
           if is_float(passg["Age"])]

idades_vivos = [float(passg["Age"])for passg in titanic_tbl
           if is_float(passg["Age"]) and passg["Survived"]=="1"]

idades_mortos = [float(passg["Age"])for passg in titanic_tbl
           if is_float(passg["Age"]) and passg["Survived"]=="0"]


media = sum(idades)/len(idades)
media_vivos = sum(idades_vivos)/len(idades_vivos)
media_mortos = sum(idades_mortos)/len(idades_mortos)

print("Media idade todos:", "%.2f" % media)
print("Media idade todos:", "%.2f" % media_vivos)
print("Media idade todos:", "%.2f" % media_mortos)
