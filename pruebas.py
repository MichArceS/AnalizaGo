from analizadorSintactico import parser

pruebas = [
    'a := 3',
    'var a string = ""',
    'var b, c int = 1, 2',
    '1 > 2',
    'var1 >= var2',
    'var1 != var2',
    'if var1 < va2 {a = 2}',
    'for i :=0 ; i < 5; i++ { a = 2}',
    '''switch opcion{
	case 1: 
		a = 1
	case 2: 
		a = 2
	default:
		a = 3
    }''',
    'array := [2]float64{7.0, 8.5, 9.1}',
    'b := make([]int, 0, 5)',
    '''mapa  =  map[string]int{
        "A":  2,
        "B": 3
    }''',
    'var1 + var2',
    'var1 * var2',
    'var1/var2',
    'var1 - var2',
    'var1 % var2',
    'var1++',
    'var1--',
    'strconv.FormatBool(true)',
    'strconv.ParseBool("true")',
    'strconv.FormatFloat(3.14,"e",32)',
    'strconv.ParseFloat("3.14", 64)',
    'strconv.FormatInt(10, 32)',
    'strconv.ParseInt("10",10, 32)',
    'func nombreFuncion(var1 int, var2 int) string{ return var3 }',
    'fmt.Printf("Hello %d\\n", 23)',
    'fmt.Println("Hello", 23)',
    'fmt.Println("Hello")',
]

for item in pruebas:
    try:
        res = parser.parse(item)
        print('PRUEBA: '+item+' | ESTADO: OK')
    except SyntaxError as e:
        print('**********************************')
        print('PRUEBA: '+item+' | ESTADO: ERROR!!')
        print('**********************************')