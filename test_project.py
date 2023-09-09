import project
import pytest


def test_incorrectnum():
    assert project.incorrectnum(7,2) == True
    assert project.incorrectnum(-3,8) == True
    assert project.incorrectnum(5,11) == False
    assert project.incorrectnum(17,17) == False


def test_clearscreen():
    assert project.clearscreen() == True


def test_num6():
    assert project.num6('helloworld', 'new_pass', 'new_pass') == True
    assert project.num6('old_password', 1234567, 1234567) == True
    assert project.num6('starlight', 'spongebob', 'patrick') == False