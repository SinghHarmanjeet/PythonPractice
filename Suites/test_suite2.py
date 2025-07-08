import pytest

if __name__ == "__main__":
    pytest.main([
        "src/test_erp_login.py",
        "--alluredir=allure-results"

    ]) 