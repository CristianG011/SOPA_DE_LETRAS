# SOPA DE LETRAS
# Explicacion del codigo

**Aclaración**:  En las siguientes secciones, se presentará la primera solución propuesta para abordar el problema, la cual presenta ciertos defectos. Al final, se mostrará la solución definitiva que se implementó para abordar estos problemas. Se detallarán las modificaciones realizadas en el código para solucionar los defectos identificados. Ambas versiones del código están disponibles en un archivo .py para su evaluación y prueba.







#### Agregar las palabras a la sopa
Para agregar las palabras que tenemos a la sopa de letras creamos, la funcion 
```python
def agregar_palabras_a_sopa(matriz_edit, lista_palabras):
```
Utilizando un bucle para cada palabra en la lista de palabras. Primero utilizamos un random para que elija al azar alguna direccion, de las siguientes. 'horizontal', 'vertical', 'diagonal'.
```python
    for palabra in lista_palabras:

        direccion = random.choice(['horizontal', 'vertical', 'diagonal'])
```
despues mediante condicionales vamos a usar una accion segun cual haya sido la eleccion del random.
```python
        if direccion == 'horizontal':
            fila = random.randint(0, len(matriz_edit) - 1)
            columna = random.randint(0, len(matriz_edit[0]) - len(palabra))
            for i in range(len(palabra)):
                matriz_edit[fila][columna + i] = palabra[i]
        elif direccion == 'vertical':
            fila = random.randint(0, len(matriz_edit) - len(palabra))
            columna = random.randint(0, len(matriz_edit[0]) - 1)
            for i in range(len(palabra)):
                matriz_edit[fila + i][columna] = palabra[i]
        elif direccion == 'diagonal':
            fila = random.randint(0, len(matriz_edit) - len(palabra))
            columna = random.randint(0, len(matriz_edit[0]) - len(palabra))
```
Como se puede apreciar utilando random randint,para horizontal tomamos aleatoriamente una fila inicial que puede estar entre 0 y el largo de la matriz(len) menos uno y para la columna se elige aleatoriamente una columna en la matriz de manera que la palabra quepa completamente en esa fila y por eso utilizamos la longitud de la palabra(len(palabra)) y la misma situacion con vertical pero lo que se hizo con filas lo haces con columnas y lo de columnas lo haces con filas

Para la diagonal se hizo lo siguiente; eleccion de fila inicial vamos a verificar que entre la palabra completa, para ello le restamos al largo de la matriz el largo de la palabra, de igual manera para la columna, ahora hay que ingresar la palabra a la matriz, para ello se utiliza un bucle que recorre las letras de la palabra y para cada una va a ir añadiendola sumando una fila y una columna.

#### Crear matriz


#### Imprimir matriz con coordenadas


#### Ingresar coordenadas


#### Dificultad
Teniendo cuenta que ahora vamos a empeza a enviar valores a las funciones, toca empezar a utilizar los inputs desde este punto, para ello vamos a llamar las funciones de la siguiente manera

```python
if __name__ == "__main__":
```
Lo primero que le voy a solicitar al usuario el la dificultad, para realizar esto vamos a usar los valores 1, 2, 3 facil, medio y dificil respectivamente:
```python
dificultad = int(input("Ingrese la dificultad. Escriba '1' para dificultad fácil, '2' para dificultad media y '3' para dificultad difícil: "))
```
utilizando condicionales quedaria algo asi:
```python
    if dificultad == 1:
        filas = 10
        columnas = 10
        cantidad = 5
    elif dificultad == 2:
        filas = 20
        columnas = 20
        cantidad = 10
    elif dificultad == 3:
        filas = 30
        columnas = 30
        cantidad = 15
```
Haciendo esto pudimos definir "x" filas y "x" columnas y "x" palabras(cantidad de palabras) por dificultad, pero ahora tenemos que meter esas dimensiones en la funcion que crea la matriz, eso se hace de la siguiente manera;
```python
    matriz_edit = crear_matriz(filas, columnas)
```
y con eso quedaria esta parte
#### Palabras suyas o del programa
El programa le va a preguntar si quiere ingresar usted las palabras o por el contrario que las ingrese el mismo, de esta manera;
```python
    Palabras_ingresadas = []
    Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")
```
Para verificar que las letras sean las que se solicita usamos un mientras que no sean esas letras, el programa va a volver a pedir letras
```python
    while Tipo_palabras not in ["s", "n"]:
        print("Respuesta no válida. Por favor, ingrese 'S' o 'N'.")
        Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")
```
Creamos una lista vacia la cual a la cual ira agregando las palabras segun la eleccion,
despues si el usuario elije llenar las palabras el, mediante un bucle va a ir pidiendo palabra por palabra metras que largo de la lista "Palabras_ingresadas" sea menor al de cantidad (osea cantidad de palabras), esto se hace de esta manera:
```python
    if Tipo_palabras == "s":
        while len(Palabras_ingresadas) < cantidad:
            palabra = input("Ingrese una palabra: ")
            Palabras_ingresadas.append(palabra.upper())
        print(Palabras_ingresadas)
```
y las agregamos ahora a la funcion

```python
agregar_palabras_a_sopa(matriz_edit, Palabras_ingresadas)
```








### Solución a la transposición de las palabras: 

Para rellenar la sopa de letras primero se creó inicialmente una matriz utilizando la comprensión de listas, y se rellenó con letras aleatoriamente. Luego se ingresaron las palabras. Utilizando este método se generó un problema principalmente y es la transposición de palabras, se intentaron varias soluciones pero a la final se optó por utilizar la biblioteca numpy para el manejo de matrices.

Se crearon distintas funciones con el fin de generar la matriz y evitar este problema. Pero el resto de la lógica del código se conserva:

El siguiente código resuelve el problema de la transposición. Evaluando si se encuentra un espacio un vacío, para cada dirección en la que se vaya a poner la palabra
```python
def esposicionVacia(matriz, fila, col, longitudPalabra, direccion):
    if direccion == 'horizontal':
        return all(matriz[fila, col + i] == ' ' for i in range(longitudPalabra))    #Cada letra que se va agregando en una posición vacía
    elif direccion == 'vertical':
        return all(matriz[fila + i, col] == ' ' for i in range(longitudPalabra))
    elif direccion == 'diagonal':
        return all(matriz[fila + i, col + i] == ' ' for i in range(longitudPalabra))
    else:
        return False
```

El siguiente código utiliza la función ```shape``` la cual permite agregar letras aleatorias en cada espacio que se encuentre en blanco. Esto utilizando la comprensión de listas para recorrer filas y columnas
```python
def letrasAzar(matriz):
    for i in range(matriz.shape[0]):                                                 #Representa las filas
        for j in range(matriz.shape[1]):                                             #Representa las columnas
            if matriz[i, j] == ' ':                                                  #Si se encuentra en blanco
                matriz[i, j] = random.choice('abcdefghijklmnopqrstuvwxyzñ').upper()  #Rellena con letras al azar
    return(matriz)
```
Por último, la función más importante. Ésta nos permitirá ingresar las palabras a la sopa de letras como tal:

Cosas a tener en cuenta:
- Las palabras ingresadas deberán ser transformadas a mayúsculas
- Se deberá generar una matriz vacía para poder trabajar en base a esta
- Se deben inicializar número de intentos para que se prueben distintas formas de probar las palabras en distintas direcciones
- El break es importante para que las palabras no salgan repetidas
- Las coordenadas se escogen aleatoriamente
- Se tiene en cuenta que las palabras no vayan a sobrepasar la matriz

```python
def rellenarLetras(palabras, filas, columnas):
    palabras = [entrada.upper() for entrada in palabras]   #Genera las palabras en mayúsculas
    matriz = np.full((filas, columnas), ' ', dtype=str)    #Genera una matriz vacía usando numpy

    for k in range(len(palabras)):
        num_intentos = 25                             # Este es el número de veces que se va a validar cada palabra en el caso en el que no se pueda ingresar en una posición específica
        for intento in range(num_intentos):
            direccion = random.choice(['horizontal', 'vertical', 'diagonal'])                         #Escoge una dirección al azar
            fila, col = np.random.randint(0, matriz.shape[0]), np.random.randint(0, matriz.shape[1])  #Ingresa a fila y columna el número de la posición aleatoria


#El siguiente código agrega las palabras según la posición que se haya escogido aleatoriamente según dos parámetros:
#Que la palabra al ingresarse no se vaya a salir del tamaño de la matriz Y con la función esposicionVacia evualamos que efectivamente se ingrese en un espacio vacío
#El break es importante ya que permite que una vez se ingrese la palabra salga del bucle, con esto evitamos que la palabra se repita más veces dentro de la sopa de letras

            if direccion == 'horizontal' and col + len(palabras[k]) <= matriz.shape[1] and esposicionVacia(matriz, fila, col, len(palabras[k]), direccion):
                matriz[fila, col:col+len(palabras[k])] = list(palabras[k])
                break
            elif direccion == 'vertical' and fila + len(palabras[k]) <= matriz.shape[0] and esposicionVacia(matriz, fila, col, len(palabras[k]), direccion):
                matriz[fila:fila+len(palabras[k]), col] = list(palabras[k])
                break
            else:
                if direccion == 'diagonal' and fila + len(palabras[k]) <= matriz.shape[0] and col + len(palabras[k]) <= matriz.shape[1] and esposicionVacia(matriz, fila, col, len(palabras[k]), direccion):
                    for i in range(len(palabras[k])):
                        matriz[fila+i, col+i] = palabras[k][i]
                    break
    letrasAzar(matriz)
    return matriz
```
```python
# Imprime la matriz usando la función de rellenar letras, ya teniendo las palabras ingresadas
resultado_sopa = rellenarLetras(Palabras_ingresadas, filas, columnas) # Función que da el resultado

#Según el rango (Es decir el tamaño de la matriz), se añaden los números en las filas y columnas, simulando las coordenadas
col_names = [str(i) for i in range(resultado_sopa.shape[1])]

#Usando la biblioteca de pandas, se usa la función dataframe para mostrar la sopa de letras mucho más bonita
df = pd.DataFrame(resultado_sopa, columns=col_names)    #Para las coordenadas se llama a la variable "resultado_sopa" que contiene, la matriz impresa en forma de matriz como tal

print(df)   #Imprime la matriz resultante
```
Éstos fueron los cambios sustanciales que se realizaron. Los siguientes códigos no fueron modificados a excepción de algunas variables, que fueron necesarias cambiar para su buen funcionamiento:
```python
#El siguiente código define la dificultad del juego. Entre más fácil será más pequeña la matriz y tendrá menos palabras. La dificultad está definida por el usuario

# Escoger nivel de dificultad
print("Bienvenido a nuestra sopa de letras, esperamos que disfrutes")
dificultad = int(input("Ingrese la dificultad. Escriba '1' para dificultad fácil, '2' para dificultad media y '3' para dificultad difícil: "))

if dificultad == 1:
        filas = 10
        columnas = 10
        cantidad = 5
elif dificultad == 2:
        filas = 20
        columnas = 20
        cantidad = 10
elif dificultad == 3:
        filas = 30
        columnas = 30
        cantidad = 15
```
```python
# Se crea una lista de palabras ingresadas que se utilizará más adelante
#Se le da la opción al usuario de si quiere ingresar las palabras él mismo o prefiere que las genere el programa

Palabras_ingresadas = []
Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")
```
```python
#Si la respuesta no está dentro de las opciones dadas se imprime un mensaje de respuesta no válida

while Tipo_palabras not in ["S","s", "N", "n"]:
    print("Respuesta no válida. Por favor, ingrese 'S' o 'N'.")
    Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")

#En este caso, cuando la opción sea palabras ingresadas:
#El usuario ingresará las palabras que quiera (Teniendo en cuenta la dificultad será el número de palabras que se permitirá ingresar)
#Las palabras ingresadas se meterán a la lista antes hecha "Palabras_ingresadas" y se pondrán en mayúscula

if Tipo_palabras == "s" or Tipo_palabras == 'S':
    while len(Palabras_ingresadas) < cantidad:
            palabras = input("Ingrese una palabra: ")
            Palabras_ingresadas.append(palabras.upper())

#Si el usuario quiere que las palabras las genere el programa:
#Se va a crear un diccionario con categorías definidas

elif Tipo_palabras == "N" or Tipo_palabras == "n":
   Palabras = {

"Colores": ["AMARILLO", "ROJO", "VERDE", "AZUL", "NARANJA", "NEGRO", "ROSADO", "MORADO", "BLANCO", "DORADO", "PLATEADO", "GRIS", "TURQUESA", "MARRON", "CELESTE", "LIMA", "MAGENTA",
            "CIAN", "BEIGE", "AGUAMARINA", "VIOLETA"],

"Animales": ["DELFIN", "BALLENA", "TIBURON", "TORTUGA", "ELEFANTE", "JIRAFA", "LEON", "TIGRE", "OSO", "LOBO", "ZORRO", "CONEJO", "ARDILLA", "NUTRIA", "CASTOR", "CIERVO", "JABALI",
             "PUMA", "LEOPARDO", "PANTERA", "COCODRILO", "LAGARTO", "IGUANA", "CAMALEON", "SERPIENTE", "VIBORA", "ARAÑA", "ESCORPION", "ABEJA", "AVISPA", "MOSQUITO", "MARIPOSA",
             "POLILLA", "ESCARABAJO", "CUCARACHA", "MOSCA", "HORMIGA", "CIGARRA", "SURICATA"],

"Emociones": ["AMOR", "FELICIDAD", "TRISTEZA", "MIEDO", "ENOJO", "SORPRESA", "ASOMBRO", "VERGUENZA", "CONFUSIÓN", "ORGULLO", "CULPA", "CELOS", "GRATITUD", "ESPERANZA", "DOLOR",
              "EMPATIA", "COMPASION", "DESPRECIO", "ANSIEDAD", "ESTUPOR", "NOSTALGIA", "CULPA", "HOSTILIDAD", "EUFORIA", "INSEGURIDAD", "ADMIRACION", "IMPACIENCIA", "DESDEN",
              "AVERSION", "ESTIMA", "CAUTELA", "ALIVIO", "ENTUSIASMO", "RESIGNACIÓN", "AGOBIO", "CURIOSIDAD"],

"Medios de transporte": ["COCHE", "AUTOBUS", "TREN", "METRO", "BICICLETA", "MOTO", "AVION", "BARCO", "TRANVIA", "CAMION", "HELICOPTERO", "TAXI", "PATINETA", "TRINEO", "AMBULANCIA",
                         "BARCA", "SUBMARINO", "TRACTOR", "CANOA"],

"Tecnologías": ["TABLETA", "LAPTOP", "SMARTWATCH", "TELEVISOR", "CONSOLA", "CELULAR", "TELEFONO", "DRON", "IMPRESORA", "CAMARA", "COMPUTADOR", "AUDIFONOS"],

"Objetos cotidianos": ["LLAVE", "CARTERA", "GAFAS", "RELOJ", "BOLIGRAFO", "PAPEL", "CUADERNO", "BOTELLA", "MOCHILA", "SOMBRILLA", "ROPA", "CEPILLO", "JABON", "TOALLA", "PLATO", "TAZA",
                       "LAMPARA", "ESPEJO", "MAQUILLAJE", "CARGADOR", "ALMOHADA", "SILLA", "PAÑUELO", "LINTERNA", "LAPIZ", "ENCHUFE", "CONTROL", "CORTINA", "BOLSA", "TARJETA", "CINTA",
                       "SARTEN", "ESCOBA"],

"Comidas": ["PIZZA", "PASTA", "SUSHI", "ENSALADA", "TACO", "POLLO", "SOPA", "FILETE", "CURRY", "PAELLA", "LASAÑA", "PASTEL", "PESCADO", "TAPAS", "SANDWICH", "BURRITO", "RISOTTO",
            "CEVICHE", "EMPANADA", "CHURRASCO"],

"Países": ["EEUU", "CHINA", "RUSIA", "INDIA", "BRASIL", "MEXICO", "CANADA", "FRANCIA", "ALEMANIA", "ITALIA", "JAPON", "AUSTRALIA", "ESPAÑA", "COREA", "SUDAFRICA", "NIGERIA", "ARGENTINA",
           "TURQUIA", "INDONESIA", "EGIPTO", "ISRAEL", "COLOMBIA", "PERU"],

"Animes": ["NARUTO", "ONEPIECE", "DRAGONBALL", "ATTACKONTITAN", "DEATHNOTE", "MYHEROACADEMIA", "ONEPUNCHMAN", "TOKYOGHOUL", "DEMONSLAYER", "EVANGELION", "BLEACH", "BLACKCLOVER",
           "JUJUTSUKAISEN", "CODEGEASS", "VIOLETEVERGARDEN", "HAIKYUU", "PROMISEDNEVERLAND", "CHAINSAWMAN", "DRSTONE", "BEASTARS", "MONSTER", "LOVEISWAR", "POKEMON", "FIREFORCE", "BAKI"],

"Videojuegos": ["MARIOKART", "ZELDA", "MINECRAFT", "TETRIS", "GTAV", "FORTNITE", "OVERWATCH", "CALLOFDUTY", "LOL", "RESIDENTEVIL", "HALO", "GODOFWAR", "ASSASSINSCREED", "DARKSOULS",
                "GENSHINIMPACT", "COUNTERSTRIKE", "ROCKETLEAGUE", "APEXLEGENDS"],

"Marcas": ["COCACOLA", "APPLE", "GOOGLE", "MICROSOFT", "AMAZON", "SAMSUNG", "NIKE", "ADIDAS", "MCDONALDS", "TOYOTA", "BMW", "SONY", "FACEBOOK", "TWITTER", "INSTAGRAM", "WALMART",
           "PEPSI", "DISNEY", "VISA", "FORD", "GUCCI", "ROLEX"],

"Peliculas": ["TITANIC", "STAR WARS", "JURASSICPARK", "HARRYPOTTER", "FORRESTGUMP", "AVATAR", "MATRIX", "GLADIADOR", "INTERESTELAR", "INDIANAJONES", "REGRESOALFUTURO", "SPIDERMAN",
              "INCEPTION", "LALALAND", "TOYSTORY", "FROZEN", "AVENGERS"],

"Alimentos": ["MANZANA", "BANANO", "NARANJA", "UVA", "KIWI", "FRESA", "MANGO", "SANDIA", "PIÑA", "MELON", "PERA", "DURAZNO", "CEREZA", "PAPAYA", "CIRUELA", "HIGO", "MANDARINA", "GUAYABA",
              "LECHUGA", "TOMATE", "ZANAHORIA", "BROCOLI", "COLIFLOR", "ESPINACA", "PEPINO", "PIMENTON", "CALABACIN", "CALABAZA", "CEBOLLA", "AJO", "PATATA", "BERENJENA", "CHAMPIÑON"],

"Acciones": ["TRABAJO", "ESTUDIAR", "JUGAR", "CORRER", "CAMINAR", "BAILAR", "CANTAR", "DORMIR", "COMER", "BEBER", "REIR", "LLORAR", "SONAR", "PENSAR", "HABLAR", "ESCUCHAR", "VER",
             "SENTIR", "TOCAR", "OLER", "GUSTAR", "DISFRUTAR", "VIAJAR", "CONDUCIR", "NADAR", "SURFEAR", "ESQUIAR", "MONTAR", "SALTAR", "CAER", "LEVANTAR", "EMPUJAR", "JALAR", "ABRIR",
             "CERRAR", "EMPACAR", "ENVIAR", "RECIBIR", "REGALAR", "COMPRAR", "VENDER", "CAMBIAR", "BUSCAR", "ENCONTRAR", "PERDER", "GANAR", "COMPETIR", "AYUDAR", "APRENDER", "ENSENAR",
             "CONOCER", "CREER", "DUDAR", "ESPERAR", "QUERER", "AMAR", "ODIAR", "OLVIDAR", "RECORDAR", "DESEAR", "NECESITAR", "PODER", "DEBER", "SER", "ESTAR", "IR", "VENIR", "QUEDAR",
             "PARTIR", "LLEGAR", "SALIR", "VOLVER", "ANDAR", "PASEAR", "VISITAR", "CONOCER", "INVITAR", "ACEPTAR", "RECHAZAR", "PROBAR", "EXPERIMENTAR", "REALIZAR", "CREAR", "DIBUJAR",
             "PINTAR", "ESCRIBIR", "LEER", "RESOLVER", "CELEBRAR", "ORGANIZAR", "PREPARAR", "COCINAR", "HORNEAR", "PICAR", "CORTAR", "MEZCLAR", "BATIR", "HERVIR", "FREIR", "ASAR",
             "ALQUILAR", "COMPARTIR", "CUIDAR", "PROTEGER", "RESPETAR", "TRATAR", "ESFORZARSE", "DESCANSAR", "RELAJARSE", "MEDITAR", "RESPIRAR", "EXHALAR", "INHALAR", "SOPLAR", "SILBAR",
             "SONREIR", "ABRAZAR", "BESAR", "ESTRECHAR", "ACARICIAR", "MIRAR", "OBSERVAR", "VIGILAR", "ANALIZAR", "PENSAR", "REFLEXIONAR", "IMAGINAR", "COMPRENDER", "ENTENDER", "ASIMILAR",
             "DUDAR", "CUESTIONAR", "INVESTIGAR", "EXPLORAR", "DESCUBRIR", "ADMIRAR", "APRECIAR", "VALORAR", "DISFRUTAR", "APROVECHAR", "APLAUDIR", "ELOGIAR", "FELICITAR", "CRITICAR",
             "REPROCHAR", "EXIGIR", "PEDIR", "SOLICITAR", "CONSEGUIR", "OBTENER", "GANAR", "SACRIFICAR", "RENUNCIAR", "DESECHAR", "RECHAZAR", "EVITAR", "PREVENIR", "SUPERAR", "VENCER",
             "ESCAPAR", "HUIR", "ESCONDER", "OCULTAR", "MOSTRAR", "REVELAR", "EXPONER", "DEMOSTRAR", "EXPLICAR", "COMUNICAR", "TRANSMITIR", "INTERCAMBIAR", "DIALOGAR", "NEGOCIAR",
             "RESOLVER", "CONFRONTAR", "ENFRENTAR", "ASUMIR", "ACEPTAR", "PERDONAR", "CONVENCER", "PERSUADIR"],

"Lugares": ["PARQUE", "PLAYA", "BOSQUE", "MONTAÑA", "LAGO", "RIO", "DESIERTO", "CAMPO", "GRANJA", "JARDIN", "PLAZA", "MERCADO", "BIBLIOTECA", "MUSEO", "TEATRO", "CINE", "CAFE",
            "RESTAURANTE", "BAR", "GIMNASIO", "PISCINA", "SPA", "HOSPITAL", "CLINICA", "FARMACIA", "ESCUELA", "UNIVERSIDAD", "OFICINA", "CASA", "APARTAMENTO", "IGLESIA", "AUDITORIO",
            "ESTACION", "AEROPUERTO"],

"Deportes": ["FUTBOL", "BALONCESTO", "BEISBOL", "TENIS", "GOLF", "HOCKEY", "CRIQUET", "RUGBY", "ATLETISMO", "NATACION", "CICLISMO", "BOXEO", "SNOWBOARD", "SURF", "SKATEBOARDING",
             "VOLEIBOL", "ESCALADA", "PESCA", "KARATE", "TAEKWONDO", "BOLOS", "BILLAR", "AJEDREZ", "PARKOUR"]

}

#Dentro del elif

   Palabras_ingresadas.append(Palabras)                                                    #Se agregan las palabaras a la lista "Palabras_ingresadas"
   categorias = list(Palabras.keys())                                                      #Almacena todas las llaves las cuales son las categorías, en una lista
   categoria_elegida = input(f"Ingrese una categoría(Escríbela tal cual): {categorias}")   #Muestra todas las categorías y da la opción de escoger una

#Creamos un if para asegurarnos de que la categoría ingresada exista en el diccionario

   if categoria_elegida in Palabras:
            valor = Palabras[categoria_elegida]                        #Almacena las palabras asociadas a las categorías
            Palabras_ingresadas = random.sample(valor, cantidad)       #Escoge palabras aleatoriamente. Teniendo en cuenta que escogerá el número de palabras asociadas a su dificultad
            print()
            print("Todas las palabras están en singular")
            print()
            print(Palabras_ingresadas)
            print()
            categoria_seleccionada = categoria_elegida                 #Guardar la categoria elegida
   else:
            print("La categoría ingresada no está en el diccionario.")
```
```python
#Función para que el usuario ingrese las coorenadas

def ingresar_coordenadas(matriz, coordenadaA, coordenadaB):


    x1, y1 = coordenadaA
    x2, y2 = coordenadaB

    palabra = ""

#Para palabras en horizontal

    if x1 == x2:
        if y1 < y2:
            for j in range(y1, y2 + 1):
                palabra += matriz[x1][j]
        else:
            for j in range(y2, y1 + 1):
                palabra += matriz[x1][j]
        return palabra

#Para palabras en vertical

    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                palabra += matriz[i][y1]
        else:
            for i in range(x2, x1 + 1):
                palabra += matriz[i][y1]
        return palabra

#Para palabras en diagonal

    if abs(x2 - x1) == abs(y2 - y1):
        if x2 > x1 and y2 > y1:
            for i in range(x2 - x1 + 1):
                palabra += matriz[x1 + i][y1 + i]
        elif x2 > x1 and y2 < y1:
            for i in range(x2 - x1 + 1):
                palabra += matriz[x1 + i][y1 - i]
        elif x2 < x1 and y2 > y1:
            for i in range(x1 - x2 + 1):
                palabra += matriz[x1 - i][y1 + i]
        else:
            for i in range(x1 - x2 + 1):
                palabra += matriz[x1 - i][y1 - i]
        return palabra

    return None

cantidad_palabras = len(Palabras_ingresadas)

while cantidad_palabras != 0:
    coordenada1 = (int(input("Ingrese la fila de la coordenada 1: ")), int(input("Ingrese la columna de la coordenada 1: ")))
    coordenada2 = (int(input("Ingrese la fila de la coordenada 2: ")), int(input("Ingrese la columna de la coordenada 2: ")))
    intento_palabra = ingresar_coordenadas(resultado_sopa, coordenada1, coordenada2)

    palabra_encontrada = False

    #lista_palabras = Palabras[categoria_seleccionada]

    if intento_palabra in Palabras_ingresadas:
        palabra_encontrada = True
        Palabras_ingresadas.remove(intento_palabra)

        cantidad_palabras -= 1
        if cantidad_palabras == 0:
            print("Felicidades ha ganado el juego")
        else:
          print(f"Felicidades, encontró la palabra {intento_palabra} le faltan {cantidad_palabras} por encontrar ")
    else:
        print(f"La palabra {intento_palabra} no hace parte de las palabras por buscar, por favor intente con otra")
```
