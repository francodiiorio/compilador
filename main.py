# main.py (Intérprete interactivo REPL)
from lexer import lexer
from mi_parser import parser

print("🧉 MateLang REPL - Escribí 'salir' para terminar 🧉")

codigo_completo = ''

while True:
    try:
        entrada = input('>>> ')
        if entrada.strip() == 'salir':
            print("👋 ¡Chau, nos vemos pronto!")
            break
        if entrada.strip() == '':
            continue

        # Añadimos cada línea ingresada al código completo
        codigo_completo += entrada + '\n'

        # Intentamos parsear y ejecutar inmediatamente
        resultado = parser.parse(codigo_completo)

        # Reiniciamos código_completo si la ejecución es exitosa
        codigo_completo = ''

    except Exception as e:
        print(f"⚠️ Error: {e}")
        # Si hay error, limpiamos para seguir ingresando
        codigo_completo = ''
