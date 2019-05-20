Feature: Computer can be added, including validation

    Scenario: Delete Computer via API

        Given A user has created a computer with known details for API deletion
        When  The Computer is Deleted via the API
        Then the response status should be 200
        And the Computer will have been deleted from the UI





