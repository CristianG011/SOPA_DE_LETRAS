import random
import string

def agregar_palabras_a_sopa(matriz_edit, lista_palabras):

    for palabra in lista_palabras:

        direccion = random.choice(['horizontal', 'vertical', 'diagonal'])

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

            for i in range(len(palabra)):
                matriz_edit[fila + i][columna + i] = palabra[i]

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

if __name__ == "__main__":
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

    matriz_edit = crear_matriz(filas, columnas)


    for i in range(len(matriz_edit)):  # Empieza desde la segunda fila
        for j in range(len(matriz_edit[i])):  # Empieza desde el segundo elemento de la fila
            matriz_edit[i][j]

    matriz_vis = []





    # Palabras
    Palabras_ingresadas = []
    Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")

    while Tipo_palabras not in ["s", "n"]:
        print("Respuesta no válida. Por favor, ingrese 'S' o 'N'.")
        Tipo_palabras = input("¿Quiere ingresar usted las palabras? S/N: ")

    if Tipo_palabras == "s":
        while len(Palabras_ingresadas) < cantidad:
            palabra = input("Ingrese una palabra: ")
            Palabras_ingresadas.append(palabra.upper())
        print(Palabras_ingresadas)

        #for p in Palabras_ingresadas:
           # lista_palabras = list(p)
           # print(lista_palabras)

        agregar_palabras_a_sopa(matriz_edit, Palabras_ingresadas)
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

    lista_palabras = []
    categorias = list(Palabras.keys())
    categoria_elegida = input(f"Ingrese una categoría: {categorias}")

if categoria_elegida in Palabras:
            valor = Palabras[categoria_elegida]
            lista_palabras = random.sample(valor, cantidad)
            print()
            print(lista_palabras)
            print()
            categoria_seleccionada = categoria_elegida       # Guardar la categoria elegida
else:
            print("La categoría ingresada no está en el diccionario.")

agregar_palabras_a_sopa(matriz_edit, lista_palabras)


matriz_vis = []

for fila in matriz_edit:
        fila_actual = []
        for elemento in fila:
            fila_actual.append(elemento)
        matriz_vis.append(fila_actual)

imprimir_matriz_con_coordenadas(matriz_vis)

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

        cantidad_palabras -= 1
        print(f"Felicidades, encontró la palabra {intento_palabra} le faltan {cantidad_palabras} por encontrar ")
    else:
        print(f"La palabra {intento_palabra} no hace parte de las palabras por buscar, por favor intente con otra")










