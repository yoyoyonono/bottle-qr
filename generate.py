import base64
import qrcode
import qrcode.constants
import hmac
import hashlib
import os

def generate_qr_data(serial_number: int, secret_key: bytes) -> str:
    data = serial_number.to_bytes(8, 'big')
    # Use truncated HMAC-SHA256 (16 bytes) for smaller QR codes
    mac = hmac.new(secret_key, data, hashlib.sha256).digest()[:16]
    qr_data = base64.b64encode(data + mac).decode('utf-8')
    return qr_data

def generate_invalid_qr(serial_number: int) -> str:
    # Generate random MAC to simulate invalid signature
    data = serial_number.to_bytes(8, 'big')
    invalid_mac = os.urandom(16)  # 16 random bytes
    qr_data = base64.b64encode(data + invalid_mac).decode('utf-8')
    return qr_data

if __name__ == "__main__":
    serial_number: int = 0
    while True:
        input_text = input("Serial Number: ")
        if input_text[0] == 'b':
            serial_number = int(input_text[1:])
            qr_data = generate_invalid_qr(serial_number)
        else:
            serial_number = int(input_text)
            qr_data = generate_qr_data(serial_number, secret_key)
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(qr_data)

        print(f"Generated QR Code for Serial Number: {serial_number}")
        print(f"QR Data: {qr_data}")
        qr.print_ascii()
        