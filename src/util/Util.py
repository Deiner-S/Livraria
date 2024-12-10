import random
import string

def remover_especiais(text):    
    replacements = [('Ã', 'A'),('Â', 'A'),('Á', 'A'),('À', 'A'),
                    ('É', 'E'),('Ê', 'E'),('Í', 'I'),('Ó', 'O'),
                    ('Ô', 'O'),('Õ', 'O'),('Ú', 'U'),('Ç', 'C')
                    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def id_alfanumerico():
    caracteres = string.ascii_letters + string.digits
    id_pedido = ''.join(random.choices(caracteres, k=6))
    return id_pedido
def id_numerico():
    id_pedido = random.random()
    return round(id_pedido*100000000)
def main():
    print(id_numerico())
if __name__ == "__main__":
    main()