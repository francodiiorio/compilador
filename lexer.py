# lexer.py
import ply.lex as lex

# Palabras reservadas
reserved = {
    'si': 'SI',
    'entonces': 'ENTONCES',
    'sino': 'SINO',
    'mientras': 'MIENTRAS',
    'leer': 'LEER',
    'escribir': 'ESCRIBIR'
}

# Lista de tokens
tokens = (
    'IDENTIFICADOR',
    'NUMERO',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'IGUAL',
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'DISTINTO',
    'PUNTOCOMA',
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZQ',
    'LLAVEDER'
) + tuple(reserved.values())

# Expresiones regulares para tokens simples
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_IGUAL = r'='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUALIGUAL = r'=='
t_DISTINTO = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_PUNTOCOMA = r';'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'

# Ignorar espacios y tabs
t_ignore = ' \t'

# Definición para tokens complejos (IDENTIFICADOR y NUMERO)
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Chequear palabras reservadas
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# Construir lexer
lexer = lex.lex()

# Prueba del lexer
if __name__ == "__main__":
    data = '''
    leer x;
    si (x > 10) entonces {
        escribir x + 5;
    } sino {
        escribir x - 5;
    }
    '''

    lexer.input(data)
    for tok in lexer:
        print(tok)