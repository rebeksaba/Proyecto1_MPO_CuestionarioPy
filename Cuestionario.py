#Cuestionario de preguntas para la obtención de la nacionalidad española------REBECA SÁNCHEZ
#Este cuestionario está diseñado para ayudar a los solicitantes de nacionalidad española a prepararse para el examen de conocimientos constitucionales y socioculturales de España (CCSE).


#1. Lista de Preguntas:

preguntas = [

{
    "pregunta": "¿Cómo se llama la ley más importante de cada comunidad autónoma?",
    "opciones": ["A. Estatuto de Autonomía", "B. Normativa autonómica", "C. Ley de la Comunidad", "D. Constitución autonómica"],
    "respuesta_correcta": "A"
},

{
    "pregunta": "¿Cuántas mujeres han sido presidentas del Gobierno en España?",
    "opciones": ["A. Ninguna", "B. Una", "C. Dos", "D. Tres"],
    "respuesta_correcta": "A"
},

{
    "pregunta": "¿Cómo se llama la organización que defiende los intereses de los trabajadores?",
    "opciones": ["A. Asociación", "B. Partido", "C. Sindicato", "D. Cámara de comercio"],
    "respuesta_correcta": "C"
},

{
    "pregunta": "¿Cuál es la montaña más alta de la península ibérica?",
    "opciones": ["A. Mulhacén", "B. Aneto", "C. Teide", "D. Himalaya"],
    "respuesta_correcta": "A"
},

{
    "pregunta": "¿Cuál de las siguientes mujeres es una científica española reconocida mundialmente?",
    "opciones": ["A. Montserrat Caballé", "B. Ana María Matute", "C. Margarita Salas", "D. Almudena Grandes"],
    "respuesta_correcta": "C"
},

{
    "pregunta": "La educación infantil en España…",
    "opciones": ["A. Es obligatoria", "B. Tiene dos ciclos", "C. Empieza a los cuatro años", "D. No existe"],
    "respuesta_correcta": "B"
},

{
    "pregunta": "La organización que trabaja para conseguir la integración de las personas con discapacidad visual es…",
    "opciones": ["A. La ONCE", "B. UNICEF", "C. Cáritas", "D. Médicos Sin Fronteras"],
    "respuesta_correcta": "A"
},

{
    "pregunta": "En España está permitido el matrimonio…",
    "opciones": ["A. Solo entre personas del mismo sexo", "B. Entre personas del mismo y diferente sexo", "C. Solo entre personas de diferente sexo", "D. Solo por la iglesia"],
    "respuesta_correcta": "B"
},

{
    "pregunta": "La sidra es una bebida típica de…",
    "opciones": ["A. Asturias", "B. Valencia", "C. Madrid", "D. Canarias"],
    "respuesta_correcta": "A"
},

{
    "pregunta": "¿Quién hace el DNI?",
    "opciones": ["A. La Guardia Civil", "B. La Policía Local", "C. La Policía Nacional", "D. La DGT"],
    "respuesta_correcta": "C"
},

{
    "pregunta": "Las temperaturas suaves con abundantes lluvias son propias del clima…",
    "opciones": ["A. Continental", "B. Oceánico", "C. Subtropical", "D. Desértico"],
    "respuesta_correcta": "B"
},

{
    "pregunta": "¿Dónde se encuentra la Cueva de Altamira que es Patrimonio Mundial de UNESCO?",
    "opciones": ["A. En Cataluña", "B. En Aragón", "C. En Cantabria", "D. En Galicia"],
    "respuesta_correcta": "C"
},

{
    "pregunta": "¿Cómo se llaman los órganos de gobierno que solo existen en Canarias?",
    "opciones": ["A. Cabildos", "B. Consejos Insulares", "C. Diputaciones", "D. Ayuntamientos"],
    "respuesta_correcta": "A"   
},

{
    "pregunta": "¿En qué ciudad de España hay una mezquita que es Patrimonio de la Humanidad?",
    "opciones": ["A. Madrid", "B. Córdoba", "C. Granada", "D. Santiago de Compostela"],
    "respuesta_correcta": "B"
},

{
    "pregunta": "¿Quién puede presentar una queja al Defensor del Pueblo?",
    "opciones": ["A. Solo los ciudadanos legalmente residentes", "B. Solo los españoles mayores de 18 años", "C. Todos los ciudadanos, españoles o extranjeros", "D. Ninguno de los anteriores"],
    "respuesta_correcta": "C"
},

]

#2. Función para mostrar el menú principal:

def mostrar_menu():
    print("Bienvenido al Cuestionario de Nacionalidad Española")
    print("Seleccione una opción:")
    print("1. Iniciar cuestionario")
    print("2. Salir")
    opcion = input("Elige una opción (1 o 2): ")
    return opcion

#3. Función para iniciar el cuestionario:

def iniciar_cuestionario():
    aciertos = 0
    
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta = input("Tu respuesta (A, B, C o D): ").upper()
        if respuesta == pregunta["respuesta_correcta"]:
            print("¡Muy bien!")
            aciertos += 1
        else:
            print(f"No has acertado. La respuesta correcta es: {pregunta['respuesta_correcta']}")
            print("A por la siguiente! ")

    print("\nCuestionario finalizado.")
    print(f"Has acertado {aciertos} de {len(preguntas)} preguntas.")
    porcentaje = (aciertos / len(preguntas)) * 100
    print(f"Tu porcentaje de aciertos es de: {porcentaje:.2f}%")
    
    if aciertos == len(preguntas):
        print("¡Perfecto! Has respondido todo bien, eso es un 10!!!.")
    elif aciertos >= len(preguntas) * 0.5:
        print("¡Muy bien! Estás preparad@ para el examen.")
    else:
        print("Estudia un poco más y lo conseguirás")


 #4. Función principal para ejecutar el programa:       

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            iniciar_cuestionario()
        elif opcion == "2":
            print("Gracias por usar el cuestionario. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

    


