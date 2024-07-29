import pygame
import requests

def play_song(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def get_lyrics(artist, title):
    """For Lyrics"""
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        lyrics = response.json().get('lyrics', 'Lirik tidak ditemukan')
    else:
        lyrics = 'Lirik tidak ditemukan'
    return lyrics

def main():
    artist = "Yanaginagi"
    title = "Yukitoki"
    file_path = 'Example/Yukitoki.mp3'  #Your Path

    lyrics = get_lyrics(artist, title)
    print(f"\nLirik untuk {title} oleh {artist}:\n")
    print(lyrics)

    play_song(file_path)

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
