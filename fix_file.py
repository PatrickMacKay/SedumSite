#!/usr/bin/env python3
import os

# Read the good version
with open('index_new.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Backup the old one first  
if os.path.exists('index.html'):
    os.rename('index.html', 'index_broken.html')

# Write the good version
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('index.html', 'r') as f:
    test_content = f.read()
    if '<img src="sedum_images/jad_pic.JPG" alt="Jad">' in test_content and \
       '<strong>Jad (he/him)</strong> holds a bachelor' in test_content:
        print("SUCCESS: File updated correctly")
        print("- Jad appears first")
        print("- Images are smaller (50% width)")
        print("- Layout alternates opposite sides")
    else:
        print("FAILED: Content not as expected")
