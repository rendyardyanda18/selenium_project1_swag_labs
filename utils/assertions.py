from selenium.common.exceptions import NoSuchElementException

class Assertions:
    """Kelas utility untuk berbagai macam assertion di testing."""

    @staticmethod
    def assert_url_contains(driver, keyword):
        """
        Verifikasi URL saat ini mengandung kata tertentu.
        Jika benar, print pesan. Jika salah, raise AssertionError.
        """
        actual_result = driver.current_url
        expected_result = keyword
        if expected_result in actual_result:
            print(f"\n✅ {expected_result} was found in {actual_result}")
        assert expected_result in actual_result, \
            f"Expected URL to contain '{expected_result}', but got '{actual_result}'"

    @staticmethod
    def assert_text_equal(actual, expected):
        """
        Verifikasi teks aktual sama dengan yang diharapkan.
        """
        assert actual == expected, f"Expected '{expected}', but got '{actual}'"


    @staticmethod
    def assert_error_contains(actual, expected):
        """
        Verifikasi pesan error sama dengan yang diharapkan.
        """
        if actual == expected:
            print(f"\n✅ Error message passed. actual: {actual}, expected: {expected}")
        assert actual == expected, f"Error message is different. actual: {actual}, expected: {expected}"

    @staticmethod
    def assert_element_displayed(element_callable, step_name="Element"):
        """
        Verifikasi element ditampilkan di halaman, handle 3 kemungkinan:
        1. Element ada dan tampil → pass
        2. Element ada tapi hidden → fail
        3. Element tidak ada → fail
        element_callable : function/lambda yang mengembalikan element
        """
        try:
            elem = element_callable()  # panggil fungsi untuk ambil element
            if elem.is_displayed():
                print(f"\n✅ {step_name} appeared")
            else:
                print(f"\n❌ {step_name} found but hidden")
                assert False, f"{step_name} found but hidden"
        except NoSuchElementException:
            print(f"\n❌ {step_name} not found")
            assert False, f"{step_name} not found"