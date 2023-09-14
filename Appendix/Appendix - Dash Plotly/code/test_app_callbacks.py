from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

import pytest
import main
from pages import model1

submit = 1
def test_calculate_y_hardcode_1_plus_2_equal_3():
    output = model1.calculate_y_hardcode(1,2, submit)
    assert output == 3

def test_calculate_y_hardcode_2_plus_2_equal_4():
    output = model1.calculate_y_hardcode(2,2, submit)
    assert output == 4

def test_model_output_shape():
    output = model1.calculate_model(1,2)
    assert output.shape == (1,1), f"Expecting the shape to be (1,1) but got {output.shape=}"

def test_model_coeff_shape():
    output = model1.get_coeff()
    assert output.shape == (1,2), f"Expecting the shape to be (1,2) but got {output.shape=}"
