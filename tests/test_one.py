# coding: utf-8
import time

import allure
import pytest
import logging

from models.datasets import DatasetsPage
from models.login import LoginPage
from services.dataset_service import DatasetService
from client.http_client import HttpClient
from env import *
from playwright.sync_api import Page

from pathlib import Path

# note loging configuration will be moved to separate file
Path("logs").mkdir(parents=True, exist_ok=True)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("{0}/{1}.log".format('logs', 'current'))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)
rootLogger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


@pytest.fixture(scope='module', autouse=True)
def test_suite_setup(request):
    # test connection

    try:
        conn = DatasetService(HttpClient(BASE_URL)).healthcheck()
    except:
        raise pytest.UsageError("Errors during connection to {0}, "
                                "aborting all suite".
                                format(BASE_URL))

    if conn.status_code != 200:
        raise pytest.UsageError("Response code: {0}, Issue with getting list".format(conn.status))

    def test_suite_teardown():
        print('\nSUITE TEARDOWN WILL BE HERE')

    request.addfinalizer(test_suite_teardown)


@pytest.fixture(scope='function')
def client(request):
    # perform some actions like
    # DB().delete_user(TEST_CREDENTIALS['username'])
    client = DatasetService(HttpClient(BASE_URL))
    yield client

    def activate_user_teardown():
        # do teardown
        pass

    request.addfinalizer(activate_user_teardown)


@allure.feature('Datasets')
@allure.story('Datasets Story')
@pytest.mark.datasets
def test_datasets_list(client):
    """
    Testing datasets list
    """

    with allure.step("Step1: Check response HTTP Status Code"):
        resp = client.get_datasets()
        assert resp.status_code == 200

    with allure.step("Step2: Check if response not empty"):
        resp = client.get_datasets()
        assert len(resp.json()) != 0


@allure.feature('UI')
@allure.story('UI base page')
@pytest.mark.datasets
def test_main_ui_page(page: Page):
    """
    Example of simple UI
    """
    with allure.step("Step1: Log into application"):
        full_url = BASE_URL + '/login'

        # Example how log useful info into file or console
        logging.info('Go to ' + full_url)

        login_page = LoginPage(page)
        login_page.login(G_USER, G_PASS)

    with allure.step("Step2: check button 'Greate new dataset'"):
        dataset_page = DatasetsPage(page)
        dataset_page.create_new_dataset("DataSetForTest001")

    with allure.step("Step3: Verify header"):
        dataset_page.verify_header()

    # Example how to perform snapshot for report
    allure.attach(page.screenshot())
