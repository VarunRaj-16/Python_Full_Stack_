# DAY 35 - WEB SCRAPING USING PYTHON
import requests
from bs4 import BeautifulSoup
print("1. BASIC WEB SCRAPING - Codegnan Website")
url = "https://codegnan.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print("Website Title:", soup.title.text)
print("First Heading:", soup.h1.text)   # Extract first heading
print("\nAll Hyperlinks:")   # Extract all hyperlinks
for link in soup.find_all("a")[:5]:   # First 5 links
    print(link.get("href"))
print("\nAll Images:")  # Extract all images
for img in soup.find_all("img")[:5]:
    print(img.get("src"))
print("2. COMMON METHODS")
print("find('h1'):", soup.find("h1").text)
print("find_all('p') count:", len(soup.find_all("p")))
print("select('a') count:", len(soup.select("a")))
print("3. HTML PARSING & ATTRIBUTES")
title = soup.title
print("Title Text:", title.text)
print("Title Attribute:", title.get("class"))
# Extract all links
for link in soup.find_all("a"):
    print(link.get("href"))
