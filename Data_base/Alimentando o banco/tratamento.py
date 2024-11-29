import os
def remover_especiais(text):    
    replacements = [('Ã', 'A'),('Â', 'A'),('Á', 'A'),('À', 'A'),
                    ('É', 'E'),('Ê', 'E'),('Í', 'I'),('Ó', 'O'),
                    ('Ô', 'O'),('Õ', 'O'),('Ú', 'U'),('Ç', 'C')
                    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def main():
    with open("Data_base\livro.txt", "r", encoding="utf-8") as arquivo:
        lista = arquivo.readlines()
        lista_tratada = []
        for i in lista:
            lista_tratada.append(remover_especiais(i.upper()))

    with open("Data_base\livro.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(lista_tratada)

if __name__ == "__main__":
    main()