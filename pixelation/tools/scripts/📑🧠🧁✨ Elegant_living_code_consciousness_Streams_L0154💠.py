
import requests
from bs4 import BeautifulSoup
import os
import pdfkit

config = pdfkit.configuration(wkhtmltopdf="/path/to/wkhtmltopdf")  # Replace with the actual path
pdfkit.from_string(html_content, output_pdf, configuration=config)


def download_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def extract_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [link.get('href') for link in soup.find_all('a') if link.get('href') and link.get('href').startswith('http')]

def save_html_file(url, output_dir, file_number):
    try:
        html_content = download_page(url)
        file_path = os.path.join(output_dir, f"page_{file_number}.html")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"Saved HTML file {file_number}: {url}")
        return file_path
    except Exception as e:
        print(f"Error saving HTML file {file_number}: {e}")
        return None

def verify_page(url):
    try:
        response = requests.head(url, timeout=10)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Invalid URL: {url} - {e}")
        return False

def convert_html_to_pdf(html_file, output_dir, file_number, total_files, max_retries=2):
    for attempt in range(max_retries):
        try:
            with open(html_file, 'r', encoding='utf-8') as file:
                html_content = file.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.title.string.strip() if soup.title else "Untitled"
            truncated_title = ''.join(char for char in title[:50] if char.isalnum())

            output_pdf = os.path.join(output_dir, f"{truncated_title}.pdf")

            # Use the path to wkhtmltopdf
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')  # Adjust this path as necessary
            pdfkit.from_file(html_file, output_pdf, configuration=config, options={'enable-local-file-access': '', 'load-error-handling': 'ignore'})

            print(f"Converted HTML file {file_number} of {total_files} to PDF: {output_pdf}")
            return output_pdf
        except Exception as e:
            print(f"Error converting HTML file {file_number} of {total_files} to PDF: {e}")
            if attempt < max_retries - 1:
                backoff = 2 ** attempt
                print(f"Retry {attempt + 1} of {max_retries} for file {file_number} in {backoff} seconds...")
                time.sleep(backoff)
    return None

def main():
    # Read the base URL from the file
    with open('base_url.txt', 'r') as file:
        base_url = file.read().strip()

    output_dir = os.path.join(os.getcwd(), 'recycling_data')
    os.makedirs(output_dir, exist_ok=True)

    print("Downloading base webpage...")
    base_html = download_page(base_url)
    print("Base webpage downloaded successfully.")

    print("Extracting URLs...")
    urls = extract_urls(base_html)
    if not urls:
        print("\x1b[31mNo pages found.\x1b[0m")
        return
    print(f"Found {len(urls)} URLs.")

    # Save extracted URLs to a text file
    url_list_file = os.path.join(output_dir, 'extracted_urls.txt')
    with open(url_list_file, 'w') as file:
        for url in urls:
            file.write(url + '\n')
    print(f"URLs saved to {url_list_file}")

    html_files = []
    total_files = len(urls)
    for i, url in enumerate(urls):
        if verify_page(url):
            html_file = save_html_file(url, output_dir, i + 1)
            if html_file:
                pdf_file = convert_html_to_pdf(html_file, output_dir, i + 1, total_files)
                if not pdf_file:
                    print(f"\x1b[31mError converting page {i + 1} to PDF.\x1b[0m")
            else:
                print(f"\x1b[31mError processing page {i + 1}.\x1b[0m")
        else:
            print(f"\x1b[31mSkipping invalid page {i + 1}: {url}\x1b[0m")

    print("\nDownload, saving of HTML files, and conversion to PDF complete.")

if __name__ == '__main__':
    main()
