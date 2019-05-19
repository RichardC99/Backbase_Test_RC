# Summary

Manual Tests are stored in the Manual Test spreadsheet. These tests have all be run an da number of issues identified. I have also indicated which of these tests have been automated. 
Please note that due to the way the automation code has been structured it is easy to increase/decrease the number of validation tests as required. 

I have also included details of API manual testing I completed using Postman. 

The Automation Framework is split into 2 secions, Web testing utilising Selenium and API testing using code I have written in order to be able test the API. 
In both cases the tests have been set up using Behave. 

The only Hardcoded values are test setup data (Details of computer to be edited/deleted) all other test data can be dynamically deined int he relevant Behave feature file. 

All UI tests initially carry out a check to find and delete any data that is identical to the intended test data. this is done to avoid the possibility of tests failing/passing due to bad data. 
Each test also has a cleanup stage carried out at th eend of each scenario. 

 

# Test Coverage


# Installation (Windows/linux PC)
1. Install python 3.6 (see instructions below) and make sure it is enabled if multiple versions of Python on system
2. Install virtualenv `pip install virtualenv`
3. Make a new directory called something like 'virtual-behave' and go into that directory
4. Create a Python virtual environment in that directory with `virtualenv .`
5. Activate the virtual environment from directory created in step 3.
  - Windows `Scripts\activate.bat`
  - Linux `source bin/activate`
6. Git clone this project into the new virtualenv directory created in step 3 `git clone https://github.com/RichardC99/Computers_Database_Tests_RC.git`
7. Change into behave directory
8. Install Behave and all it's dependencies using `pip install -r requirements.txt`
9. Install an applicable IDE, these tests where written and run using JetBrains PyCharm a community edition is available from https://www.jetbrains.com/pycharm/download/#section=windows
10. Requirements.txt contains the additional libraries required to run tests. PyCharm will automatically ask to install these the first time you open the project. In addition pandas may require an install of lxml (pip install lxml) 

# Config 
1. copy config.py.example to config.py and set values for your environment for 
  - url - set as default to "http://computer-database.gatling.io/computers"
  - driver - which browser to test, firefox or chrome
  - <browser>_driver_path - local directory path to driver executable
  

# Run tests
1. Activate the virtual environment
  - Windows `Scripts\activate.bat`
  - Linux `source bin/activate`
2. to run a specific test pass the path or filename of feature file to `behave` 
 - `behave "Backbase_Test_RC\features\<test_name>"` # run individual feature test
 - `behave "Backbase_Test_RC\features\"` # run all tests
3. to run tests from within an IDE for debugging etc run via `run_behave.py`. To run specific tests edit `run_behave.py` and add path to feature file into `behave_main(".")`
4. Web_UI tests require the @web to distinguish from non UI tests. Note without this tag present Selenium Webdriver will not be run. 
# Getting started with behave
http://behave.readthedocs.io/en/latest/tutorial.html

# Coding standards
All python code has been written to to adhere to pep8 style guide (https://www.python.org/dev/peps/pep-0008/)

