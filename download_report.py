from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import os
import time

def download_report():
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://fragilestatesindex.org/excel/")

    try:
        link = driver.find_element(By.XPATH, "//a[contains(@href, '.xlsx')]")
        file_url = link.get_attribute("href")

        response = requests.get(file_url)
        filename = os.path.join(download_dir, os.path.basename(file_url))

        with open(filename, "wb") as f:
            f.write(response.content)

        print("File downloaded")

    except Exception as e:
        print("Download failed")

    finally:
        driver.quit()

if __name__ == "__main__":
    download_report()
