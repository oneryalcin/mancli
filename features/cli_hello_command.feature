Feature: Testing `hello` argument for cli

  Scenario: Run only with hello
      When user runs command klickbrick hello
      Then CLI prints `hello world`

  Scenario: Run with hello and name argument Oner
      When user runs command klickbrick hello --name Oner
      Then CLI prints `hello Oner`
