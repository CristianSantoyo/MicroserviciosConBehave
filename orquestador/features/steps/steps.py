from behave import *
import requests

#Steps para la suma
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

#Steps para la resta
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

#Steps para la multiplicacion
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

#Steps para la division
@given('a {values} to divide')
def step_impl(context, values):
    context.api_url = 'http://localhost:6060/api/division'
    context.values = values.split(',')
    context.data = {'n1': int(context.values[0]), 'n2': int(context.values[1])}  

@when('the calculator divide the values')
def step_impl(context):    
    r = requests.post(url=context.api_url, params=context.data, headers="")    
    context.res = float(r.text)

@then('the {total:d} of divide is correct')
def step_impl(context, total):    
    assert (context.res == total)
