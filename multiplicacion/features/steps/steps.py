from behave import *
import requests


@given('a {values} to multiply')
def step_impl(context, values):
    context.api_url = 'http://localhost:5050/api/multiplicacion'
    context.values = values.split(',')
    context.data = {'n1': int(context.values[0]), 'n2': int(context.values[1])}  

@when('the calculator multiply the values')
def step_impl(context):    
    r = requests.post(url=context.api_url, params=context.data, headers="")    
    context.res = float(r.text)

@then('the {total:d} of multiply is correct')
def step_impl(context, total):    
    assert (context.res == total)
