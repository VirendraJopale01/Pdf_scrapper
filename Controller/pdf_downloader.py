from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time




def download_pdf(url, download_directory, filename):
    """
    Downloads a PDF from the given URL to the specified directory with the given filename.

    Args:
        url (str): The URL of the PDF to be downloaded.
        download_directory (str): The directory where the PDF should be downloaded.
        filename (str): The name to save the downloaded PDF as.

    Returns:
        str: The path to the downloaded PDF file, or None if an error occurred.
    """
    # Set up Chrome options for headless download
    chrome_option = Options()
    chrome_option.add_experimental_option('prefs', {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True  # Ensure PDFs are downloaded instead of opened
    })
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    chrome_option.add_argument(f"user-agent={user_agent}")
    chrome_option.add_argument("--disable-blink-features=AutomationControlled")
    chrome_option.add_argument("--headless")  # Run in headless mode for no GUI

    # Initialize the Chrome driver  options
    driver = webdriver.Chrome(options=chrome_option)
    
    driver.maximize_window()  # Maximize window to ensure all elements are visible
    driver.get(url)  # Navigate to the URL
    wait = WebDriverWait(driver, 10)  # Create a WebDriverWait object with a timeout of 10 seconds

    try:
        # Construct the full path to the downloaded file
        downloaded_file = os.path.join(download_directory, filename)
        print(downloaded_file)

        # Check if the file already exists
        if os.path.exists(downloaded_file):
            print('Exist Already')
            return None
        
        # Wait for the file to be downloaded
        while not os.path.exists(downloaded_file):
            time.sleep(1)
            print("Waiting for the download to complete...")
            
        print(f"Downloaded file: {downloaded_file}")
        return downloaded_file
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    finally:
        driver.quit()  # Ensure the driver is quit in all cases

def threaded_download(url,directories,filename):
    file=download_pdf(url,directories,filename)
    print(f'Downloaded file: {file}')    
    