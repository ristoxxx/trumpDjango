[![Daily API Call](https://github.com/ristoxxx/trumpDjango/actions/workflows/dailyapicall.yml/badge.svg)](https://github.com/ristoxxx/trumpDjango/actions/workflows/dailyapicall.yml)
# Django app to store and serve news articles about Trump

This is a Django based backend that runs automatically once a day and stores news about Trump.
Backend is hosted at [Railway](https://trumpdjango-production.up.railway.app/) and it has 3 endpoints.
    /           Root has a micro frontend to display stored data
    /store      This endpoit fetches current news, Filters those that have word "Trump" and stores those
    /read       This endpoint delivers stored data in JSON format to be used elsewhere

