Feature: Testing `hello` argument for cli

  Scenario: Run only with hello
      When user runs command klickbrick hello
      Then CLI prints `Hello world`

  Scenario: Run with hello and name argument Oner
      When user runs command klickbrick hello --name Oner
      Then CLI prints `Hello Oner`
