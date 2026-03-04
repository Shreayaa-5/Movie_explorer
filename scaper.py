from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

def get_tamil_movies_selenium(target_count=100):
    # 1. Setup Chrome to run 'headless' (in the background) or visible
    options = Options()
    # options.add_argument("--headless") # Uncomment this to hide the browser window
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = "https://www.imdb.com/search/title/?title_type=feature&primary_language=ta"
    
    driver.get(url)
    time.sleep(5) # Give the page time to load

    all_movies = []
    seen_titles = set()

    print("--- 🚀 Starting Human-Like Scroll ---")

    # 2. Scroll and Collect
    while len(all_movies) < target_count:
        # Find all current movie items on the screen
        items = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
        
        for item in items:
            try:
                name = item.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text.strip()
                
                if name.lower() not in seen_titles:
                    # Find description
                    desc = item.find_element(By.CSS_SELECTOR, ".ipc-html-content-inner-div").text.strip()
                    
                    all_movies.append({"Name": name, "Description": desc})
                    seen_titles.add(name.lower())
                    
                if len(all_movies) >= target_count:
                    break
            except:
                continue

        print(f"Current Count: {len(all_movies)}")

        # 3. Scroll to the bottom to trigger "Load More" or pagination
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) # Wait for new movies to pop up

        # If we get stuck, try to find a 'Load More' button if it exists
        try:
            load_more = driver.find_element(By.CLASS_NAME, "ipc-see-more__button")
            load_more.click()
            time.sleep(3)
        except:
            pass 

    driver.quit()

    # 4. Save to CSV
    with open("tamil_movies_final.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Description"])
        writer.writeheader()
        writer.writerows(all_movies)

    print(f"\n✅ SUCCESS! Saved {len(all_movies)} UNIQUE movies using Selenium.")

if __name__ == "__main__":
    get_tamil_movies_selenium(200)