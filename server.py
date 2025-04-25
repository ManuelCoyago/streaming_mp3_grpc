import grpc
from concurrent import futures
import os
import soundfile as sf
import pydub
import audio_pb2
import audio_pb2_grpc
import io  # Agregar esta línea


AUDIO_DIR = "./audio_files/descargas"

class AudioService(audio_pb2_grpc.AudioServiceServicer):
    def ListFiles(self, request, context):
        files = [f for f in os.listdir(AUDIO_DIR) if f.endswith(".mp3")]
        return audio_pb2.FileList(files=files)

    def StreamAudio(self, request, context):
        filepath = os.path.join(AUDIO_DIR, request.filename)
        if not os.path.exists(filepath):
            context.set_details("File not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return

        # Convertir el archivo MP3 a PCM usando pydub
        audio = pydub.AudioSegment.from_file(filepath, format="mp3").set_frame_rate(44100).set_channels(
            2).set_sample_width(2)

        # Dividir el audio en chunks y enviarlos al cliente
        chunk_size = 1024  # Tamaño del chunk en bytes
        for i in range(0, len(audio.raw_data), chunk_size):
            chunk = audio.raw_data[i:i + chunk_size]
            yield audio_pb2.AudioChunk(data=chunk)

    def GetMetadata(self, request, context):
        filepath = os.path.join(AUDIO_DIR, request.filename)
        if not os.path.exists(filepath):
            context.set_details("File not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return

        audio = pydub.AudioSegment.from_file(filepath, format="mp3")
        return audio_pb2.Metadata(
            filename=request.filename,
            duration=audio.duration_seconds,
            sample_rate=audio.frame_rate,
            channels=audio.channels
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audio_pb2_grpc.add_AudioServiceServicer_to_server(AudioService(), server)
    server.add_insecure_port("[::]:50051")
    print("Servidor escuchando en el puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()