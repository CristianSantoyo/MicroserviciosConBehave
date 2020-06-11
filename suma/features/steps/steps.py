from behave import *
import requests


@given('a {values} to sum')
def step_impl(context, values):
    context.api_url = 'http://localhost:3030/api/suma'
    context.values = values.split(',')
    context.data = {'n1': int(context.values[0]), 'n2': int(context.values[1])}  

@when('the calculator sums the values')
def step_impl(context):    
    r = requests.post(url=context.api_url, params=context.data, headers="")    
    context.res = float(r.text)

@then('the {total:d} of sum is correct')
def step_impl(context, total):    
    assert (context.res == total)
