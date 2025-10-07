import csv
#Aqui é onde vai pegar os itens do csv e instanciar objetos

# Class
# Lista musicas, podcasts, etc...

# Colocar num try pois pode dar erro caso não encontre o arquivo.
def carregar_csv():
    with open("nome.csv", "r", newline="", encoding = "utf-8") as csv:
        reader = csv.DictReader(csv)
        for row in reader:
            print(row)
            # self.__muscias.append(Musica.row...)