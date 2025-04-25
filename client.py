import grpc
import audio_pb2
import audio_pb2_grpc
import pyaudio
import time

def list_files(stub):
    response = stub.ListFiles(audio_pb2.Empty())
    return response.files

def stream_audio(stub, filename):
    request = audio_pb2.AudioRequest(filename=filename)
    return stub.StreamAudio(request)

def get_metadata(stub, filename):
    request = audio_pb2.AudioRequest(filename=filename)
    return stub.GetMetadata(request)

def play_audio(stream, audio_stream):
    for chunk in audio_stream:
        stream.write(chunk.data)

def main():
    channel = grpc.insecure_channel("localhost:50051")
    stub = audio_pb2_grpc.AudioServiceStub(channel)

    files = list_files(stub)
    if not files:
        print("No hay archivos disponibles.")
        return

    print("Archivos disponibles:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")

    choice = int(input("Selecciona un archivo para reproducir: ")) - 1
    if choice < 0 or choice >= len(files):
        print("Selección inválida.")
        return

    filename = files[choice]
    metadata = get_metadata(stub, filename)
    print(f"Reproduciendo: {metadata.filename}")
    print(f"Duración: {metadata.duration:.2f} segundos")
    print(f"Sample Rate: {metadata.sample_rate} Hz")
    print(f"Canales: {metadata.channels}")

    audio_stream = stream_audio(stub, filename)

    # Configurar pyaudio para reproducir el audio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=metadata.channels,
                    rate=metadata.sample_rate,
                    output=True)

    play_audio(stream, audio_stream)

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()