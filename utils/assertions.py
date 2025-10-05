def assert_url_contains(driver, keyword):
    # verifikasi URL saat ini mengandung kata tertentu
    actual_result = driver.current_url
    expected_result = keyword
    # tambahan if untuk menampilkan pesan jika true
    if expected_result in actual_result:
        print(f"\n {expected_result} was found in {actual_result}")
    # assert memvalidasi kebenaran dan menghentikan eksekusi jika salah
    assert expected_result in actual_result, f"Expected URL to contain '{expected_result}', but got '{actual_result}'"


def assert_text_equal(actual, expected):
    # Verifikasi teks aktual sama dengan yang diharapkan
    assert actual == expected, f"Expected '{expected}', but got '{actual}'"