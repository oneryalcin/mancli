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


@then("CLI prints `hello world`")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.result.stdout == "hello world\n"
# ----------------------------------------------------------------------------------------------------


@when("user runs command klickbrick hello --name Oner")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = subprocess.run(
        ["poetry", "run", "klickbrick", "hello", "--name", "Oner"], capture_output=True, text=True
    )


@then("CLI prints `hello Oner`")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.result.stdout == "hello Oner\n"
# ----------------------------------------------------------------------------------------------------
