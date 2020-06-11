from behave import *
import requests

@given('a {values} to subtract')
def step_impl(context, values):
    context.api_url = 'http://localhost:4040/api/resta'
    context.values = values.split(',')
    context.data = {'n1': int(context.values[0]), 'n2': int(context.values[1])}  

@when('the calculator subtracts the values')
def step_impl(context):    
    r = requests.post(url=context.api_url, params=context.data, headers="")    
    context.res = float(r.text)

@then('the {total:d} of substraction  is correct')
def step_impl(context, total):
    print(context.res, total)
    assert (context.res == total)
