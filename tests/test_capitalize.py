# test_capitalize.py
import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

# def test_raises_exception_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         capital_case(9)

# def test_comparewithAA(supply_AA_BB_CC):
# 	zz=35
# 	assert supply_AA_BB_CC[0]==zz,"aa and zz comparison failed"

# def test_comparewithBB(supply_AA_BB_CC):
# 	zz=35
# 	assert supply_AA_BB_CC[1]==zz,"bb and zz comparison failed"

# @pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
# def test_add(input1, input2, output):
# 	assert input1+input2 == output,"failed"