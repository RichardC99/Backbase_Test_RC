Feature: Computer can be added, including validation



    Scenario Outline: User can create computer with valid data via API
        Given a user creates a new record with name "<Computer_name>", intro_date "<Introduced_Date>", discon_date "<Discontinued_Date>" and company "<Company>"
        Then the response status should be 200


        Examples:
        |Computer_name         |Introduced_Date|Discontinued_Date|Company                |
        |BBRC_Create_API_Test_1|null           |null             |null                   |
        |BBRC_Create_API_Test_2|2008-02-29     |null             |null                   |
        |BBRC_Create_API_Test_3|2020-04-30     |2002-04-30       |null                   |
        |BBRC_Create_API_Test_4|2004-7-1       |2020-02-29       |Commodore International|
        |BBRC_Create_API_Test_5|null           |2020-02-29       |Netronics              |
        |BBRC_Create_API_Test_6|null           |null             |Thinking Machines      |
        |BBRC_Create_API_Test_7|1997-09-05     |null             |IBM                    |
        |BBRC_Create_API_Test_8|null           |1986-04-07       |null                   |


    Scenario Outline: User cannot create a computer with invalid data via API
        Given a user creates a new record with name "<Computer_name>", intro_date "<Introduced_Date>", discon_date "<Discontinued_Date>" and company "<Company>"
        Then the response status should be 400

        Examples:
        |Computer_name             |Introduced_Date|Discontinued_Date|Company           |
        |null                      |2008-01-01     |2008-01-01       |IBM               |
        |BBRC_Invalid_intro_Date1  |2008/01/01     |null             |null              |
        |BBRC_Invalid_intro_Date2  |29-02-2008     |null             |null              |
        |BBRC_Invalid_intro_Date3  |29/02/2008     |null             |null              |
        |BBRC_Invalid_intro_Date4  |test           |null             |null              |
        |BBRC_Invalid_intro_Date5  |2007-02-29     |2007-02-29       |null              |
        |BBRC_Invalid_Discon_Date1 |null           |2008/01/01       |null              |
        |BBRC_Invalid_Discon_Date2 |null           |29-02-2008       |null              |
        |BBRC_Invalid_Discon_Date3 |null           |29/02/2008       |null              |
        |BBRC_Invalid_Discon_Date4 |null           |test             |null              |
        |BBRC_Invalid_Discon_Date5 |null           |2007-02-29       |null              |
        |BBRC_Invalid_intro_Date5  |2007-02-29     |2007-02-29       |null              |
        |null                      |2008/01/01     |29-02-2008       |null              |
