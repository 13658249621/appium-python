#!/bin/bash
pytest tests --alluredir=reports/allure_results
allure serve reports/allure_results
