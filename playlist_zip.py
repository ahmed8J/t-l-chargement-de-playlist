import os
import shutil
import zipfile
from yt_dlp import YoutubeDL

def download_youtube_playlist(playlist_url, output_folder='playlist_videos'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'format': 'mp4',
        'quiet': False,
        'ignoreerrors': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        print("[*] Téléchargement de la playlist...")
        ydl.download([playlist_url])

    print("[*] Téléchargement terminé.")
    return output_folder

def zip_folder(folder_path, zip_name='playlist_archive.zip'):
    print(f"[*] Compression en cours vers {zip_name}...")
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, folder_path)
                zipf.write(filepath, arcname)
    print(f"[*] Archive créée : {zip_name}")

if __name__ == "__main__":
    playlist_url = input("Entrez l'URL de la playlist YouTube : ")
    folder = download_youtube_playlist(playlist_url)
    zip_folder(folder)
