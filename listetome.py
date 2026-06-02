import time
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# .env dosyasındaki verileri yükle
load_dotenv()

# Bilgileri güvenli bir şekilde çevre değişkenlerinden çekiyoruz
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
PLAYLIST_ID = os.getenv("SPOTIFY_PLAYLIST_ID")
REDIRECT_URI = "http://127.0.0.1:8888/callback"

scope = "user-read-currently-playing playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))

def get_playlist_tracks():
    try:
        results = sp.playlist_items(PLAYLIST_ID, fields="items(track(id))")
        track_ids = []
        for item in results.get('items', []):
            if item and 'track' in item and item['track']:
                track_id = item['track'].get('id')
                if track_id:
                    track_ids.append(track_id)
        return track_ids
    except Exception as e:
        print(f"Playlist okunurken hata oluştu: {e}")
        return []

def main():
    print("Sistem başlatıldı... Şarkı geçişleri takip ediliyor.")
    last_tracked_track = None

    while True:
        try:
            current_track = sp.currently_playing()
            
            if current_track is not None and current_track['is_playing']:
                if current_track['currently_playing_type'] == 'track':
                    track_id = current_track['item']['id']
                    track_name = current_track['item']['name']
                    artist_name = current_track['item']['artists'][0]['name']

                    if track_id != last_tracked_track:
                        print(f"Yeni şarkı algılandı: {artist_name} - {track_name}")
                        
                        current_playlist_tracks = get_playlist_tracks()

                        if track_id in current_playlist_tracks:
                            sp.playlist_remove_all_occurrences_of_items(PLAYLIST_ID, [track_id])
                            print(f"'{track_name}' zaten listedeydi, pozisyonu güncelleniyor.")

                        sp.playlist_add_items(PLAYLIST_ID, [track_id], position=0)
                        print(f"'{track_name}' listeye başarıyla eklendi.")

                        updated_tracks = get_playlist_tracks()
                        if len(updated_tracks) > 10:
                            excess_tracks = updated_tracks[10:]
                            sp.playlist_remove_all_occurrences_of_items(PLAYLIST_ID, [excess_tracks[-1]])
                            print("Liste 10 şarkıda sabit tutuldu, en eski şarkı silindi.")

                        last_tracked_track = track_id
            
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            
        time.sleep(10)

if __name__ == "__main__":
    main()
