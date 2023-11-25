# SOPA_DE_LETRAS
# Explicacion del codigo
#### letras: 
La lista en la cual tenemos las letras del abecedario.

#### Palabras: 
Lista vacia, en la cual vamos a ingresar las "cantidad_palabras", segun la seleccion del usuario, ya sea de forma manual o que el programa las elija de manera aleatoria.

#### Tipo_palabras: 
En este apartado, elije si ingresar la palabra usted o que el programa las elija al azar.

#### Tipo_palabras = Tipo_palabras.lower()
En algunas ocasiones, las personas tienen las mayusculas activadas y no se dan cuenta, para no tener que crear una condicion para cada una, el .lower vuelve en minuscula la letra ingresada.

#### dificultad: 
Segun, el numero que escoja entre 1 y 3 se va a elegir la dificultad, esto mediante el tamaño de la matriz, y la cantidad de palabras:
para esto creamos las variables:
```
filas = x

columnas = x

cantidad_palabras = x
```
Esto va  variando por eso "x", para cada dificultad hemos elegido utilizar condicionales.
```
if dificultad == 1:

elif dificultad == 2:

elif dificultad == 3:
```
Al ser condicional, va a ejecutar una accion especifica, donse se cumpla la CONDICION puesta.

#### while Tipo_palabras not in ["s", "n"]:
Hay mucha gente, que comete errores ingresando un digito, y puede ser que no se encuentre entre lo que le pedimos, por eso en "Tipo_palabras" el in recorre dentro de la cadena de strings buscando el "s" y "n", y mietras(while) sea "s" o "n" va a realizar una accion, y ahi es donde entra el NOT o sea que si es cualquier cosa que no sea "s" o "n", va SOLAMENTE a imprimir esto "Respuesta no válida. Por favor, ingrese 'S' o 'N'." y posteriormente, para continuar con el ciclo hasta que sea "s" o "n" se coloca de nuevo el input "Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")", una vez cumplida la condicion, definimos:

```
if Tipo_palabras == "s":
```
Aca quiere decir que USTED va a ingresar las palabras, por ende, tenemos que definir ciertas cosas;

"vamor a utilizar ya nuestra lista vacia: Palabras, para ingresar en esta las palabras que queremos."

Primero, un bucle, que se va a repertir segun la cantidad de palabras que tenga la dificultad elegida. ¿Lo recuerdan arriba?. Asi es, es la variable "cantidad_palabras", con esto ya sabemos con hacer un bucle, mientras(while) el largo de nuestra lista(len(Palabras) sea menor a "cantidad_palabras" ejecute... Ahora en codigo
```
while len(Palabras) < cantidad_palabras:
```
Ahora, tenemos que ingresar las palabras que queremos, para ello usamos un input de esta manera:

```
palabra = input("Ingrese una palabra: ")
```
Con esto tenemos la palabra, pero eso no es todo, aun nos falta ingresar la palabra a la lista, esto lo haremos con un ".append", quedando de esta manera.
```
Palabras.append(palabra)
```
Codigo completo
```
if Tipo_palabras == "s":
  while len(Palabras) < cantidad_palabras:
    palabra = input("Ingrese una palabra: ") 
    Palabras.append(palabra)
```












