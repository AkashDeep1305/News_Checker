import requests
import csv
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://www.bbc.com/news"  # Change to any news site
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = [item.text.strip() for item in soup.find_all("p")]
    data = [(headline, 1) for headline in headlines[:40]]  # Add label 1 to each headline

    with open("backend/news_headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["text", "label"])  # Write headers
        writer.writerows(data)  # Write headline data
    
    print("News headlines saved to news_headlines.csv")

if __name__ == "__main__":
    scrape_news()
