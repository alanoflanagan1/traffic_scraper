import requests
import time
import datetime
import os

# Camera URLs (primary + secondary)
CAMERAS = {
    "A1_Hillsborough_Roundabout": "https://cctv.trafficwatchni.com/3273.jpg",
    "A1_Dromore": "https://cctv.trafficwatchni.com/3274.jpg",
    "A1_Hillsborough_South": "https://cctv.trafficwatchni.com/2.jpg",
    "A2_Holywood_Exchange": "https://cctv.trafficwatchni.com/308.jpg",
    "Greenhaw": "https://cctv.trafficwatchni.com/3293.jpg",
    "M3_Sydenham_Bypass": "https://cctv.trafficwatchni.com/3298.jpg",
    "A2_BangorRd_OldStationRd": "https://cctv.trafficwatchni.com/3262.jpg"
}

# Folder to save images
SAVE_DIR = "traffic_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# Pretend to be a normal web browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36",
    "Referer": "https://www.trafficwatchni.com/",
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
}

def download_camera_image(name, url):
    try:
        # Add timestamp to avoid caching
        timestamp_param = int(time.time() * 1000)
        url_cache = f"{url}?cache={timestamp_param}"

        response = requests.get(url_cache, headers=HEADERS, timeout=10)
        response.raise_for_status()

        # Save with timestamp and camera name
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_DIR, f"{name}_{timestamp}.jpg")

        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"✅ Saved image for {name}: {filename}")

    except Exception as e:
        print(f"⚠️ Error downloading {name}: {e}")

def main():
    print("🚦 Starting TrafficWatchNI multi-camera downloader...\n")

    for name, url in CAMERAS.items():
        download_camera_image(name, url)

    print("\n🏁 Done — all cameras processed.")

if __name__ == "__main__":
    main()
