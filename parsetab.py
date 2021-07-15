
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNACIONleftIGUALDADMAYORMENORMENOR_IGUMAYOR_IGUleftMASMENOSleftMULTIPLICADORDIVISORleftPARENT_IZQPARENT_DERAMPERSAND ARRPUNTOS ASIGNACION BOOLEAN BREAK CADENA CASE COMA COMILLA COMMENT_BLOQUE_DER COMMENT_BLOQUE_IZQ COMMENT_LINEA CONST CONTAINS CONTINUE CORCHETE_DER CORCHETE_IZQ DECREMENTO DEFAULT DEFER DELETE DESIGUALDAD DIVISOR DOBLE_COMILLA DOS_PUNTOS ELSE ESPACIADO FALLTHROUGH FALSE FIN_SENTENCIA FLOAT FLOAT32 FLOAT64 FMT FOR FORMATBOOL FORMATFLOAT FORMATINT FUNC GO ID IF IGUAL IGUALDAD IMPORT INCREMENTO INT INT32 INT64 INTERFACE LEN LLAVE_DER LLAVE_IZQ MAKE MAP MAS MAYOR MAYOR_IGU MENOR MENOR_IGU MENOS MOD_DIVISION MULTIPLICADOR NUMERO PACKAGE PARENT_DER PARENT_IZQ PARSEBOOL PARSEFLOAT PARSEINT PIPE PRINTF PRINTLN PUNTO RANGE RETURN SELECT SPLIT STRCONV STRING STRINGS STRUCT SWITCH TRUE TYPE VACIO VARprograma : expression\n                | impresion\n                | sentencia \n                | asignacion\n                | longvariable\n                | boolcadena\n                | companum\n                | compaid\n                | sentenciafor\n                | arreglo\n                | slice\n                | capslice\n                | switch\n                | map\n                | asignar_valor_map\n                | eliminar_valor_map\n                | obtener_valor_map\n                | funcion\n                | cadenabool\n                | enterocadena\n                | cadenaentero\n                | flotantecadena\n                | cadenaflotante\n                | seman_operacion\n                | incrementoimpresion : FMT PUNTO PRINTF PARENT_IZQ CADENA COMA NUMERO PARENT_DER\n                | FMT PUNTO PRINTF PARENT_IZQ empty PARENT_DER\n                | FMT PUNTO PRINTLN PARENT_IZQ CADENA COMA NUMERO PARENT_DER\n                | FMT PUNTO PRINTLN PARENT_IZQ empty PARENT_DER\n                | FMT PUNTO PRINTLN PARENT_IZQ CADENA PARENT_DER\n                longvariable : ID PARENT_IZQ CADENA PARENT_DER\n                        | ID PARENT_IZQ ID PARENT_DERcompanum : NUMERO comparacion NUMEROcompaid : ID comparacion IDasignacion : ID ASIGNACION factor\n                    | VAR ID tipo_dato ASIGNACION factor\n                    | VAR ID COMA ID tipo_dato ASIGNACION factor COMA factorsentenciafor : FOR ID ASIGNACION factor FIN_SENTENCIA ID comparacion factor FIN_SENTENCIA incremento LLAVE_IZQ programa LLAVE_DERincremento : ID INCREMENTO\n                    | ID ASIGNACION ID\n                    | ID DECREMENTOarreglo : ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato \n                    | ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DERcantidad : NUMERO \n                    | ARRPUNTOSvalores : factor\n                    | factor COMA valoresslice : ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO PARENT_DER\n                | ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO COMA NUMERO PARENT_DERcapslice : ID PARENT_IZQ ID PARENT_DERexpression : expression MAS termexpression : expression MENOS termexpression : termterm : term MULTIPLICADOR factorterm : term DIVISOR factorterm : term MOD_DIVISION factorterm : factorsentencia : IF factor comparacion factor LLAVE_IZQ programa LLAVE_DERcomparacion : IGUALDADcomparacion : MAYORcomparacion : MENORcomparacion : MAYOR_IGUcomparacion : MENOR_IGUcomparacion : DESIGUALDADfactor : NUMEROfactor : IDfactor : CADENAfactor : FLOATfactor : PARENT_IZQ expression PARENT_DERswitch : SWITCH ID LLAVE_IZQ cases LLAVE_DERcases : case \n                | case default \n                | case casescase : CASE factor DOS_PUNTOS programadefault : DEFAULT DOS_PUNTOS programamap : VAR ID MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER \n                | ID ASIGNACION MAKE PARENT_IZQ MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato PARENT_DER\n                | ID ASIGNACION MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DERtipo_dato : INT \n                    | STRING \n                    | INT64 \n                    | FLOAT32 \n                    | FLOAT64 \n                    | INT32valores : clave_valor \n                | clave_valor COMA valoresclave_valor : valor DOS_PUNTOS valorvalor : CADENA\n                | NUMEROasignar_valor_map : ID CORCHETE_IZQ valor CORCHETE_DER ASIGNACION valoreliminar_valor_map : DELETE PARENT_IZQ ID COMA valor PARENT_DERobtener_valor_map : ID CORCHETE_IZQ valor CORCHETE_DERfuncion : FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa LLAVE_DER \n                    | FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa RETURN ID LLAVE_DER\n                    | FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ RETURN ID LLAVE_DERargumentos : ID tipo_dato \n                    | ID tipo_dato COMA argumentosempty : seman_operacion : NUMERO MAS NUMERO \n                        | NUMERO MENOS NUMERO\n                        | NUMERO MULTIPLICADOR NUMERO\n                        | NUMERO DIVISOR NUMERO\n                        | NUMERO MOD_DIVISION NUMERO\n                        | FLOAT MAS NUMERO\n                        | FLOAT MENOS NUMERO\n                        | FLOAT MULTIPLICADOR NUMERO\n                        | FLOAT DIVISOR NUMERO\n                        | NUMERO MAS FLOAT\n                        | NUMERO MENOS FLOAT\n                        | NUMERO MULTIPLICADOR FLOAT\n                        | NUMERO DIVISOR FLOAT\n                        | FLOAT MAS FLOAT\n                        | FLOAT MENOS FLOAT\n                        | FLOAT MULTIPLICADOR FLOAT\n                        | FLOAT DIVISOR FLOATboolcadena : STRCONV PUNTO FORMATBOOL PARENT_IZQ BOOLEAN PARENT_DERcadenabool : STRCONV PUNTO PARSEBOOL PARENT_IZQ CADENA PARENT_DERflotantecadena : STRCONV PUNTO FORMATFLOAT PARENT_IZQ FLOAT COMA CADENA COMA NUMERO PARENT_DERcadenaflotante : STRCONV PUNTO PARSEFLOAT PARENT_IZQ CADENA COMA NUMERO PARENT_DERenterocadena : STRCONV PUNTO FORMATINT PARENT_IZQ NUMERO COMA NUMERO PARENT_DERcadenaentero : STRCONV PUNTO PARSEINT PARENT_IZQ CADENA COMA NUMERO COMA NUMERO PARENT_DER'
    
_lr_action_items = {'FMT':([0,169,213,214,235,287,],[28,28,28,28,28,28,]),'IF':([0,169,213,214,235,287,],[32,32,32,32,32,32,]),'ID':([0,29,32,35,37,38,40,42,43,44,45,46,58,59,60,61,62,63,65,66,67,75,99,112,126,129,149,161,169,184,204,213,214,216,221,231,235,246,247,248,255,257,258,267,269,286,287,],[34,50,50,71,73,74,76,50,50,50,50,50,-59,-60,-61,-62,-63,-64,100,105,107,128,50,150,50,163,50,50,34,212,50,34,34,163,50,50,34,50,50,50,270,50,50,281,283,290,34,]),'VAR':([0,169,213,214,235,287,],[35,35,35,35,35,35,]),'STRCONV':([0,169,213,214,235,287,],[36,36,36,36,36,36,]),'NUMERO':([0,29,32,42,43,44,45,46,52,53,54,55,56,57,58,59,60,61,62,63,65,68,77,78,79,80,99,102,126,149,154,161,162,169,174,193,195,204,208,209,211,213,214,221,231,235,244,246,247,248,250,251,257,258,259,274,287,],[31,49,49,49,49,49,49,49,89,90,92,94,96,98,-59,-60,-61,-62,-63,-64,49,110,131,133,135,137,49,142,49,49,180,49,110,31,110,218,219,49,227,228,230,31,31,241,49,31,260,241,49,241,265,266,241,241,110,285,31,]),'FOR':([0,169,213,214,235,287,],[37,37,37,37,37,37,]),'SWITCH':([0,169,213,214,235,287,],[38,38,38,38,38,38,]),'DELETE':([0,169,213,214,235,287,],[39,39,39,39,39,39,]),'FUNC':([0,169,213,214,235,287,],[40,40,40,40,40,40,]),'FLOAT':([0,29,32,42,43,44,45,46,53,54,55,56,58,59,60,61,62,63,65,77,78,79,80,99,126,149,156,161,169,204,213,214,221,231,235,246,247,248,257,258,287,],[41,51,51,51,51,51,51,51,91,93,95,97,-59,-60,-61,-62,-63,-64,51,130,132,134,136,51,51,51,182,51,41,51,41,41,51,51,41,51,51,51,51,51,41,]),'CADENA':([0,29,32,42,43,44,45,46,58,59,60,61,62,63,65,66,68,99,126,138,139,149,153,155,157,161,162,169,174,204,210,213,214,221,231,235,246,247,248,257,258,259,287,],[30,30,30,30,30,30,30,30,-59,-60,-61,-62,-63,-64,30,106,109,30,30,165,167,30,179,181,183,30,109,30,109,30,229,30,30,242,30,30,242,30,242,242,242,109,30,]),'PARENT_IZQ':([0,29,32,34,39,42,43,44,45,46,58,59,60,61,62,63,65,76,86,87,99,103,120,121,122,123,124,125,126,149,161,169,204,213,214,221,231,235,246,247,248,257,258,287,],[29,29,29,66,75,29,29,29,29,29,-59,-60,-61,-62,-63,-64,29,129,138,139,29,144,152,153,154,155,156,157,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,33,34,41,49,50,51,69,70,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,98,100,101,107,109,110,114,115,116,117,118,119,130,131,132,133,134,135,136,137,146,147,148,175,185,194,196,197,199,203,206,207,215,220,236,237,249,252,256,263,268,275,276,277,278,279,280,284,288,289,292,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-53,-67,-65,-57,-66,-68,-65,-66,-68,-39,-41,-51,-52,-54,-55,-56,-69,-33,-99,-108,-100,-109,-101,-110,-102,-111,-103,-40,-35,-34,-88,-89,-79,-80,-81,-82,-83,-84,-112,-104,-113,-105,-114,-106,-115,-107,-32,-31,-92,-36,-70,-27,-30,-29,-42,-90,-116,-117,-91,-58,-26,-28,-120,-119,-43,-37,-93,-48,-77,-78,-76,-121,-118,-95,-94,-49,-38,]),'LLAVE_DER':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,33,34,41,49,50,51,69,70,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,98,100,101,107,109,110,114,115,116,117,118,119,130,131,132,133,134,135,136,137,146,147,148,159,160,175,185,186,187,194,196,197,198,199,203,206,207,215,220,232,233,236,237,238,239,240,241,242,249,252,254,256,262,263,264,268,270,271,272,273,275,276,277,278,279,280,283,284,288,289,291,292,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-53,-67,-65,-57,-66,-68,-65,-66,-68,-39,-41,-51,-52,-54,-55,-56,-69,-33,-99,-108,-100,-109,-101,-110,-102,-111,-103,-40,-35,-34,-88,-89,-79,-80,-81,-82,-83,-84,-112,-104,-113,-105,-114,-106,-115,-107,-32,-31,-92,185,-71,-36,-70,-72,-73,-27,-30,-29,220,-42,-90,-116,-117,-91,-58,-75,-74,-26,-28,256,-46,-85,-65,-67,-120,-119,268,-43,277,-37,278,-93,284,-47,-86,-87,-48,-77,-78,-76,-121,-118,288,-95,-94,-49,292,-38,]),'DEFAULT':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,33,34,41,49,50,51,69,70,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,98,100,101,107,109,110,114,115,116,117,118,119,130,131,132,133,134,135,136,137,146,147,148,160,175,185,194,196,197,199,203,206,207,215,220,233,236,237,249,252,256,263,268,275,276,277,278,279,280,284,288,289,292,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-53,-67,-65,-57,-66,-68,-65,-66,-68,-39,-41,-51,-52,-54,-55,-56,-69,-33,-99,-108,-100,-109,-101,-110,-102,-111,-103,-40,-35,-34,-88,-89,-79,-80,-81,-82,-83,-84,-112,-104,-113,-105,-114,-106,-115,-107,-32,-31,-92,188,-36,-70,-27,-30,-29,-42,-90,-116,-117,-91,-58,-74,-26,-28,-120,-119,-43,-37,-93,-48,-77,-78,-76,-121,-118,-95,-94,-49,-38,]),'CASE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,33,34,41,49,50,51,69,70,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,98,100,101,107,109,110,114,115,116,117,118,119,127,130,131,132,133,134,135,136,137,146,147,148,160,175,185,194,196,197,199,203,206,207,215,220,233,236,237,249,252,256,263,268,275,276,277,278,279,280,284,288,289,292,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-53,-67,-65,-57,-66,-68,-65,-66,-68,-39,-41,-51,-52,-54,-55,-56,-69,-33,-99,-108,-100,-109,-101,-110,-102,-111,-103,-40,-35,-34,-88,-89,-79,-80,-81,-82,-83,-84,161,-112,-104,-113,-105,-114,-106,-115,-107,-32,-31,-92,161,-36,-70,-27,-30,-29,-42,-90,-116,-117,-91,-58,-74,-26,-28,-120,-119,-43,-37,-93,-48,-77,-78,-76,-121,-118,-95,-94,-49,-38,]),'RETURN':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,30,31,33,34,41,49,50,51,69,70,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,98,100,101,107,109,110,114,115,116,117,118,119,130,131,132,133,134,135,136,137,146,147,148,175,185,194,196,197,199,203,206,207,215,220,235,236,237,249,252,254,256,263,268,275,276,277,278,279,280,284,288,289,292,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-53,-67,-65,-57,-66,-68,-65,-66,-68,-39,-41,-51,-52,-54,-55,-56,-69,-33,-99,-108,-100,-109,-101,-110,-102,-111,-103,-40,-35,-34,-88,-89,-79,-80,-81,-82,-83,-84,-112,-104,-113,-105,-114,-106,-115,-107,-32,-31,-92,-36,-70,-27,-30,-29,-42,-90,-116,-117,-91,-58,255,-26,-28,-120,-119,269,-43,-37,-93,-48,-77,-78,-76,-121,-118,-95,-94,-49,-38,]),'MAS':([2,27,30,31,33,34,41,48,49,50,51,81,82,83,84,85,88,],[42,-53,-67,53,-57,-66,77,42,-65,-66,-68,-51,-52,-54,-55,-56,-69,]),'MENOS':([2,27,30,31,33,34,41,48,49,50,51,81,82,83,84,85,88,],[43,-53,-67,54,-57,-66,78,43,-65,-66,-68,-51,-52,-54,-55,-56,-69,]),'PARENT_DER':([27,30,33,48,49,50,51,81,82,83,84,85,88,105,106,109,110,114,115,116,117,118,119,138,139,164,166,167,168,178,179,190,191,218,219,227,230,234,260,261,265,266,285,],[-53,-67,-57,88,-65,-66,-68,-51,-52,-54,-55,-56,-69,146,147,-88,-89,-79,-80,-81,-82,-83,-84,-98,-98,192,194,196,197,206,207,215,-96,236,237,249,252,-97,275,276,279,280,289,]),'MULTIPLICADOR':([27,30,31,33,34,41,49,50,51,81,82,83,84,85,88,],[44,-67,55,-57,-66,79,-65,-66,-68,44,44,-54,-55,-56,-69,]),'DIVISOR':([27,30,31,33,34,41,49,50,51,81,82,83,84,85,88,],[45,-67,56,-57,-66,80,-65,-66,-68,45,45,-54,-55,-56,-69,]),'MOD_DIVISION':([27,30,31,33,34,41,49,50,51,81,82,83,84,85,88,],[46,-67,57,-57,-66,-68,-65,-66,-68,46,46,-54,-55,-56,-69,]),'PUNTO':([28,36,],[47,72,]),'IGUALDAD':([30,31,34,49,50,51,64,88,212,],[-67,58,58,-65,-66,-68,58,-69,58,]),'MAYOR':([30,31,34,49,50,51,64,88,212,],[-67,59,59,-65,-66,-68,59,-69,59,]),'MENOR':([30,31,34,49,50,51,64,88,212,],[-67,60,60,-65,-66,-68,60,-69,60,]),'MAYOR_IGU':([30,31,34,49,50,51,64,88,212,],[-67,61,61,-65,-66,-68,61,-69,61,]),'MENOR_IGU':([30,31,34,49,50,51,64,88,212,],[-67,62,62,-65,-66,-68,62,-69,62,]),'DESIGUALDAD':([30,31,34,49,50,51,64,88,212,],[-67,63,63,-65,-66,-68,63,-69,63,]),'LLAVE_IZQ':([30,49,50,51,69,70,74,88,114,115,116,117,118,119,140,199,217,224,226,282,290,],[-67,-65,-66,-68,-39,-41,127,-69,-79,-80,-81,-82,-83,-84,169,221,235,246,248,287,-40,]),'FIN_SENTENCIA':([30,49,50,51,88,158,253,],[-67,-65,-66,-68,-69,184,267,]),'DOS_PUNTOS':([30,49,50,51,88,188,189,241,242,243,],[-67,-65,-66,-68,-69,213,214,-89,-88,259,]),'COMA':([30,49,50,51,71,88,109,110,114,115,116,117,118,119,128,165,167,180,181,182,183,191,222,225,228,229,239,240,241,242,260,273,],[-67,-65,-66,-68,112,-69,-88,-89,-79,-80,-81,-82,-83,-84,162,193,195,208,209,210,211,216,244,247,250,251,257,258,-65,-67,274,-87,]),'ASIGNACION':([34,73,111,114,115,116,117,118,119,148,176,281,],[65,126,149,-79,-80,-81,-82,-83,-84,174,204,286,]),'CORCHETE_IZQ':([34,65,104,113,144,172,],[68,102,145,151,171,201,]),'INCREMENTO':([34,281,],[69,69,]),'DECREMENTO':([34,281,],[70,70,]),'PRINTF':([47,],[86,]),'PRINTLN':([47,],[87,]),'MAKE':([65,],[103,]),'MAP':([65,71,144,],[104,113,172,]),'INT':([71,145,150,151,163,170,192,200,201,202,205,245,],[114,114,114,114,114,114,114,114,114,114,114,114,]),'STRING':([71,145,150,151,163,170,192,200,201,202,205,245,],[115,115,115,115,115,115,115,115,115,115,115,115,]),'INT64':([71,145,150,151,163,170,192,200,201,202,205,245,],[116,116,116,116,116,116,116,116,116,116,116,116,]),'FLOAT32':([71,145,150,151,163,170,192,200,201,202,205,245,],[117,117,117,117,117,117,117,117,117,117,117,117,]),'FLOAT64':([71,145,150,151,163,170,192,200,201,202,205,245,],[118,118,118,118,118,118,118,118,118,118,118,118,]),'INT32':([71,145,150,151,163,170,192,200,201,202,205,245,],[119,119,119,119,119,119,119,119,119,119,119,119,]),'FORMATBOOL':([72,],[120,]),'PARSEBOOL':([72,],[121,]),'FORMATINT':([72,],[122,]),'PARSEINT':([72,],[123,]),'FORMATFLOAT':([72,],[124,]),'PARSEFLOAT':([72,],[125,]),'ARRPUNTOS':([102,],[143,]),'CORCHETE_DER':([108,109,110,114,115,116,117,118,119,141,142,143,171,173,177,223,],[148,-88,-89,-79,-80,-81,-82,-83,-84,170,-44,-45,200,202,205,245,]),'BOOLEAN':([152,],[178,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,169,213,214,235,287,],[1,198,232,233,254,291,]),'expression':([0,29,169,213,214,235,287,],[2,48,2,2,2,2,2,]),'impresion':([0,169,213,214,235,287,],[3,3,3,3,3,3,]),'sentencia':([0,169,213,214,235,287,],[4,4,4,4,4,4,]),'asignacion':([0,169,213,214,235,287,],[5,5,5,5,5,5,]),'longvariable':([0,169,213,214,235,287,],[6,6,6,6,6,6,]),'boolcadena':([0,169,213,214,235,287,],[7,7,7,7,7,7,]),'companum':([0,169,213,214,235,287,],[8,8,8,8,8,8,]),'compaid':([0,169,213,214,235,287,],[9,9,9,9,9,9,]),'sentenciafor':([0,169,213,214,235,287,],[10,10,10,10,10,10,]),'arreglo':([0,169,213,214,235,287,],[11,11,11,11,11,11,]),'slice':([0,169,213,214,235,287,],[12,12,12,12,12,12,]),'capslice':([0,169,213,214,235,287,],[13,13,13,13,13,13,]),'switch':([0,169,213,214,235,287,],[14,14,14,14,14,14,]),'map':([0,169,213,214,235,287,],[15,15,15,15,15,15,]),'asignar_valor_map':([0,169,213,214,235,287,],[16,16,16,16,16,16,]),'eliminar_valor_map':([0,169,213,214,235,287,],[17,17,17,17,17,17,]),'obtener_valor_map':([0,169,213,214,235,287,],[18,18,18,18,18,18,]),'funcion':([0,169,213,214,235,287,],[19,19,19,19,19,19,]),'cadenabool':([0,169,213,214,235,287,],[20,20,20,20,20,20,]),'enterocadena':([0,169,213,214,235,287,],[21,21,21,21,21,21,]),'cadenaentero':([0,169,213,214,235,287,],[22,22,22,22,22,22,]),'flotantecadena':([0,169,213,214,235,287,],[23,23,23,23,23,23,]),'cadenaflotante':([0,169,213,214,235,287,],[24,24,24,24,24,24,]),'seman_operacion':([0,169,213,214,235,287,],[25,25,25,25,25,25,]),'incremento':([0,169,213,214,235,267,287,],[26,26,26,26,26,282,26,]),'term':([0,29,42,43,169,213,214,235,287,],[27,27,81,82,27,27,27,27,27,]),'factor':([0,29,32,42,43,44,45,46,65,99,126,149,161,169,204,213,214,221,231,235,246,247,248,257,258,287,],[33,33,64,33,33,83,84,85,101,140,158,175,189,33,225,33,33,239,253,33,239,263,239,239,239,33,]),'comparacion':([31,34,64,212,],[52,67,99,231,]),'valor':([68,162,174,221,246,248,257,258,259,],[108,190,203,243,243,243,243,243,273,]),'tipo_dato':([71,145,150,151,163,170,192,200,201,202,205,245,],[111,173,176,177,191,199,217,222,223,224,226,261,]),'cantidad':([102,],[141,]),'cases':([127,160,],[159,187,]),'case':([127,160,],[160,160,]),'argumentos':([129,216,],[164,234,]),'empty':([138,139,],[166,168,]),'default':([160,],[186,]),'valores':([221,246,248,257,258,],[238,262,264,271,272,]),'clave_valor':([221,246,248,257,258,],[240,240,240,240,240,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> expression','programa',1,'p_programa','analizadorSintactico.py',14),
  ('programa -> impresion','programa',1,'p_programa','analizadorSintactico.py',15),
  ('programa -> sentencia','programa',1,'p_programa','analizadorSintactico.py',16),
  ('programa -> asignacion','programa',1,'p_programa','analizadorSintactico.py',17),
  ('programa -> longvariable','programa',1,'p_programa','analizadorSintactico.py',18),
  ('programa -> boolcadena','programa',1,'p_programa','analizadorSintactico.py',19),
  ('programa -> companum','programa',1,'p_programa','analizadorSintactico.py',20),
  ('programa -> compaid','programa',1,'p_programa','analizadorSintactico.py',21),
  ('programa -> sentenciafor','programa',1,'p_programa','analizadorSintactico.py',22),
  ('programa -> arreglo','programa',1,'p_programa','analizadorSintactico.py',23),
  ('programa -> slice','programa',1,'p_programa','analizadorSintactico.py',24),
  ('programa -> capslice','programa',1,'p_programa','analizadorSintactico.py',25),
  ('programa -> switch','programa',1,'p_programa','analizadorSintactico.py',26),
  ('programa -> map','programa',1,'p_programa','analizadorSintactico.py',27),
  ('programa -> asignar_valor_map','programa',1,'p_programa','analizadorSintactico.py',28),
  ('programa -> eliminar_valor_map','programa',1,'p_programa','analizadorSintactico.py',29),
  ('programa -> obtener_valor_map','programa',1,'p_programa','analizadorSintactico.py',30),
  ('programa -> funcion','programa',1,'p_programa','analizadorSintactico.py',31),
  ('programa -> cadenabool','programa',1,'p_programa','analizadorSintactico.py',32),
  ('programa -> enterocadena','programa',1,'p_programa','analizadorSintactico.py',33),
  ('programa -> cadenaentero','programa',1,'p_programa','analizadorSintactico.py',34),
  ('programa -> flotantecadena','programa',1,'p_programa','analizadorSintactico.py',35),
  ('programa -> cadenaflotante','programa',1,'p_programa','analizadorSintactico.py',36),
  ('programa -> seman_operacion','programa',1,'p_programa','analizadorSintactico.py',37),
  ('programa -> incremento','programa',1,'p_programa','analizadorSintactico.py',38),
  ('impresion -> FMT PUNTO PRINTF PARENT_IZQ CADENA COMA NUMERO PARENT_DER','impresion',8,'p_impresion','analizadorSintactico.py',42),
  ('impresion -> FMT PUNTO PRINTF PARENT_IZQ empty PARENT_DER','impresion',6,'p_impresion','analizadorSintactico.py',43),
  ('impresion -> FMT PUNTO PRINTLN PARENT_IZQ CADENA COMA NUMERO PARENT_DER','impresion',8,'p_impresion','analizadorSintactico.py',44),
  ('impresion -> FMT PUNTO PRINTLN PARENT_IZQ empty PARENT_DER','impresion',6,'p_impresion','analizadorSintactico.py',45),
  ('impresion -> FMT PUNTO PRINTLN PARENT_IZQ CADENA PARENT_DER','impresion',6,'p_impresion','analizadorSintactico.py',46),
  ('longvariable -> ID PARENT_IZQ CADENA PARENT_DER','longvariable',4,'p_longitud_variables','analizadorSintactico.py',50),
  ('longvariable -> ID PARENT_IZQ ID PARENT_DER','longvariable',4,'p_longitud_variables','analizadorSintactico.py',51),
  ('companum -> NUMERO comparacion NUMERO','companum',3,'p_comparacion_num','analizadorSintactico.py',54),
  ('compaid -> ID comparacion ID','compaid',3,'p_comparacion_id','analizadorSintactico.py',58),
  ('asignacion -> ID ASIGNACION factor','asignacion',3,'p_asignacion_var','analizadorSintactico.py',62),
  ('asignacion -> VAR ID tipo_dato ASIGNACION factor','asignacion',5,'p_asignacion_var','analizadorSintactico.py',63),
  ('asignacion -> VAR ID COMA ID tipo_dato ASIGNACION factor COMA factor','asignacion',9,'p_asignacion_var','analizadorSintactico.py',64),
  ('sentenciafor -> FOR ID ASIGNACION factor FIN_SENTENCIA ID comparacion factor FIN_SENTENCIA incremento LLAVE_IZQ programa LLAVE_DER','sentenciafor',13,'p_sentencia_for','analizadorSintactico.py',68),
  ('incremento -> ID INCREMENTO','incremento',2,'p_incremento','analizadorSintactico.py',72),
  ('incremento -> ID ASIGNACION ID','incremento',3,'p_incremento','analizadorSintactico.py',73),
  ('incremento -> ID DECREMENTO','incremento',2,'p_incremento','analizadorSintactico.py',74),
  ('arreglo -> ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato','arreglo',6,'p_definir_arreglo','analizadorSintactico.py',78),
  ('arreglo -> ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER','arreglo',9,'p_definir_arreglo','analizadorSintactico.py',79),
  ('cantidad -> NUMERO','cantidad',1,'p_cantidad_arreglo','analizadorSintactico.py',83),
  ('cantidad -> ARRPUNTOS','cantidad',1,'p_cantidad_arreglo','analizadorSintactico.py',84),
  ('valores -> factor','valores',1,'p_valores_arreglo','analizadorSintactico.py',88),
  ('valores -> factor COMA valores','valores',3,'p_valores_arreglo','analizadorSintactico.py',89),
  ('slice -> ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO PARENT_DER','slice',10,'p_definir_slice','analizadorSintactico.py',93),
  ('slice -> ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO COMA NUMERO PARENT_DER','slice',12,'p_definir_slice','analizadorSintactico.py',94),
  ('capslice -> ID PARENT_IZQ ID PARENT_DER','capslice',4,'p_cap_slice','analizadorSintactico.py',98),
  ('expression -> expression MAS term','expression',3,'p_expression_mas','analizadorSintactico.py',102),
  ('expression -> expression MENOS term','expression',3,'p_expression_menos','analizadorSintactico.py',106),
  ('expression -> term','expression',1,'p_expression_term','analizadorSintactico.py',110),
  ('term -> term MULTIPLICADOR factor','term',3,'p_term_multiplicador','analizadorSintactico.py',114),
  ('term -> term DIVISOR factor','term',3,'p_term_divisor','analizadorSintactico.py',118),
  ('term -> term MOD_DIVISION factor','term',3,'p_term_mod','analizadorSintactico.py',122),
  ('term -> factor','term',1,'p_term_factor','analizadorSintactico.py',126),
  ('sentencia -> IF factor comparacion factor LLAVE_IZQ programa LLAVE_DER','sentencia',7,'p_sentencia_if','analizadorSintactico.py',130),
  ('comparacion -> IGUALDAD','comparacion',1,'p_comparacion_igu','analizadorSintactico.py',134),
  ('comparacion -> MAYOR','comparacion',1,'p_comparacion_mayor','analizadorSintactico.py',138),
  ('comparacion -> MENOR','comparacion',1,'p_comparacion_menor','analizadorSintactico.py',142),
  ('comparacion -> MAYOR_IGU','comparacion',1,'p_comparacion_mayor_igu','analizadorSintactico.py',146),
  ('comparacion -> MENOR_IGU','comparacion',1,'p_comparacion_menor_igu','analizadorSintactico.py',150),
  ('comparacion -> DESIGUALDAD','comparacion',1,'p_comparacion_desigu','analizadorSintactico.py',154),
  ('factor -> NUMERO','factor',1,'p_factor_num','analizadorSintactico.py',158),
  ('factor -> ID','factor',1,'p_factor_id','analizadorSintactico.py',162),
  ('factor -> CADENA','factor',1,'p_factor_cadena','analizadorSintactico.py',166),
  ('factor -> FLOAT','factor',1,'p_factor_float','analizadorSintactico.py',169),
  ('factor -> PARENT_IZQ expression PARENT_DER','factor',3,'p_factor_expr','analizadorSintactico.py',172),
  ('switch -> SWITCH ID LLAVE_IZQ cases LLAVE_DER','switch',5,'p_definir_switch','analizadorSintactico.py',175),
  ('cases -> case','cases',1,'p_cases','analizadorSintactico.py',178),
  ('cases -> case default','cases',2,'p_cases','analizadorSintactico.py',179),
  ('cases -> case cases','cases',2,'p_cases','analizadorSintactico.py',180),
  ('case -> CASE factor DOS_PUNTOS programa','case',4,'p_case','analizadorSintactico.py',183),
  ('default -> DEFAULT DOS_PUNTOS programa','default',3,'p_default','analizadorSintactico.py',186),
  ('map -> VAR ID MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER','map',10,'p_definir_map','analizadorSintactico.py',189),
  ('map -> ID ASIGNACION MAKE PARENT_IZQ MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato PARENT_DER','map',10,'p_definir_map','analizadorSintactico.py',190),
  ('map -> ID ASIGNACION MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER','map',10,'p_definir_map','analizadorSintactico.py',191),
  ('tipo_dato -> INT','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',194),
  ('tipo_dato -> STRING','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',195),
  ('tipo_dato -> INT64','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',196),
  ('tipo_dato -> FLOAT32','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',197),
  ('tipo_dato -> FLOAT64','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',198),
  ('tipo_dato -> INT32','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',199),
  ('valores -> clave_valor','valores',1,'p_valores','analizadorSintactico.py',202),
  ('valores -> clave_valor COMA valores','valores',3,'p_valores','analizadorSintactico.py',203),
  ('clave_valor -> valor DOS_PUNTOS valor','clave_valor',3,'p_clave_valor','analizadorSintactico.py',206),
  ('valor -> CADENA','valor',1,'p_valor','analizadorSintactico.py',209),
  ('valor -> NUMERO','valor',1,'p_valor','analizadorSintactico.py',210),
  ('asignar_valor_map -> ID CORCHETE_IZQ valor CORCHETE_DER ASIGNACION valor','asignar_valor_map',6,'p_asignar_valor_map','analizadorSintactico.py',213),
  ('eliminar_valor_map -> DELETE PARENT_IZQ ID COMA valor PARENT_DER','eliminar_valor_map',6,'p_eliminar_valor_map','analizadorSintactico.py',216),
  ('obtener_valor_map -> ID CORCHETE_IZQ valor CORCHETE_DER','obtener_valor_map',4,'p_obtener_valor_map','analizadorSintactico.py',219),
  ('funcion -> FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa LLAVE_DER','funcion',9,'p_funcion','analizadorSintactico.py',222),
  ('funcion -> FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa RETURN ID LLAVE_DER','funcion',11,'p_funcion','analizadorSintactico.py',223),
  ('funcion -> FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ RETURN ID LLAVE_DER','funcion',10,'p_funcion','analizadorSintactico.py',224),
  ('argumentos -> ID tipo_dato','argumentos',2,'p_argumentos','analizadorSintactico.py',227),
  ('argumentos -> ID tipo_dato COMA argumentos','argumentos',4,'p_argumentos','analizadorSintactico.py',228),
  ('empty -> <empty>','empty',0,'p_empty','analizadorSintactico.py',231),
  ('seman_operacion -> NUMERO MAS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',246),
  ('seman_operacion -> NUMERO MENOS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',247),
  ('seman_operacion -> NUMERO MULTIPLICADOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',248),
  ('seman_operacion -> NUMERO DIVISOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',249),
  ('seman_operacion -> NUMERO MOD_DIVISION NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',250),
  ('seman_operacion -> FLOAT MAS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',251),
  ('seman_operacion -> FLOAT MENOS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',252),
  ('seman_operacion -> FLOAT MULTIPLICADOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',253),
  ('seman_operacion -> FLOAT DIVISOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',254),
  ('seman_operacion -> NUMERO MAS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',255),
  ('seman_operacion -> NUMERO MENOS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',256),
  ('seman_operacion -> NUMERO MULTIPLICADOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',257),
  ('seman_operacion -> NUMERO DIVISOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',258),
  ('seman_operacion -> FLOAT MAS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',259),
  ('seman_operacion -> FLOAT MENOS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',260),
  ('seman_operacion -> FLOAT MULTIPLICADOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',261),
  ('seman_operacion -> FLOAT DIVISOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',262),
  ('boolcadena -> STRCONV PUNTO FORMATBOOL PARENT_IZQ BOOLEAN PARENT_DER','boolcadena',6,'p_bool_cadena','analizadorSintactico.py',266),
  ('cadenabool -> STRCONV PUNTO PARSEBOOL PARENT_IZQ CADENA PARENT_DER','cadenabool',6,'p_cadena_bool','analizadorSintactico.py',269),
  ('flotantecadena -> STRCONV PUNTO FORMATFLOAT PARENT_IZQ FLOAT COMA CADENA COMA NUMERO PARENT_DER','flotantecadena',10,'p_flotante_cadena','analizadorSintactico.py',272),
  ('cadenaflotante -> STRCONV PUNTO PARSEFLOAT PARENT_IZQ CADENA COMA NUMERO PARENT_DER','cadenaflotante',8,'p_cadena_flotante','analizadorSintactico.py',275),
  ('enterocadena -> STRCONV PUNTO FORMATINT PARENT_IZQ NUMERO COMA NUMERO PARENT_DER','enterocadena',8,'p_entero_cadena','analizadorSintactico.py',278),
  ('cadenaentero -> STRCONV PUNTO PARSEINT PARENT_IZQ CADENA COMA NUMERO COMA NUMERO PARENT_DER','cadenaentero',10,'p_cadena_entero','analizadorSintactico.py',281),
]
