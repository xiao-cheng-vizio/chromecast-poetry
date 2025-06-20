import time
from zeroconf import ServiceBrowser, Zeroconf, ServiceListener

class MyListener(ServiceListener):
    def remove_service(self, zeroconf_instance: Zeroconf, type: str, name: str) -> None:
        print(f"Service {name} removed")

    def add_service(self, zeroconf_instance: Zeroconf, type: str, name: str) -> None:
        info = zeroconf_instance.get_service_info(type, name)
        print(f"Service {name} added, service info: {info}")

    def update_service(self, zeroconf_instance: Zeroconf, type: str, name: str) -> None:
        # This method is part of ServiceListener in newer zeroconf versions
        # For older versions, you might not need it or it might not be called.
        info = zeroconf_instance.get_service_info(type, name)
        print(f"Service {name} updated, service info: {info}")


import time
import pychromecast
import zeroconf

def main():
    zeroconf_instance = Zeroconf()
    listener = MyListener()
    # Chromecast service type
    service_type = "_googlecast._tcp.local."
    browser = ServiceBrowser(zeroconf_instance, service_type, listener)

    print(f"Scanning for Chromecast services ({service_type}) for 20 seconds...")
    try:
        time.sleep(20)
    finally:
        print("Stopping scan.")
        zeroconf_instance.close()

   
if __name__ == '__main__':
    main()
