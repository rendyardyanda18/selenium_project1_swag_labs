import os
import time
import allure

# modified adding to allure
def take_screenshot(driver, folder_ss="screenshots", step_name="step"):
    """Ambil screenshot, simpan ke folder DAN attach ke Allure report."""

    # 1. Pastikan folder local screenshots ada
    os.makedirs(folder_ss, exist_ok=True)

    # 2. Buat filename untuk local storage
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(
        folder_ss,
        f"screenshot_{step_name}_{timestamp}.png"
    )

    # 3. Ambil screenshot
    screenshot_data = driver.get_screenshot_as_png()

    # 4. Simpan ke local folder
    with open(filename, 'wb') as f:
        f.write(screenshot_data)
    print("📸 Screenshot saved locally:", filename)

    # 5. Attach ke Allure report
    allure.attach(
        screenshot_data,
        name=f"screenshot_{step_name}",
        attachment_type=allure.attachment_type.PNG
    )
    print("📸 Screenshot attached to Allure report")

    return filename