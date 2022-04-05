from behave import given, when, then

@given(u'I need to enter multiple fields of information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I need to enter multiple fields of information')


@when(u'I click on the dollar amount box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the dollar amount box')


@when(u'I fill in the dollar amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill in the dollar amount')


@when(u'I click on the comments section')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the comments section')


@when(u'I fill in the comments section')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill in the comments section')


@when(u'I click on the expense category section')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the expense category section')


@when(u'I select the "Travel" expense category from the drop down box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select the "Travel" expense category from the drop down box')


@when(u'I click on the "Submit" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the "Submit" button')


@then(u'I will receive a "Successfully Submitted" notification for my request')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will receive a "Successfully Submitted" notification for my request')

####

PS C:\Users\skinn\OneDrive\Desktop\P1_Team_International\jeryl\features> behave reimbursement_request_feature.feature
Exception SyntaxError: invalid syntax (cancel_reimbursement_request_feature.feature.py, line 24)
Traceback (most recent call last):
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\Scripts\behave.exe\__main__.py", line 7, in <module>
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\__main__.py", line 183, in main
    return run_behave(config)
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\__main__.py", line 127, in run_behave
    failed = runner.run()
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\runner.py", line 804, in run
    return self.run_with_paths()
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\runner.py", line 809, in run_with_paths
    self.load_step_definitions()
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\runner.py", line 796, in load_step_definitions
    load_step_modules(step_paths)
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\runner_util.py", line 412, in load_step_modules
    exec_file(os.path.join(path, name), step_module_globals)
  File "C:\Users\skinn\AppData\Local\Programs\Python\Python310\lib\site-packages\behave\runner_util.py", line 385, in exec_file
    code = compile(f.read(), filename2, "exec", dont_inherit=True)
  File "..\steps\cancel_reimbursement_request_feature.feature.py", line 24
    Feature: Employees can cancel their Reimbursement Request # cancel_reimbursement_request_feature.feature:1
                       ^^^
SyntaxError: invalid syntax
