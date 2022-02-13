1)Install Python, along with selenium , pytest, pipenv packages.
2)The pages for the project are maintained mainly in the accounts folder.
3)The test is maintained in the tests/account folder.
4)Pycharm IDE was used for test execution.
5)Script can also be run from a command prompt.
Cd to the directory where the test file exists: 
eg: sample_project\smartbizloans\tests\account
And then run the command: pipenv run pytest test_register.py

-------------
Chromedriver needs to be seperately downloaded and it was placed in the path:C:\Drivers in order to run the tests in Chrome browser
Emailid is maintained in the conftest.py