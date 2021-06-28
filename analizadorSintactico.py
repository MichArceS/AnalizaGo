import ply.yacc as yacc
from analizadorLexico import tokens

precedence = (
    ("right", "ASIGNACION"),
    ("left", "IGUALDAD", "MAYOR", "MENOR", "MENOR_IGU", "MAYOR_IGU"),
    ("left", "MAS", "MENOS"),
    ("left", "MULTIPLICADOR", "DIVISOR"),
    ("left", "PARENT_IZQ", "PARENT_DER")
)

def p_programa(p):
    '''programa : expression
                | impresion
                | sentencia 
                | asignacion
                | longvariable
                | boolcadena
                | companum
                | compaid
                | sentenciafor
                | arreglo
                | slice
                | capslice'''

def p_impresion(p):
    """impresion :  PARENT_IZQ expression PARENT_DER
                | PARENT_IZQ empty PARENT_DER"""

def p_longitud_variables(p):
    '''longvariable : ID PARENT_IZQ CADENA PARENT_DER
                        | ID PARENT_IZQ ID PARENT_DER'''

def p_bool_cadena(p):
    'boolcadena : ID PUNTO ID PARENT_IZQ factor PARENT_DER'

def p_comparacion_num(p):
    'companum : NUMERO comparacion NUMERO'

def p_comparacion_id(p):
    'compaid : ID comparacion ID'

def p_asignacion_var(p):
    '''asignacion : ID ASIGNACION factor
                    | VAR ID ID ASIGNACION factor
                    | VAR ID COMA ID ID ASIGNACION factor COMA factor'''

def p_sentencia_for(p):
    'sentenciafor : FOR ID ASIGNACION factor FIN_SENTENCIA ID comparacion factor FIN_SENTENCIA incremento LLAVE_IZQ programa LLAVE_DER'

def p_incremento(p):
    '''incremento : ID INCREMENTO
                    | ID ASIGNACION ID
                    | ID DECREMENTO'''

def p_definir_arreglo(p):
    '''arreglo : ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER ID 
                    | ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER ID LLAVE_IZQ valores LLAVE_DER'''

def p_cantidad_arreglo(p):
    '''cantidad : NUMERO 
                    | ARRPUNTOS'''

def p_valores_arreglo(p):
    '''valores : factor
                    | factor COMA valores'''

def p_definir_slice(p):
    '''slice : ID ASIGNACION ID PARENT_IZQ CORCHETE_IZQ CORCHETE_DER ID COMA NUMERO PARENT_DER
                | ID ASIGNACION ID PARENT_IZQ CORCHETE_IZQ CORCHETE_DER ID COMA NUMERO COMA NUMERO PARENT_DER'''

def p_cap_slice(p):
    'capslice : ID PARENT_IZQ ID PARENT_DER'

def p_expression_mas(p):
    'expression : expression MAS term'

def p_expression_menos(p):
    'expression : expression MENOS term'

def p_expression_term(p):
    'expression : term'

def p_term_multiplicador(p):
    'term : term MULTIPLICADOR factor'

def p_term_divisor(p):
    'term : term DIVISOR factor'

def p_term_mod(p):
    'term : term MOD_DIVISION factor'

def p_term_factor(p):
    'term : factor'

def p_sentencia_if(p):
    'sentencia : IF factor comparacion factor LLAVE_IZQ programa LLAVE_DER'

def p_comparacion_igu(p):
    'comparacion : IGUALDAD'

def p_comparacion_mayor(p):
    'comparacion : MAYOR'

def p_comparacion_menor(p):
    'comparacion : MENOR'

def p_comparacion_mayor_igu(p):
    'comparacion : MAYOR_IGU'

def p_comparacion_menor_igu(p):
    'comparacion : MENOR_IGU'

def p_comparacion_desigu(p):
    'comparacion : DESIGUALDAD'

def p_factor_num(p):
    'factor : NUMERO'

def p_factor_id(p):
    'factor : ID'

def p_factor_cadena(p):
    'factor : CADENA'

def p_factor_expr(p):
    'factor : PARENT_IZQ expression PARENT_DER'

def p_empty(p):
    'empty : '
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Error de sintaxis en el token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Error de sintaxis en EOF")

# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('Go >> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)