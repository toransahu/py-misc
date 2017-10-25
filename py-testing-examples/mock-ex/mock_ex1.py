from unittest import mock
import ex1

def use_simple_function():
    result = ex1.simple_function()
    print(result)

use_simple_function()

@mock.patch('ex1.simple_function')
def mock_simple_function(arg):
# =============================================================================
#     print(mock_simple_func)
#     print(ex1.simple_function)
#     result = ex1.simple_function()
#     print(result)
# =============================================================================
    arg.return_value = "You have mocked simple_function"
    result = ex1.simple_function()
    print(result)

mock_simple_function()    

print(ex1.simple_function())

def side_effect_function():
    return "XYZ"

@mock.patch('ex1.simple_function')
def mock_simple_function_with_side_effect(arg_mock_simple_function):
    arg_mock_simple_function.side_effect = side_effect_function
    result = ex1.simple_function()
    print(result)
    
mock_simple_function_with_side_effect()

def use_simple_class():
    inst = ex1.SimpleClass()
    print(inst.explode())
    
use_simple_class()

@mock.patch("ex1.SimpleClass")
def mock_simple_class(arg_mock_class):
    print("MockClass object of SimpleClass: ", arg_mock_class)
    print("MockClass object of SimpleClass: ", ex1.SimpleClass)
    print()
    inst = ex1.SimpleClass()
    print("MockClass object of instance of SimpleClass: ", inst)
    print("MockClass object of instance of SimpleClass: ", arg_mock_class())
    print()
    print("MockClass object of member function of instance of SimpleClass: ", inst.explode())
    print("MockClass object of member function of instance of SimpleClass: ", arg_mock_class().explode())
    print()
    print("return_value of arg_mock_class: ", arg_mock_class.return_value)
    print()
    print("===================To Change The return_value of explode()============")
    inst.explode.return_value="return value changed using instance ex1.SimpleClass()"
    print("Result: ",inst.explode())
    print("===========OR==============")
    arg_mock_class.return_value.explode.return_value="return value changed using instance arg_mock_class.return_value"
    print("Result: ",inst.explode())
    
mock_simple_class()