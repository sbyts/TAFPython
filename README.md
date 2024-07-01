# TAFPython

### API tests:

As a runner "pytest" is used. It has configurable instruments for organizing setup, tear down sections on suite and all scope levels, run by labels, sending data to test etc. https://docs.pytest.org/en/6.2.x/fixture.html 
- from my point of view each automation framework should be able to log necessary data into the console or file with appropriate level. the simplest and powerful - "logging" module.
- for paralization test  this plugin can be used https://pypi.org/project/pytest-xdist/
- A http client for API call for http server was constructed based on "requests" but https://github.com/swagger-api/swagger-codegen an alternative solution (just need to check a compatibility of the latest version for python 3.x)

### UI tests:

2 variants can be in this case "Selenium" and "Playwright"
comparison:
https://www.axelerant.com/blog/cypress-selenium-playwright

I prefere:

https://playwright.dev/python/docs/api/class-playwright

Advantages:

Playwright can run tests on Chromium, WebKit and Firefox browsers as well as branded browsers such as Google Chrome and Microsoft Edge
https://playwright.dev/python/docs/browsers

With Playwright you can test your app on any browser as well as emulate a real device such as a mobile phone or tablet
https://playwright.dev/python/docs/emulation
if such emulation is not enough - we can find solution here https://www.browserstack.com/

if you need some specific version(of several last versions of a certain browser) as an alternative is https://www.selenium.dev/documentation/grid/ but requires more effort and resources.
https://playwright.dev/python/docs/selenium-grid (for Playwright  Selenium Grid on experimental level - potentially will be implemented in future. 

### Performance testing:

can be organized based on modules "asyncio", "multiprocessing", "threading" or specific solution like "Locust" It depends on infrastructure and requirements. 

### Test environment preparation:
Python version: 3.x


* ** Lib's and packages:**
```
pip install -U pytest
pip install allure-pytest
pip install pytest-html
pip install pytest-playwright
pip install requests
```

* ** install playwright:**
use command:
```
playwright install
```
see more details at:
https://playwright.dev/python/docs/intro#installing-playwright-pytest

* **update credentials in env file**
note: file should be located only locally or data should be encrypted
./env

* **verbose run in console:**

```
run:
 
pytest -s -v -q  ./tests/test_one.py
```
* **with report generation and opening in browser:**

```
pytest --alluredir ./allure_rep ./tests/test_one.py

bin\allure.bat serve .\allure_rep
```
note: see doc for allure how it works

* **can be run by severities, features, story** (Example)

```
pytest my_tests/ --allure_severities=critical,blocker
pytest my_tests/ --allure_features=feature1,feature2
pytest my_tests/ --allure_features=feature1,feature2 --allure_stories=story1,story2
```

* **can be run by specific tag (pytest marker)**

```
pytest -s -v -q  ./tests/./tests/test_one.py -m datasets

```

* ** with html report generation**

```
pytest --html=report.html  -s -v -q  ./tests/test_one.py

```

* ** using with poetry**

```
pip install poetry
poetry install
```

run:
```
poetry run pytest --alluredir ./allure_rep ./tests/test_one.py
```
file with configuration - pyproject.toml