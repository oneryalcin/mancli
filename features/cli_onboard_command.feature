#Feature: `onboard` argument Feature
#
#  Scenario: Toolchain Configuration for git
#    When the user runs KlickBrick 'onboard --toolchain git -- first-name Ole --last-name Christiansen --email o.christiansen@klickbrick.com'
#    Then the git user profile is set with users name
#    And the git email is set with users email
#    And the git commit template is configured