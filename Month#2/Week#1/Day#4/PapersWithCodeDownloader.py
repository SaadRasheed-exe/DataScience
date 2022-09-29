from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print('Please enter the URL for the paper you wish to download.')


def print_prompt(text):
    dashes_len = 100 - len(text) - 2
    br = '-'*(dashes_len // 2)
    final_prompt = f'{br} {text} {br}'
    final_prompt += '-' if len(final_prompt) != 100 else ''
    print(final_prompt)


def get_pdf_url(url):
    print_prompt('Retrieving PDF Link')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find_all('h1')[-1].text.strip() + '.pdf'
    pdf_tag = soup.find_all('a', attrs={'class': 'badge-light'})[0]
    pdf_url = pdf_tag.attrs['href']
    print_prompt('PDF Link Retrieved')
    return title, pdf_url


def download_and_save(url, file_name):
    print_prompt(f'Downloading {file_name}')
    file_ = requests.get(url)

    with open(file_name, 'wb') as f:
        f.write(file_.content)
        f.close()

    print_prompt(f'Sucessfully downloaded {file_name}')


def main():
    title, pdf_url = get_pdf_url(url)
    download_and_save(pdf_url, title)


if __name__ == '__main__':
    main()
