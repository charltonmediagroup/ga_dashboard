import requests
from bs4 import BeautifulSoup

# 1️⃣ The URL to scrape
url = "https://www.traveldailymedia.com/category/exclusives/"  # <-- Change this

# 2️⃣ Fetch the page
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Failed to fetch page: {response.status_code}")
    exit()

html = response.text

# 3️⃣ Parse HTML
soup = BeautifulSoup(html, "html.parser")

# 4️⃣ Extract titles and links
results = []
for h2 in soup.find_all("h2", class_="archive-title"):
    a_tag = h2.find("a")
    if a_tag:
        title = a_tag.get_text(strip=True)
        link = a_tag.get("href")
        results.append((title, link))

# 5️⃣ Generate HTML
html_output = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Scraped Titles</title>
<style>
body { font-family: Arial, sans-serif; padding: 20px; }
h1 { color: #333; }
.result { margin-bottom: 10px; }
.result a { text-decoration: none; color: #0066cc; }
.result a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>Scraped Titles</h1>
<div id="results">
"""

if results:
    for title, link in results:
        html_output += f'<div>{title}</div>\n'
else:
    html_output += "<p>No titles found.</p>"

html_output += """
</div>
</body>
</html>
"""

# 6️⃣ Save HTML to file
with open("scraped_titles.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("Scraping complete! Open 'scraped_titles.html' to see results.")
