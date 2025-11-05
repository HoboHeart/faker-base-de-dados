from faker import Faker
import pandas as pd
import random

#1. Instanciando o Faker
fake = Faker('pt_BR')

#2. Definindo a quantidade de prédios
NUMERO_DE_PREDIOS = 100

#Criando as listas para armazenar os dados:
dados_locacoes = []
dados_detalhes = []

print(f"Gerando {NUMERO_DE_PREDIOS} registros de prédios...")

CIDADES_DO_ESTADO = ['Fortaleza', 'Caucaia', 'Juazeiro do Norte', 'Maracanaú', 'Sobral', 'Crato', 'Itapipoca', 'Maranguape', 'Iguatu', 'Quixadá', 'Tianguá', 'Quixeramobim', 'Pacatuba', 'Aquiraz', 'Eusébio']

#3. Criação dos dados:
for i in range(1, NUMERO_DE_PREDIOS + 1):
    
    #ID único, padronizado como PREDDIO_0001, PREDIO_0002, etc.
    predio_id = f"PREDIO_{i:04d}"

    
    cidade_escolhida = random.choice(CIDADES_DO_ESTADO)

    #BASE DE DADOS 01 - LOCAÇÕES:
    locacao = {
        "predio_id": predio_id,
        "endereco": fake.street_address(),
        "bairro": fake.bairro(),
        "cidade": cidade_escolhida,
        "estado": 'CE',
        "cep": fake.postcode(),
    }

    dados_locacoes.append(locacao)

    #BASE DE DADOS 02 - DETALHES DAS LOCAÇÕES:

    tamanho_m2 = random.randint(150,2000) #Randomização do tamanho em m2
    preco_base = random.randint(3000, 15000) #Randomização do preço base por m2
    #O preço estimado está sendo calculado com uma variação de 10%
    

    detalhe = {
        "predio_id": predio_id,
        "tamanho_m2": tamanho_m2,
        "preco_estimado": round(tamanho_m2 * preco_base * (1 + random.uniform(-0.1, 0.1)), 2),
        "quantidade_de_salas": random.randint(5,50),
        "ano_construcao": fake.year(),
        "descricao": fake.text(max_nb_chars=200),
        "responsavel": fake.name(),
        "telefone": fake.cellphone_number()
    }
    dados_detalhes.append(detalhe)

#4. Conversão para Dataframes

df_locacoes = pd.DataFrame(dados_locacoes)
df_detalhes = pd.DataFrame(dados_detalhes)

#5. Salvando em CSV(Locações) e JSON(Detalhes)

#Locações em CSV
df_locacoes.to_csv('base_1_locacoes.csv', index=False, encoding='utf-8-sig')
print("\nArquivo 'base_1_locacoes.csv' criado com sucesso!")

df_detalhes.to_json('base_2_detalhes_predios.json', orient='records', indent=4, force_ascii=False)
print("\nArquivo 'base_2_detalhes_predios.json' criado com sucesso!")

print("\n--- Amostra Base 1: Locações (CSV) ---")
print(df_locacoes.head())

print("\n--- Amostra Base 2: Detalhes (JSON) ---")
print(df_detalhes.head())