import pytest

from cool.main import compile
from cool.util.exceptions import *


def test_anattributenamedself():
    with pytest.raises(anattributenamedself):
        compile('cool/resources/semantic/input/anattributenamedself.cool')


def test_badredefineint():
    with pytest.raises(badredefineint):
        compile('cool/resources/semantic/input/badredefineint.cool')


def test_inheritsbool():
    with pytest.raises(inheritsbool):
        compile('cool/resources/semantic/input/inheritsbool.cool')


def test_inheritsselftype():
    with pytest.raises(inheritsselftype):
        compile('cool/resources/semantic/input/inheritsselftype.cool')


def test_inheritsstring():
    with pytest.raises(inheritsstring):
        compile('cool/resources/semantic/input/inheritsstring.cool')


def test_letself():
    with pytest.raises(letself):
        compile('cool/resources/semantic/input/letself.cool')


def test_nomain():
    with pytest.raises(nomain):
        compile('cool/resources/semantic/input/nomain.cool')


def test_redefinedobject():
    with pytest.raises(redefinedobject):
        compile('cool/resources/semantic/input/redefinedobject.cool')


def test_selfassignment():
    with pytest.raises(selfassignment):
        compile('cool/resources/semantic/input/self-assignment.cool')


def test_selfinformalparameter():
    with pytest.raises(selfinformalparameter):
        compile('cool/resources/semantic/input/selfinformalparameter.cool')


def test_selftypeparameterposition():
    with pytest.raises(selftypeparameterposition):
        compile('cool/resources/semantic/input/selftypeparameterposition.cool')


def test_selftyperedeclared():
    with pytest.raises(selftyperedeclared):
        compile('cool/resources/semantic/input/selftyperedeclared.cool')
