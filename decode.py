import base64
import hmac
import hashlib
import os

if __name__ == "__main__":
    # Load the secret key for HMAC verification
    secret_key_file = "secret_key.bin"
    
    if not os.path.exists(secret_key_file):
        print(f"Error: Secret key file '{secret_key_file}' not found!")
        print("Please run generate.py first to create the secret key.")
        exit(1)
        
    with open(secret_key_file, "rb") as f:
        secret_key = f.read()

    while True:
        qr_data = input()
        try:
            decoded_data = base64.b64decode(qr_data)
            print(f"QR Data: {list(decoded_data)}")
            
            if len(decoded_data) < 24:  # 8 bytes data + 16 bytes MAC
                print("Error: QR data too short!")
                continue
                
            serial_number = int.from_bytes(decoded_data[:8], 'big')
            received_mac = decoded_data[8:24]  # 16-byte MAC
            print(f"Serial Number: {serial_number}")
            print(f"MAC (hex): {received_mac.hex()}")

            # Verify HMAC
            data = decoded_data[:8]
            expected_mac = hmac.new(secret_key, data, hashlib.sha256).digest()[:16]
            
            if hmac.compare_digest(received_mac, expected_mac):
                print("MAC is VALID")
            else:
                print("Invalid MAC!")
                
        except (ValueError, base64.binascii.Error) as e:
            print(f"Error decoding QR data: {e}")
