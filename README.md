# SOPA_DE_LETRAS
# Explicacion del codigo
#### Agregar las palabras a la sopa
Para agregar las palabras que tenemos a la sopa de letras creamos, la funcion 
```
def agregar_palabras_a_sopa(matriz_edit, lista_palabras):
```
Utilizando un bucle para cada palabra en la lista de palabras. Primero utilizamos un random para que elija al azar alguna direccion, de las siguientes. 'horizontal', 'vertical', 'diagonal'.
```
    for palabra in lista_palabras:

        direccion = random.choice(['horizontal', 'vertical', 'diagonal'])
```
despues mediante condicionales vamos a usar una accion segun cual haya sido la eleccion del random.
```
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

#### crear matriz


#### imprimir matriz con coordenadas


#### Tipo_palabras = Tipo_palabras.lower()

#### dificultad: 

#### while Tipo_palabras not in ["s", "n"]:

```

```
#### FUNCIONES

#### def generar_sopa_de_letras(filas, columnas, palabras):



#### def imprimir_matriz(matriz):


#### def direccion_v(palabra, matriz):


#### def direccion_dA(palabra, matriz):


#### def direccion_dB(palabra, matriz):


#### def llenar_espacios_blanco():









