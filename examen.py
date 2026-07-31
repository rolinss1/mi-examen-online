import streamlit as st

# Configuración visual de la ventana
st.set_page_config(page_title="Simulador MINEDU - Ascenso 2024", page_icon="📝", layout="centered")

st.title("📝 Simulador de Examen MINEDU")
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
