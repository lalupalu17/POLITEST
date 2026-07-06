## PoliTest - Descubre Qué Polinesio Eres

### Descripción del Proyecto
Este es un divertido test de personalidad interactivo que te ayuda a descubrir cuál de los famosos Polinesios (Rafael, Karen o Lesslie) resuena más con tu forma de ser. A través de una serie de 35 preguntas con opciones múltiples, el programa calcula un puntaje basado en tus respuestas y te presenta un resultado personalizado. Cada resultado incluye una descripción detallada de la personalidad del Polinesio asignado y una imagen representativa.

### Características
*   **Test Interactivo**: 35 preguntas diseñadas para explorar diferentes aspectos de tu personalidad.
*   **Validación de Entrada**: Incluye una función `pedir_respuesta()` para asegurar que las respuestas sean números válidos (1, 2 o 3).
*   **Resultados Personalizados**: Basado en la suma de tus respuestas, el test te asigna a uno de los tres Polinesios.
*   **Descripciones Detalladas**: Cada resultado viene acompañado de una descripción de la personalidad que se alinea con Rafael, Karen o Lesslie.
*   **Visualización**: Muestra una imagen del Polinesio correspondiente al resultado final.

### Cómo Ejecutar el Código
Para correr este test en tu entorno local (o en Google Colab):

1.  **Instalar Dependencias**: Asegúrate de tener Python instalado. Necesitarás las librerías `Pillow` (para manejar imágenes) y `requests` (para descargar imágenes de internet). Puedes instalarlas usando `pip`:
    ```bash
    pip install Pillow requests
    ```
2.  **Copiar el Código**: Copia todo el código del test en un archivo Python (por ejemplo, `politest.py`) o ejecútalo directamente en un entorno como Google Colab.
3.  **Ejecutar**: Abre tu terminal o consola y navega hasta el directorio donde guardaste el archivo. Luego, ejecuta el script:
    ```bash
    python politest.py
    ```
    Si estás en Google Colab, simplemente ejecuta todas las celdas del notebook.

4.  **Interactuar**: El programa te irá mostrando las preguntas. Ingresa el número correspondiente a tu respuesta (1, 2 o 3) y presiona Enter.

### Dependencias
*   `PIL` (Pillow)
*   `requests`
*   `IPython.display` (para mostrar imágenes en entornos como Colab/Jupyter)

### Limitaciones y Posibles Mejoras

*   **Problemas con Rutas de Imágenes Locales**: Las líneas `imagen_karen = Image.open("/karenpolinesio.jpg")` e `imagen_leslie = Image.open("/lesliepolinesia.jpg")` intentan cargar imágenes desde rutas absolutas locales (`/karenpolinesio.jpg`, `/lesliepolinesia.jpg`). Esto causará un `FileNotFoundError` a menos que esos archivos existan exactamente en esas ubicaciones en el sistema de archivos donde se ejecuta el código. Las imágenes de resultado (`foto_rafa`, `foto_karen`, `foto_less`) se cargan correctamente desde URLs, lo cual es una mejor práctica.
    *   **Mejora Sugerida**: Eliminar las líneas de carga de imágenes locales innecesarias o asegurarse de que todas las imágenes se carguen de manera consistente (por ejemplo, todas desde URLs o todas gestionadas como archivos locales incluidos en el proyecto).

*   **Validación de Entrada**: La función `pedir_respuesta()` es útil, pero el mensaje de error para `ValueError` ("Respuesta no válida. Debes ingresar un número del 1 al 3") es un poco genérico y podría ser más específico para diferenciar entre entradas no numéricas y números fuera de rango.
    *   **Mejora Sugerida**: Personalizar los mensajes de error para indicar si la entrada no es un número o si está fuera del rango permitido.

*   **Rango de Suma para Karen**: El rango para Karen es `59 < suma <= 81`. Si el valor de `suma` fuera exactamente `59`, no caería en ninguna de las condiciones `if/elif`. Aunque con las respuestas de 1 a 3 es menos probable, por robustez, el rango debería ser `59 <= suma <= 81`.
    *   **Mejora Sugerida**: Ajustar el rango a `59 <= suma <= 81` para cubrir el límite inferior.

*   **Modularidad y Escalabilidad**: Las preguntas están codificadas directamente en el script. Si se quisieran añadir o modificar preguntas frecuentemente, esto podría volverse tedioso.
    *   **Mejora Sugerida**: Almacenar las preguntas y sus opciones en una estructura de datos (como una lista de diccionarios) o en un archivo externo (JSON, CSV) para facilitar la administración y escalabilidad del test.
