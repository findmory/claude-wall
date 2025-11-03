#!/usr/bin/env python3
import os
import json

# Get all PNG files from images directory
images_dir = 'images'
png_files = [f for f in os.listdir(images_dir) if f.lower().endswith('.png')]

# Write to JSON file
with open('images.json', 'w') as f:
    json.dump(png_files, f, indent=2)

print(f'✓ Generated images.json with {len(png_files)} images')
print('Images:', png_files)
