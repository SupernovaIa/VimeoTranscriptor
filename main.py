import os
import yt_dlp
import whisper
from tqdm import tqdm

# Definir las carpetas de trabajo
folder_audio = "audios"
folder_transcriptions = "transcriptions"
url_file = "vimeo.txt"

# Crear carpetas si no existen
os.makedirs(folder_audio, exist_ok=True)
os.makedirs(folder_transcriptions, exist_ok=True)

# Cargar el modelo Whisper
model = whisper.load_model("base")


def descargar_audio_vimeo(url, output_path):
    """Descarga solo el audio del vídeo de Vimeo y lo guarda en la ubicación especificada."""
    opciones = {
        "format": "bestaudio",
        "outtmpl": output_path,
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}]
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


def transcribir_audio(audio_path, output_text_path):
    """Transcribe el audio y guarda el resultado en un archivo de texto."""
    result = model.transcribe(audio_path)
    with open(output_text_path, "w", encoding="utf-8") as text_file:
        text_file.write(result["text"])


def procesar_urls():
    """Lee las URLs, descarga el audio, lo transcribe y lo elimina después."""
    with open(url_file, "r") as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]
    
    for url in tqdm(urls):
        print(f"\n🔽 Procesando: {url}")
        
        # Determinar el nombre del archivo de salida
        output_audio_path = os.path.join(folder_audio, "%(title)s.%(ext)s")
        descargar_audio_vimeo(url, output_audio_path)
        
        # Buscar el archivo descargado
        mp3_files = [f for f in os.listdir(folder_audio) if f.endswith(".mp3")]
        if not mp3_files:
            print(f"⚠️ No se encontró el archivo descargado para {url}")
            continue
        
        audio_file = os.path.join(folder_audio, mp3_files[0])
        output_text_path = os.path.join(folder_transcriptions, f"{os.path.splitext(mp3_files[0])[0]}.txt")
        
        # Transcribir y eliminar el audio
        transcribir_audio(audio_file, output_text_path)
        os.remove(audio_file)
        print(f"✅ Transcripción guardada y audio eliminado: {output_text_path}")

if __name__ == "__main__":
    procesar_urls()
