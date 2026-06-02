# 🎵 ListenToMe - Real-Time Spotify Last 10 Tracks Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Author-Yigit%20Tekis-blueviolet?style=for-the-badge" alt="Author">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge" alt="Python Version">
  <img src="https://img.shields.io/badge/API-Spotify%20Web%20API-1DB954.svg?style=for-the-badge" alt="Spotify API">
</p>

Spotify'ın kendi içinde barındırmadığı "anlık dinamik geçmiş listesi" eksikliğini gidermek amacıyla geliştirdiğim bu otomasyon projesi, hesabımda çalan son 10 şarkıyı **tam zamanlı (real-time)** olarak takip eder ve sadece bu iş için oluşturduğum özel bir çalma listesinde (Playlist) anlık olarak senkronize tutar.

---

## 🧠 Projenin Çalışma Mantığı ve Mimari Yaklaşımım

Sistemi tamamen asenkron mantıkta, Spotify API'yi gereksiz isteklerle (Rate Limit) yormayacak ve arka planda minimum kaynak tüketecek şekilde optimize ettim.

1. **Anlık Durum Analizi:** Geliştirdiğim betik, Spotify Web API (`currently-playing` endpoint'i) üzerinden her 10 saniyede bir hesabımın aktiflik durumunu sorgular.
2. **Akıllı Şarkı Yakalama:** Eğer dinlediğim parça değiştiyse, sistem yeni şarkının benzersiz `Track ID` değerini, sanatçı adını ve şarkı ismini hafızaya alır.
3. **Mükerrer ve Pozisyon Kontrolü:** Dinlemekte olduğum şarkı listede halihazırda mevcutsa, listede çift kayıt (duplication) oluşmaması için eski kaydı otomatik olarak siler ve şarkıyı güncel haliyle çalma listesinin en tepesine (`index: 0`) taşır.
4. **Kayan Liste Algoritması:** Çalma listesindeki toplam parça sayısı 10'u geçtiği an, listenin en sonundaki (en eski) şarkıyı otomatik olarak uçurur. Böylece liste sürekli yaşayan, kayan bir "Son 10 Şarkım" hafızasına dönüşür.

---

## ⚡ Karşılaştığım Problemler ve Geliştirdiğim Çözümler (Fail-Safe)

Geliştirme sürecinde karşılaştığım bazı teknik sınırları aşmak için koda entegre ettiğim siber güvenlik ve yazılım çözümleri:

* **Veri Tipi Çakışmaları (`'track'` Hatası):** Spotify API üzerinden playlist elemanlarını çekerken, listede yerel dosyalar, silinmiş şarkılar veya podcastler olduğunda standart indeksleme mimarisi çökebiliyordu. Bunu engellemek için `get_playlist_tracks()` fonksiyonunda sıkı bir **hata koruması (fail-safe)** kurguladım. `item.get('track')` doğrulamasıyla geçersiz nesneleri ayıklayarak sistemin kesintisiz çalışmasını sağladım.
* **Hassas Verilerin İzolasyonu:** Projede kullanılan `Client ID` ve `Client Secret` gibi doğrudan Spotify hesabıma tam yetki veren API anahtarlarını kaynak kodun içinde bırakmadım. Güvenli kod geliştirme pratiklerine (Secure Coding Practices) uygun olarak bu verileri **`.env`** dosyasında çevre değişkeni (Environment Variables) olarak izole ettim.
* **Güvenli Yönlendirme (Authentication):** Spotify'ın yerel geliştirmeler için kullandığı OAuth 2.0 protokolünü entegre ettim. Kimlik doğrulama esnasında `localhost` yerine doğrudan loopback IP adresi olan `http://127.0.0.1:8888/callback` mimarisini kullanarak veri akışını sorunsuz hale getirdim.

---

## 🛠️ Kurulum ve Lokal Çalıştırma

### 1. Kütüphanelerin Kurulması
Sistem mimarisinde kullandığım temel bağımlılıkları yüklemek için:

```bash
pip install spotipy python-dotenv
