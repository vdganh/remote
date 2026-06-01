import os
import zlib
import base64

def encrypt():
    agent_path = r"d:\laragon\www\remote2\agent.php"
    if not os.path.exists(agent_path):
        print("Error: agent.php not found.")
        return
        
    with open(agent_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    # Check if already encrypted
    if "eval(gzinflate(base64_decode" in code:
        print("agent.php is already encrypted/obfuscated.")
        return
        
    # Strip the opening PHP tag <?php from code because eval() executes PHP code directly (without opening tags)
    if code.startswith("<?php"):
        code = code[5:]
    elif code.startswith("<?"):
        code = code[2:]
        
    # Compress the code
    compressed = zlib.compress(code.encode("utf-8"))[2:-4] # strip zlib headers to get raw deflate data
    encoded = base64.b64encode(compressed).decode("utf-8")
    
    wrapper = f"""<?php
/**
 * AI Project Intelligence Console - agent.php (Encrypted & Protected)
 * Do not edit or modify this file directly.
 */
eval(gzinflate(base64_decode('{encoded}')));
"""

    with open(agent_path, "w", encoding="utf-8") as f:
        f.write(wrapper)
        
    print("agent.php successfully encrypted and protected!")

if __name__ == "__main__":
    encrypt()
