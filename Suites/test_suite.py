import pytest

if __name__ == "__main__":
    pytest.main([
        "src/test_fill_timesheet.py",
        "src/test_applyleave.py",
        "--alluredir=allure-results"

    ]) 