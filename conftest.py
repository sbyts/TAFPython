from typing import Generator
from playwright.sync_api import Playwright, BrowserContext
import pytest


@pytest.fixture()
def context(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    context = playwright.chromium.launch_persistent_context(
        "",
        headless=False,
        args=[
            f"--disable-component-extensions-with-background-pages",
            f"--disable-blink-features=AutomationControlled",
            f"--disable-web-security",
            f"--allow-running-insecure-content"

        ],
    )
    yield context
    context.close()


def pytest_configure(config):
    config.addinivalue_line("markers", "datasets: test suite datasets")
    config.addinivalue_line(
        "markers", "mark_with(arg, arg2): this marker takes arguments."
    )
