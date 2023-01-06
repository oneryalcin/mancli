# from behave import *
# import subprocess
#
# use_step_matcher("re")
#
#
# @when(
#     "the user runs KlickBrick 'onboard --toolchain git -- first-name Ole --last-name Christiansen --email o\.christiansen@klickbrick\.com'")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     output = subprocess.run(
#         "poetry run klickbrick --onboard --dry-run",
#         stdout=subprocess.PIPE,
#         stderr=subprocess.STDOUT,
#         shell=True,
#         executable="/bin/bash",
#     )
#     print(f"Output: {output.stdout}")
#
#
# @then("the git user profile is set with users name")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then the git user profile is set with users name')
#
#
# @step("the git email is set with users email")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And the git email is set with users email')
#
#
# @step("the git commit template is configured")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And the git commit template is configured')