import ply.lex as lex

#lista de tokens
token = ("NUMERO", "MAS", "MENOS", "MULTIPLICADOR", "DIVISOR", "MOD_DIVISION", "PARENT_IZQ","PARENT_DER",
           "CORCHETE_IZQ", "CORCHETE_DER", "LLAVE_IZQ", "LLAVE_DER", "PUNTO", "DOS_PUNTOS", "COMA","COMILLA",
           "DOBLE_COMILLA","COMENT_BLOQUE_IZQ", "COMENT_BLOQUE_DER", "COMENT_LINEA", "FIN_SENTENCIA", "ID", "ASIGNACION",
           "ESPACIADO", "CADENA", "MENOR", "MAYOR", "IGUALDAD", "VACIO", "MENOR_IGU", "MAYOR_IGU")
print(len(token)) #31

#lista de palabras reservadas
reservada = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'defer': 'DEFER',
    'select': 'SELECT',
    'func': 'FUNC',
    'interface': 'INTERFACE',
    'go': 'GO',
    'map': 'MAP',
    'struct': 'STRUCT',
    'chan': 'CHAN',
    'const': 'CONST',
    'package': 'Package',
    'fallthrough': 'FALLTHROUGH',
    'range': 'RANGE',
    'type': 'TYPE',
    'for': 'FOR',
    'import': 'IMPORT',
    'return': 'RETURN',
    'var': 'VAR',
    'fmt': 'FMT',
    'io': 'IO',
    'log': 'LOG',
    'os': 'OS',
    'main': 'MAIN'
}
print(len(reservada)) #30

token = token + tuple(reservada.values())
print(len(token)) #61
print(token)

#expresiones regulares para tokens simples
t_ignore = r' \t'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICADOR = r'\*'
t_DIVISOR = r'/'
t_MOD_DIVISION = r'%'
t_PARENT_IZQ = r'\('
t_PARENT_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PUNTO = r'\.'
t_DOS_PUNTOS = r':'
t_VACIO = r'_'
t_ASIGNACION = r':='
t_IGUALDAD = r'=='
t_FIN_SENTENCIA = r';'
t_COMA = r','
t_COMILLA = r'\''
t_DOBLE_COMILLA = r'\"'
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MENOR_IGU = r'\<='
t_MAYOR_IGU = r'\>='
t_ESPACIADO = r' '

#funcion para reconocer identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservada.get(t.value, 'ID')
    return t

#funcion para reconocer comentarios y no tomarlos en cuenta
def t_COMMENT(t):
    r'(\#.*)|(\/\*.*\*\/)'
    pass

#función para reconocer números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#función para conocer el número de linea donde me encuentro
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#función para manejar errores en los tokens
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#función para obtener tokens
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

#crear el analizador lexico:
lexer = lex.lex()
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")