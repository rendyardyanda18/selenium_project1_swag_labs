import os
import allure

def take_screenshot(driver, step_name="step", run_timestamp=None, base_folder="screenshots"):
    """
    Ambil screenshot, simpan ke folder sesuai timestamp run,
    dan attach ke Allure report.
    """

    # Pakai folder base + timestamp run
    if run_timestamp is None:
        # fallback kalau run_timestamp tidak diberikan
        run_timestamp = "no-timestamp"
    folder_ss = os.path.join(base_folder, run_timestamp)
    os.makedirs(folder_ss, exist_ok=True)

    # Nama file
    filename = os.path.join(folder_ss, f"screenshot_{step_name}.png")

    # Ambil screenshot
    screenshot_data = driver.get_screenshot_as_png()

    # Simpan ke folder
    with open(filename, 'wb') as f:
        f.write(screenshot_data)
    print("📸 Screenshot saved locally:", filename)

    # Attach ke Allure
    allure.attach(
        screenshot_data,
        name=f"screenshot_{step_name}",
        attachment_type=allure.attachment_type.PNG
    )
    print("📸 Screenshot attached to Allure report")

    return filename