.. image:: https://travis-ci.org/github/Maxayer/booking_automation.png
  :target: https://travis-ci.org/github/Maxayer/booking_automation

the project allows to commit tests on three browsers: chrome, firefox and opera

launch the tests from the root directory, for example:

pytest -v -s Project/tests/test_class.py

this command launches the tests in Google Chrome

if you want to see the tests running in another browser, note this in the line:

pytest -s -v --browser_name=opera Project/tests/test_class.py

or:

pytest -s -v --browser_name=firefox Project/tests/test_class.py