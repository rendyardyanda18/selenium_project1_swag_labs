import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.config import Config
import os
from datetime import datetime
import subprocess
import time

@pytest.fixture # karena tidak terbaca dipindahkan ke root directory
def browser_chrome():
    # Panggil path chromedriver
    service = Service(executable_path=Config.CHROMEDRIVER_PATH)
    # tambahkan opsi saat buka chrome
    options = Options()
    options.add_argument("--start-maximized")
    # Object browser
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(Config.IMPLICIT_WAIT)
    # yield untuk melanjutkan proceed di test
    yield browser
    # dijalankan setelah test selesai
    browser.quit()

def pytest_configure(config):
    """Setup folder report Allure dengan timestamp unik"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = os.path.join("reports", timestamp)
    os.makedirs(report_dir, exist_ok=True)
    config.option.allure_report_dir = report_dir

    # Simpan path report di config untuk diakses oleh hook berikutnya
    config._metadata = {"allure_report_dir": report_dir}

def pytest_sessionfinish(session, exitstatus):
    """Generate Allure report otomatis setelah test selesai dengan timestamp"""
    report_dir = getattr(session.config.option, "allure_report_dir", "reports")

    # Buat folder baru di dalam allure-report berdasarkan timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    allure_base_dir = "allure-report"
    allure_html_dir = os.path.join(allure_base_dir, f"report_{timestamp}")

    allure_path = Config.ALLURE_PATH  # path dari config.py

    try:
        print("\n[Allure] Generating HTML report...")
        subprocess.run(
            [allure_path, "generate", report_dir, "-o", allure_html_dir, "--clean"],
            check=True
        )
        print(f"[Allure] ✅ Report generated at: {allure_html_dir}/index.html")

    except FileNotFoundError:
        print(f"[Allure] ❌ Allure CLI not found at: {allure_path}")
    except subprocess.CalledProcessError:
        print("[Allure] ⚠️ Gagal generate report. Cek folder report.")
    except Exception as e:
        print(f"[Allure] ⚠️ Unexpected error: {e}")