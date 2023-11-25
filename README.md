# SOPA_DE_LETRAS
# Cosas a tener en cuenta
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
Aca quiere decir que















