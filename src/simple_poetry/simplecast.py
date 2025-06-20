import pychromecast

VIDEO_URL = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

def main():
    # Discover Chromecast devices
    print("Searching for Chromecast devices on your network...")
    try:
        chromecasts, browser = pychromecast.get_chromecasts()
    except Exception as e:
        print(f"Error discovering Chromecasts: {e}")
        return

    if not chromecasts:
        print("No Chromecast devices found.")
        return

    print("Discovered devices:")
    for i, cast in enumerate(chromecasts):
        print(f"{i+1}. {cast.name}")

 # Select device
    try:
        idx = int(input("Select a device by number: ")) - 1
        cast = chromecasts[idx]
    except (ValueError, IndexError):
        print("Invalid selection.")
        pychromecast.discovery.stop_discovery(browser)
        return

    # Connect and play video
    print(f"Connecting to {cast.name}...")
    cast.wait()
    mc = cast.media_controller
    print(f"Playing video: {VIDEO_URL}")
    mc.play_media(VIDEO_URL, "video/mp4")
    mc.block_until_active()
    mc.play()

    # Shut down discovery
    pychromecast.discovery.stop_discovery(browser)

if __name__ == '__main__':
    main()