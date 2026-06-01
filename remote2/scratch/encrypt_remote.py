import os
import zlib
import base64

def encrypt():
    remote_path = r"d:\laragon\www\remote2\remote.py"
    if not os.path.exists(remote_path):
        print("Error: remote.py not found.")
        return
        
    with open(remote_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    # Check if already encrypted
    if "exec(zlib.decompress(base64.b64decode" in code:
        print("remote.py is already encrypted/obfuscated.")
        return
        
    # Compress and encode
    compressed = zlib.compress(code.encode("utf-8"))
    encoded = base64.b64encode(compressed).decode("utf-8")
    
    wrapper = f"""# -*- coding: utf-8 -*-
import zlib
import base64

# Protected Remote Console Engine
exec(zlib.decompress(base64.b64decode(b'{encoded}')).decode('utf-8'))
"""

    with open(remote_path, "w", encoding="utf-8") as f:
        f.write(wrapper)
        
    print("remote.py successfully encrypted and protected!")

if __name__ == "__main__":
    encrypt()
