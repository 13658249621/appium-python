#!/bin/bash
#pytest -m smoke tests --alluredir=reports/allure_results
pytest tests --alluredir=reports/allure_results
allure serve reports/allure_results
