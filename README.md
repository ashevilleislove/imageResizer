
# Python Utility Scripts

This repository contains a collection of useful Python utility scripts that can help with common tasks such as image resizing, data conversion, and setting up a basic web server. Each script is accompanied by a README file that provides detailed instructions on how to use the script.

## Contents

1. **Image Resizer** (`image_resizer.py`)
   - This script resizes an image to specified dimensions using the Python Imaging Library (PIL).
   - [README](./README_image_resizer.md)

2. **CSV to JSON Converter** (`csv_to_json.py`)
   - This script converts a CSV file to a JSON file.
   - [README](./README_csv_to_json.md)

3. **Basic Web Server** (`web_server.py`)
   - This script sets up a basic web server using Flask.
   - [README](./README_web_server.md)

## Usage

### Image Resizer

This script resizes an image to the specified dimensions using the Python Imaging Library (PIL).

**Requirements:**
- Pillow

**Installation:**
```sh
pip install Pillow
```

**Usage:**
Place your input image in the same directory as the script and run the script:
```sh
python image_resizer.py
```
Modify the `input_path`, `output_path`, and `size` variables as needed.

### CSV to JSON Converter

This script converts a CSV file to a JSON file.

**Requirements:**
- None

**Usage:**
Place your input CSV file in the same directory as the script and run the script:
```sh
python csv_to_json.py
```
Modify the `csv_file_path` and `json_file_path` variables as needed.

### Basic Web Server

This script sets up a basic web server using Flask.

**Requirements:**
- Flask

**Installation:**
```sh
pip install Flask
```

**Usage:**
Run the script to start the web server:
```sh
python web_server.py
```
Access the web server at `http://127.0.0.1:5000/`.

## License

This repository is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
