Feature: Testing `hello` argument for cli

  Scenario: Run only with hello
      When user runs command klickbrick hello
      Then CLI prints `hello world`
