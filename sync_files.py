import shutil
import os

source = "index_new.html"
target = "index.html"

try:
    shutil.copy2(source, target)
    print(f"✓ Copied {source} to {target}")
    
    # Verify
    with open(target, 'r') as f:
        content = f.read()
        if "Jad (he/him) holds a bachelor" in content:
            print("✓ Verified: Correct Jad content found")
        else:
            print("✗ Verification failed")
except Exception as e:
    print(f"Error: {e}")
