import pytest
from rod_cislo_DU_22_03 import isvalid_rc

def test_je_platne():
    rc = '8301010003'
    assert isvalid_rc(rc) == True

def test_neplatny_datum():
    rc = '8300010003'
    assert isvalid_rc(rc) == (False, 'condition broken: month format')

def test_nespravna_dlzka():
    rc = '830001000333'
    assert isvalid_rc(rc) == (False, 'condition broken: incorrect length')

def test_nedelitelne_11():
    rc = '8301010004'
    assert isvalid_rc(rc) == (False, 'condition broken: divisibility by 11')

def test_zenske():
    rc = '8351010008'
    assert isvalid_rc(rc) == True

def test_necisleny_vstup():
    rc = '830101000e'
    assert isvalid_rc(rc) == (False, 'condition broken: not integers')


# @pytest.mark.parametrize("a,b,c,expected", [
#     (1,-3,2,[2,1]),
#     (1,2,1,[-1,-1]),
# ])
# def test_korene(a,b,c,expected):
#     calc=Calculator()
#     assert calc.korene(a, b, c)==expected