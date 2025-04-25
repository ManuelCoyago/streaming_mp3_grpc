import os
from pytubefix import Playlist, YouTube

# URL de la playlist de YouTube
# playlist_url = input("Introduce la URL de la playlist: ")
playlist_url = "https://www.youtube.com/watch?v=iwEnBFqgHkA&list=PLMeHLPJo-o67vXWnbSVhEez_d0FHYUFhU"

# Crear objeto Playlist con pytubefix
playlist = Playlist(playlist_url)
lista_videos = playlist.video_urls

# Seleccionamos el rango deseado: del video 100 al 200
# Recordatorio: en Python la indexación inicia en 0, por lo que [99:200] corresponde al 100° al 200°.
videos_seleccionados = lista_videos[5:10]

# Directorio donde se guardarán las descargas
output_path = "descargas"
if not os.path.exists(output_path):
    os.makedirs(output_path)


# Función para convertir un archivo descargado a wav usando ffmpeg
def convertir_a_wav(archivo_entrada):
    base, ext = os.path.splitext(archivo_entrada)
    archivo_salida = base + ".mp3"
    # Se invoca ffmpeg para extraer solo el audio y convertirlo a mp3.
    # -vn: ignora el video; -ab: bitrate del audio; -ar: frecuencia de muestreo; -y: sobrescribe sin preguntar.
    comando = f'ffmpeg -i "{archivo_entrada}" -vn -ab 192k -ar 44100 -y "{archivo_salida}"'
    resultado = os.system(comando)
    if resultado != 0:
        print(f"Error al convertir {archivo_entrada}")
    else:
        # Se elimina el archivo original, si ya no se requiere
        os.remove(archivo_entrada)
        print(f"Convertido y guardado: {archivo_salida}")


# Iteramos sobre cada video en el rango seleccionado para descargar su audio
for url in videos_seleccionados:
    try:
        yt = YouTube(url)
        # Se filtra para obtener el stream que contenga solo audio
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream is None:
            print(f"No se encontró stream de audio para {url}")
            continue

        # Descargar el archivo (el formato resultante puede ser .mp4 o .webm)
        archivo_descargado = audio_stream.download(output_path=output_path)
        print(f"Descargado: {archivo_descargado}")

        # Convertimos el archivo descargado a mp3 utilizando ffmpeg
        convertir_a_wav(archivo_descargado)

    except Exception as e:
        print(f"Error al procesar {url}: {e}")