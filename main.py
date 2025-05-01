# main.py
from lexer import lexer
from mi_parser import parser

# Ruta del archivo con el código fuente
archivo_codigo = "codigo.txt"

try:
    with open(archivo_codigo, 'r') as archivo:
        codigo = archivo.read()
        print("📄 Código a analizar:\n", codigo)
        print("\n🔍 Analizando...\n")
        resultado = parser.parse(codigo, lexer=lexer)
        print("\n✅ Análisis completado.")
except FileNotFoundError:
    print(f"❌ No se encontró el archivo '{archivo_codigo}'")
except Exception as e:
    print(f"⚠️ Error durante el análisis: {e}")
