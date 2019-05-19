# Summary

Behave is a Python based BDD framework (https://behave.readthedocs.io/en/latest/) used to write automated tests for Smartpipe components

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

