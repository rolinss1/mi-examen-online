import streamlit as st

# Configuración visual de la ventana
st.set_page_config(page_title="Simulador MINEDU - Ascenso 2024", page_icon="imagen rolinss3.jpg", layout="centered")
st.sidebar.image("imagen rolinss3.jpg", width=120, caption="Profesor(a) Administrador(a)")
st.title("Simulador de Examen MINEDU")
st.subheader("Concurso de Ascenso 2024 - Educación Religiosa Secundaria")
st.write("Responde las preguntas y obtén tu calificación instantánea al finalizar.")
st.markdown("---")

# Base de datos con las preguntas extraídas del cuadernillo y sus respuestas correctas
# Formato: 0=A, 1=B, 2=C
banco_preguntas = [
    {
        "numero": 1,
        "enunciado": "Como parte de una sesión de aprendizaje, los estudiantes han identificado el mensaje del texto bíblico 'Jesús y Zaqueo'. Como siguiente actividad, la docente busca que los estudiantes comparen dicho texto con otros que tengan un mensaje similar. ¿Cuál de los siguientes textos bíblicos es adecuado para el propósito de la docente?",
        "opciones": ["'Jesús sana a la hija de una pagana' (Mateo 15, 21-28).", "'El fariseo y la mujer pecadora' (Lucas 7, 36-50).", "'Jesús resucita al hijo de una viuda' (Lucas 7, 11-17)."],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 2,
        "enunciado": "Una docente implementará el método ver-juzgar-actuar. Tras presentar un informe ambiental y la encíclica Laudato si´, la docente busca que los estudiantes implementen el momento actuar del método. ¿Cuál de las siguientes acciones pedagógicas promueve el logro del propósito de la docente?",
        "opciones": ["Pedir que organicen una propuesta para que, desde la comunidad, se soliciten medidas para la reducción de los gases contaminantes a las autoridades locales.", "Pedir que elaboren un resumen a partir del análisis realizado entre el informe y el apartado 1 de la encíclica.", "Pedir que busquen información sobre los diversos tipos de actividades que contaminan el aire dentro de su comunidad."],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 3,
        "enunciado": "Durante una sesión, un docente busca que los estudiantes reflexionen sobre la importancia de la fraternidad cristiana basándose en un fragmento de la encíclica Fratelli Tutti. ¿Cuál de las siguientes actividades pedagógicas es más adecuada para el logro del propósito del docente?",
        "opciones": ["Pedirles que expliquen qué actitudes se resaltan sobre el samaritano. Luego leer la parábola y comentar valores.", "Pedirles que expliquen qué quiere decir la frase 'Cuidemos la fragilidad...'. Luego buscar en evangelios cómo actuaba Jesús y preguntarles si estarían dispuestos a actuar de acuerdo al mensaje.", "Pedirles que expliquen el significado de 'El samaritano del camino se fue sin esperar reconocimientos...'. Relacionarlo con Mateo 6,3 y compartir hallazgos."],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 4,
        "enunciado": "Durante una reunión pedagógica, los docentes del área de Educación Religiosa están planificando un proyecto de aprendizaje. Entre las siguientes actividades propuestas por los docentes, ¿cuál plantea mayor demanda cognitiva a los estudiantes?",
        "opciones": ["Juan dice: 'Identificar mensajes y principales enseñanzas de las parábolas La oveja perdida y El hijo pródigo...'", "Bernabé dice: 'Realizar un listado de las obras de misericordia puestas en práctica...'", "María dice: 'Sobre la base de las bienaventuranzas, dialoguen sobre problemas recurrentes, indaguen qué acciones se han implementado, las evalúen y propongan alternativas de solución...'"],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 5,
        "enunciado": "Como parte de una sesión de aprendizaje, los estudiantes están empleando el método de la Lectio Divina para analizar la parábola 'La semilla que crece por sí sola'. Un estudiante comenta: 'El mensaje de la parábola me ha motivado a realizar algunas acciones con mi familia para que, día a día, pueda ir creciendo la Palabra de Dios...'. ¿A qué momento de la Lectio Divina corresponde el comentario?",
        "opciones": ["Al momento de la oración.", "Al momento de la meditación.", "Al momento de la contemplación."],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 6,
        "enunciado": "De acuerdo con la secuencia didáctica presentada sobre el cuidado del ambiente, ¿Qué proceso de aprendizaje se busca promover, principalmente, con la primera actividad de la secuencia didáctica?",
        "options_alt": "1. Pide a los estudiantes que dialoguen sobre las diferentes actividades socioeconómicas...",
        "opciones": ["La activación de saberes previos.", "La generación del conflicto cognitivo.", "La gestión autónoma del aprendizaje."],
        "correcta": 0  # Clave: A
    },    {
        "numero": 7,
        "enunciado": "¿Qué proceso de aprendizaje se busca promover, principalmente, con la quinta actividad de la secuencia didáctica presentada en el folleto?",
        "opciones": ["La transferencia del aprendizaje.", "La metacognición del aprendizaje.", "La generación del conflicto cognitivo."],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 8,
        "enunciado": "Un estudiante nota que en las fiestas de la Iglesia católica hay imágenes de Jesús, la virgen y los santos, y pregunta si es una falta de respeto para Dios utilizarlas, basándose en que la Biblia prohíbe adorar imágenes. ¿Qué documento debe seleccionar el docente para atender su duda sobre el uso de imágenes?",
        "opciones": ["El capítulo cuarto de la carta encíclica Fratelli Tutti: 'Un corazón abierto al mundo entero'.", "El capítulo primero de la primera parte del documento conclusivo de Aparecida: 'Los discípulos misioneros'.", "El capítulo primero, 'Amarás al Señor tu Dios con todo tu corazón (...)', de la sección 'Los diez mandamientos' del Catecismo de la Iglesia católica."],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 9,
        "enunciado": "Un estudiante comenta que la virgen María tiene diferentes representaciones y nombres en el Perú (Chapi, Cocharcas, Asunta). El docente busca desarrollar actividades para que comprendan por qué existen estas representaciones y su significado para las comunidades. ¿Cuál acción pedagógica es más adecuada?",
        "opciones": ["Pedir que mencionen qué representaciones marianas son homenajeadas en sus localidades, identificar rasgos culturales locales en las imágenes y preguntar por qué cada comunidad añade elementos locales.", "Pedirles que comenten qué valores cristianos se relacionan con la virgen María, presentar las diversas representaciones que existen en el Perú para que las analicen e indicarles que expliquen la importancia de rendirle homenaje.", "Pedirles que expliquen por qué las representaciones marianas de las diversas regiones son auténticas expresiones de fe, pedir su opinión sobre las muestras de fe y señalar la importancia de las fiestas marianas."],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 10,
        "enunciado": "Al inicio del año escolar, un docente planifica actividades para promover el diálogo ecuménico. ¿Cuál actividad es más adecuada para fomentar que los estudiantes trabajen en conjunto sin importar la iglesia cristiana a la que pertenecen?",
        "opciones": ["Pedir que, en equipos, propongan un proyecto de ayuda social para la comunidad de la IE, describan los valores de su confesión involucrados e identifiquen las coincidencias entre sus confesiones que favorecen el proyecto.", "Pedir que, en equipos, lean la parábola 'Yo soy la vid: produzcan frutos en mí', expliquen los símbolos de unidad y organicen una exposición sobre las razones por las cuales las personas se separaron.", "Pedir que, en equipos, señalen cuál es la celebración religiosa más importante de sus confesiones, describan las acciones, ritos y veneraciones, y pregunten las semejanzas y diferencias."],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 11,
        "enunciado": "La docente revisó las interpretaciones escritas del texto 'Las bienaventuranzas' realizadas por los estudiantes y les entregó sus productos con anotaciones en forma de preguntas reflexivas (ej. 'Si son personas pecadoras, ¿por qué se les promete el Reino?'). Según el Minedu, ¿qué tipo de retroalimentación ha realizado la docente?",
        "opciones": ["Retroalimentación reflexiva.", "Retroalimentación elemental.", "Retroalimentación descriptiva."],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 12,
        "enunciado": "La docente planifica actividades sobre las cartas católicas. ¿Cuál de las siguientes acciones pedagógicas planificadas se centra en que los estudiantes se organicen para trabajar de forma colaborativa?",
        "opciones": ["Designar a cada integrante del equipo una carta para resumir, identificar el tema principal y brindar pautas para su exposición individual.", "Pedir que acuerden los criterios y contenidos que consideran pertinente incluir, evaluar los acuerdos para orientarlos en el reparto equitativo de tareas y llevar un control mediante un cuadro de responsabilidades.", "Solicitar que se organicen y nombren a un líder, pedir al líder que designe las tareas y responsabilidades de cada integrante y entregar al líder una ficha de evaluación."],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 13,
        "enunciado": "En un organizador gráfico, los estudiantes sintetizaron cómo se presenta a Jesús y cuál es el mensaje en cada evangelio (ej. Mateo: como rey; Marcos: como servidor). ¿Cuál de los siguientes aprendizajes se evidencia, principalmente, en este organizador?",
        "opciones": ["Identifica en qué pasajes bíblicos las acciones de Jesús expresan el cumplimiento de las profecías del Antiguo Testamento.", "Identifica las principales enseñanzas de los evangelios sobre la vida de Jesús.", "Identifica cómo cada evangelista caracteriza a Jesús."],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 14,
        "enunciado": "Después de leer la parábola 'El árbol se conoce por los frutos' (Mateo 7, 15-20), el docente se propone que los estudiantes la analicen a través del método histórico-crítico. ¿Qué acciones pedagógicas son adecuadas para iniciar este análisis?",
        "opciones": ["Preguntarles qué significado tiene la frase 'el árbol sano da frutos buenos' y pedir que comenten qué acciones de las personas se relacionan con los frutos buenos.", "Proponerles indagar sobre cuál era la percepción que tenía la sociedad judía del Mesías y pedir que comenten por qué Jesús decía a la comunidad que se debían cuidar de aquellos que daban un mensaje falso.", "Pedirles que comenten por qué se dice que todo árbol que no da buenos frutos se echa al fuego y solicitar que lean el texto 'La higuera que no da fruto' para señalar su relación."],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 15,
        "enunciado": "Después de leer la parábola 'El árbol se conoce por los frutos', el docente se propone que reflexionen sobre su mensaje. ¿Cuál de las siguientes actividades es más adecuada para ello?",
        "opciones": ["Pedir que, en equipos, dialoguen sobre la advertencia de cuidarse de los falsos profetas con piel de oveja, mencionar ejemplos y establecer criterios para poner en práctica el mensaje.", "Solicitar que dialoguen sobre el simbolismo de los árboles, los frutos y el lobo, explicarles el contexto en que Jesús presentó estos símbolos y preguntar cómo contribuyen a comprender las enseñanzas.", "Pedir que expliquen quiénes eran los falsos profetas, por qué Jesús los relaciona con lobos feroces e indicar que lean el Catecismo apartado 2850 para comprender cómo actuar."],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 16,
        "enunciado": "Durante una reunión colegiada, los docentes de una institución educativa están dialogando sobre las actividades que implementarán con el fin de que los estudiantes adquieran herramientas para resolver conflictos. ¿Cuál de las siguientes propuestas de los docentes favorece más ello?",
        "opciones": [
            "Esteban dice: 'Si ocurre un conflicto durante un trabajo grupal, es mejor separar a los estudiantes y enviarlos a diferentes grupos...'",
            "María dice: 'Podemos decirles que, cuando se presente algún desacuerdo, se tomen un tiempo para tranquilizarse y piensen en las razones. Luego, que cada uno explique cómo se sintió y cómo cree que podría solucionarse...'",
            "Pedro dice: 'Cuando ocurra un conflicto, podemos pedirles que, voluntariamente, un estudiante comunique a todos las normas de convivencia...'"
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 17,
        "enunciado": "Una docente presenta un organizador sobre las Fases de la historia de la salvación (El tiempo del Antiguo Testamento, El tiempo de Jesús, El tiempo de la Iglesia). ¿Por qué se puede afirmar que el organizador es pertinente para el propósito de que los estudiantes comprendan los principales hechos?",
        "opciones": [
            "Porque sirve como guía completa y detallada para que los estudiantes puedan conocer los hechos de la historia de la salvación en el Génesis, evangelios y Hechos.",
            "Porque ofrece una visión general de cómo se realiza, en la historia de la humanidad, la salvación que Dios ofrece: el anuncio de la promesa, el cumplimiento con Jesús y el esfuerzo de la Iglesia.",
            "Porque permite que los estudiantes conozcan profundamente los medios y las personas a través de las cuales Dios reveló su plan."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 18,
        "enunciado": "La docente va a desarrollar la unidad 'La Creación es una expresión del amor de Dios a las personas' a partir del Génesis. Tiene como propósito activar los saberes previos. ¿Cuál de las siguientes actividades es adecuada?",
        "opciones": [
            "Indicar que lean 'Dios ordena el universo' (Génesis 1, 1-20) y orientarlos para que expliquen el mensaje del texto.",
            "Indicar que lean la teoría científica de la creación del mundo y los relatos bíblicos de la creación e identifiquen sus diferencias.",
            "Indicar que escriban las ideas que conozcan sobre las teorías o relatos sobre el origen del mundo y pedirles que las compartan con la clase."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 19,
        "enunciado": "Tras observar la pintura 'La creación de Adán' de Miguel Ángel, la docente se propone que interpreten la representación que planteó el pintor acerca del relato del Génesis. ¿Cuál actividad es más adecuada?",
        "opciones": [
            "Pedirles que lean Génesis 1, 26 ('Hagamos al hombre a nuestra imagen...') y comenten cómo se representa en la pintura, y por qué Eva está al lado de Dios.",
            "Pedirles que lean ''El Adán' en el jardín de Edén' (Génesis 2, 4b-24). Luego, indicar que comenten qué elementos están representados, cuáles de manera diferente y con qué finalidad el pintor los destacó.",
            "Pedirles que lean los dos relatos del Génesis, analicen cuál tiene más elementos en la pintura y expliquen por qué el pintor se basó principalmente en uno."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 20,
        "enunciado": "Una estudiante nota que el manto que rodea a Dios en la pintura tiene forma de cerebro humano. La docente quiere que reflexionen sobre la intención del pintor. ¿Cuál acción pedagógica es más adecuada?",
        "opciones": [
            "Preguntarles si notaron la forma, pedir que comparen el manto con el Génesis 1, y explicarles por qué el pintor incluyó elementos que no están en el texto.",
            "Solicitar que señalen en qué pasaje se narra cómo Dios otorgó el conocimiento. Luego, explicarles que el pintor representó el cerebro para comunicar que la razón proviene de Dios, y preguntar por los dedos unidos.",
            "Pedirles que, en equipos, expliquen qué creen que representa el manto, indicar que comparen sus explicaciones con la frase 'La razón y la fe (...) provienen de Dios' de la encíclica Fides et Ratio, y compartir conclusiones."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 21,
        "enunciado": "La docente se propone que los estudiantes comprendan cómo se relacionan ambos relatos de la creación del Génesis. ¿Cuál actividad es más adecuada?",
        "opciones": [
            "Pedir que investiguen cuál de los dos relatos fue escrito primero y busquen en comentarios bíblicos la explicación de por qué existen dos versiones.",
            "Pedir que identifiquen la secuencia de eventos en cada relato y señalen qué evento se destaca. Luego, pedirles que, en pares, expliquen el propósito de cada uno y si se complementan.",
            "Pedir que comparen los pasajes de la creación del hombre y la mujer en Génesis 1 y 2, identifiquen cuál es más detallado y expliquen por qué."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 22,
        "enunciado": "La docente se propone una actividad para promover que los estudiantes comprendan el origen de los relatos de la creación del libro del Génesis. ¿Cuál actividad es más adecuada?",
        "opciones": [
            "Presentarles algunos mitos sobre la creación de culturas contemporáneas al Génesis, pedir que los comparen, señalen semejanzas y pregunten por qué existen esas semejanzas.",
            "Presentarles el contexto histórico de cada relato, brindarles un texto que explique las fuentes orales y escritas que sirvieron de base al pueblo de Israel, y pedir que expliquen por qué hay dos relatos.",
            "Presentarles una línea de tiempo del pueblo de Israel, pedir que investiguen las tradiciones orales de las tribus y comentarles que por mantenerse de forma oral existe más de una versión."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 23,
        "enunciado": "Una docente busca que los estudiantes reflexionen sobre la importancia de poner en práctica una cultura de paz y diálogo siguiendo el ejemplo de Jesús. ¿Cuál de las siguientes actividades permite iniciar con este propósito?",
        "opciones": [
            "Pedir que, en equipos, busquen y contrasten textos de diálogo y paz en el Catecismo y evangelios, seleccionen personajes de la Iglesia que promovieron la paz y presenten un listado de acciones.",
            "Comentarles sobre la situación de algunos países con conflictos. Luego, presentarles pasajes de la vida de Jesús que narren problemas de su sociedad y pedir que expliquen cómo respondía Jesús y cómo ayuda hoy.",
            "Indicar que busquen información sobre las jornadas mundiales de la paz, analicen el mensaje que quieren trasmitir y pregunten si estas jornadas contribuyen a tomar conciencia."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 24,
        "enunciado": "Un estudiante comenta que, aunque siempre ora, Dios no lo escucha pues no responde a sus peticiones. La docente se propone que el estudiante analice su forma de orar. ¿Cuál acción pedagógica es más adecuada?",
        "opciones": [
            "Comentarle que Dios no le concede sus peticiones porque no se comunica de manera correcta, y pedir que lea 'El Padrenuestro' para expresar sus deseos en la forma y orden correspondiente.",
            "Indicarle que lea la parábola 'El fariseo y el publicano' (Lucas 18, 9-14) y explique la diferencia al orar. Luego, pedir que analice su propia forma de orar, identificando sus expectativas sobre Dios y si pide bienes o dones.",
            "Pedirle que lea Santiago 4, 2-3 ('...si piden algo, no lo consiguen porque piden mal...'). Sobre esta base, decirle cuál es el mensaje y ayudarlo a encontrar oraciones más pertinentes."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 25,
        "enunciado": "La docente tiene como propósito que los estudiantes investiguen la concordancia que existe entre el Antiguo Testamento y el Nuevo Testamento. Para guiarlos, ha decidido darles un organizador. Evaluando el folleto, ¿cuál de las opciones (Gráficos A, B o C) guarda la estructura de libros históricos, didácticos y proféticos cruzados entre ambos testamentos?",
        "opciones": [
            "El organizador A (Tabla con columnas de Libro Sagrado, AT, NT, Grupo, Resumen y Objetivo).",
            "El organizador B (Diagrama de Venn con intersección de Libros Proféticos).",
            "El organizador C (Matriz de doble entrada que contrasta Libros Históricos, Didácticos y Proféticos para el Antiguo y Nuevo Testamento con preguntas guía)."
        ],
        "correcta": 2  # Clave: C
    },
        {
        "numero": 26,
        "enunciado": "Los estudiantes están leyendo la parábola 'El hijo pródigo' (Lucas 15, 11-32). A partir de este texto, la docente busca que los estudiantes reflexionen sobre el sacramento de la Reconciliación. ¿Cuál de las siguientes actividades es más pertinente para lograr este propósito?",
        "opciones": [
            "Pedir que indiquen a quiénes representan el padre, el hijo menor y el hijo mayor de la parábola. Luego, explicarles por qué es importante que los cristianos conozcan las enseñanzas de la parábola leída.",
            "Pedir que escojan el pasaje de la parábola que más les gustó y expliquen por qué lo escogieron. Luego, solicitar que expliquen cuál es el mensaje de dicho pasaje y si contiene alguna enseñanza sobre los sacramentos.",
            "Pedir que comparen las actitudes del hijo menor cuando se fue, cuando se arrepintió y cuando regresó a casa. Luego, solicitar que expliquen cuáles fueron las razones del cambio de actitud del hijo menor hacia su padre."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 27,
        "enunciado": "Una docente busca que sus estudiantes reflexionen sobre la importancia de respetar la dignidad humana desde la perspectiva cristiana. ¿Cuál de las siguientes acciones pedagógicas es más adecuada para que la docente logre su propósito?",
        "opciones": [
            "Presentar el caso de una persona que no recibe una atención de salud adecuada. Luego, en equipos, solicitar que lean el texto 'Jesús sana a un ciego de nacimiento' (Juan 9, 1-16) y comenten sobre el trato que Jesús brinda al ciego. Finalmente, pedir que, sobre la base del texto bíblico, dialoguen sobre si es que consideran que todas las personas merecen un trato digno.",
            "Pedir que lean y analicen, en la Declaración universal de los derechos humanos, si es que existen algunas bases de la dignidad humana provenientes del cristianismo. Luego, solicitar que, en equipos, elijan uno de los derechos y elaboren ejemplos del cumplimiento de dicho derecho. Finalmente, invitar a que compartan con la clase los ejemplos que crearon y señalen cómo se relacionan con la dignidad humana.",
            "Pedir que lean y analicen el texto sobre la creación del hombre (Génesis 1, 26-27). Luego, sobre la base de lo leído, comentarles cómo el análisis de la frase 'Dijo Dios: Hagamos al hombre a nuestra imagen y semejanza' permite comprender el significado de la dignidad humana según el cristianismo. Finalmente, pedir que, en equipos, analicen otros textos bíblicos que contienen las bases de la dignidad humana, como 'La curación del leproso'."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 28,
        "enunciado": "Los estudiantes, orientados por la docente, han leído e interpretado las bienaventuranzas. A continuación, la docente busca conocer qué estrategias metacognitivas emplearon para comprenderlas. ¿Cuál de las siguientes acciones es adecuada para ello?",
        "opciones": [
            "Pedir que expliquen si tuvieron dificultades al leer las bienaventuranzas. Luego, preguntar por las acciones que realizaron para lograr superarlas.",
            "Pedir que mencionen cuál es el mensaje de las bienaventuranzas. Luego, indicar que busquen una lectura que tenga un mensaje similar.",
            "Pedir que mencionen qué aspecto de las bienaventuranzas llamó más su atención. Luego, indicar cómo podrían incorporar en sus vidas las enseñanzas que ofrecen."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 29,
        "enunciado": "Durante una actividad de análisis bíblico, un docente presenta a los estudiantes el texto de Mateo 9, 20-22 (la mujer con hemorragias que toca el manto de Jesús). ¿Cuál de las siguientes actividades es más adecuada para que los estudiantes interpreten el mensaje del texto?",
        "opciones": [
            "Comentar cuáles fueron las razones por las cuales la mujer que fue curada no se acercaba directamente a Jesús. Luego, indicar que, a partir de la explicación, busquen otros ejemplos de personas que no se acercaban a Jesús por sentirse impuros. Finalmente, pedir que presenten sus hallazgos a sus compañeros de aula e identifiquen coincidencias.",
            "Pedir que describan qué sucedía con la mujer mencionada en el relato y por qué esperaba a Jesús. Luego, solicitar que, en equipos, comenten el significado de la frase 'Tu fe te ha salvado'. Finalmente, pedirles que lean otros textos en los cuales Jesús sana a enfermos e indicarles que los comparen con el que han leído.",
            "Indicar que lean el significado del texto en los comentarios del contexto bíblico. Luego, pedir que, sobre la base de lo leído, comenten cómo la mujer logró que Jesús la curara. Finalmente, solicitar que, en equipos, opinen sobre la importancia de la fe que Jesús destacó en la mujer enferma."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 30,
        "enunciado": "Como parte de la planificación de una sesión que busca que los estudiantes reflexionen sobre las celebraciones cristianas, un docente diseña algunas actividades para que los estudiantes comprendan qué es la cuaresma. ¿Cuál de las siguientes actividades es más adecuada para iniciar dicho aprendizaje?",
        "opciones": [
            "Presentarles la historia del pueblo de Israel en el desierto, en la cual dicho pueblo tuvo que pasar por un periodo largo de pruebas y penitencias. Luego, solicitar que busquen, en la Biblia, algunos personajes que pasaron por un proceso de conversión y penitencia. Finalmente, explicarles por qué todo cristiano debe pasar por periodos de penitencia personal.",
            "Preguntar si es que sus familias celebran la semana santa. Luego, decirles que, en equipos, comenten las tradiciones que tienen sus familias para prepararse para la semana santa y señalen las que tienen en común. Finalmente, a partir de lo señalado, preguntarles por qué es importante tener un tiempo de preparación previo a la semana santa.",
            "Pedir que, en equipos, elaboren un escrito con las ideas que tienen sobre el significado de la cuaresma. Luego, indicar que señalen las semejanzas encontradas sobre la cuaresma entre los escritos. Finalmente, solicitar que busquen, en el Catecismo de la Iglesia católica, el significado de la cuaresma y lo comparen con sus escritos."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 31,
        "enunciado": "Los estudiantes, en equipos, realizarán una investigación sobre el respeto de la dignidad humana en el Perú. Como parte de la planificación, la docente les dará orientaciones para favorecer la gestión autónoma del aprendizaje. ¿Cuál de las siguientes acciones pedagógicas favorece más este propósito?",
        "opciones": [
            "Pedirles que dialoguen sobre cómo podrían organizar las tareas para realizar su investigación. Luego, brindarles algunos criterios para distribuir equitativamente las tareas a los miembros del equipo y animarlos a proponer otras en caso de ser necesario. Finalmente, solicitar que implementen una estrategia que les permita verificar el cumplimiento de las tareas según la distribución que hicieron.",
            "Pedirles que mencionen algunos casos de discriminación que hayan presenciado en sus comunidades. Luego, decirles que elijan uno de los casos señalados y compartan argumentos que expliquen por qué estos evidencian una vulneración de la dignidad y los derechos humanos. Finalmente, pedirles que, en cada equipo, consideren los mejores argumentos expuestos para desarrollarlos en su investigación.",
            "Pedirles que identifiquen, a través de un esquema, las partes que tendrá su trabajo de investigación. Luego, decirles que, en equipos, se distribuyan cada una de las partes del trabajo y busquen fuentes bibliográficas con la información necesaria sobre el tema. Finalmente, solicitarles que extraigan las principales ideas de las fuentes consultadas para que, sobre esta base, inicien un borrador de las diversas partes de la investigación."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 32,
        "enunciado": "Un docente presenta el pasaje 'Dios-Amor es fuente del amor' (1 Juan 4, 7-11). Después de que los estudiantes comprendieran el mensaje, busca que reflexionen sobre él para aplicarlo en su vida diaria. ¿Cuál de las siguientes acciones pedagógicas es más adecuada?",
        "opciones": [
            "Pedir que expliquen qué creen que significa la frase 'El que no ama no ha conocido a Dios'. Luego, solicitar que compartan sus opiniones sobre cómo se manifiesta el amor de Dios a las personas, según el texto. Finalmente, pedir que examinen sus acciones y evalúen si estas se corresponden con el mensaje del texto leído.",
            "Solicitar que describan algunas definiciones que conozcan sobre la palabra 'amor'. Luego, a partir de las definiciones descritas, compartir con ellos el significado del amor cristiano. Finalmente, decirles que, tomando como referencia el amor cristiano, comenten el mensaje de la frase 'Amémonos unos a otros, porque el amor viene de Dios'.",
            "Indicar que comenten por qué el texto dice que 'el amor viene de Dios'. Luego, pedir que busquen, en las parábolas de la misericordia (Lucas 15), algunas características del amor de Dios y señalen si se relacionan con el texto 'Dios-Amor es fuente del amor'. Finalmente, a partir de sus hallazgos, elaborar con los estudiantes un listado de ejemplos que muestran cómo Dios manifiesta su amor a los hombres."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 33,
        "enunciado": "La docente ha pedido a los estudiantes que analicen el texto 'Dios-Amor es fuente del amor' a través del método de la Lectio Divina. ¿Cuál de los siguientes textos elaborados por los estudiantes se corresponde con el momento de la meditación?",
"opciones": [
    "Agradeceré a Dios por su infinito amor, por salvarnos del pecado enviando a su Hijo único para que tengamos vida eterna. Le pediré que este amor esté presente en mí cada día.",
    "El amor de Dios nos permite ver nuestra reality de otra manera. Por eso, trataré de poner en práctica la frase 'amémonos unos a otros' en mi familia, institución educativa y comunidad.",
    "Este relato dice cómo es el amor de Dios y cómo se ha manifestado entre nosotros. Además, me ha llamado la atención esa frase que dice: 'El que no ama no ha conocido a Dios, pues Dios es amor'."
],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 34,
        "enunciado": "Como parte de una actividad de aprendizaje sobre el respeto por la dignidad humana, una docente se propone que los estudiantes analicen un documento de la Iglesia católica que favorezca la reflexión sobre el rol de las mujeres en la transmisión de la fe en sus comunidades. ¿Cuál de los siguientes documentos es pertinente para ello?",
        "opciones": [
            "La exhortación apostólica Querida Amazonía.",
            "La carta encíclica Fratelli Tutti.",
            "La carta encíclica Laudato si´."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 35,
     "enunciado": "Un docente tiene como propósito que los estudiantes analicen textos bíblicos a través del método histórico-crítico. Para ello, les presenta el texto bíblico 'Curación de un leproso' (Mateo 8, 1-4). ¿Cuál de las siguientes acciones pedagógicas es más adecuada para el momento inicial del método histórico-crítico?",
     "opciones": [
         "Indicarles que expliquen cómo creen que Jesús actuaría en el contexto actual para ayudar a las personas enfermas que no tienen medios ni apoyo para cuidar de su salud.",
         "Explicarles que las personas de la época de Jesús rechazaban a las personas enfermas porque creían que eran impuras y su enfermedad era castigo de Dios.",
         "Comentarles que el texto expresa, como enseñanza principal, que la fe, por más pequeña que sea, puede lograr milagros."
     ],
     "correcta": 1  # Clave: B
    },
    {
        "numero": 36,
     "enunciado": "En el marco de una actividad de aprendizaje, la docente se propone que los estudiantes comprendan la importancia del principio de participación de la Doctrina Social de la Iglesia para que fomenten acciones de ayuda en su comunidad. ¿Cuál de las siguientes actividades es más adecuada para ello?",
     "opciones": [
         "Pedir que comenten por qué las decisiones políticas pueden influenciar positiva o negativamente en sus comunidades. Luego, investigar propuestas políticas que hayan favorecido a las comunidades y mostrar cómo se complementan con la Iglesia.",
         "Brindar información sobre los problemas más recurrentes en el país. Luego, pedir que elaboren un escrito sobre cómo estos problemas han afectado a la sociedad peruana y señalar qué aspectos se relacionan con el principio de participación.",
         "Pedir que señalen las problemáticas que hay al interior de sus comunidades. Luego, solicitar que analicen las causas y consecuencias del problema de mayor incidencia e indicarles que expliquen si consideran que la puesta en práctica del principio de participación podría contribuir a afrontarlo."
     ],
     "correcta": 2  # Clave: C
    },
    {
        "numero": 37,
     "enunciado": "De acuerdo con la perspectiva del enfoque inclusivo, ¿cuál de las siguientes propuestas es más pertinente para que los estudiantes con ceguera participen significativamente en las sesiones de clase?",
     "opciones": [
         "Indagar sobre las preferencias de los estudiantes en cuanto a la presentación o el formato de la información (si quieren que alguien les lea o leer en Braille) para que accedan a la misma información que sus compañeros.",
         "Asignar a un estudiante que asista a los estudiantes con ceguera durante las actividades de lectura para que sientan siempre el apoyo de sus compañeros y aumente su confianza.",
         "Darles una explicación general sobre el contenido antes de una lectura grupal para evitar que se enfrenten con muchas dificultades y mantener el ritmo de sus compañeros."
     ],
     "correcta": 0  # Clave: A
    },
        {
        "numero": 38,
        "enunciado": "Como parte del análisis de la oración del 'Padre Nuestro', un equipo presentó un organizador gráfico relacionando frases (ej. 'venga a nosotros tu reino') con significados doctrinales. ¿Qué aprendizaje se evidencia principalmente a través de este organizador gráfico?",
        "opciones": [
            "Identifica la estructura de la oración del 'Padre Nuestro'.",
            "Identifica el mensaje central de la oración del 'Padre Nuestro'.",
            "Identifica las enseñanzas contenidas en la oración del 'Padre Nuestro'."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 39,
        "enunciado": "Después de interpretar el mensaje de la oración del 'Padre Nuestro', los estudiantes comentan sobre la actividad. ¿Cuál de los siguientes estudiantes evidencia un conflicto cognitivo?",
        "opciones": [
            "Pedro dice: 'Durante la interpretación me fue difícil comprender Venga a nosotros tu reino. Pero, con ayuda del Catecismo y comentarios bíblicos, pude comprender el significado'.",
            "Juan dice: 'Yo pude comprender el significado de la oración porque la relacioné con las enseñanzas de algunos textos bíblicos...'",
            "María dice: 'Al analizar la oración, encontré que dice que Dios es santo. Pero, Él es un dios, no un santo. Únicamente a un dios se le adora, mientras que a un santo solo se le venera. Tal vez, en la traducción se cambió el significado...'"
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 40,
        "enunciado": "Después de la lectura del 'Padre Nuestro', la docente busca que los estudiantes reconozcan algunas características de la oración cristiana. ¿Cuál de las siguientes actividades es más adecuada para dicho propósito?",
        "opciones": [
            "Solicitarles que lean el apartado 'La oración en la vida cristiana' del Catecismo (N.º 2558 al 2565). Luego, explicar por qué la oración es un don de Dios y elaborar recomendaciones sobre la disposición del cristiano al orar.",
            "Decirles que describan cómo aprendieron a orar y cuáles fueron las primeras oraciones que aprendieron para que compartan en qué situaciones suelen emplearlas.",
            "Indicarles que lean el texto 'Orar sin desanimarse' (Lucas 18, 1-8), identifiquen los personajes y expliquen qué aprendizaje para sus vidas extraen de la viuda."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 41,
        "enunciado": "Durante una reunión colegiada, los docentes dialogan sobre cómo evaluar y retroalimentar durante las sesiones. ¿Cuál de las siguientes sugerencias formula una propuesta explícitamente alineada con la evaluación formativa?",
        "opciones": [
            "María dice: 'Para verificar que están logrando los aprendizajes, les indicaré desde el inicio las características del producto final. Se les calificará según un criterio estándar para evitar subjetividades'.",
            "Marta dice: 'Tras la implementación de una actividad, elaboraré una prueba escrita para conocer el nivel del logro e identificar las fortalezas y aspectos por mejorar en las siguientes sesiones'.",
            "Pedro dice: 'Durante las actividades, me acercaré a los estudiantes para verificar si han comprendido el propósito de la tarea. Así, podré comprobar su avance o si debo reorientar la actividad para darles más herramientas'."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 42,
        "enunciado": "El docente tiene como propósito que los estudiantes comprendan el mensaje de la parábola 'Los trabajadores de la viña' (Mateo 20, 1-16). ¿Cuál de las siguientes acciones pedagógicas es más adecuada para lograrlo?",
        "opciones": [
            "Pedir que expliquen en equipos el significado de la frase '¿O será porque soy generoso y tú envidioso?' e identifiquen las coincidencias en plenaria.",
            "Pedir que lean en los comentarios del contexto bíblico el significado de la frase 'Los últimos serán primeros...' y busquen otros textos similares.",
            "Pedir que identifiquen a quién representa el propietario, la viña y el salario, así como el simbolismo de los primeros y últimos trabajadores. Luego, interpretar la frase 'Yo quiero dar al último lo mismo que a ti'."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 43,
        "enunciado": "Teniendo en cuenta el fragmento de 'Los trabajadores de la viña' donde el dueño defiende su generosidad frente al reclamo de los primeros trabajadores, el docente busca un texto bíblico cuyo mensaje principal sea similar. ¿Cuál texto favorece más este propósito?",
        "opciones": [
            "El texto en el que Jesús, crucificado, habla con el ladrón arrepentido y le dice: 'En verdad te digo que hoy mismo estarás conmigo en el paraíso'.",
            "El texto en el que Jesús conversa con un joven rico y le comenta: 'Si quieres ser perfecto, vende todo lo que posees y reparte el dinero entre los pobres...'.",
            "El texto en el que Jesús narra una parábola que culmina con la frase: 'Átenlo de pies y manos, y échenlo en las tinieblas... Porque muchos son los llamados, y pocos los escogidos'."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 44,
        "enunciado": "Un docente pide a los estudiantes que indiquen qué creencia tienen en común el cristianismo, el islam y el judaísmo. ¿Qué estudiante identifica una creencia correcta común entre estas tres religiones?",
        "opciones": [
            "Ana dice: 'La creencia que tienen en común es que Dios busca tener una relación personal con los seres humanos'.",
            "Bruno dice: 'A mí me parece que lo que tienen en común es la creencia de que se salvarán las personas que hagan buenas obras sean creyentes o no'.",
            "Carlos dice: 'Creo que las tres coinciden en que Dios se presenta ante la humanidad a través de su creación'."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 45,
        "enunciado": "Ante la confusión de un estudiante por el texto literal de Lucas 14, 25-35 ('Si no dejo a mis padres y a mis hermanos no puedo ser su discípulo'), la docente busca orientarlos sobre cómo interpretar esta frase. ¿Cuál actividad es más pertinente?",
        "opciones": [
            "Indicarles que dialoguen sobre las actividades de los apóstoles para difundir las enseñanzas, los sacrificios identificados y el contexto político-religioso de la época.",
            "Explicarles que los textos no deben ser interpretados de manera literal y deben analizarse considerando su contexto, comentando las circunstancias en que Jesús lo dijo para que deduzcan a qué se refería.",
            "Solicitarles que busquen en el Catecismo información sobre el primer y cuarto mandamiento, contrastando por qué amar a Dios sobre todas las cosas antecede a honrar padre y madre."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 46,
        "enunciado": "Después de leer la parábola 'El juicio final' (Mateo 25, 31-46), la docente se propone que comprendan su mensaje. ¿Cuál de las siguientes acciones pedagógicas es más adecuada para el logro de este propósito?",
        "opciones": [
            "Presentar y explicar el significado de las obras de misericordia corporales y espirituales, para luego pedir que relacionen las acciones del texto con dichas obras.",
            "Pedir que, en equipos, dialoguen sobre a quiénes se refiere la parábola (Rey, ovejas, chivos) y analicen por qué Jesús se identifica con 'los más pequeños', quienes fueron destituidos de su propia dignidad.",
            "Pedir que expliquen el significado literal de dar de comer, beber y recibir en casa, señalando acciones de cómo ponerlo en práctica en su entorno."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 47,
        "enunciado": "Tras identificar el mensaje de 'El juicio final', la docente se propone que los estudiantes comprendan la importancia de las obras de misericordia. ¿Cuál de las siguientes actividades es más adecuada?",
        "opciones": [
            "Pedirles que analicen el significado de la frase referida a la segunda venida del Hijo del Hombre y explicar qué pide Jesús para entrar al Reino de los Cielos.",
            "Pedirles que comenten qué es la misericordia para ellos, analicen las enseñanzas que brinda la Iglesia católica en el Catecismo sobre las obras de misericordia y expliquen por qué a quienes las practican se les permitirá tomar posesión del Reino.",
            "Pedirles que expliquen el significado de 'Vengan, benditos de mi Padre...' y preguntarles si conocen otras acciones diferentes a las obras de misericordia para acceder al Reino."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 48,
        "enunciado": "Una estudiante pregunta por qué su Biblia tiene comentarios debajo de los textos bíblicos. ¿Qué acción pedagógica es más adecuada para que comprenda la importancia de los comentarios del contexto bíblico?",
        "opciones": [
            "Pedirle que explique a quiénes representan los Magos en Mateo 2, 1-12 y contrastar sus hallazgos iniciales con el simbolismo técnico descrito en las notas de pie de página.",
            "Pedirle que lea los comentarios del contexto bíblico de 'Del Oriente vienen unos Magos' y explicar si, leyendo solo el texto, habría identificado su relación con el nacimiento de Moisés, evaluando qué otros datos aportan.",
            "Pedirle que busque directamente el mensaje del texto en las notas, explicar las dificultades de interpretar la Biblia de forma aislada e investigar qué iglesias usan dichos comentarios."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 49,
        "enunciado": "Una docente organiza un proyecto de ayuda al comedor de la comunidad para promover la práctica de las enseñanzas de Jesús. ¿Cuál de las siguientes actividades favorece más este propósito?",
        "opciones": [
            "Pedir que expliquen por qué apoyar comedores populares sigue el mensaje de Jesús, investigar el incentivo de la Iglesia a estas organizaciones y leer Fratelli Tutti.",
            "Pedir que lean 'El primer milagro, en la boda de Caná', describir la actitud de Jesús ante el pedido de su madre y explicar cómo aplicar esa disposición en el comedor.",
            "Pedir que lean 'Primera multiplicación de los panes' (Mateo 14, 13-21) para comentar las actitudes de Jesús al brindar alimento. Luego, indagar las necesidades reales del comedor cercano a la IE y elaborar una propuesta concreta basada en su ejemplo."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 50,
        "enunciado": "En una sesión sobre la promoción de la paz, la docente presenta un pasaje de Fratelli Tutti ('Dios no mira con los ojos, Dios mira con el corazón...'). ¿Cuál acción pedagógica es más adecuada para orientar la comprensión del pasaje?",
        "opciones": [
            "Pedir que lean 'Jesús y Zaqueo' (Lucas 19, 1-10), comenten por qué Jesús lo escogió para comer con él, dialoguen sobre el amor de Dios sin importar la religión (o si es ateo) y relacionen ambos textos.",
            "Pedir que lean la parábola 'El hijo pródigo' para comentar la actitud del padre al regreso de su hijo, buscando la relación conceptual con mirar con el corazón.",
            "Pedir que lean el texto 'La ofrenda de la viuda' para identificar su mensaje y argumentar si este contribuye a que las religiones construyan un camino de paz."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 51,
        "enunciado": "Tras identificar el mensaje de 'El trigo y la hierba mala', la docente propone leer la parábola 'La red' (Mateo 13, 47-50) para hallar similitudes. ¿Cuál acción es más pertinente?",
        "opciones": [
            "Pedirles que señalen las ideas principales y comenten qué simboliza el tiempo de cosecha en una y la acción de recoger peces en otra, deduciendo qué comunican sobre el juicio final.",
            "Indicarles que expliquen por qué una parábola usa plantas y la otra usa peces como símbolos para detallar las características del Reino de Dios.",
            "Decirles que busquen entre otras parábolas del Reino cuál se parece más a cada una de las dos propuestas y sustentar la similitud de forma escrita."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 52,
        "enunciado": "La docente busca que los estudiantes analicen la influencia del contexto político-religioso en la misión de Jesús utilizando textos bíblicos. ¿Cuál acción es la más adecuada?",
        "opciones": [
            "Leer y analizar 'La mujer adúltera' (Juan 8, 1-11), interpretar la frase 'El que esté libre de pecado, que tire la primera piedra' y explicar por qué los acusadores se retiraron.",
            "Pedir que analicen 'Siete maldiciones contra los fariseos' (Mateo 23, 13-39) en equipos para señalar las características de los líderes fariseos y las razones de Jesús para cuestionarlos.",
            "Entregarles un texto histórico sobre los conflictos entre líderes de comunidades judías bajo el Imperio Romano. Luego, leer 'El impuesto debido al César' (Mateo 22, 15-22) para identificar las motivaciones de los grupos para probar a Jesús y explicar la intención de estas interacciones."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 53,
        "enunciado": "Una docente tiene como propósito desarrollar una actividad que promueva el diálogo ecuménico entre los estudiantes. ¿Cuál de las siguientes actividades favorece más ello?",
        "opciones": [
            "Presentar las creencias de diferentes iglesias cristianas, proponer que lean 'El buen samaritano' en equipos y preguntar si el mensaje de dicha parábola contiene las mismas enseñanzas para todas las iglesias.",
            "Comentar las posturas de diferentes iglesias cristianas sobre el uso de imágenes, comparar las ideas de cada una y solicitarles que expliquen si están de acuerdo según su propia confesión.",
            "Solicitar que investiguen las creencias de las principales confesiones cristianas en el Perú, comparar en equipos los hallazgos e indicar cuáles son las principales diferencias identificadas."
        ],
        "correcta": 0  # Clave: A
    },
    {
        "numero": 54,
        "enunciado": "La docente ha pedido que analicen la parábola 'El banquete de bodas' mediante la aplicación del método histórico-crítico. ¿Cuál de los siguientes textos escritos por los estudiantes aplica correctamente el paso inicial?",
        "opciones": [
            "Un texto que relaciona la parábola con 'La red' centrándose en la separación de buenos y malos y la advertencia general de estar preparados para el Reino de Dios.",
            "Un texto que describe que el relato fue un impacto para quienes se creían elegidos, detalla el contexto de las bodas judías donde se entregaban las túnicas y concluye que el hombre rechazó ponérsela.",
            "Un texto que explica que la parábola recrea de forma mística la boda entre Jesús y la humanidad, donde todos los humildes están invitados a la mesa final."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 55,
        "enunciado": "Los estudiantes dialogaron sobre Mateo 5, 9 ('Felices los que trabajan por la paz...'). El docente busca que elaboren compromisos que incorporen estrategias para buscar la paz en su vida diaria. ¿Cuál actividad es más adecuada?",
        "opciones": [
            "Indicar que lean en el Catecismo los comentarios sobre el tema de la paz, señalar las ideas principales y proponerles diversas formas de ponerla en práctica.",
            "Pedir que señalen personajes de la Iglesia que han trabajado por soluciones pacíficas a conflictos, dialogar sobre cómo actúan según la bienaventuranza e investigar a otros personajes.",
            "Solicitar que comenten noticias de campañas mundiales por la paz, organizar un debate sobre qué acciones serían eficientes en su comunidad según la bienaventuranza y presentar actividades concretas basadas en ello."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 56,
        "enunciado": "Un docente busca que los estudiantes elaboren su proyecto de vida cristiana tomando como base las enseñanzas de 'Las bienaventuranzas' (Mateo 5, 1-12). ¿Cuál actividad es más adecuada?",
        "opciones": [
            "Solicitar que expliquen el contexto en que Jesús proclamó las bienaventuranzas, señalar cómo respondía al entorno social de la época y debatir si se puede aplicar en la actualidad.",
            "Pedir que dialoguen en equipos sobre el significado de cada bienaventuranza, seleccionen algunas para proponer ejemplos prácticos de su entorno y elaboren un plan de seguimiento para comprometerse con ellos.",
            "Brindar un texto con la catequesis del Papa Francisco sobre las bienaventuranzas, extraer las ideas principales y preguntar cuál les parece más importante para la vida cristiana."
        ],
        "correcta": 1  # Clave: B
    },
        {
        "numero": 57,
        "enunciado": "Un docente busca planificar una sesión que promueva el pensamiento crítico en los estudiantes mediante el análisis de textos doctrinales. De acuerdo con las orientaciones pedagógicas del Currículo Nacional (Minedu), ¿cuál de las siguientes acciones es más adecuada para este propósito?",
        "opciones": [
            "Presentar un resumen elaborado por expertos sobre la postura oficial de la Iglesia y pedir que lo memoricen.",
            "Plantear preguntas abiertas que cuestionen los supuestos del texto, promuevan la argumentación propia y conecten el mensaje con problemáticas éticas de su entorno actual.",
            "Solicitar que copien textualmente los versículos clave del fragmento analizado y resalten con diferentes colores las palabras desconocidas."
        ],
        "correcta": 1  # Clave: B
    },
    {
        "numero": 58,
        "enunciado": "Durante el desarrollo de un proyecto de aprendizaje sobre solidaridad comunitaria, el docente realiza una evaluación formativa constante. ¿Qué instrumento y uso es el más adecuado según el enfoque del Minedu para registrar el progreso de las competencias?",
        "opciones": [
            "Aplicar un examen escrito acumulativo sorpresa al final de cada semana para registrar notas cuantitativas definitivas.",
            "Publicar la lista de alumnos con menor rendimiento en la pizarra del aula para incentivar la competencia interna del grupo.",
            "Utilizar una rúbrica analítica explícita compartida previamente con los estudiantes, aplicando notas de campo y retroalimentación oportuna durante el proceso para ajustar las estrategias de aprendizaje."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 59,
        "enunciado": "Para generar un verdadero aprendizaje significativo al introducir la temática de las parábolas de la misericordia, ¿cuál de las siguientes secuencias didácticas es más pertinente en el inicio de la sesión?",
        "opciones": [
            "Pedir que busquen definiciones técnicas del término 'misericordia' en diccionarios teológicos oficiales antes de empezar.",
            "Dictar una breve introducción histórica sobre el contexto social y geográfico del pueblo de Israel en el siglo I d.C.",
            "Recoger las experiencias vividas o presenciadas por los estudiantes sobre situaciones reales de perdón y reconciliación dentro de sus familias o la escuela, abriendo un espacio de diálogo."
        ],
        "correcta": 2  # Clave: C
    },
    {
        "numero": 60,
        "enunciado": "Teniendo en cuenta los enfoques transversales del Currículo Nacional, el docente busca abordar la interculturalidad en el área de Educación Religiosa. ¿Qué acción pedagógica evidencia mejor la puesta en práctica de este enfoque?",
        "opciones": [
            "Reconocer y valorar con respeto las diversas expresiones y manifestaciones de fe de las comunidades andinas, amazónicas y costeñas del Perú, dialogando sobre sus puntos de encuentro con los valores del Evangelio.",
            "Indicar a los estudiantes que provienen de diferentes regiones del país que deben homogeneizar sus costumbres religiosas bajo un único modelo litúrgico estándar.",
            "Evitar tocar cualquier tema que involucre tradiciones o costumbres locales de las regiones para no generar debates ni desacuerdos dentro del aula de clase."
        ],
        "correcta": 0  # Clave: A
    }

]

# Inicializar variables de estado para el control de páginas y almacenamiento de respuestas
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}
if "pagina" not in st.session_state:
    st.session_state.pagina = 0

PREGUNTAS_POR_PAGINA = 5
total_paginas = (len(banco_preguntas) - 1) // PREGUNTAS_POR_PAGINA + 1
inicio = st.session_state.pagina * PREGUNTAS_POR_PAGINA
fin = min(inicio + PREGUNTAS_POR_PAGINA, len(banco_preguntas))

st.sidebar.markdown(f"### 📋 Progreso")
st.sidebar.markdown(f"Página **{st.session_state.pagina + 1}** de **{total_paginas}**")

# Mostrar bloque de preguntas de la página actual
for idx in range(inicio, fin):
    p = banco_preguntas[idx]
    st.markdown(f"#### ❓ Pregunta {p['numero']}")
    st.write(p["enunciado"])
    
    # Buscar índice guardado previamente si existe
    valor_previo = st.session_state.respuestas.get(idx, None)
    
    opcion_seleccionada = st.radio(
        "Selecciona tu respuesta:",
        p["opciones"],
        index=p["opciones"].index(valor_previo) if valor_previo in p["opciones"] else None,
        key=f"preg_{idx}",
        label_visibility="collapsed"
    )
    if opcion_seleccionada:
        st.session_state.respuestas[idx] = opcion_seleccionada
    st.markdown("---")

# Botones de navegación en la parte inferior
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.pagina > 0:
        if st.button("⬅️ Anterior"):
            st.session_state.pagina -= 1
            st.rerun()

with col3:
    if st.session_state.pagina < total_paginas - 1:
        if st.button("Siguiente ➡️"):
            st.session_state.pagina += 1
            st.rerun()

# Botón de finalización en la última página
if st.session_state.pagina == total_paginas - 1:
    if st.button("🏁 Terminar Examen y Ver Nota", type="primary"):
        if len(st.session_state.respuestas) < len(banco_preguntas):
            st.warning("⚠️ No has respondido todas las preguntas. Por favor revisa las páginas anteriores.")
        else:
            # Procesamiento de calificaciones
            buenas = 0
            st.markdown("### 📊 Reporte Final de Resultados")
            
            for idx, p in enumerate(banco_preguntas):
                correcta_str = p["opciones"][p["correcta"]]
                elegida_str = st.session_state.respuestas.get(idx, "")
                
                if elegida_str == correcta_str:
                    buenas += 1
                    st.success(f"✅ **Pregunta {p['numero']}: Correcta.** Respondiste la opción esperada.")
                else:
                    st.error(f"❌ **Pregunta {p['numero']}: Incorrecta.** Tu respuesta: '{elegida_str}'. La respuesta correcta era: '{correcta_str}'")
            
            # Nota calculada sobre escala estándar de 20 puntos
            nota_vigesimal = (buenas / len(banco_preguntas)) * 20
            st.markdown("---")
            st.metric(label="Tu Calificación Final", value=f"{nota_vigesimal:.2f} / 20.0", delta=f"{buenas} acertadas")
            
            # Mensajes personalizados de logro según escalas magisteriales
            if buenas >= 46:
                st.balloons()
                st.success("🎉 ¡Excelente rendimiento! Apto para clasificar hasta la Octava Escala Magisterial.")
            elif buenas >= 36:
                st.success("👍 ¡Aprobado! Cumples el puntaje mínimo para las primeras escalas magisteriales.")
            else:
                st.warning("⚠️ Tu puntaje está por debajo de los requerimientos mínimos de clasificación. ¡Sigue practicando!")
