class Config:
    # URL
    URL_MAINPAGE = "https://www.saucedemo.com/"
    # Browser
    BASE_PATH = "D:\\Selenium Try\\pythonbasics\\browser_driver"
    CHROMEDRIVER_PATH = BASE_PATH +"\\chromedriver.exe"
    FIREFOX_PATH = BASE_PATH +"\\geckodriver.exe"

    # Path ke Allure CLI (langsung ke .bat) pakai r agar tidak usah ubah ke \\
    ALLURE_PATH = r"C:\Users\Rendy Theoanantyo\scoop\apps\allure\current\bin\allure.bat"

    # timeout
    IMPLICIT_WAIT = 15

    # User & Pass
    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"
    PERFORMANCE_USER = "performance_glitch_user"
    PASSWORD = "secret_sauce"
