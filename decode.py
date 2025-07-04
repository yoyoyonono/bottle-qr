import base64
if __name__ == "__main__":
    while True:
        qr_data = input()
        try:
            serial_number = int.from_bytes(base64.b64decode(qr_data), 'big')
            print(f"Serial Number: {serial_number}")
        except (ValueError, base64.binascii.Error) as e:
            print(f"Error decoding QR data: {e}")