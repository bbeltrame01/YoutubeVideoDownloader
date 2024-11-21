
# YouTubeVideoDownloader

Este é um programa em Python que permite fazer o download de vídeos e áudios do YouTube de maneira simples e eficiente. Ele utiliza as bibliotecas `pytubefix` para baixar vídeos e áudios e `ffmpeg` para manipulação de formatos e qualidade dos arquivos baixados.

## **Funcionalidades**

- **Baixar Vídeos**: Baixe vídeos do YouTube em alta qualidade.
- **Baixar Áudios**: Extraia o áudio dos vídeos e salve no formato M4A.

## **Dependências**

Para rodar o programa, você precisa instalar as seguintes dependências:

- [pytubefix](https://github.com/yt-dlp/pytubefix): Biblioteca usada para baixar vídeos e áudios do YouTube.
- [ffmpeg](https://ffmpeg.org/): Ferramenta poderosa para manipulação de arquivos de áudio e vídeo, necessária para converter e melhorar os downloads.

### **Como Instalar as Dependências**

1. **Instalar `pytubefix`**:

   ```bash
   pip install pytubefix
   ```

2. **Instalar `ffmpeg`**:

   - **Windows**:  
     Baixe o instalador em [FFmpeg.org](https://ffmpeg.org/download.html) e adicione a pasta `bin` ao **PATH** do sistema.
   - **Linux**:  
     Use o gerenciador de pacotes da sua distribuição:  
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - **macOS**:  
     Use o Homebrew:  
     ```bash
     brew install ffmpeg
     ```

## **Como Usar**

1. Clone este repositório para sua máquina local:  
   ```bash
   git clone https://github.com/bbeltrame01/YouTubeVideoDownloader.git
   ```

2. Navegue até o diretório do projeto:  
   ```bash
   cd YouTubeVideoDownloader
   ```

3. Execute o programa:  
   ```bash
   python main.py
   ```

4. Insira o link do vídeo do YouTube quando solicitado.

5. Escolha a opção desejada: baixar o vídeo completo ou apenas o áudio.

6. Aguarde o download e encontre o arquivo na pasta de destino especificada.

## **Exemplo de Uso**

### **Interface de Linha de Comando**
```bash
python main.py
Informe o link do vídeo: https://www.youtube.com/watch?v=example
Informe o formato [(A)udio, (V)ídeo]: 
A - Baixar Áudio
V - Baixar Vídeo
Baixando...  
Áudio/Vídeo baixado com sucesso!  
```

### **Saída do Arquivo**
Os arquivos baixados serão salvos na pasta `downloads/` (ou outra especificada no programa).

## **Contribuições**

Contribuições são sempre bem-vindas! Para relatar problemas ou sugerir melhorias, abra uma issue no repositório.

## **Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
