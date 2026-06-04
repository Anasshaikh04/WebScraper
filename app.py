from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import time


def get_driver():
    options = Options()
    options.add_argument("--headless")         
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


def get_text(product, css):
    """Safely extract text from a CSS selector."""
    try:
        return product.find_element(By.CSS_SELECTOR, css).text.strip()
    except Exception:
        return ""


def get_attr(product, css, attr):
    """Safely extract an attribute from a CSS selector."""
    try:
        return product.find_element(By.CSS_SELECTOR, css).get_attribute(attr)
    except Exception:
        return ""


def is_sponsored(product):
    """Check if a product listing is an ad."""
    try:
        product.find_element(By.XPATH, ".//*[contains(text(),'Sponsored')]")
        return True
    except Exception:
        return False


def scrape_laptops(url="https://www.amazon.in/s?k=laptop"):
    driver = get_driver()
    print("Opening Amazon...")
    driver.get(url)
    time.sleep(5)  # Wait for page to load

    cards = driver.find_elements(
        By.CSS_SELECTOR, "div[data-component-type='s-search-result']"
    )
    print(f"Found {len(cards)} product cards.")

    results = []
    for card in cards:
        results.append({
            "Title":             get_text(card, "h2 span"),
            "Price":             get_text(card, "span.a-price-whole"),
            "Rating":            get_text(card, "span.a-icon-alt"),
            "Image":             get_attr(card, "img", "src"),
            "Ad_Organic_Result": "Ad" if is_sponsored(card) else "Organic",
        })

    driver.quit()
    return results


def save_to_csv(data):
    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"amazon_laptops_{timestamp}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"\nSaved {len(df)} rows → {filename}")
    print(df.head())


if __name__ == "__main__":
    data = scrape_laptops()
    save_to_csv(data)