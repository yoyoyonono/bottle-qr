import base64
import qrcode

def generate_qr_data(serial_number: int) -> str:
    return base64.b64encode(serial_number.to_bytes(8, 'big')).decode('utf8')


if __name__ == "__main__":
    starting_serial_number: int = 12345
    qr_data = generate_qr_data(starting_serial_number)

    qr = qrcode.QRCode()
    qr.add_data(qr_data)
    qr.print_ascii()
