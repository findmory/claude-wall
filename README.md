# PNG File Renamer - Extract Orange Text

This script automatically renames PNG files based on orange-colored text found in the images using OCR (Optical Character Recognition).

## Features

- Extracts orange text from PNG screenshots
- Safely renames files with dry-run mode by default
- Handles duplicate filenames
- Cleans text for valid filenames

## Requirements

- Python 3.6+
- Tesseract OCR engine
- Python packages: PIL/Pillow, pytesseract, numpy

## Installation

### 1. Install Tesseract OCR

**macOS:**
```bash
brew install tesseract
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

**Windows:**
Download installer from: https://github.com/UB-Mannheim/tesseract/wiki

### 2. Install Python dependencies

```bash
pip install pillow pytesseract numpy
```

## Usage

### Dry Run (Preview Only - Recommended First)

Test the script without actually renaming files:

```bash
python rename_pngs.py /path/to/your/folder
```

This will show you what files would be renamed without making any changes.

### Execute Mode (Actually Rename Files)

Once you're satisfied with the preview, run with `--execute`:

```bash
python rename_pngs.py /path/to/your/folder --execute
```

## Examples

```bash
# Preview what would happen
python rename_pngs.py ~/Desktop/screenshots

# Actually rename the files
python rename_pngs.py ~/Desktop/screenshots --execute
```

## How It Works

1. The script scans for all `.png` files in the specified folder
2. For each image, it identifies orange-colored pixels (RGB range: 200-255 red, 100-180 green, 0-100 blue)
3. Extracts text from those orange pixels using Tesseract OCR
4. Cleans the text to create a valid filename
5. Renames the file (or shows what would be renamed in dry-run mode)

## Color Customization

If your orange text doesn't match the default range, you can modify the color range in the script:

```python
# In the extract_orange_text function, adjust these values:
lower_orange = np.array([200, 100, 0])   # [Red, Green, Blue]
upper_orange = np.array([255, 180, 100]) # [Red, Green, Blue]
```

## Troubleshooting

**Issue: "No text extracted"**
- The orange color might be outside the default range
- Try adjusting the color range values in the script
- Check if Tesseract is properly installed: `tesseract --version`

**Issue: "Command not found: tesseract"**
- Make sure Tesseract OCR is installed (see Installation section)
- On macOS, you may need to restart your terminal after installing

**Issue: Incorrect text extraction**
- OCR isn't perfect - verify the dry-run output before executing
- Consider manually adjusting filenames if OCR makes mistakes

## Safety Features

- **Dry-run by default**: No files are changed unless you use `--execute`
- **Duplicate checking**: Won't overwrite existing files
- **Error handling**: Continues processing other files if one fails

## License

Free to use and modify as needed.
