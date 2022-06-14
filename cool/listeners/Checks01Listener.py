from cool.antlr.coolListener import coolListener
from cool.antlr.coolParser import coolParser
from cool.util.Klass import setBaseKlasses
from cool.util.KlassRegistry import getKlassByString
from cool.util.exceptions import *


class Checks01Listener(coolListener):

    def __init__(self):
        setBaseKlasses()
        self.main = False

    def enterKlass(self, ctx: coolParser.KlassContext):
        if ctx.TYPE(0).getText() == 'Main':
            self.main = True

    def exitProgram(self, ctx: coolParser.KlassContext):
        if not self.main:
            raise nomain()

    def enterAtribute(self, ctx: coolParser.AtributeContext):
        if ctx.ID().getText() == 'self':
            raise anattributenamedself()

    def enterLetDeclear(self, ctx: coolParser.LetDeclearContext):
        if ctx.ID().getText() == 'self':
            raise letself()

    def enterFormal_Expression(self, ctx):
        if ctx.ID().getText() == 'self':
            raise selfinformalparameter()
        if ctx.TYPE().getText() == 'SELF_TYPE':
            raise selftypeparameterposition()

    def enterAssign(self, ctx: coolParser.AssignContext):
        if ctx.ID().getText() == 'self':
            raise selfassignment()

    def enterInt(self, ctx: coolParser.IntContext):
        ctx.type = getKlassByString("Int")

    def enterString(self, ctx: coolParser.StringContext):
        ctx.type = getKlassByString("String")

    def enterBoolTrue(self, ctx: coolParser.BoolTrueContext):
        ctx.type = getKlassByString("Bool")

    def enterBoolFalse(self, ctx: coolParser.BoolTrueContext):
        ctx.type = getKlassByString("Bool")

    def enterSubexpresion(self, ctx: coolParser.SubexpresionContext):
        ctx.type = ctx.expr()
