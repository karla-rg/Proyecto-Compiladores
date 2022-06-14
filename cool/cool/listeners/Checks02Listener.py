from cool.antlr.coolListener import coolListener
from cool.antlr.coolParser import coolParser
from cool.util.KlassRegistry import getKlass, getAllKlasses
from cool.util.exceptions import badarith, badwhilecond, badwhilebody, baddispatch, selftypebadreturn, \
    returntypenoexist, badequalitytest2, badequalitytest


class Checks02Listener(coolListener):
    def __init__(self):
        self.currentClass = None
        self.table = None
        self.inwhile = False

    def enterKlass(self, ctx: coolParser.KlassContext):
        self.currentClass = getKlass(ctx.TYPE(0).getText())

    def enterProgram(self, ctx: coolParser.ProgramContext):
        self.table = ctx.table

    def exitAdd(self, ctx: coolParser.AddContext):
        if (ctx.expr(0).type.name == 'Int') and (ctx.expr(1).type.name == 'Int'):
            ctx.type = ctx.expr(0).Tipo
        else:
            raise badarith()

    def enterWhile(self, ctx: coolParser.WhileContext):
        self.inwhile = True

    def exitWhile(self, ctx: coolParser.WhileContext):
        if ctx.expr(0).Tipo.name != "Bool":
            raise badwhilecond()

    def exitCall(self, ctx: coolParser.CallContext):
        try:
            self.currentClass.lookupMethod(ctx.ID().getText())
        except KeyError:
            if self.inwhile:
                raise badwhilebody()
            try:
                ctx.expr(0).Tipo.lookupMethod(ctx.ID().getText())
            except KeyError:
                raise baddispatch()

    def enterMetodo(self, ctx: coolParser.MetodoContext):
        self.table.openScope()
        if ctx.TYPE().getText() == "SELF_TYPE":
            raise selftypebadreturn()
        if ctx.TYPE().getText() not in getAllKlasses():
            raise returntypenoexist()

    def exitEqual(self, ctx: coolParser.EqualContext):
        expr = [ctx.expr(i).type.name for i in range(2)]
        if "Int" in expr and "Bool" in expr:
            raise badequalitytest2()
        if expr[0] != expr[1]:
            raise badequalitytest()
        ctx.type = ctx.expr(0).type
