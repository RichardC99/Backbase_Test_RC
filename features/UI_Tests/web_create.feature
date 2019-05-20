@web
Feature: Computer can be added, including validation

    Background: Navigate to Create Computer page
       Given A user has navigated to the BB_Test_Webpage


    Scenario: User can open Create Computer screen
       And add a new computer is clicked
       Then the user will be navigated to "Create_Computer" page

    Scenario Outline: User can create computer with valid data
        Given computer <Computer_name> does not exist
        And add a new computer is clicked
        And the User enters <Computer_name> computer name
        And the user enters <Introduced_Date> introduced date
        And the user enters <Discontinued_Date> discontinued date
        And the user selects <Company> company
        When the user clicks create_this_computer
        Then the Computer will be created
        And the number of computers found will increase by 1
        And the computer has been added to the table with the correct information
        And delete computer cleanup create

        Examples:
        |Computer_name     |Introduced_Date|Discontinued_Date|Company                |
        |BBRC_Create_Test_1|null           |null             |null                   |
        |BBRC_Create_Test_2|2008-02-29     |null             |null                   |
        |BBRC_Create_Test_3|2020-04-30     |2002-04-30       |null                   |
        |BBRC_Create_Test_4|2004-7-1       |2020-02-29       |Commodore International|
        |BBRC_Create_Test_5|null           |2020-02-29       |Netronics              |
        |BBRC_Create_Test_6|null           |null             |Thinking Machines      |
        |BBRC_Create_Test_7|1997-09-05     |null             |IBM                    |
        |BBRC_Create_Test_8|null           |1986-04-07       |null                   |


    Scenario Outline: User cannot create a computer with invalid data
        Given add a new computer is clicked
        And the User enters <Computer_name> computer name
        And the user enters <Introduced_Date> introduced date
        And the user enters <Discontinued_Date> discontinued date
        And the user selects <Company> company
        When the user clicks create_this_computer
        Then the user will remain at the add computer screen
        And the correct error message will appear <error>


#
        Examples:
        |Computer_name             |Introduced_Date|Discontinued_Date|Company           |error                     |
        |null                      |2008-01-01     |2008-01-01       |IBM               |name_required             |
        |BBRC_Invalid_intro_Date1  |2008/01/01     |null             |null              |invalid_intro_date_format |
        |BBRC_Invalid_intro_Date2  |29-02-2008     |null             |null              |Invalid_intro_Date_Format |
        |BBRC_Invalid_intro_Date3  |29/02/2008     |null             |null              |Invalid_intro_Date_Format |
        |BBRC_Invalid_intro_Date4  |test           |null             |null              |Invalid_intro_Date_Format |
        |BBRC_Invalid_intro_Date5  |2007-02-29     |2007-02-29       |null              |Invalid_intro_Date_Format |
        |BBRC_Invalid_Discon_Date1 |null           |2008/01/01       |null              |invalid_discon_date_format|
        |BBRC_Invalid_Discon_Date2 |null           |29-02-2008       |null              |invalid_discon_date_format|
        |BBRC_Invalid_Discon_Date3 |null           |29/02/2008       |null              |invalid_discon_date_format|
        |BBRC_Invalid_Discon_Date4 |null           |test             |null              |invalid_discon_date_format|
        |BBRC_Invalid_Discon_Date5 |null           |2007-02-29       |null              |invalid_discon_date_format|
        |BBRC_Invalid_intro_Date5  |2007-02-29     |2007-02-29       |null              |Invalid_intro_Date_Format |
        |null                      |2008/01/01     |29-02-2008       |null              |all_data_invalid          |

    Scenario: User can cancel adding a computer
        Given add a new computer is clicked
        And the User enters Cancel_Button computer name
        And the user enters 2008-01-01 introduced date
        And the user enters 2020-01-01 discontinued date
        And the user selects IBM company
        When the user clicks cancel
        Then the user will be navigated back to the homepage
        And the number of computers found will increase by 0
        And the computer will not be present in the table







