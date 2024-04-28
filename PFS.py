from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def extract_linked_page_text(base_url, link_url):
    full_url = urljoin(base_url, link_url)
    response = requests.get(full_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        text_content = soup.get_text(separator="\n", strip=True)
        return text_content
    else:
        print(f"Failed to fetch content from: {full_url}")
        return None


base_url = "https://www.fullstackpython.com/"
response = requests.get(base_url)
pfs_page = response.text
soup = BeautifulSoup(pfs_page, "html.parser")

article_links = []
content = soup.find_all(class_="tc")
for article_tag in content:
    anchor_tag = article_tag.find("a")
    if anchor_tag:
        link_url = anchor_tag["href"]
        article_links.append(link_url)

with open("linked_page_contents.txt", "w", encoding="utf-8") as file:
    for link_url in article_links:
        linked_page_text = extract_linked_page_text(base_url, link_url)
        if linked_page_text:
            file.write(linked_page_text)
            file.write("\n\n")
