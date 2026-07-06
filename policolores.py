# --- PERSONALIZACIÓN CON TUS COLORES ---
st.markdown(
    """
    <style>
    /* Importar una tipografía divertida y estética de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300..700&display=swap');

    /* Aplicar la tipografía y color negro a los títulos principales */
    .stApp h1, .stApp h2, .stApp h3 {
        font-family: 'Fredoka', sans-serif !important;
        color: #000000 !important; 
    }

    /* Fondo de la pantalla (#FAFAF0) */
    .stApp {
        background-color: #FAFAF0 !important;
    }

    /* Cajitas de las preguntas (#86CDEB) con texto negro (#000000) */
    div[data-testid="stForm"] div[data-testid="stVerticalBlockBorder"] {
        background-color: #86CDEB !important;
        border-radius: 15px !important;
        padding: 20px !important;
        border: none !important;
    }
    
    /* Asegurar que el texto de las preguntas dentro de las cajitas sea negro */
    div[data-testid="stForm"] p, div[data-testid="stForm"] label {
        color: #000000 !important;
        font-weight: 500 !important;
    }

    /* Botón para descubrir el resultado (#86CDEB) */
    div.stButton > button {
        background-color: #86CDEB !important; 
        color: #000000 !important; /* Texto negro para contraste */
        font-family: 'Fredoka', sans-serif !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 25px !important; 
        border: 2px solid #000000 !important; /* Borde negro sutil */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1) !important; 
        transition: 0.3s;
        width: 100% !important; 
    }

    /* Efecto al pasar el mouse por encima del botón */
    div.stButton > button:hover {
        background-color: #59B2DB !important; /* Un azul un poco más oscuro al pasar el cursor */
        border-color: #000000 !important;
        color: #000000 !important;
        transform: scale(1.01); 
    }
    </style>
    """,
    unsafe_allow_html=True
)