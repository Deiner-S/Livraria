
def remover_especiais(text):    
    replacements = [('Ã', 'A'),('Â', 'A'),('Á', 'A'),('À', 'A'),
                    ('É', 'E'),('Ê', 'E'),('Í', 'I'),('Ó', 'O'),
                    ('Ô', 'O'),('Õ', 'O'),('Ú', 'U'),('Ç', 'C')
                    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text
