Feature: Computer can be added, including validation

    Scenario: Delete Computer

        Given A user has created a computer with known details
        And the User navigates to the Update Computer screen
        When the Delete Computer button is clicked
        Then the Computer is deleted from the table
        And the number of computers found will decrease by 1
        And the computer will not be able to be found






