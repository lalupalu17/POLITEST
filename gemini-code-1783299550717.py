import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Configuración del título de la página web
st.title("¡Hola Polinesios! ¿Cómo están?")
st.subheader("Bienvenidos al PoliTest, donde descubrirás qué polinesio eres en base a tu personalidad :)")

# --- CARGA DE IMÁGENES DESDE INTERNET ---
link_rafa = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcU8LpRGXHs8XasZjgZpZxrbMgaGD1Lr2_TPtoBjGMMU99qavdGz7pPxc&s=10"
link_karen = "https://static.wikia.nocookie.net/wiki-random/images/6/6f/50b5682a0bf73c375857bfc030f0ff747db9dc94_00.jpg/revision/latest?cb=20180703003459&path-prefix=es"
link_less = "https://i.pinimg.com/736x/54/26/de/5426de3c1929269521bb22deeb4032a2.jpg"

@st.cache_data
def cargar_imagenes():
    try:
        foto_rafa = Image.open(BytesIO(requests.get(link_rafa).content))
        foto_karen = Image.open(BytesIO(requests.get(link_karen).content))
        foto_less = Image.open(BytesIO(requests.get(link_less).content))
        return foto_rafa, foto_karen, foto_less
    except:
        st.error("Error al cargar las imágenes desde internet.")
        return None, None, None

foto_rafa, foto_karen, foto_less = cargar_imagenes()

# Función auxiliar para simular el valor de la respuesta (1, 2 o 3) según el índice seleccionado
def calcular_puntos(pregunta, opciones):
    return opciones.index(pregunta) + 1

# --- FORMULARIO DEL TEST ---
with st.form("politest_form"):
    st.write("Responde a todas las preguntas y presiona el botón al final para ver tu resultado.")
    
    p1 = st.radio("1) ¿Cuál es tu color favorito?", ["Verde", "Morado", "Rosado"])
    p2 = st.radio("2) ¿Te consideras una persona sensible?", ["De vez en cuando", "No", "Sí"])
    p3 = st.radio("3) ¿Quién te consideras en tu grupo de amigos?", ["El funable", "El directo o consejero", "El cariñoso"])
    p4 = st.radio("4) ¿Qué prefieres hacer en tu cumpleaños?", ["Ir de viaje", "Planificar con tiempo lo que deseo", "Sorpresa preparada por mis seres queridos"])
    p5 = st.radio("5) Si pudieras vivir en uno de los siguientes países ¿cuál sería?", ["Japón", "Inglaterra", "Estados Unidos"])
    p6 = st.radio("6) ¿Qué tipo de slime prefieres?", ["De detergente", "De crema para afeitar", "De pegamento con borax"])
    p7 = st.radio("7) ¿Te gustaría tener hijos?", ["Sí, con una gran familia", "No lo tengo entre mis planes", "Sí, una familia tradicional"])
    p8 = st.radio("8) ¿Qué películas prefieres ver?", ["Comedia", "Terror", "Drama romántico"])
    p9 = st.radio("9) En el salón de clases ¿Quién eres?", ["El payaso", "El dormilón", "El aplicado"])
    p10 = st.radio("10) ¿Alguna vez te has obsesionado tanto con una canción que la cantas por semanas?", ["Solo con canciones en específico", "No", "Sí, siempre me sucede"])
    p11 = st.radio("11) ¿Qué rol tomas en los viajes?", ["Quién busca actividades para divertirse", "Quien solo se guía por sus acompañantes", "Quien organiza el itinerario y presupuestos"])
    p12 = st.radio("12) ¿Qué regalo prefieres recibir?", ["Algo inesperado y gracioso", "Algo útil", "Algo significativo y sentimental"])
    p13 = st.radio("13) ¿Qué haces cuando alguien te cuenta un problema?", ["Intento hacerlo reír", "Le doy consejos y soluciones", "Lo escucho y le doy apoyo emocional"])
    p14 = st.radio("14) ¿Qué tan puntuable eres?", ["Lego justo a la hora", "Llego tarde", "Siempre llego antes de tiempo"])
    p15 = st.radio("15) ¿Qué red social utilizas más?", ["Tiktok", "Instagram", "Twitter"])
    p16 = st.radio("16) Cuando te gusta alguien...", ["Huyo", "Se lo digo de frente", "Me pongo nervios@"])
    p17 = st.radio("17) ¿Qué genero musical prefieres?", ["Reggeaton", "Rock", "Pop"])
    p18 = st.radio("18) ¿Qué tan ordenado eres?", ["Medianamente ordenado", "Para nada ordenado", "Muy ordenado"])
    p19 = st.radio("19) ¿Cuál es tu comida favorita?", ["Hamburguesa", "Pizza", "Sushi"])
    p20 = st.radio("20) ¿Qué tan romantico eres?", ["Normal", "Poco", "Muchísimo"])
    p21 = st.radio("21) ¿Cuál es tu estación favorita?", ["Verano", "Invierno/Otoño", "Primavera"])
    p22 = st.radio("22) ¿Qué tan llorón eres?", ["Poco", "Casi nada", "Mucho"])
    p23 = st.radio("23) Si tuvieras un superpoder, ¿cuál eligirías?", ["Leer mentes", "Supervelocidad", "Curar personas"])
    p24 = st.radio("24) ¿Cuál es tu bebida favorita?", ["Gaseosa", "Té", "Agua"])
    p25 = st.radio("25) ¿Qué gastronomía es tu favorita?", ["Japonesa", "Peruana", "Mexicana"])
    p26 = st.radio("26) ¿Cuál sería tu trabajo soñado?", ["Influencer", "Empresario", "Artista"])
    p27 = st.radio("27) ¿Cómo gastas tu dinero?", ["Lo invierto", "Lo ahorro", "Lo gasto sin pensar"])
    p28 = st.radio("28) ¿Te consideras una persona más lógica o más emocional?", ["Un poco de ambos", "Lógica", "Emocional"])
    p29 = st.radio("29) ¿Cómo prefieres recargar tu energía después de un día cansado?", ["Meditación", "Dormir", "Ejercitarme"])
    p30 = st.radio("30) ¿En qué momento del día prefieres hacer las cosas?", ["En la tarde", "En la noche", "En la mañana"])
    p31 = st.radio("31) Si fueses un animal ¿cuál serías?", ["Perro", "Gato", "Conejo"])
    p32 = st.radio("32) ¿Sueles enfadarte con facilidad?", ["Depende de la situación", "No", "Sí"])
    p33 = st.radio("33) Para tí, ¿qué es el arte?", ["Cualquier creación propia sin importar el significado", "Una forma compleja de expresar nuestra identidad", "Un balance entre la realidad y la fantasía"])
    p34 = st.radio("34) ¿Con quién de tu familia sueles apoyarte más?", ["Madre", "Padre", "Hermanos"])
    p35 = st.radio("35) ¿Cuál es tu polinesio favorito?", ["Rafael", "Karen", "Lesslie"])

    # El botón de envío obligatorio para procesar el formulario completo
    enviado = st.form_submit_button("¡Descubrir mi Polinesio!")

# --- PROCESAMIENTO DEL RESULTADO ---
if enviado:
    suma = (
        calcular_puntos(p1, ["Verde", "Morado", "Rosado"]) +
        calcular_puntos(p2, ["De vez en cuando", "No", "Sí"]) +
        calcular_puntos(p3, ["El funable", "El directo o consejero", "El cariñoso"]) +
        calcular_puntos(p4, ["Ir de viaje", "Planificar con tiempo lo que deseo", "Sorpresa preparada por mis seres queridos"]) +
        calcular_puntos(p5, ["Japón", "Inglaterra", "Estados Unidos"]) +
        calcular_puntos(p6, ["De detergente", "De crema para afeitar", "De pegamento con borax"]) +
        calcular_puntos(p7, ["Sí, con una gran familia", "No lo tengo entre mis planes", "Sí, una familia tradicional"]) +
        calcular_puntos(p8, ["Comedia", "Terror", "Drama romántico"]) +
        calcular_puntos(p9, ["El payaso", "El dormilón", "El aplicado"]) +
        calcular_puntos(p10, ["Solo con canciones en específico", "No", "Sí, siempre me sucede"]) +
        calcular_puntos(p11, ["Quién busca actividades para divertirse", "Quien solo se guía por sus acompañantes", "Quien organiza el itinerario y presupuestos"]) +
        calcular_puntos(p12, ["Algo inesperado y gracioso", "Algo útil", "Algo significativo y sentimental"]) +
        calcular_puntos(p13, ["Intento hacerlo reír", "Le doy consejos y soluciones", "Lo escucho y le doy apoyo emocional"]) +
        calcular_puntos(p14, ["Lego justo a la hora", "Llego tarde", "Siempre llego antes de tiempo"]) +
        calcular_puntos(p15, ["Tiktok", "Instagram", "Twitter"]) +
        calcular_puntos(p16, ["Huyo", "Se lo digo de frente", "Me pongo nervios@"]) +
        calcular_puntos(p17, ["Reggeaton", "Rock", "Pop"]) +
        calcular_puntos(p18, ["Medianamente ordenado", "Para nada ordenado", "Muy ordenado"]) +
        calcular_puntos(p19, ["Hamburguesa", "Pizza", "Sushi"]) +
        calcular_puntos(p20, ["Normal", "Poco", "Muchísimo"]) +
        calcular_puntos(p21, ["Verano", "Invierno/Otoño", "Primavera"]) +
        calcular_puntos(p22, ["Poco", "Casi nada", "Mucho"]) +
        calcular_puntos(p23, ["Leer mentes", "Supervelocidad", "Curar personas"]) +
        calcular_puntos(p24, ["Gaseosa", "Té", "Agua"]) +
        calcular_puntos(p25, ["Japonesa", "Peruana", "Mexicana"]) +
        calcular_puntos(p26, ["Influencer", "Empresario", "Artista"]) +
        calcular_puntos(p27, ["Lo invierto", "Lo ahorro", "Lo gasto sin pensar"]) +
        calcular_puntos(p28, ["Un poco de ambos", "Lógica", "Emocional"]) +
        calcular_puntos(p29, ["Meditación", "Dormir", "Ejercitarme"]) +
        calcular_puntos(p30, ["En la tarde", "En la noche", "En la mañana"]) +
        calcular_puntos(p31, ["Perro", "Gato", "Conejo"]) +
        calcular_puntos(p32, ["Depende de la situación", "No", "Sí"]) +
        calcular_puntos(p33, ["Cualquier creación propia sin importar el significado", "Una forma compleja de expresar nuestra identidad", "Un balance entre la realidad y la fantasía"]) +
        calcular_puntos(p34, ["Madre", "Padre", "Hermanos"]) +
        calcular_puntos(p35, ["Rafael", "Karen", "Lesslie"])
    )

    st.write("---")
    if 35 <= suma <= 58:
        st.header("¡Eres Rafa!")
        if foto_rafa: st.image(foto_rafa, width=400)
        st.write("Tienes una personalidad ruidosa, impulsiva y sumamente cómica, convirtiéndote siempre en el alma impredecible de cualquier grupo. Lejos de ser alguien serio, eres el más loco y desatado, el responsable de las bromas más pesadas, las ocurrencias extremas y de buscar la adrenalina en dinámicas intensas o deportes extremos. Tu estilo de humor es irreverente, directo y sin filtros, al punto de que muchas veces rozas lo polémico y te ganas la reputación de ser el más funable por decir lo que piensas sin medir las consecuencias. Eres un espíritu libre que prefiere la diversión espontánea antes que la rigidez, aportando siempre esa chispa de caos que rompe por completo con la normalidad.")
    
    elif 59 <= suma <= 81:
        st.header("¡Eres Karen!")
        if foto_karen: st.image(foto_karen, width=400)
        st.write("Tienes una personalidad sumamente auténtica, magnética y llena de contrastes fascinantes. No necesitas buscar riesgos físicos innecesarios ni te llaman la atención los deportes extremos; de hecho, eres alguien bastante dormilón que disfruta enormemente de un buen descanso. Tu verdadera fuerza radica en una mente brillante y una tremenda seguridad en ti mismo, siendo el perfil más analítico de los tres hermanos, aunque a veces tu mente procesa tantas cosas a la vez que pareces una persona un poco distraída o despistada en el día a día. Tu esencia es una mezcla única de un espíritu hippie —relajado, amante de la libertad, la paz y el arte— con una actitud punk, manteniéndote firme en tus convicciones, defendiendo tu individualidad y rompiendo con las reglas tradicionales sin temor al qué dirán.")
    
    elif 82 <= suma <= 105:
        st.header("¡Eres Lesslie!")
        if foto_less: st.image(foto_less, width=400)
        st.write("Tienes una personalidad que destaca por ser el corazón emotivo, dulce y equilibrado de tu entorno. Eres una persona sumamente sensible y empática, capaz de construir vínculos de confianza profundos y cercanos con los demás gracias a tu calidez y autenticidad. A pesar de tener una esencia soñadora y muy creativa, demuestras un crecimiento constante hacia la madurez, asumiendo las responsabilidades de la vida con gran sensatez y templanza. Te conviertes de forma natural en el pilar afectivo que abraza, cuida y protege a tus seres queridos, combinando esa ternura innata con una fuerza interior protectora que te hace el refugio seguro de quienes te rodean.")
    
    st.success("¡Test Finalizado!")