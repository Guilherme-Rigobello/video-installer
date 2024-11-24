import yt_dlp

url = input("Link do vídeo: ")

try:
    opcoes = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'best[height<=1080]'
    }
    yt_dlp.YoutubeDL(opcoes).download([url])
    print("Download feito!")

except Exception as e:
    print(f"Erro: {e}")
