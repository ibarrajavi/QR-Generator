# Static QR Code Generator

A simple CLI tool to generate QR codes from URLs.

## Features

- Auto-increments filenames to avoid overwrites
- Input validation
- Colored terminal output

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python qr_generator.py
```

## Example

```bash
python qr_generator.py
Enter a URL for QR generation: github.com/ibarrajavi
Enter a file name for the QR: my_github
QR successfully saved: qr_codes/my_github.png
```
