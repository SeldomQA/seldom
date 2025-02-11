import os


def get_device_info(device: str) -> dict:
    """
    Get device name and serial number.
    :param device:
    :return:
    """
    try:
        name = os.popen(f"adb -s {device} shell getprop ro.product.model").read().strip().replace(' ', '')
        return {device: name}
    except Exception as e:
        print(f"Error retrieving device info for {device}: {e}")
        return {}


def get_devices() -> dict:
    """
    Get a list of dictionaries, each containing a single device's name and serial number.
    :return:
    """
    devices = {}
    raw_devices = os.popen("adb devices").read().splitlines()[1:]  # Skip the first line which is a header
    for line in raw_devices:
        parts = line.split()
        if len(parts) > 1 and parts[1] == "device":
            serial = parts[0]
            device_info = get_device_info(serial)
            if device_info:
                # Create a dictionary from the tuple and add it to the list
                devices = {**devices, **device_info}
    return devices


if __name__ == '__main__':
    a = get_devices()
    print(a)
