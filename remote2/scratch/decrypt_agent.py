import os
import zlib
import base64
import re

def decrypt():
    agent_path = r"d:\laragon\www\remote2\agent.php"
    if not os.path.exists(agent_path):
        print("Error: agent.php not found.")
        return
        
    with open(agent_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    # Search for the base64 payload
    match = re.search(r"base64_decode\('(.*?)'\)", code)
    if not match:
        print("agent.php is not encrypted/obfuscated using our wrapper.")
        return
        
    encoded_payload = match.group(1)
    try:
        compressed = base64.b64decode(encoded_payload)
        # Decompress raw deflate data (no headers)
        decompressed = zlib.decompress(compressed, -zlib.MAX_WBITS).decode("utf-8")
        
        # Add back the <?php opening tag if it was removed
        if not decompressed.strip().startswith("<?php"):
            decompressed = "<?php\n" + decompressed
            
        with open(agent_path, "w", encoding="utf-8") as f:
            f.write(decompressed)
            
        print("agent.php successfully decrypted and restored to original plain text!")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    decrypt()
