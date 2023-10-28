import pytest
from grapich_interface import graphic_interface


@pytest.fixture
def funct_testing():
    return graphic_interface


def test_funct_to_add(funct_testing):    
    assert funct_testing.sumarNumeros(funct_testing) == 30