import os
import zlib
import base64
import re

def decrypt():
    remote_path = r"d:\laragon\www\remote2\remote.py"
    if not os.path.exists(remote_path):
        print("Error: remote.py not found.")
        return
        
    with open(remote_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    # Check if encrypted
    match = re.search(r"base64\.b64decode\(b'(.*?)'\)", code, re.DOTALL)
    if not match:
        print("remote.py is not encrypted using our wrapper.")
        return
        
    encoded_payload = match.group(1)
    try:
        compressed = base64.b64decode(encoded_payload)
        decompressed = zlib.decompress(compressed).decode("utf-8")
        
        with open(remote_path, "w", encoding="utf-8") as f:
            f.write(decompressed)
            
        print("remote.py successfully decrypted and restored to original plain text!")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    decrypt()
