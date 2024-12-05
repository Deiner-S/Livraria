import os

diretorio_atual = os.getcwd()
print("Diretório atual:", diretorio_atual)

diretorio_pai = os.path.dirname(diretorio_atual)
print(f"Diretório pai: {diretorio_pai}")