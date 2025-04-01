# mi_parser.py
import ply.yacc as yacc
from lexer import tokens

variables = {}

# Regla principal del lenguaje
def p_programa(p):
    '''programa : sentencias'''
    pass

def p_sentencias(p):
    '''sentencias : sentencias sentencia
                  | sentencia'''
    pass

def p_sentencia(p):
    '''sentencia : asignacion
                 | entrada
                 | salida'''
    pass

# Reglas que ya tenías (las mismas, completas)

def p_asignacion(p):
    'asignacion : IDENTIFICADOR IGUAL expresion PUNTOCOMA'
    variables[p[1]] = p[3]

def p_expresion_operacion(p):
    '''expresion : expresion MAS termino
                 | expresion MENOS termino'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]

def p_expresion_termino(p):
    'expresion : termino'
    p[0] = p[1]

def p_termino_operacion(p):
    '''termino : termino POR factor
               | termino DIVIDIDO factor'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        p[0] = p[1] / p[3]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]

def p_factor_numero(p):
    'factor : NUMERO'
    p[0] = p[1]

def p_factor_variable(p):
    'factor : IDENTIFICADOR'
    p[0] = variables.get(p[1], 0)

def p_entrada(p):
    'entrada : LEER IDENTIFICADOR PUNTOCOMA'
    variables[p[2]] = int(input(f"Ingrese el valor de {p[2]}: "))

def p_salida(p):
    'salida : ESCRIBIR expresion PUNTOCOMA'
    print("Salida:", p[2])

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error sintáctico cerca de '{p.value}' en línea {p.lineno}")
    else:
        print("Error sintáctico al final del archivo")

parser = yacc.yacc()
