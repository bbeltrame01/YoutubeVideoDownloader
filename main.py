# Para rodar o programa é necessário possuir o 'ffmpeg' instalado.
# https://github.com/FFmpeg/FFmpeg
# FFmpeg é uma coleção de bibliotecas e ferramentas para processar conteúdo multimídia, como áudio, vídeo, legendas e metadados relacionados.
# Utilizado neste projeto para mesclar os arquivos de áudio e vídeo baixados separadamente.
from pytubefix import YouTube  # type: ignore
from pytubefix.cli import on_progress  # type: ignore
import subprocess
import os
import re

class VideoDownloader:
    def __init__(self, url: str):
        self.url = url
        self.yt = YouTube(url, on_progress_callback=on_progress)

    def download(self, only_audio=False, output_path='./'):
        if not os.path.exists(output_path):
            os.makedirs(output_path)  # Cria o diretório, caso não exista.

        if only_audio:
            self.download_audio(output_path + '/Audios')
        else:
            self.download_video(output_path + '/Videos')
    
    def download_audio(self, output_path):
        print("Baixando o áudio...")
        audio_stream = self.yt.streams.get_audio_only()
        
        if audio_stream:
            audio_stream.download(output_path=output_path)
            print(f"Áudio baixado com sucesso em '{output_path}'. ")
        else:
            print("Nenhum stream de áudio disponível para este vídeo.")

    def download_video(self, output_path):
        def remove_invalid_characters(text):
          return re.sub(r'[^a-zA-Z0-9-áéíóúãõâêîôûàèìòùäëïöüçÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙÄËÏÖÜÇ ]', '', text)
        
        print("Baixando o vídeo com a maior resolução disponível...")
        video_stream = self.yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()
        audio_stream = self.yt.streams.get_audio_only()

        if video_stream and audio_stream:
            print(f"Baixando vídeo na resolução {video_stream.resolution} e áudio com qualidade {audio_stream.abr}...")
            # Baixar arquivos temporários de áudio e vídeo separadamente
            video_stream.download(output_path=output_path, filename="video")
            audio_stream.download(output_path=output_path, filename="audio")
            print(f"Vídeo e áudio baixados com sucesso. ")
            # Mesclar áudio e vídeo
            self.join_audio_video(output_path + "/video.mp4", output_path + "/audio.m4a", output_path + "/{}.mp4".format(remove_invalid_characters(self.yt.title)))
            # Remover arquivos temporários de áudio e vídeo
            os.remove(output_path + "/video.mp4")
            os.remove(output_path + "/audio.m4a")
        else:
            print("Nenhum stream de vídeo disponível para este vídeo.")
    
    def join_audio_video(self, video_path, audio_path, output_path):
      print("Combinando áudio e vídeo...")
      try:
        subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', '-loglevel', 'quiet', output_path], check=True)
        print(f"Vídeo baixado com sucesso em '{output_path}'. ")
      except subprocess.CalledProcessError as e:
        print(f'Erro ao mesclar áudio e vídeo: {e}')

if __name__ == "__main__":
    # Recebe a URL do vídeo do YouTube.
    url = input("Informe a URL do vídeo: ").strip()
    
    # Recebe o tipo de download (Áudio ou Vídeo).
    while True:
        only_audio = input("Informe o formato [(A)udio, (V)ídeo]: ").upper().strip()
        if only_audio in ['A', 'V']:
            break
        else:
            print("Opção inválida. Por favor, digite 'A' para áudio ou 'V' para vídeo.")
    
    # Instancia o downloader e faz o download conforme a escolha.
    downloader = VideoDownloader(url)
    downloader.download(only_audio=only_audio == 'A', output_path='./Downloads')
