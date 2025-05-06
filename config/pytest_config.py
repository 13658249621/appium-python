# pytest_config.py
import pytest

# 自定义 pytest 标记
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
