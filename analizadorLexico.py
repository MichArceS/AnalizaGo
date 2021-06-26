import ply.lex as lex
# lista de tokens
tokens = ("NUMERO", "CADENA", "MAS", "MENOS", "MULTIPLICADOR", "DIVISOR", "MOD_DIVISION", "PARENT_IZQ", "PARENT_DER",
          "CORCHETE_IZQ", "CORCHETE_DER", "LLAVE_IZQ", "LLAVE_DER", "PUNTO", "DOS_PUNTOS", "COMA", "COMILLA",
          "DOBLE_COMILLA", "COMMENT_BLOQUE_IZQ", "COMMENT_BLOQUE_DER", "COMMENT_LINEA", "FIN_SENTENCIA", "ID", "ASIGNACION",
          "ESPACIADO", "MENOR", "MAYOR", "IGUALDAD", "VACIO", "MENOR_IGU", "MAYOR_IGU", "BOOLEAN", "DESIGUALDAD", "INCREMENTO", 
          "DECREMENTO", "PIPE", "AMPERSAND", "FMT", "PRINT")
print(len(tokens))  # 31

# lista de palabras reservadas
reservada = {
    'break': 'BREAK',
    'default': 'DEFAULT',
    'func': 'FUNC',
    'interface': 'INTERFACE',
    'select': 'SELECT',
    'case': 'CASE',
    'defer': 'DEFER',
    'go': 'GO',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'continue': 'CONTINUE',
    'map': 'MAP',
    'struct': 'STRUCT',
    'const': 'CONST',
    'package': 'Package',
    'fallthrough': 'FALLTHROUGH',
    'range': 'RANGE',
    'type': 'TYPE',
    'for': 'FOR',
    'import': 'IMPORT',
    'return': 'RETURN',
    'var': 'VAR'
}
print(len(reservada))  # 30

tokens = tokens + tuple(reservada.values())
print(len(tokens))  # 61

# expresiones regulares para tokens simples
t_ignore = ' \t'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTIPLICADOR = r'\*'
t_DIVISOR = r'\/'
t_MOD_DIVISION = r'\%'
t_PARENT_IZQ = r'\('
t_PARENT_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PUNTO = r'\.'
t_DOS_PUNTOS = r'\:'
t_VACIO = r'\_'
t_ASIGNACION = r'\:?\='
t_IGUALDAD = r'=='
t_FIN_SENTENCIA = r';'
t_COMA = r','
t_COMILLA = r'\''
t_DOBLE_COMILLA = r'\"'
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MENOR_IGU = r'\<='
t_MAYOR_IGU = r'\>='
t_DESIGUALDAD = r'!='
t_INCREMENTO = r'\+{2}'
t_DECREMENTO = r'\-{2}'
t_PIPE = r'\|'
t_AMPERSAND = '\&'
# funcion para reconocer identificadores


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservada.get(t.value, 'ID')
    return t

# funcion para reconocer comentarios y no tomarlos en cuenta


def t_COMMENT(t):
    r'(\/\/.*)|(\/\*.*\*\/)'
    pass

# función para reconocer número


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# función para reconocer cadena


def t_CADENA(t):
    r'(\'.*\')|(".*")'
    return t

# función para reconocer boolean


def t_BOOLEAN(t):
    r'true|false'
    return t


# función para reconocer flotantes
def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    return t

# función para conocer el número de linea donde me encuentro


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# función para manejar errores en los tokens


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# función para obtener tokens


def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


# Build the lexer
lexer = lex.lex()

# linea = " "
# while linea != "":
#     linea = input("Go >>")
#     lexer.input(linea)
#     getTokens(lexer)
