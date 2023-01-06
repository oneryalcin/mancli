from behave import *
import subprocess
use_step_matcher("re")


# ------------------------------------------------------------------------------------------------
@when("user runs command klickbrick hello")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = subprocess.run(
        ["poetry", "run", "klickbrick", "hello"], capture_output=True, text=True
    )


@then("CLI prints `Hello world`")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(f'CONTEXT: {context.result}')
    assert context.result.stdout == "Hello world\n"
# ----------------------------------------------------------------------------------------------------


@when("user runs command klickbrick hello --name Oner")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = subprocess.run(
        ["poetry", "run", "klickbrick", "hello", "--name", "Oner"], capture_output=True, text=True
    )


@then("CLI prints `Hello Oner`")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.result.stdout == "Hello Oner\n"
# ----------------------------------------------------------------------------------------------------
