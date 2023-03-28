import youtube_dl

def download_video_as_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = input("Por favor ingrese la URL del video de YouTube: ")
    download_video_as_audio(video_url)
    print("El audio ha sido extraído exitosamente.")
