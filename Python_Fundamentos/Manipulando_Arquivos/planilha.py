import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
ID_COLUMN = 0
NAME_COLUMN = 1

# try:
#     with open(f"{ROOT_PATH}/usuario.csv", "w", encoding="utf-8") as file:
#         escritor = csv.writer(file)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "otoniel"])
#         escritor.writerow(["2", "João"])
# except IOError as exc:
#     print(f"Erro de ao criar arquivo: {exc}")

# try:
#     with open(f"{ROOT_PATH}/usuario.csv", "r", newline="", encoding="utf-8") as file:
#         leitor = csv.reader(file)
#         for idx, row in enumerate(leitor):
#             if idx == 0:
#                 continue
#             print(f"ID: {row[ID_COLUMN]}")
#             print(f"Nome: {row[NAME_COLUMN]}")
# except IOError as exc:
#     print(f"Erro de ao criar arquivo: {exc}")

try:
    with open(f"{ROOT_PATH}/usuario.csv", "r", newline="", encoding="utf-8") as file:
        leitor = csv.DictReader(file)
        for idx, row in enumerate(leitor):
            print(row["id"], row["nome"])
except IOError as exc:
    print(f"Erro de ao criar arquivo: {exc}")
