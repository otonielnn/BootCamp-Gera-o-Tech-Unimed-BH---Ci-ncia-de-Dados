from pathlib import Path

ROOT_PATH = Path(__file__).parent
try:
    with open(f"{ROOT_PATH}/lorem.txt", "r") as file:
        print("file open")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

# try:
#     with open(f"{ROOT_PATH}/arquivo-utf-8.txt", "w", encoding="utf-8") as file:
#         file.write("Apredendo a manipular arquivos utilizando python. çç")
# except IOError:
#     print(f"Erro ao abrir o arquivo: {exc}")

try:
    with open(f"{ROOT_PATH}/arquivo-utf-8.txt", "r", encoding="ascii") as file:
        print(file.read())
except IOError:
    print(f"Erro ao abrir o arquivo: {exc}")
except UnicodeDecodeError as exc:
    print(exc)
