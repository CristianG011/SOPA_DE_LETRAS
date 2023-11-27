# SOPA_DE_LETRAS
# Explicacion del codigo
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
Creamos una lista vacia la cual a la cual ira agregando las palabras segun la eleccion,
despues si el usuario elije llenar las palabras el, mediante un bucle va a ir pidiendo palabra por palabra metras que largo de la lista "Palabras_ingresadas" sea menor al de cantidad (osea cantidad de palabras)









