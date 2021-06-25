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
    """programa : expression
                |impresion
                |sentencia """

def p_impresion(p):
    '''impresion : FMT.PRINT PARENT_IZQ expression PARENT_DER|PRINT PARENT_IZQ PARENT_DER'''

def p_expression_plus(p):
    'expression : expression MAS term'

def p_expression_minus(p):
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
    'sentencia : IF factor comparacion factor LKEY cuerpo RKEY'

def p_comparacion(p):
    '''comparacion : IGUALDAD
                    |MAYOR
                    |MENOR
                    |MAYOR_IGU
                    |MENOR_IGU'''

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_id(p):
    'factor : ID'

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'

def p_empty(p):
    'empty : '
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")
# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)