# Proyecto de Descarga y Transcripción de Videos de Vimeo

Este proyecto permite descargar el audio de videos de Vimeo, transcribirlo utilizando el modelo Whisper de OpenAI y guardar la transcripción en archivos de texto.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- yt-dlp
- OpenAI Whisper
- ffmpeg
- tqdm

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install yt-dlp
```

Para instalar `openai-whisper`, puedes hacerlo mediante pip o clonar el repositorio:

```bash
pip install git+https://github.com/openai/whisper.git
```

Además, debes tener `ffmpeg` instalado. En sistemas Debian/Ubuntu, puedes instalarlo con:

```bash
sudo apt install ffmpeg
```

Para Windows, descarga e instala `ffmpeg` desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).

En macOS, puedes instalarlo con:

```bash
brew install ffmpeg
```

## Uso

1. Crea un archivo `urls.txt` y añade una URL de Vimeo por línea.
2. Ejecuta el script con:

```bash
python main.py
```

El script realizará las siguientes tareas:

1. Leer las URLs del archivo `urls.txt`.
2. Descargar el audio de cada video.
3. Transcribir el audio utilizando el modelo Whisper.
4. Guardar la transcripción en un archivo de texto en la carpeta `transcriptions`.
5. Eliminar el archivo de audio una vez transcrito.

## Estructura del Proyecto

```
/
├── audios/            # Carpeta donde se almacenan los audios descargados
├── transcriptions/    # Carpeta donde se guardan las transcripciones
├── main.py           # Script principal
├── urls.txt          # Archivo con las URLs de los videos
```

## Notas
- La transcripción se realiza utilizando el modelo `base` de Whisper. Puedes cambiar el modelo en el script (`whisper.load_model("base")`) si necesitas un modelo más preciso.
- Si hay varios audios descargados en la carpeta `audios`, el script solo procesará el primero que encuentre.
- Asegúrate de que el archivo `urls.txt` contiene URLs válidas de Vimeo.

## Licencia
Este proyecto es de código abierto y se distribuye bajo la licencia MIT.

