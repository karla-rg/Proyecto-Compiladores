import pytest

from cool.main import compile
from cool.util.exceptions import *


def test_badarith():
    with pytest.raises(badarith):
        compile('cool/resources/semantic/input/badarith.cool')


def test_baddispatch():
    with pytest.raises(baddispatch):
        compile('cool/resources/semantic/input/baddispatch.cool')


def test_badequalitytest():
    with pytest.raises(badequalitytest):
        compile('cool/resources/semantic/input/badequalitytest.cool')


def test_badequalitytest2():
    with pytest.raises(badequalitytest2):
        compile('cool/resources/semantic/input/badequalitytest2.cool')


def test_badwhilebody():
    with pytest.raises(badwhilebody):
        compile('cool/resources/semantic/input/badwhilebody.cool')


def test_badwhilecond():
    with pytest.raises(badwhilecond):
        compile('cool/resources/semantic/input/badwhilecond.cool')


def test_caseidenticalbranch():
    with pytest.raises(caseidenticalbranch):
        compile('cool/resources/semantic/input/caseidenticalbranch.cool')


def test_missingclass():
    with pytest.raises(missingclass):
        compile('cool/resources/semantic/input/missingclass.cool')


def test_outofscope():
    with pytest.raises(outofscope):
        compile('cool/resources/semantic/input/outofscope.cool')


def test_redefinedclass():
    with pytest.raises(redefinedclass):
        compile('cool/resources/semantic/input/redefinedclass.cool')


def test_returntypenoexist():
    with pytest.raises(returntypenoexist):
        compile('cool/resources/semantic/input/returntypenoexist.cool')


def test_selftypebadreturn():
    with pytest.raises(selftypebadreturn):
        compile('cool/resources/semantic/input/selftypebadreturn.cool')
