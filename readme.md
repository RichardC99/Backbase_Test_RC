Manual Tests are stored in the Manual Test spreadsheet. These tests have all been run and a number of issues identified. I have also indicated which of these tests have been automated. 
Please note that due to the way the automation code has been structured it is easy to increase/decrease the number of validation tests as required. 

I have also included details of API manual testing I completed using Postman. 

The Automation Framework is split into 2 sections, Web testing utilising Selenium and API testing in both cases the tests have been set up using Behave. 

The only Hardcoded values are test setup data (Details of computer to be edited/deleted) all other test data can be dynamically edited in the relevant Behave feature file. 

All UI tests initially carry out a check to find and delete any data that is identical to the intended test data. this is done to avoid the possibility of tests failing/passing due to bad data. 
Each test also has a clean-up stage carried out at the end of each scenario. 

Future Enhancment
- I have started the process of adding a Janitor Cleanup method which would replace the current cleanup steps, this would provide a cleaner cleanup process. 
- The API tests currently utilise UI code for confirming the correct process has taken place, in future I would look to chage this to utilise the API to do all validation directly 
- Currently setup is completed by the Selenium Steps, in future I would look to refactor to make better use of the Create and Delete functionality of the API tests for setup and cleanup steps. 


# Installation (MAC, OSX)
1. Install python 3.6 and make sure it is set as the project interpreter for your IDE
2. Git clone this project into your chosen directory git clone `git clone https://github.com/RichardC99/Computers_Database_Tests_RC.git`
3. Install Selenium, ChromeDriver and Behave
    - Selenium = pip3 install selenium 
    - Behave = sudo pip install behave
    - Chromedriver = brew cask install chromedriver
   

Alternativly the requirements.txt file lists all required compnents. PyCharm will automatically prompt the user and then install these on opening the project

# Config (OSX)
Copy the config mac example txt file into config.py 
Because HomeBrew installs Chrome Driver directly into the path you do not need to specify the home directory of the chromedriver.exe
In the environmtent file ensure the correct context.browser line is commented out 

        context.browser = webdriver.Chrome() ---- un commented

        context.browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options) ---- commented out (WIndows/Linux only)

# Run Tests(OSX)
In the terminal navigate to the location of the features folder 
To run tests enter behave features\(the chosen feature file to run)
Running behave features/ will run all feature files and tests. 


# Installation (Windows/linux PC)
1. Install python 3 and make sure it is enabled if multiple versions of Python on system
2. Install virtualenv `pip install virtualenv`
3. Make a new directory called something like 'virtual-behave' and go into that directory
4. Create a Python virtual environment in that directory with `virtualenv .`
5. Activate the virtual environment from directory created in step 3.
  - Windows `Scripts\activate.bat`
  - Linux `source bin/activate`
6. Git clone this project into the new virtualenv directory created in step 3 `git clone https://github.com/RichardC99/Computers_Database_Tests_RC.git`
7. Change into behave directory
8. Install Behave and all its dependencies using `pip install -r requirements.txt`
9. Install Selenium 
10. Install an applicable IDE, these tests where written and run using JetBrains PyCharm a community edition is available from https://www.jetbrains.com/pycharm/download/#section=windows
11. Requirements.txt contains the additional libraries required to run tests. PyCharm will automatically ask to install these the first time you open the project. In addition, pandas may require an install of lxml (pip install lxml) 

# Config Windows/ Linux
1. copy config.py.example to config.py and set values for your environment for 
  - url - set as default to "http://computer-database.gatling.io/computers"
  - driver - which browser to test, firefox or chrome
  - <browser>_driver_path - local directory path to driver executable (chrome driver etc) 
 
        context.browser = webdriver.Chrome() ---- comment out for Windows

        context.browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options) ---- Not commented out (WIndows/Linux only)

  

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
All python code has been written to adhere to pep8 style guide (https://www.python.org/dev/peps/pep-0008/)

