
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNACIONleftIGUALDADMAYORMENORMENOR_IGUMAYOR_IGUleftMASMENOSleftMULTIPLICADORDIVISORleftPARENT_IZQPARENT_DERAMPERSAND ARRPUNTOS ASIGNACION BOOLEAN BREAK CADENA CASE COMA COMILLA COMMENT_BLOQUE_DER COMMENT_BLOQUE_IZQ COMMENT_LINEA CONST CONTAINS CONTINUE CORCHETE_DER CORCHETE_IZQ DECREMENTO DEFAULT DEFER DELETE DESIGUALDAD DIVISOR DOBLE_COMILLA DOS_PUNTOS ELSE ESPACIADO FALLTHROUGH FALSE FIN_SENTENCIA FLOAT FLOAT32 FLOAT64 FMT FOR FORMATBOOL FORMATFLOAT FORMATINT FUNC GO ID IF IGUAL IGUALDAD IMPORT INCREMENTO INT INT32 INT64 INTERFACE LEN LLAVE_DER LLAVE_IZQ MAKE MAP MAS MAYOR MAYOR_IGU MENOR MENOR_IGU MENOS MOD_DIVISION MULTIPLICADOR NUMERO PACKAGE PARENT_DER PARENT_IZQ PARSEBOOL PARSEFLOAT PARSEINT PIPE PRINTF PRINTLN PUNTO RANGE RETURN SELECT SPLIT STRCONV STRING STRINGS STRUCT SWITCH TRUE TYPE VACIO VARprograma : expression\n                | impresion\n                | sentencia \n                | asignacion\n                | longvariable\n                | boolcadena\n                | companum\n                | compaid\n                | sentenciafor\n                | arreglo\n                | slice\n                | capslice\n                | switch\n                | map\n                | asignar_valor_map\n                | eliminar_valor_map\n                | obtener_valor_map\n                | funcion\n                | cadenabool\n                | enterocadena\n                | cadenaentero\n                | flotantecadena\n                | cadenaflotante\n                | seman_operacionimpresion : FMT PUNTO PRINTF PARENT_IZQ CADENA COMA NUMERO PARENT_DER\n                | FMT PUNTO PRINTF PARENT_IZQ empty PARENT_DER\n                | FMT PUNTO PRINTLN PARENT_IZQ CADENA COMA NUMERO PARENT_DER\n                | FMT PUNTO PRINTLN PARENT_IZQ empty PARENT_DER\n                longvariable : ID PARENT_IZQ CADENA PARENT_DER\n                        | ID PARENT_IZQ ID PARENT_DERcompanum : NUMERO comparacion NUMEROcompaid : ID comparacion IDasignacion : ID ASIGNACION factor\n                    | VAR ID tipo_dato ASIGNACION factor\n                    | VAR ID COMA ID tipo_dato ASIGNACION factor COMA factorsentenciafor : FOR ID ASIGNACION factor FIN_SENTENCIA ID comparacion factor FIN_SENTENCIA incremento LLAVE_IZQ programa LLAVE_DERincremento : ID INCREMENTO\n                    | ID ASIGNACION ID\n                    | ID DECREMENTOarreglo : ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato \n                    | ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DERcantidad : NUMERO \n                    | ARRPUNTOSvalores : factor\n                    | factor COMA valoresslice : ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO PARENT_DER\n                | ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO COMA NUMERO PARENT_DERcapslice : ID PARENT_IZQ ID PARENT_DERexpression : expression MAS termexpression : expression MENOS termexpression : termterm : term MULTIPLICADOR factorterm : term DIVISOR factorterm : term MOD_DIVISION factorterm : factorsentencia : IF factor comparacion factor LLAVE_IZQ programa LLAVE_DERcomparacion : IGUALDADcomparacion : MAYORcomparacion : MENORcomparacion : MAYOR_IGUcomparacion : MENOR_IGUcomparacion : DESIGUALDADfactor : NUMEROfactor : IDfactor : CADENAfactor : PARENT_IZQ expression PARENT_DERswitch : SWITCH ID LLAVE_IZQ cases LLAVE_DERcases : case \n                | case default \n                | case casescase : CASE factor DOS_PUNTOS programadefault : DEFAULT DOS_PUNTOS programamap : VAR ID MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER \n                | ID ASIGNACION MAKE PARENT_IZQ MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato PARENT_DER\n                | ID ASIGNACION MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DERtipo_dato : INT \n                    | STRING \n                    | INT64 \n                    | FLOAT32 \n                    | FLOAT64 \n                    | INT32valores : clave_valor \n                | clave_valor COMA valoresclave_valor : valor DOS_PUNTOS valorvalor : CADENA\n                | NUMEROasignar_valor_map : ID CORCHETE_IZQ valor CORCHETE_DER ASIGNACION valoreliminar_valor_map : DELETE PARENT_IZQ ID COMA valor PARENT_DERobtener_valor_map : ID CORCHETE_IZQ valor CORCHETE_DERfuncion : FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa LLAVE_DER \n                    | FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa RETURN ID LLAVE_DERargumentos : ID tipo_dato \n                    | ID tipo_dato COMA argumentosempty : seman_operacion : NUMERO MAS NUMERO \n                        | NUMERO MENOS NUMERO\n                        | NUMERO MULTIPLICADOR NUMERO\n                        | NUMERO DIVISOR NUMERO\n                        | NUMERO MOD_DIVISION NUMERO\n                        | FLOAT MAS NUMERO\n                        | FLOAT MENOS NUMERO\n                        | FLOAT MULTIPLICADOR NUMERO\n                        | FLOAT DIVISOR NUMERO\n                        | NUMERO MAS FLOAT\n                        | NUMERO MENOS FLOAT\n                        | NUMERO MULTIPLICADOR FLOAT\n                        | NUMERO DIVISOR FLOAT\n                        | FLOAT MAS FLOAT\n                        | FLOAT MENOS FLOAT\n                        | FLOAT MULTIPLICADOR FLOAT\n                        | FLOAT DIVISOR FLOATboolcadena : STRCONV PUNTO FORMATBOOL PARENT_IZQ BOOLEAN PARENT_DERcadenabool : STRCONV PUNTO PARSEBOOL PARENT_IZQ CADENA PARENT_DERflotantecadena : STRCONV PUNTO FORMATFLOAT PARENT_IZQ FLOAT COMA CADENA COMA NUMERO PARENT_DERcadenaflotante : STRCONV PUNTO PARSEFLOAT PARENT_IZQ FLOAT COMA NUMERO PARENT_DERenterocadena : STRCONV PUNTO FORMATINT PARENT_IZQ CADENA COMA NUMERO PARENT_DERcadenaentero : STRCONV PUNTO PARSEINT PARENT_IZQ CADENA COMA NUMERO COMA NUMERO PARENT_DER'
    
_lr_action_items = {'FMT':([0,164,207,208,229,280,],[27,27,27,27,27,27,]),'IF':([0,164,207,208,229,280,],[31,31,31,31,31,31,]),'ID':([0,28,31,34,36,37,39,41,42,43,44,45,56,57,58,59,60,61,63,64,65,71,95,107,121,124,144,156,164,179,198,207,208,210,215,225,229,240,241,242,250,251,260,262,278,280,],[33,49,49,67,69,70,72,49,49,49,49,49,-57,-58,-59,-60,-61,-62,49,100,102,123,49,145,49,158,49,49,33,206,49,33,33,158,49,49,33,49,49,49,49,49,273,275,283,33,]),'VAR':([0,164,207,208,229,280,],[34,34,34,34,34,34,]),'STRCONV':([0,164,207,208,229,280,],[35,35,35,35,35,35,]),'NUMERO':([0,28,31,41,42,43,44,45,50,51,52,53,54,55,56,57,58,59,60,61,63,66,73,74,75,76,95,97,121,144,156,157,164,169,188,190,198,202,203,205,207,208,215,225,229,238,240,241,242,244,245,250,251,252,266,280,],[30,48,48,48,48,48,48,48,85,86,88,90,92,94,-57,-58,-59,-60,-61,-62,48,105,126,128,130,132,48,137,48,48,48,105,30,105,212,213,48,221,222,224,30,30,235,48,30,253,235,48,235,258,259,235,235,105,276,30,]),'FOR':([0,164,207,208,229,280,],[36,36,36,36,36,36,]),'SWITCH':([0,164,207,208,229,280,],[37,37,37,37,37,37,]),'DELETE':([0,164,207,208,229,280,],[38,38,38,38,38,38,]),'FUNC':([0,164,207,208,229,280,],[39,39,39,39,39,39,]),'FLOAT':([0,51,52,53,54,73,74,75,76,151,152,164,207,208,229,280,],[40,87,89,91,93,125,127,129,131,177,178,40,40,40,40,40,]),'CADENA':([0,28,31,41,42,43,44,45,56,57,58,59,60,61,63,64,66,95,121,133,134,144,148,149,150,156,157,164,169,198,204,207,208,215,225,229,240,241,242,250,251,252,280,],[29,29,29,29,29,29,29,29,-57,-58,-59,-60,-61,-62,29,101,104,29,29,160,162,29,174,175,176,29,104,29,104,29,223,29,29,236,29,29,236,29,236,236,236,104,29,]),'PARENT_IZQ':([0,28,31,33,38,41,42,43,44,45,56,57,58,59,60,61,63,72,82,83,95,98,115,116,117,118,119,120,121,144,156,164,198,207,208,215,225,229,240,241,242,250,251,280,],[28,28,28,64,71,28,28,28,28,28,-57,-58,-59,-60,-61,-62,28,124,133,134,28,139,147,148,149,150,151,152,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,32,33,48,49,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,96,102,104,105,109,110,111,112,113,114,125,126,127,128,129,130,131,132,141,142,143,170,180,189,191,193,197,200,201,209,214,230,231,243,246,249,256,261,267,268,269,270,271,272,281,282,285,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-51,-65,-63,-55,-64,-63,-64,-49,-50,-52,-53,-54,-66,-31,-95,-104,-96,-105,-97,-106,-98,-107,-99,-33,-32,-85,-86,-76,-77,-78,-79,-80,-81,-108,-100,-109,-101,-110,-102,-111,-103,-30,-29,-89,-34,-67,-26,-28,-40,-87,-112,-113,-88,-56,-25,-27,-116,-115,-41,-35,-90,-46,-74,-75,-73,-117,-114,-91,-47,-36,]),'LLAVE_DER':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,32,33,48,49,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,96,102,104,105,109,110,111,112,113,114,125,126,127,128,129,130,131,132,141,142,143,154,155,170,180,181,182,189,191,192,193,197,200,201,209,214,226,227,230,231,232,233,234,235,236,243,246,248,249,255,256,257,261,263,264,265,267,268,269,270,271,272,275,281,282,284,285,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-51,-65,-63,-55,-64,-63,-64,-49,-50,-52,-53,-54,-66,-31,-95,-104,-96,-105,-97,-106,-98,-107,-99,-33,-32,-85,-86,-76,-77,-78,-79,-80,-81,-108,-100,-109,-101,-110,-102,-111,-103,-30,-29,-89,180,-68,-34,-67,-69,-70,-26,-28,214,-40,-87,-112,-113,-88,-56,-72,-71,-25,-27,249,-44,-82,-63,-65,-116,-115,261,-41,269,-35,270,-90,-45,-83,-84,-46,-74,-75,-73,-117,-114,281,-91,-47,285,-36,]),'DEFAULT':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,32,33,48,49,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,96,102,104,105,109,110,111,112,113,114,125,126,127,128,129,130,131,132,141,142,143,155,170,180,189,191,193,197,200,201,209,214,227,230,231,243,246,249,256,261,267,268,269,270,271,272,281,282,285,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-51,-65,-63,-55,-64,-63,-64,-49,-50,-52,-53,-54,-66,-31,-95,-104,-96,-105,-97,-106,-98,-107,-99,-33,-32,-85,-86,-76,-77,-78,-79,-80,-81,-108,-100,-109,-101,-110,-102,-111,-103,-30,-29,-89,183,-34,-67,-26,-28,-40,-87,-112,-113,-88,-56,-71,-25,-27,-116,-115,-41,-35,-90,-46,-74,-75,-73,-117,-114,-91,-47,-36,]),'CASE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,32,33,48,49,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,96,102,104,105,109,110,111,112,113,114,122,125,126,127,128,129,130,131,132,141,142,143,155,170,180,189,191,193,197,200,201,209,214,227,230,231,243,246,249,256,261,267,268,269,270,271,272,281,282,285,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-51,-65,-63,-55,-64,-63,-64,-49,-50,-52,-53,-54,-66,-31,-95,-104,-96,-105,-97,-106,-98,-107,-99,-33,-32,-85,-86,-76,-77,-78,-79,-80,-81,156,-108,-100,-109,-101,-110,-102,-111,-103,-30,-29,-89,156,-34,-67,-26,-28,-40,-87,-112,-113,-88,-56,-71,-25,-27,-116,-115,-41,-35,-90,-46,-74,-75,-73,-117,-114,-91,-47,-36,]),'RETURN':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,32,33,48,49,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,96,102,104,105,109,110,111,112,113,114,125,126,127,128,129,130,131,132,141,142,143,170,180,189,191,193,197,200,201,209,214,230,231,243,246,248,249,256,261,267,268,269,270,271,272,281,282,285,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-51,-65,-63,-55,-64,-63,-64,-49,-50,-52,-53,-54,-66,-31,-95,-104,-96,-105,-97,-106,-98,-107,-99,-33,-32,-85,-86,-76,-77,-78,-79,-80,-81,-108,-100,-109,-101,-110,-102,-111,-103,-30,-29,-89,-34,-67,-26,-28,-40,-87,-112,-113,-88,-56,-25,-27,-116,-115,262,-41,-35,-90,-46,-74,-75,-73,-117,-114,-91,-47,-36,]),'MAS':([2,26,29,30,32,33,40,47,48,49,77,78,79,80,81,84,],[41,-51,-65,51,-55,-64,73,41,-63,-64,-49,-50,-52,-53,-54,-66,]),'MENOS':([2,26,29,30,32,33,40,47,48,49,77,78,79,80,81,84,],[42,-51,-65,52,-55,-64,74,42,-63,-64,-49,-50,-52,-53,-54,-66,]),'PARENT_DER':([26,29,32,47,48,49,77,78,79,80,81,84,100,101,104,105,109,110,111,112,113,114,133,134,159,161,163,173,174,185,186,212,213,221,224,228,253,254,258,259,276,],[-51,-65,-55,84,-63,-64,-49,-50,-52,-53,-54,-66,141,142,-85,-86,-76,-77,-78,-79,-80,-81,-94,-94,187,189,191,200,201,209,-92,230,231,243,246,-93,267,268,271,272,282,]),'MULTIPLICADOR':([26,29,30,32,33,40,48,49,77,78,79,80,81,84,],[43,-65,53,-55,-64,75,-63,-64,43,43,-52,-53,-54,-66,]),'DIVISOR':([26,29,30,32,33,40,48,49,77,78,79,80,81,84,],[44,-65,54,-55,-64,76,-63,-64,44,44,-52,-53,-54,-66,]),'MOD_DIVISION':([26,29,30,32,33,48,49,77,78,79,80,81,84,],[45,-65,55,-55,-64,-63,-64,45,45,-52,-53,-54,-66,]),'PUNTO':([27,35,],[46,68,]),'IGUALDAD':([29,30,33,48,49,62,84,206,],[-65,56,56,-63,-64,56,-66,56,]),'MAYOR':([29,30,33,48,49,62,84,206,],[-65,57,57,-63,-64,57,-66,57,]),'MENOR':([29,30,33,48,49,62,84,206,],[-65,58,58,-63,-64,58,-66,58,]),'MAYOR_IGU':([29,30,33,48,49,62,84,206,],[-65,59,59,-63,-64,59,-66,59,]),'MENOR_IGU':([29,30,33,48,49,62,84,206,],[-65,60,60,-63,-64,60,-66,60,]),'DESIGUALDAD':([29,30,33,48,49,62,84,206,],[-65,61,61,-63,-64,61,-66,61,]),'LLAVE_IZQ':([29,48,49,70,84,109,110,111,112,113,114,135,193,211,218,220,274,277,279,283,],[-65,-63,-64,122,-66,-76,-77,-78,-79,-80,-81,164,215,229,240,242,280,-37,-39,-38,]),'FIN_SENTENCIA':([29,48,49,84,153,247,],[-65,-63,-64,-66,179,260,]),'DOS_PUNTOS':([29,48,49,84,183,184,235,236,237,],[-65,-63,-64,-66,207,208,-86,-85,252,]),'COMA':([29,48,49,67,84,104,105,109,110,111,112,113,114,123,160,162,175,176,177,178,186,216,219,222,223,233,234,235,236,253,265,],[-65,-63,-64,107,-66,-85,-86,-76,-77,-78,-79,-80,-81,157,188,190,202,203,204,205,210,238,241,244,245,250,251,-63,-65,266,-84,]),'ASIGNACION':([33,69,106,109,110,111,112,113,114,143,171,273,],[63,121,144,-76,-77,-78,-79,-80,-81,169,198,278,]),'CORCHETE_IZQ':([33,63,99,108,139,167,],[66,97,140,146,166,195,]),'PRINTF':([46,],[82,]),'PRINTLN':([46,],[83,]),'MAKE':([63,],[98,]),'MAP':([63,67,139,],[99,108,167,]),'INT':([67,140,145,146,158,165,187,194,195,196,199,239,],[109,109,109,109,109,109,109,109,109,109,109,109,]),'STRING':([67,140,145,146,158,165,187,194,195,196,199,239,],[110,110,110,110,110,110,110,110,110,110,110,110,]),'INT64':([67,140,145,146,158,165,187,194,195,196,199,239,],[111,111,111,111,111,111,111,111,111,111,111,111,]),'FLOAT32':([67,140,145,146,158,165,187,194,195,196,199,239,],[112,112,112,112,112,112,112,112,112,112,112,112,]),'FLOAT64':([67,140,145,146,158,165,187,194,195,196,199,239,],[113,113,113,113,113,113,113,113,113,113,113,113,]),'INT32':([67,140,145,146,158,165,187,194,195,196,199,239,],[114,114,114,114,114,114,114,114,114,114,114,114,]),'FORMATBOOL':([68,],[115,]),'PARSEBOOL':([68,],[116,]),'FORMATINT':([68,],[117,]),'PARSEINT':([68,],[118,]),'FORMATFLOAT':([68,],[119,]),'PARSEFLOAT':([68,],[120,]),'ARRPUNTOS':([97,],[138,]),'CORCHETE_DER':([103,104,105,109,110,111,112,113,114,136,137,138,166,168,172,217,],[143,-85,-86,-76,-77,-78,-79,-80,-81,165,-42,-43,194,196,199,239,]),'BOOLEAN':([147,],[173,]),'INCREMENTO':([273,],[277,]),'DECREMENTO':([273,],[279,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,164,207,208,229,280,],[1,192,226,227,248,284,]),'expression':([0,28,164,207,208,229,280,],[2,47,2,2,2,2,2,]),'impresion':([0,164,207,208,229,280,],[3,3,3,3,3,3,]),'sentencia':([0,164,207,208,229,280,],[4,4,4,4,4,4,]),'asignacion':([0,164,207,208,229,280,],[5,5,5,5,5,5,]),'longvariable':([0,164,207,208,229,280,],[6,6,6,6,6,6,]),'boolcadena':([0,164,207,208,229,280,],[7,7,7,7,7,7,]),'companum':([0,164,207,208,229,280,],[8,8,8,8,8,8,]),'compaid':([0,164,207,208,229,280,],[9,9,9,9,9,9,]),'sentenciafor':([0,164,207,208,229,280,],[10,10,10,10,10,10,]),'arreglo':([0,164,207,208,229,280,],[11,11,11,11,11,11,]),'slice':([0,164,207,208,229,280,],[12,12,12,12,12,12,]),'capslice':([0,164,207,208,229,280,],[13,13,13,13,13,13,]),'switch':([0,164,207,208,229,280,],[14,14,14,14,14,14,]),'map':([0,164,207,208,229,280,],[15,15,15,15,15,15,]),'asignar_valor_map':([0,164,207,208,229,280,],[16,16,16,16,16,16,]),'eliminar_valor_map':([0,164,207,208,229,280,],[17,17,17,17,17,17,]),'obtener_valor_map':([0,164,207,208,229,280,],[18,18,18,18,18,18,]),'funcion':([0,164,207,208,229,280,],[19,19,19,19,19,19,]),'cadenabool':([0,164,207,208,229,280,],[20,20,20,20,20,20,]),'enterocadena':([0,164,207,208,229,280,],[21,21,21,21,21,21,]),'cadenaentero':([0,164,207,208,229,280,],[22,22,22,22,22,22,]),'flotantecadena':([0,164,207,208,229,280,],[23,23,23,23,23,23,]),'cadenaflotante':([0,164,207,208,229,280,],[24,24,24,24,24,24,]),'seman_operacion':([0,164,207,208,229,280,],[25,25,25,25,25,25,]),'term':([0,28,41,42,164,207,208,229,280,],[26,26,77,78,26,26,26,26,26,]),'factor':([0,28,31,41,42,43,44,45,63,95,121,144,156,164,198,207,208,215,225,229,240,241,242,250,251,280,],[32,32,62,32,32,79,80,81,96,135,153,170,184,32,219,32,32,233,247,32,233,256,233,233,233,32,]),'comparacion':([30,33,62,206,],[50,65,95,225,]),'valor':([66,157,169,215,240,242,250,251,252,],[103,185,197,237,237,237,237,237,265,]),'tipo_dato':([67,140,145,146,158,165,187,194,195,196,199,239,],[106,168,171,172,186,193,211,216,217,218,220,254,]),'cantidad':([97,],[136,]),'cases':([122,155,],[154,182,]),'case':([122,155,],[155,155,]),'argumentos':([124,210,],[159,228,]),'empty':([133,134,],[161,163,]),'default':([155,],[181,]),'valores':([215,240,242,250,251,],[232,255,257,263,264,]),'clave_valor':([215,240,242,250,251,],[234,234,234,234,234,]),'incremento':([260,],[274,]),}

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
  ('impresion -> FMT PUNTO PRINTF PARENT_IZQ CADENA COMA NUMERO PARENT_DER','impresion',8,'p_impresion','analizadorSintactico.py',41),
  ('impresion -> FMT PUNTO PRINTF PARENT_IZQ empty PARENT_DER','impresion',6,'p_impresion','analizadorSintactico.py',42),
  ('impresion -> FMT PUNTO PRINTLN PARENT_IZQ CADENA COMA NUMERO PARENT_DER','impresion',8,'p_impresion','analizadorSintactico.py',43),
  ('impresion -> FMT PUNTO PRINTLN PARENT_IZQ empty PARENT_DER','impresion',6,'p_impresion','analizadorSintactico.py',44),
  ('longvariable -> ID PARENT_IZQ CADENA PARENT_DER','longvariable',4,'p_longitud_variables','analizadorSintactico.py',48),
  ('longvariable -> ID PARENT_IZQ ID PARENT_DER','longvariable',4,'p_longitud_variables','analizadorSintactico.py',49),
  ('companum -> NUMERO comparacion NUMERO','companum',3,'p_comparacion_num','analizadorSintactico.py',52),
  ('compaid -> ID comparacion ID','compaid',3,'p_comparacion_id','analizadorSintactico.py',56),
  ('asignacion -> ID ASIGNACION factor','asignacion',3,'p_asignacion_var','analizadorSintactico.py',60),
  ('asignacion -> VAR ID tipo_dato ASIGNACION factor','asignacion',5,'p_asignacion_var','analizadorSintactico.py',61),
  ('asignacion -> VAR ID COMA ID tipo_dato ASIGNACION factor COMA factor','asignacion',9,'p_asignacion_var','analizadorSintactico.py',62),
  ('sentenciafor -> FOR ID ASIGNACION factor FIN_SENTENCIA ID comparacion factor FIN_SENTENCIA incremento LLAVE_IZQ programa LLAVE_DER','sentenciafor',13,'p_sentencia_for','analizadorSintactico.py',66),
  ('incremento -> ID INCREMENTO','incremento',2,'p_incremento','analizadorSintactico.py',70),
  ('incremento -> ID ASIGNACION ID','incremento',3,'p_incremento','analizadorSintactico.py',71),
  ('incremento -> ID DECREMENTO','incremento',2,'p_incremento','analizadorSintactico.py',72),
  ('arreglo -> ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato','arreglo',6,'p_definir_arreglo','analizadorSintactico.py',76),
  ('arreglo -> ID ASIGNACION CORCHETE_IZQ cantidad CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER','arreglo',9,'p_definir_arreglo','analizadorSintactico.py',77),
  ('cantidad -> NUMERO','cantidad',1,'p_cantidad_arreglo','analizadorSintactico.py',81),
  ('cantidad -> ARRPUNTOS','cantidad',1,'p_cantidad_arreglo','analizadorSintactico.py',82),
  ('valores -> factor','valores',1,'p_valores_arreglo','analizadorSintactico.py',86),
  ('valores -> factor COMA valores','valores',3,'p_valores_arreglo','analizadorSintactico.py',87),
  ('slice -> ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO PARENT_DER','slice',10,'p_definir_slice','analizadorSintactico.py',91),
  ('slice -> ID ASIGNACION MAKE PARENT_IZQ CORCHETE_IZQ CORCHETE_DER tipo_dato COMA NUMERO COMA NUMERO PARENT_DER','slice',12,'p_definir_slice','analizadorSintactico.py',92),
  ('capslice -> ID PARENT_IZQ ID PARENT_DER','capslice',4,'p_cap_slice','analizadorSintactico.py',96),
  ('expression -> expression MAS term','expression',3,'p_expression_mas','analizadorSintactico.py',100),
  ('expression -> expression MENOS term','expression',3,'p_expression_menos','analizadorSintactico.py',104),
  ('expression -> term','expression',1,'p_expression_term','analizadorSintactico.py',108),
  ('term -> term MULTIPLICADOR factor','term',3,'p_term_multiplicador','analizadorSintactico.py',112),
  ('term -> term DIVISOR factor','term',3,'p_term_divisor','analizadorSintactico.py',116),
  ('term -> term MOD_DIVISION factor','term',3,'p_term_mod','analizadorSintactico.py',120),
  ('term -> factor','term',1,'p_term_factor','analizadorSintactico.py',124),
  ('sentencia -> IF factor comparacion factor LLAVE_IZQ programa LLAVE_DER','sentencia',7,'p_sentencia_if','analizadorSintactico.py',128),
  ('comparacion -> IGUALDAD','comparacion',1,'p_comparacion_igu','analizadorSintactico.py',132),
  ('comparacion -> MAYOR','comparacion',1,'p_comparacion_mayor','analizadorSintactico.py',136),
  ('comparacion -> MENOR','comparacion',1,'p_comparacion_menor','analizadorSintactico.py',140),
  ('comparacion -> MAYOR_IGU','comparacion',1,'p_comparacion_mayor_igu','analizadorSintactico.py',144),
  ('comparacion -> MENOR_IGU','comparacion',1,'p_comparacion_menor_igu','analizadorSintactico.py',148),
  ('comparacion -> DESIGUALDAD','comparacion',1,'p_comparacion_desigu','analizadorSintactico.py',152),
  ('factor -> NUMERO','factor',1,'p_factor_num','analizadorSintactico.py',156),
  ('factor -> ID','factor',1,'p_factor_id','analizadorSintactico.py',160),
  ('factor -> CADENA','factor',1,'p_factor_cadena','analizadorSintactico.py',164),
  ('factor -> PARENT_IZQ expression PARENT_DER','factor',3,'p_factor_expr','analizadorSintactico.py',168),
  ('switch -> SWITCH ID LLAVE_IZQ cases LLAVE_DER','switch',5,'p_definir_switch','analizadorSintactico.py',171),
  ('cases -> case','cases',1,'p_cases','analizadorSintactico.py',174),
  ('cases -> case default','cases',2,'p_cases','analizadorSintactico.py',175),
  ('cases -> case cases','cases',2,'p_cases','analizadorSintactico.py',176),
  ('case -> CASE factor DOS_PUNTOS programa','case',4,'p_case','analizadorSintactico.py',179),
  ('default -> DEFAULT DOS_PUNTOS programa','default',3,'p_default','analizadorSintactico.py',182),
  ('map -> VAR ID MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER','map',10,'p_definir_map','analizadorSintactico.py',185),
  ('map -> ID ASIGNACION MAKE PARENT_IZQ MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato PARENT_DER','map',10,'p_definir_map','analizadorSintactico.py',186),
  ('map -> ID ASIGNACION MAP CORCHETE_IZQ tipo_dato CORCHETE_DER tipo_dato LLAVE_IZQ valores LLAVE_DER','map',10,'p_definir_map','analizadorSintactico.py',187),
  ('tipo_dato -> INT','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',190),
  ('tipo_dato -> STRING','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',191),
  ('tipo_dato -> INT64','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',192),
  ('tipo_dato -> FLOAT32','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',193),
  ('tipo_dato -> FLOAT64','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',194),
  ('tipo_dato -> INT32','tipo_dato',1,'p_tipo_dato','analizadorSintactico.py',195),
  ('valores -> clave_valor','valores',1,'p_valores','analizadorSintactico.py',198),
  ('valores -> clave_valor COMA valores','valores',3,'p_valores','analizadorSintactico.py',199),
  ('clave_valor -> valor DOS_PUNTOS valor','clave_valor',3,'p_clave_valor','analizadorSintactico.py',202),
  ('valor -> CADENA','valor',1,'p_valor','analizadorSintactico.py',205),
  ('valor -> NUMERO','valor',1,'p_valor','analizadorSintactico.py',206),
  ('asignar_valor_map -> ID CORCHETE_IZQ valor CORCHETE_DER ASIGNACION valor','asignar_valor_map',6,'p_asignar_valor_map','analizadorSintactico.py',209),
  ('eliminar_valor_map -> DELETE PARENT_IZQ ID COMA valor PARENT_DER','eliminar_valor_map',6,'p_eliminar_valor_map','analizadorSintactico.py',212),
  ('obtener_valor_map -> ID CORCHETE_IZQ valor CORCHETE_DER','obtener_valor_map',4,'p_obtener_valor_map','analizadorSintactico.py',215),
  ('funcion -> FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa LLAVE_DER','funcion',9,'p_funcion','analizadorSintactico.py',218),
  ('funcion -> FUNC ID PARENT_IZQ argumentos PARENT_DER tipo_dato LLAVE_IZQ programa RETURN ID LLAVE_DER','funcion',11,'p_funcion','analizadorSintactico.py',219),
  ('argumentos -> ID tipo_dato','argumentos',2,'p_argumentos','analizadorSintactico.py',222),
  ('argumentos -> ID tipo_dato COMA argumentos','argumentos',4,'p_argumentos','analizadorSintactico.py',223),
  ('empty -> <empty>','empty',0,'p_empty','analizadorSintactico.py',226),
  ('seman_operacion -> NUMERO MAS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',241),
  ('seman_operacion -> NUMERO MENOS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',242),
  ('seman_operacion -> NUMERO MULTIPLICADOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',243),
  ('seman_operacion -> NUMERO DIVISOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',244),
  ('seman_operacion -> NUMERO MOD_DIVISION NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',245),
  ('seman_operacion -> FLOAT MAS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',246),
  ('seman_operacion -> FLOAT MENOS NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',247),
  ('seman_operacion -> FLOAT MULTIPLICADOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',248),
  ('seman_operacion -> FLOAT DIVISOR NUMERO','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',249),
  ('seman_operacion -> NUMERO MAS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',250),
  ('seman_operacion -> NUMERO MENOS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',251),
  ('seman_operacion -> NUMERO MULTIPLICADOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',252),
  ('seman_operacion -> NUMERO DIVISOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',253),
  ('seman_operacion -> FLOAT MAS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',254),
  ('seman_operacion -> FLOAT MENOS FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',255),
  ('seman_operacion -> FLOAT MULTIPLICADOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',256),
  ('seman_operacion -> FLOAT DIVISOR FLOAT','seman_operacion',3,'p_seman_operacion','analizadorSintactico.py',257),
  ('boolcadena -> STRCONV PUNTO FORMATBOOL PARENT_IZQ BOOLEAN PARENT_DER','boolcadena',6,'p_bool_cadena','analizadorSintactico.py',261),
  ('cadenabool -> STRCONV PUNTO PARSEBOOL PARENT_IZQ CADENA PARENT_DER','cadenabool',6,'p_cadena_bool','analizadorSintactico.py',264),
  ('flotantecadena -> STRCONV PUNTO FORMATFLOAT PARENT_IZQ FLOAT COMA CADENA COMA NUMERO PARENT_DER','flotantecadena',10,'p_flotante_cadena','analizadorSintactico.py',267),
  ('cadenaflotante -> STRCONV PUNTO PARSEFLOAT PARENT_IZQ FLOAT COMA NUMERO PARENT_DER','cadenaflotante',8,'p_cadena_flotante','analizadorSintactico.py',270),
  ('enterocadena -> STRCONV PUNTO FORMATINT PARENT_IZQ CADENA COMA NUMERO PARENT_DER','enterocadena',8,'p_entero_cadena','analizadorSintactico.py',273),
  ('cadenaentero -> STRCONV PUNTO PARSEINT PARENT_IZQ CADENA COMA NUMERO COMA NUMERO PARENT_DER','cadenaentero',10,'p_cadena_entero','analizadorSintactico.py',276),
]
