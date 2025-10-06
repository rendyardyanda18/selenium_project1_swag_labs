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
    """Setup dan simpan path report Allure dengan timestamp unik"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Folder untuk hasil .json (raw)
    report_dir = os.path.join("reports", timestamp)
    os.makedirs(report_dir, exist_ok=True)

    # Folder untuk HTML hasil generate
    allure_html_dir = os.path.join("allure-report", f"report_{timestamp}")

    # Simpan ke config agar bisa diakses di pytest_sessionfinish
    config._metadata = {
        "timestamp": timestamp,
        "report_dir": report_dir,
        "allure_html_dir": allure_html_dir,
    }

    # Update allure option
    config.option.allure_report_dir = report_dir


def pytest_sessionfinish(session, exitstatus):
    """Generate Allure HTML report otomatis setelah test selesai"""
    metadata = getattr(session.config, "_metadata", {})
    report_dir = metadata.get("report_dir", "reports")
    allure_html_dir = metadata.get("allure_html_dir", "allure-report/latest")

    allure_path = Config.ALLURE_PATH  # Path dari config.py

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

@pytest.fixture
def run_timestamp(request):
    metadata = getattr(request.config, "_metadata", {})
    ts = metadata.get("timestamp")
    if not ts:
        # fallback kalau metadata tidak ada
        ts = "no-timestamp"
    return ts
