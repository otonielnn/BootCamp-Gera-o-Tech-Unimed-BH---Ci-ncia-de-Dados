import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# os.mkdir(f"{ROOT_PATH}/novo-diretorio")
file = open("novo-arquivo.txt", "w")
# file.close()

# os.rename(f"{ROOT_PATH}/novo-arquivo.txt", F"{ROOT_PATH}/treloso.txt")

# os.remove(f"{ROOT_PATH}/alterado.txt")
# os.remove(f"{ROOT_PATH}/treloso.txt")

shutil.move(f"{ROOT_PATH}/novo-arquivo.txt", f"{ROOT_PATH}/novo-diretorio")
