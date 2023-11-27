# SOPA DE LETRAS

# Explicación del código

**Aclaración**:  En las siguientes secciones, se presentará la primera solución propuesta para abordar el problema, la cual presenta ciertos defectos. Al final, se mostrará la solución definitiva que se implementó para abordar estos problemas. Se detallarán las modificaciones realizadas en el código para solucionar los defectos identificados. Ambas versiones del código están disponibles en un archivo .py para su evaluación y prueba.







#### Agregar las palabras a la sopa
Primero se creó una matriz a partir de letras aleatorias
```python
def crear_matriz(filas, columnas):
    letras = list(string.ascii_uppercase)
    random.shuffle(letras)

    matriz = []
    for i in range(filas):
        fila = []
        for n in range(columnas):
            fila.append(random.choice(letras))
        matriz.append(fila)
    return matriz
```python

Para agregar las palabras que se agregarán posteriormente a la sopa de letras creamos la función 

def agregar_palabras_a_sopa(matriz_edit, lista_palabras):
```
Utilizando un bucle para cada palabra en la lista de palabras. Primero utilizamos un random para que elija al azar alguna direccion, de las siguientes. 'horizontal', 'vertical', 'diagonal'.
```python
    for palabra in lista_palabras:

        direccion = random.choice(['horizontal', 'vertical', 'diagonal'])
```
Posteriormente, a través de condicionales, procederemos a ejecutar una acción específica según la elección realizada mediante la función random.
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
Como se puede observar al emplear random.randint, para la orientación horizontal, seleccionamos de manera aleatoria una fila inicial entre 0 y la longitud de la matriz (len) menos uno. Asimismo, para la columna, se elige al azar una columna en la matriz, asegurándonos de que la palabra quepa completamente en esa fila. Por este motivo, utilizamos la longitud de la palabra (len(palabra)). La misma lógica se aplica a la orientación vertical, pero intercambiando filas por columnas y viceversa.

En cuanto a la orientación diagonal, se sigue el siguiente procedimiento: se elige la fila inicial asegurándonos de que la palabra completa quepa; para ello, restamos al largo de la matriz la longitud de la palabra. Este mismo enfoque se aplica a la columna. Ahora, para insertar la palabra en la matriz, se utiliza un bucle que recorre las letras de la palabra, añadiéndolas secuencialmente mediante la suma de una fila y una columna en cada iteración.

#### Crear matriz
Para crear la matriz utilizamos una lista de letras del abecedario de la función sting, posteriormente con random agarramos  letras al azar de está lista, empezamos con una matriz vacia la cuals se irá modificando mediante un bucle, el cual siguiendo los límites de la matriz va a añadir las letras de manera aleaotoria con el random
```python
    letras = list(string.ascii_uppercase)
    random.shuffle(letras)

    matriz = []
    for i in range(filas):
        fila = []
        for n in range(columnas):
            fila.append(random.choice(letras))
        matriz.append(fila)
    return matriz
```

#### Imprimir matriz con coordenadas
Para imprimir la matriz con coordenadas, realizamos un bucle que añada las letras y número que definimos, para la letras, lista letras, y para numeros usamos enumerate, de esta manera por cada fila y columna que detecte va a ir añadiendo una letra y un número respectivamente
```python
def imprimir_matriz_con_coordenadas(matriz):
    print(" ", end=" ")
    for i in range(len(matriz[0])):
        print(f"{i:2}", end=" ")
    print()
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'à',  'è' , 'ì' , 'ò', 'ù']
    for i, fila in enumerate(matriz):
        print(f"{i:2}", end=" ")
        for elemento in fila:
            print(elemento, end="  ")
        print()
```


#### Dificultad
Teniendo cuenta que ahora vamos a empezar a enviar valores a las funciones, toca empezar a utilizar los inputs desde este punto, para ello vamos a llamar las funciones de la siguiente manera

```python
if __name__ == "__main__":
```
Lo primero que le voy a solicitar al usuario es la dificultad, para realizar esto vamos a usar los valores 1, 2, 3 facil, medio y dificil respectivamente:
```python
dificultad = int(input("Ingrese la dificultad. Escriba '1' para dificultad fácil, '2' para dificultad media y '3' para dificultad difícil: "))
```
Utilizando condicionales quedaría algo asi:
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

#### Palabras suyas o del programa
El programa le va a preguntar si quiere ingresar usted las palabras o por el contrario que las ingrese él mismo, de esta manera:
```python
    Palabras_ingresadas = []
    Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")
```

Para verificar que las letras coincidan con las solicitadas, implementamos un bucle while que continúa solicitando letras hasta que estas sean las adecuadas.
```python
    while Tipo_palabras not in ["s", "n"]:
        print("Respuesta no válida. Por favor, ingrese 'S' o 'N'.")
        Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")
```
Creamos una lista vacía que se irá llenando con palabras según la elección del usuario. Luego, si decide llenar las palabras, mediante un bucle, solicitará palabra por palabra mientras la longitud de la lista "Palabras_ingresadas" sea menor que la cantidad especificada (es decir, la cantidad de palabras). Este proceso se lleva a cabo de la siguiente manera:
```python
    if Tipo_palabras == "s":
        while len(Palabras_ingresadas) < cantidad:
            palabra = input("Ingrese una palabra: ")
            Palabras_ingresadas.append(palabra.upper())
        print(Palabras_ingresadas)
```
Y las agregamos ahora a la función creada anteriormente

```python
agregar_palabras_a_sopa(matriz_edit, Palabras_ingresadas)
```
En caso contrario se hace un diccionario con distintas categorías y palabras. El diccionario permitirá que el mismo usuario escoja las categorías:
 elif Tipo_palabras == "N" or Tipo_palabras == "n":

 ```python
        Palabras = {  #nuestras palabras
    }
```

El siguiente código permite interactuar con el usuario. Permite mostrar las categorías, la opción de que se escojan, luego las guarda en una lista para poder agregarlas a la sopa de letras y escoge una cantidad asociada a la dificultad de palabras aleatorias dentro de la categoría escogida.

```python
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
Para visualizar la matriz, en forma de sopa de letras (Es decir que no se vea ni con comas ni corchetes) se van recorrieron las filas y columnas con un for de la siguiente manera
   ```python
   matriz_vis = []

    for fila in matriz_edit:
        fila_actual = []
        for elemento in fila:
            fila_actual.append(elemento)
        matriz_vis.append(fila_actual)

    imprimir_matriz_con_coordenadas(matriz_vis)
```
El resultado anterior se guardó en la lista "matriz_vis" la cual solo sirve para visualización. Ésto es porque al ingresar los datos de ésta forma con el ```.append``` el resultado no va a hacer una lista de listas, por lo que el enfoque dado no va a funcionar. Para esto, se trabajó con la variable "matriz_edit" que si bien al imprimir no se ve del todo bien, nos permite ajustarle las filas y columnas.


La siguiente y última función se encarga de gestionar las coordenadas ingresadas por el usuario en el juego de sopa de letras. Inicialmente, se definen las coordenadas x1, y1 y x2, y2 con los valores proporcionados. Luego, se crea una cadena vacía llamada palabra que se utilizará para almacenar la palabra formada por las coordenadas.

La función utiliza condicionales para determinar la orientación de la palabra (horizontal, vertical o diagonal) según las coordenadas proporcionadas. Para la orientación horizontal, se verifica si las coordenadas tienen la misma x, para vertical se verifica si tienen la misma y, y para diagonal se utiliza la diferencia absoluta entre x e y.

En cada caso, la función utiliza bucles para recorrer las letras en la matriz según las coordenadas y construir la palabra. Una vez formada la palabra, se devuelve.

Posteriormente, se inicia un bucle while que continuará ejecutándose mientras haya palabras por encontrar (la variable cantidad_palabras no sea igual a cero). En cada iteración, el usuario ingresa las coordenadas, y la función ingresar_coordenadas se utiliza para obtener la palabra formada por esas coordenadas. Se verifica si la palabra está en la lista de palabras por encontrar "Palabras_ingresadas". Si es así, se marca como encontrada, se elimina de la lista y se actualiza el contador de palabras restantes. Se imprime un mensaje indicando el progreso del jugador. El bucle continúa hasta que todas las palabras hayan sido encontradas, momento en el cual se imprime un mensaje de victoria.






```python
def ingresar_coordenadas(matriz, coordenadaA, coordenadaB):


    x1, y1 = coordenadaA
    x2, y2 = coordenadaB

    palabra = ""

    if x1 == x2:
        if y1 < y2:
            for j in range(y1, y2 + 1):
                palabra += matriz[x1][j]
        else:
            for j in range(y2, y1 + 1):
                palabra += matriz[x1][j]
        return palabra

    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                palabra += matriz[i][y1]
        else:
            for i in range(x2, x1 + 1):
                palabra += matriz[i][y1]
        return palabra

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

cantidad_palabras = len(Palabras[categoria_seleccionada])

while cantidad_palabras != 0:
    coordenada1 = (int(input("Ingrese la fila de la coordenada 1: ")), int(input("Ingrese la columna de la coordenada 1: ")))
    coordenada2 = (int(input("Ingrese la fila de la coordenada 2: ")), int(input("Ingrese la columna de la coordenada 2: ")))
    intento_palabra = ingresar_coordenadas(matriz_edit, coordenada1, coordenada2)

    palabra_encontrada = False
    lista_palabras = Palabras[categoria_seleccionada]
    if intento_palabra in lista_palabras:
        palabra_encontrada = True
        lista_palabras.remove(intento_palabra)
```
## Solución a la transposición de las palabras: 

Para rellenar la sopa de letras primero se creó inicialmente una matriz utilizando la comprensión de listas, y se rellenó con letras aleatoriamente. Luego se ingresaron las palabras. Utilizando este método se generó un problema principalmente y es la transposición de palabras, se intentaron varias soluciones pero a la final se optó por utilizar la biblioteca numpy para el manejo de matrices.

## Funciones importantes
**Return all**: Devuelve los valores(En este caso filas y columnas) en forma de tupla

**shape**: Se refiere a la dimensión de la matriz. Hace parte de la librería numpy

**Numpy.full**: Genera una matriz vacía, los elementos se dan en la misma función. En este caso se requiere que la matriz esté vacía

**Random.randint**: Escoge números al azar dentro de un rango especificado


**Se crearon distintas funciones con el fin de generar la matriz y evitar este problema. Pero el resto de la lógica del código se conserva:**

El siguiente código resuelve el problema de la transposición. Evaluando si se encuentra un espacio un vacío, para cada dirección en la que se vaya a poner la palabra. 
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
Éstos fueron los cambios sustanciales que se realizaron.

**Los siguientes códigos no fueron modificados a excepción de algunas variables, que fueron necesarias cambiar para su buen funcionamiento:**
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
#Lista al final

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


    x1, y1 = coordenadaA                                        #Definimos ambas coordenas con números
    x2, y2 = coordenadaB

    palabra = ""                                                #Creamos una palabra vacía que se usará más tarde 

                                                                #Según los valores númericos de las coordenadas podemos definir en que posicion se encuentran, por ejemplo;

                                                                #horizontal quiere decir que su valores en Y permanecen quietos, mientras que, en x cambia.

                                                                #Para vertical, ocurre la misma situación, pero en este caso los valores se invierten
                                                                #Y para diagonal, ambos son diferentes 

   #Para palabras en horizontal           

    if x1 == x2:                                                   # Acá apreciamos que x no cambia. Por lo tanto, "palabra" va a ser horizontal
        if y1 < y2:                                                # Definimos la dirrección con la cual vamos a trabajar
            for j in range(y1, y2 + 1):                            # Y creamos un bucle para que por cada iteración vaya avanzando y tomando letra por letra hasta llegar al                                                                     #extremo de  la coordenada
                palabra += matriz[x1][j]                           
        else:
            for j in range(y2, y1 + 1):                        #La misma situación pero si invirtió el orden 
                palabra += matriz[x1][j]
        return palabra                                         #Develve todas la letras que agarro en orden, formando una "palabra".

#Para palabras en vertical

    if y1 == y2:                                               #En este caso y no cambia. Por lo tanto "palabra" va a ser vertical
        if x1 < x2:                                            #Definimos la dirección con la cual vamos a trabajar
            for i in range(x1, x2 + 1):                        #Con el bucle por cada itración avanza y toma letra por letra hasta llegar al maximo de la coordenada
                palabra += matriz[i][y1]
        else:
            for i in range(x2, x1 + 1):                        #La misma situación pero si invirtió el orden 
                palabra += matriz[i][y1]
        return palabra                                         #Develve todas la letras que agarro en orden, formando una "palabra".

#Para palabras en diagonal

    if abs(x2 - x1) == abs(y2 - y1):                           #Utilizando esta fórmula aseguramos que la coordenada es diagonal
        if x2 > x1 and y2 > y1:                                #Trabajamos de está manera para cada caso
            for i in range(x2 - x1 + 1):                       #Va avanzando y tomando letra por letra, sumando o  restando 1 de manera vertical y horizontal, hasta llegar al
                palabra += matriz[x1 + i][y1 + i]              #extremo de la coordenada 
        elif x2 > x1 and y2 < y1:    
            for i in range(x2 - x1 + 1):
                palabra += matriz[x1 + i][y1 - i]
        elif x2 < x1 and y2 > y1:
            for i in range(x1 - x2 + 1):
                palabra += matriz[x1 - i][y1 + i]
        else:
            for i in range(x1 - x2 + 1):
                palabra += matriz[x1 - i][y1 - i]
        return palabra                                        #Develve todas la letras que agarro en orden, formando una "palabra".

    return None

cantidad_palabras = len(Palabras_ingresadas)                  #Para tener un conteo, utilizaremos está variable que cuenta los elemento que hay dentro de la lista

while cantidad_palabras != 0:                                 #Mientras te falten 1 o más palabras el programa se seguirá ejecutando 
    coordenada1 = (int(input("Ingrese la fila de la coordenada 1: ")), int(input("Ingrese la columna de la coordenada 1: ")))
    coordenada2 = (int(input("Ingrese la fila de la coordenada 2: ")), int(input("Ingrese la columna de la coordenada 2: ")))
    intento_palabra = ingresar_coordenadas(resultado_sopa, coordenada1, coordenada2)        #Acá ingresamos las coordenadas dadas a la función

    palabra_encontrada = False                                 #False que utilizaremos más adelante para eliminar palabras      

    #lista_palabras = Palabras[categoria_seleccionada]        

    if intento_palabra in Palabras_ingresadas:                 #Acá lo que hacemos es una prueba, si las letras que recorrio la coordenada forman una palabra que hace parte
        palabra_encontrada = True                              #de las palabras por buscar, entonces lo valemos como verdad
        Palabras_ingresadas.remove(intento_palabra)            #Y removemos la palabra de nuestras palabras por encontrar

        cantidad_palabras -= 1                                 #Al contador que teniamos antes, le restamos uno, y así susesivamente hasta que sea cero
        if cantidad_palabras == 0:                             #Si es cero, quiere decir que encontraste todas las palabras por lo tanto HAS GANADO EL JUEGO
            print("Felicidades ha ganado el juego")
        else:                                                  #Sino se repite hasta que sea cero
          print(f"Felicidades, encontró la palabra {intento_palabra} le faltan {cantidad_palabras} por encontrar ")
    else:
        print(f"La palabra {intento_palabra} no hace parte de las palabras por buscar, por favor intente con otra")
```

# Muchas gracias por la atención, esperamos este proyecto haya sido de su agrado.

### Diccionario de palabras

En caso de que el usuario desee que el programa genere las palabras, se hizo el siguiente diccionario el cual almacena las palabras por categorías

```python
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
```
