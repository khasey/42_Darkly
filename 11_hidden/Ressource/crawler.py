#!/usr/bin/env python3
# by aribeiro

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# URL de base
base_url = 'http://ip/.hidden/'

def check_readme(url, session):
    req = session.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    for link in soup.find_all('a'):
        href = link.get('href')
        if href == "README":
            readme_url = urljoin(url, href)
            readme_content = session.get(readme_url).text
            if "voisin" not in readme_content and "Toujours" not in readme_content and "veux" not in readme_content and "Non" not in readme_content:
                with open('readmes.txt', 'a') as file_handler:
                    # file_handler.write(f"URL: {readme_url}\n")
                    file_handler.write(readme_content)
                    # file_handler.write("\n\n")
        elif href != "../" and href.endswith('/'):
            check_readme(urljoin(url, href), session)

def main():
    with requests.Session() as session:
        check_readme(base_url, session)

if __name__ == "__main__":
    main()
