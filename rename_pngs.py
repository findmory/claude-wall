#!/usr/bin/env python3
"""
Script to extract orange text from PNG screenshots and rename files accordingly.
"""

import os
import sys
from pathlib import Path
from PIL import Image
import pytesseract
import numpy as np
import re

def extract_orange_text(image_path):
    """
    Extract orange-colored text from an image using OCR.
    
    Args:
        image_path: Path to the PNG image
        
    Returns:
        Extracted text string, or None if no text found
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        img_array = np.array(img)
        
        # Define orange color range (in RGB)
        # Based on actual text color analysis: RGB(199, 130, 106) to RGB(150, 94, 79)
        lower_orange = np.array([150, 90, 70])
        upper_orange = np.array([255, 180, 140])
        
        # Create a mask for orange pixels
        mask = np.all((img_array >= lower_orange) & 
                      (img_array <= upper_orange), axis=2)
        
        # Create a new image with only orange text (white on black background)
        filtered_img = np.zeros_like(img_array)
        filtered_img[mask] = [255, 255, 255]  # Make orange pixels white
        
        # Convert back to PIL Image
        filtered_pil = Image.fromarray(filtered_img.astype('uint8'))
        
        # Perform OCR on the filtered image
        text = pytesseract.image_to_string(filtered_pil, config='--psm 6')
        
        # Clean up the text
        text = text.strip()
        
        # Remove special characters and extra whitespace
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'\s+', '_', text)
        
        # Remove leading/trailing underscores and hyphens
        text = text.strip('_-')
        
        # If it starts with special characters after cleaning, remove them
        while text and not text[0].isalnum():
            text = text[1:]
        
        return text if text else None
        
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")
        return None

def rename_files(folder_path, dry_run=True):
    """
    Rename PNG files based on extracted orange text.
    
    Args:
        folder_path: Path to folder containing PNG files
        dry_run: If True, only show what would be renamed without actually renaming
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist")
        return
    
    # Get all PNG files
    png_files = list(folder.glob("*.png"))
    
    if not png_files:
        print(f"No PNG files found in '{folder_path}'")
        return
    
    print(f"Found {len(png_files)} PNG file(s)")
    print("-" * 60)
    
    renamed_count = 0
    failed_count = 0
    
    for png_file in png_files:
        print(f"\nProcessing: {png_file.name}")
        
        # Extract orange text
        text = extract_orange_text(png_file)
        
        if text:
            # Create new filename
            new_name = f"{text}.png"
            new_path = png_file.parent / new_name
            
            # Check if file already exists
            if new_path.exists() and new_path != png_file:
                print(f"  ⚠️  Warning: '{new_name}' already exists, skipping...")
                failed_count += 1
                continue
            
            if dry_run:
                print(f"  ✓ Would rename to: {new_name}")
            else:
                try:
                    png_file.rename(new_path)
                    print(f"  ✓ Renamed to: {new_name}")
                    renamed_count += 1
                except Exception as e:
                    print(f"  ✗ Failed to rename: {str(e)}")
                    failed_count += 1
        else:
            print(f"  ✗ Could not extract orange text")
            failed_count += 1
    
    print("\n" + "=" * 60)
    if dry_run:
        print("DRY RUN - No files were actually renamed")
        print(f"Would rename: {renamed_count} file(s)")
    else:
        print(f"Successfully renamed: {renamed_count} file(s)")
    print(f"Failed/Skipped: {failed_count} file(s)")
    print("=" * 60)

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python rename_pngs.py <folder_path> [--execute]")
        print("\nOptions:")
        print("  --execute    Actually rename files (default is dry-run)")
        print("\nExample:")
        print("  python rename_pngs.py /path/to/screenshots")
        print("  python rename_pngs.py /path/to/screenshots --execute")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    dry_run = "--execute" not in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be renamed")
        print("    Add --execute to actually rename files\n")
    else:
        print("⚠️  EXECUTE MODE - Files will be renamed!\n")
    
    rename_files(folder_path, dry_run=dry_run)

if __name__ == "__main__":
    main()
