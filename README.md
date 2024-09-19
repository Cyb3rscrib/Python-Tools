### Web Scraper for Digital Whisper Zines - README

---

## Overview

This script is designed to scrape and download **Digital Whisper Zines** (PDF files) from a website. It constructs URLs dynamically and fetches the zine PDFs based on hexadecimal values in the file names. The URLs are written to a text file (`urls.txt`), and the contents of the PDFs are downloaded and saved into another text file (`urlscontent.txt`).

The script leverages the **`requests`** library to make HTTP requests and fetch content from the web.

---

## Features

- Dynamically generates URLs for downloading Digital Whisper zines based on an incremental index.
- Saves the generated URLs into a text file (`urls.txt`).
- Downloads the content of each PDF and saves it into a file (`urlscontent.txt`) in binary format.
- The zine content is separated by `---` markers to distinguish between different files.

---

## Prerequisites

1. **Python 3.x** installed on your machine.
2. **`requests`** and **`beautifulsoup4`** libraries installed:
   - Install them via pip if not already installed:
     ```bash
     pip install requests beautifulsoup4
     ```

---

## Usage Instructions

1. **Clone or download the script** to your local environment.

2. **Run the script**:
   - You can run the script using Python:
     ```bash
     python web_scraper.py
     ```

3. The script will:
   - Generate URLs for Digital Whisper zines from 1 to 19 using hexadecimal values.
   - Save the list of URLs to a file named `urls.txt`.
   - Download the content of each zine in binary format and save it to `urlscontent.txt` with `---` as a separator between each file.

---

## Code Structure

### 1. **URL Generation**
```python
for i in range(1, 20):
    myhexa = hex(i)
    url = f"https://www.digitalwhisper.co.il/files/Zines/{myhexa}/DigitalWhisper{i}.pdf"
    urls.append(url)
```
- The script generates the URLs for the Digital Whisper zines by converting an incremental index `i` (ranging from 1 to 19) to its hexadecimal representation using `hex(i)`. 
- It constructs the URL dynamically based on this hexadecimal value and appends it to the `urls` list.

### 2. **Writing URLs to File**
```python
with open('urls.txt', 'w') as file:
    for url in urls:
        file.write(url + '\n')
```
- This block writes all the generated URLs into a file called `urls.txt` for easy reference.

### 3. **Downloading Zine Content**
```python
with open('urlscontent.txt', 'wb') as file:
    for url in urls:
        response = requests.get(url)
        content = response.content
        file.write(content)
        file.write(b'\n---\n')
```
- The script loops through the `urls` list, downloading the content of each PDF by making an HTTP request (`requests.get(url)`).
- It writes the binary content of each PDF into `urlscontent.txt` and separates each zine with `---` for distinction.

---

## Output Files

1. **`urls.txt`**: Contains all the dynamically generated URLs of the zines.
2. **`urlscontent.txt`**: Contains the binary content of each zine, separated by `---`.

---

## Notes

- The current implementation only supports downloading 19 zines (from index 1 to 19). If you need more, adjust the loop's range.
- **Hexadecimal URL Format**: The URLs use a hexadecimal format to fetch each zine (`myhexa = hex(i)`). Make sure this pattern aligns with the actual structure of the URLs on the website.
- **Error Handling**: The script doesn't currently handle errors. If a URL doesn't exist or if the download fails, it will not alert the user. You can add error handling to manage this.

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

Ensure that you have permission to download the content from the website. Unauthorized downloading or scraping of content is illegal and unethical in many cases.

---

## Future Improvements

1. **Error Handling**: Add error handling (e.g., check for 404 errors if a zine doesn't exist).
2. **Progress Tracking**: Display download progress or status messages during execution.
3. **Direct PDF Saving**: Save each PDF file separately rather than merging content into a single file.

--- 

This script provides a simple and efficient way to scrape content and download files, but always ensure compliance with the website’s terms of service before using it for scraping or downloading files.
