
import requests
from bs4 import BeautifulSoup
import os
import pdfkit
import time
import PyPDF2
import pandas as pd

def download_and_convert(url, output_dir, file_number, total_files, max_retries=2):
    for attempt in range(max_retries):
        try:
            print(f"
** Processing page {file_number} of {total_files} ({url})...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.title.string.strip() if soup.title else "Untitled"
            truncated_title = ''.join(char for char in title[:50] if char.isalnum())

            output_pdf = os.path.join(output_dir, f"{truncated_title}.pdf")
            pdfkit.from_string(html_content, output_pdf, options={'enable-local-file-access': '', 'load-error-handling': 'ignore'})

            print(f"Downloaded and converted file {file_number} of {total_files}: {url}")
            return output_pdf
        except Exception as e:
            print(f"Error processing file {file_number}: {e}")
            if attempt < max_retries - 1:
                backoff = 2 ** attempt
                print(f"Retry {attempt + 1} of {max_retries} for file {file_number}: {url} in {backoff} seconds")
                time.sleep(backoff)
    return False

def extract_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [link.get('href') for link in soup.find_all('a') if link.get('href') and link.get('href').startswith('http')]

def main():
    # Read base URL from the previously saved file
    try:
        with open('base_url.txt', 'r') as file:
            base_url = file.read().strip()
    except FileNotFoundError:
        print("\x1b[31mError: base_url.txt not found. Please run script1.py first.\x1b[0m")
        return

    output_dir = os.path.join(os.getcwd(), 'recycling_data')
    os.makedirs(output_dir, exist_ok=True)

    print(f"
** Downloading base webpage ({base_url})...")
    base_html = requests.get(base_url).text
    print("Base webpage downloaded successfully.")

    print("
** Extracting URLs...")
    urls = extract_urls(base_html)
    if not urls:
        print("\x1b[31mNo pages found.\x1b[0m")
        return
    print(f"Found {len(urls)} URLs.")

    pdf_files = []
    for i, url in enumerate(urls):
        print(f"
** Downloading and converting page {i+1} of {len(urls)} ({url})...")
        pdf_file = download_and_convert(url, output_dir, i+1, len(urls))
        if pdf_file:
            pdf_files.append(pdf_file)
        else:
            print(f"\x1b[31mError processing page {i+1}.\x1b[0m")

    print("
** Download and conversion complete.")

    output_pdf = os.path.join(output_dir, "combined_recycling_data.pdf")
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()
    print(f"Combined PDFs into {output_pdf}")

    data = []
    for pdf in pdf_files:
        data.append({'file': pdf, 'content': 'Extracted data (placeholder)'})  # Placeholder content

    df = pd.DataFrame(data)
    csv_file = os.path.join(output_dir, 'recycling_data.csv')
    df.to_csv(csv_file, index=False)
    print(f"Created CSV file: {csv_file}")

if __name__ == '__main__':
    main()