Feature: Computer can be updated, including validation

    Background:Navigate to edit COmputer page
        Given A user has created a computer with known details
        And The user clicks on the computer name

    Scenario: User can open edit computer screeen

        Then the user will be navigated to "Edit_Computer" page

    Scenario Outline: User can Edit computer with valid data
        Given the User edits Computer_name to <Computer_name>
        And the user edits the introduced date to <Introduced_Date>
        And the user edits the discontinued date to <Discontinued_Date>
        And the user edits the company to <Company>
        When the user clicks Save_this_computer
        Then the Computer will be edited
        And the user will be navigated back to "BB_Test_Webpage"
        And the number of computers found will increase by 0
        And the computer has been edited on the table

        Examples:
        |Computer_name   |Introduced_Date|Discontinued_Date|Company           |
        |BBRC_edit_Test_1|null           |null             |null              |
        |BBRC_edit_Test_2|2008-02-29     |null             |null              |
        |BBRC_edit_Test_3|2002-04-30     |2002-04-30       |null              |
        |BBRC_edit_Test_4|2004-7-1       |2020-02-29       |IBM               |
        |BBRC_edit_Test_5|null           |2020-02-29       |RCA               |
        |BBRC_edit_Test_6|null           |null             |Lincoln_laboratory|
        |BBRC_edit_Test_7|1997-09-05     |null             |IBM               |
        |BBRC_edit_Test_8|null           |1986-04-07       |null              |



    Scenario Outline: User cannot edit a computer with invalid data
        Given the User edits Computer_name to <Computer_name>
        And the user edits the introduced date to <Introduced_Date>
        And the user edits the discontinued date to <Discontinued_Date>
        And the user edits the company to <Company>
        When the user clicks Save_this_computer
        Then the correct error message will appear <error>
        And the Computer will not be editd
        And the number of computers found will increase by 0
        And the computer will not have been updated

        Examples:
        |Computer_name        |Introduced_Date|Discontinued_Date|Company           |error                     |
        |null                 |2008-01-01     |2008-01-01       |IBM               |name_required             |
        |Invalid_intro_Date1  |2008/01/01     |null             |null              |Invalid_intro_Date_Format |
        |Invalid_intro_Date2  |29-02-2008     |null             |null              |Invalid_intro_Date_Format |
        |Invalid_intro_Date3  |29/02/2008     |null             |null              |Invalid_intro_Date_Format |
        |Invalid_intro_Date4  |test           |null             |null              |Invalid_intro_Date_Format |
        |Invalid_intro_Date5  |2007-02-29     |2007-02-29       |null              |Invalid_intro_Date_Format |
        |Invalid_Discon_Date1 |2008/01/01     |2008/01/01       |null              |Invalid_Discon_Date_Format|
        |Invalid_Discon_Date2 |29-02-2008     |29-02-2008       |null              |Invalid_Discon_Date_Format|
        |Invalid_Discon_Date3 |29/02/2008     |29/02/2008       |null              |Invalid_Discon_Date_Format|
        |Invalid_Discon_Date4 |test           |test             |null              |Invalid_Discon_Date_Format|
        |Invalid_Discon_Date5 |2007-02-29     |2007-02-29       |null              |Invalid_Discon_Date_Format|

    Scenario: User can cancel editing a computer

        Given the User enters <Cancel_Button>
        And the user enters <2999-01-01>
        And the user enters <2999-01-01>
        And the user selects <IBM>
        When the user clicks cancel
        Then the user will be navigated back to "BB_Test_Webpage"
        And the number of computers found will increase by 0
        And the computer will not have been added to the table

        





