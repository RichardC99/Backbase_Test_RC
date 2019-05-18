@web
Feature: Computer can be updated, including validation

    Background:Navigate to edit Computer page
        Given A user has created a computer with known details and navigated to the edit screen

    Scenario: User can open edit computer screeen

        Then the user will be navigated to "Edit_Computer" page
        And delete computer cleanup

    Scenario Outline: User can Edit computer with valid data
        Given the User enters <Computer_name> computer name
        And the user enters <Introduced_Date> introduced date
        And the user enters <Discontinued_Date> discontinued date
        And the user selects <Company> company
        When the user clicks Save_this_computer
        Then the Computer will be updated
        And the user will be navigated back to the homepage
        And the number of computers found will stay the same
        And the computer is updated on the table with the correct information
        And delete computer cleanup

        Examples:
        |Computer_name   |Introduced_Date|Discontinued_Date|Company           |
        |BBRC_edit_Test_1|null           |null             |null              |
#        |BBRC_edit_Test_2|2008-02-29     |null             |null              |
#        |BBRC_edit_Test_3|2002-04-30     |2002-04-30       |null              |
#        |BBRC_edit_Test_4|2004-7-1       |2020-02-29       |IBM               |
#        |BBRC_edit_Test_5|null           |2020-02-29       |RCA               |
#        |BBRC_edit_Test_6|null           |null             |Thinking Machines|
#        |BBRC_edit_Test_7|1997-09-05     |null             |IBM               |
#        |BBRC_edit_Test_8|null           |1986-04-07       |null              |
#
#
#
#    Scenario Outline: User cannot edit a computer with invalid data
#        Given the User enters <Computer_name> computer name
#        And the user enters <Introduced_Date> introduced date
#        And the user enters <Discontinued_Date> discontinued date
#        And the user selects <Company> company
#        When the user clicks Save_this_computer
#        Then the correct error message will appear <error>
#        And the Computer will not be edited
#        And the number of computers found will increase by 0
#        And the computer will not have been updated
##
#        Examples:
#        |Computer_name                  |Introduced_Date|Discontinued_Date|Company   |error                     |
#        |null                           |2008-01-01     |2008-01-01       |IBM       |name_required             |
#        |BBRC_edit_invalid_intro_date1  |2008/01/01     |null             |null      |invalid_intro_date_format |
#        |BBRC_edit_invalid_intro_date2  |29-02-2008     |null             |null      |Invalid_intro_Date_Format |
#        |BBRC_edit_invalid_intro_date3  |29/02/2008     |null             |null      |Invalid_intro_Date_Format |
#        |BBRC_edit_invalid_intro_date4  |test           |null             |null      |Invalid_intro_Date_Format |
#        |BBRC_edit_invalid_intro_date5  |2007-02-29     |null             |null      |Invalid_intro_Date_Format |
#        |BBRC_edit_invalid_discon_date1 |null           |2008/01/01       |null      |invalid_discon_date_format|
#        |BBRC_edit_invalid_discon_date2 |null           |29-02-2008       |null      |invalid_discon_date_format|
#        |BBRC_edit_invalid_discon_date3 |null           |29/02/2008       |null      |invalid_discon_date_format|
#        |BBRC_edit_invalid_discon_date4 |null           |test             |null      |invalid_discon_date_format|
#        |BBRC_edit_invalid_discon_date5 |null           |2007-02-29       |null      |invalid_discon_date_format|
#        |null                           |2008/01/01     |29-02-2008       |null      |all_data_invalid          |
#
#    Scenario: User can cancel editing a computer
#
#        Given the User enters <Cancel_Button>
#        And the user enters <2999-01-01> introduced date
#        And the user enters <2999-01-01> discontinued date
#        And the user selects <IBM> company
#        When the user clicks cancel
#        Then the user will be navigated back to "BB_Test_Webpage"
#        And the number of computers found will increase by 0
#        And the computer will not have been updated
#
#





