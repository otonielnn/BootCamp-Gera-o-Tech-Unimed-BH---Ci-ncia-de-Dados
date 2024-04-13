from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    file = open(f"{ROOT_PATH}/novo-diretorio/novo-arquivo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possivel abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abarir o arquivo: {exc}")

file.close()
