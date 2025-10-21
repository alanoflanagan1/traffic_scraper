import requests
import time
import datetime
import os

# Direct camera image URL
CAMERA_URL = "https://cctv.trafficwatchni.com/3273.jpg"

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

def download_camera_image():
    try:
        # Add timestamp to prevent caching
        timestamp_param = int(time.time() * 1000)
        url_with_cache_buster = f"{CAMERA_URL}?cache={timestamp_param}"

        # Request image using browser-like headers
        response = requests.get(url_with_cache_buster, headers=HEADERS, timeout=10)
        response.raise_for_status()

        # Save image with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_DIR, f"traffic_cam_{timestamp}.jpg")

        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"✅ Saved image: {filename}")

    except Exception as e:
        print(f"⚠️ Error downloading image: {e}")

def main():
    print("🚦 Starting TrafficWatchNI image downloader...")
    while True:
        download_camera_image()
        time.sleep(60)  # 1 minute

if __name__ == "__main__":
    main()
