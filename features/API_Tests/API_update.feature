@web
Feature: Computer can be updated, including validation

    Background:Navigate to edit Computer page
        Given A user has created a computer with known details


    Scenario Outline: User can Edit computer with valid data
        Given computer <Computer_name> does not exist
        When a user updates record with name "<Computer_name>", intro_date "<Introduced_Date>", discon_date "<Discontinued_Date>" and company "<Company>"
        Then the response status should be 200
        Then the computer is updated on the table with the correct information
        And delete computer cleanup edit

        Examples:
        |Computer_name   |Introduced_Date|Discontinued_Date|Company           |
        |BBRC_edit_Test_1|null           |null             |null              |
#        |BBRC_edit_Test_2|2008-02-29     |null             |null              |
#        |BBRC_edit_Test_3|2020-04-30     |2002-04-30       |null              |
#        |BBRC_edit_Test_4|2004-7-1       |2020-02-29       |IBM               |
#        |BBRC_edit_Test_5|null           |2020-02-29       |RCA               |
#        |BBRC_edit_Test_6|null           |null             |Thinking Machines |
#        |BBRC_edit_Test_7|1997-09-05     |null             |IBM               |
#        |BBRC_edit_Test_8|null           |1986-04-07       |null              |



    Scenario Outline: User cannot edit a computer with invalid data
        Given the User navigates to the Update Computer screen
        And the User updates <Computer_name> computer name
        And the user updates <Introduced_Date> introduced date
        And the user updates <Discontinued_Date> discontinued date
        And the user updates <Company> company
        When the user clicks Save_this_computer
        Then the user will remain at the add computer screen
        Then the correct error message will appear <error>
        And Delete computer cleanup validation

        Examples:
        |Computer_name                  |Introduced_Date|Discontinued_Date|Company   |error                     |
        |null                           |2008-01-01     |2008-01-01       |IBM       |name_required             |
        |BBRC_edit_invalid_intro_date1  |2008/01/01     |null             |null      |invalid_intro_date_format |
        |BBRC_edit_invalid_intro_date2  |29-02-2008     |null             |null      |Invalid_intro_Date_Format |
        |BBRC_edit_invalid_intro_date3  |29/02/2008     |null             |null      |Invalid_intro_Date_Format |
        |BBRC_edit_invalid_intro_date4  |test           |null             |null      |Invalid_intro_Date_Format |
        |BBRC_edit_invalid_intro_date5  |2007-02-29     |null             |null      |Invalid_intro_Date_Format |
        |BBRC_edit_invalid_discon_date1 |null           |2008/01/01       |null      |invalid_discon_date_format|
        |BBRC_edit_invalid_discon_date2 |null           |29-02-2008       |null      |invalid_discon_date_format|
        |BBRC_edit_invalid_discon_date3 |null           |29/02/2008       |null      |invalid_discon_date_format|
        |BBRC_edit_invalid_discon_date4 |null           |test             |null      |invalid_discon_date_format|
        |BBRC_edit_invalid_discon_date5 |null           |2007-02-29       |null      |invalid_discon_date_format|
        |null                           |2008/01/01     |29-02-2008       |null      |all_data_invalid          |

    Scenario: User can cancel editing a computer
        Given the User navigates to the Update Computer screen
        And the User updates Cancel_Button computer name
        And the user updates 2999-01-01 introduced date
        And the user updates 2999-01-01 discontinued date
        And the user updates IBM company
        When the user clicks cancel
        Then the user will be navigated back to the homepage
        And the number of computers found will stay the same
        And the computer will not have been updated
        And Delete computer cleanup validation






