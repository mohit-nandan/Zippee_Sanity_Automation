from selenium import webdriver

def create_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    else:
        raise Exception(f"{browser} not supported")
