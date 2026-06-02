# 🎵 ListenToMe - Dynamic Spotify Last 10 Tracks Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/API-Spotify%20Web%20API-1DB954.svg" alt="Spotify API">
  <img src="https://img.shields.io/badge/Platform-Windows%20%2F%20Linux-orange.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

**ListenToMe**, Spotify üzerinde anlık olarak dinlediğiniz müzikleri arka planda takip eden ve tamamen sizin kontrolünüzde olan özel bir çalma listesini (Playlist) **tam zamanlı (real-time)** olarak güncelleyen bir Python otomasyon projesidir.

Siz müzik dinlerken, sistem yeni bir şarkıya geçtiğinizi anlar, bu şarkıyı listenin en tepesine ekler ve listedeki şarkı sayısını her zaman **son dinlediğiniz 10 şarkıda** sabit tutar.

---

## ✨ Özellikler

* **Tam Zamanlı Takip:** Spotify API vasıtasıyla `currently-playing` durumu her 10 saniyede bir kontrol edilir.
* **Mükerrer Kayıt Engelleme:** Eğer dinlediğiniz şarkı listede zaten varsa, eski pozisyonundan silinir ve güncel olarak tekrar en üste taşınır.
* **Akıllı Hafıza Kontrolü:** Liste boyutu 10 şarkıyı geçtiği an, en eski şarkı listeden otomatik olarak kaldırılır.
* **Güvenli Altyapı:** API anahtarları ve hassas veriler kod içinde barındırılmaz; `.env` dosyası aracılığıyla çevre değişkeni (Environment Variables) olarak yönetilir.
* **Sessiz Arka Plan Modu:** Windows Görev Zamanlayıcı entegrasyonu ile bilgisayar açıldığı an hiçbir terminal ekranı görünmeden tamamen arka planda çalışabilir.

---

## 🛠️ Kurulum ve Çalıştırma

### 1. Gereksinimler
Bilgisayarınızda Python 3 ve `pip` paket yöneticisinin kurulu olduğundan emin olun. Ardından gerekli kütüphaneleri yükleyin:

```bash
pip install spotipy python-dotenv
