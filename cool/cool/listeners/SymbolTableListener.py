from cool.antlr.coolListener import coolListener
from cool.antlr.coolParser import coolParser
from cool.util.KlassRegistry import getKlassByString, getKlass
from cool.util.exceptions import caseidenticalbranch, letbadinit, attrbadinit, assignnoconform, outofscope, \
    returntypenoexist
from cool.util.internal.SymbolTableWithScopes import SymbolTableWithScopes


class SymbolTableListener(coolListener):
    def __init__(self):
        self.currentClass = None
        self.table = None
        self.scopes = 0

    def enterKlass(self, ctx: coolParser.KlassContext):
        self.table = SymbolTableWithScopes(getKlass(ctx.TYPE(0).getText()))
        self.currentClass = getKlass(ctx.TYPE(0).getText())

    def enterCase(self, ctx: coolParser.CaseContext):
        ctx.branches = set()

    def enterCaseState(self, ctx: coolParser.CaseStateContext):
        if ctx.TYPE().getText() in ctx.parentCtx.branches:
            raise caseidenticalbranch()
        else:
            ctx.parentCtx.branches.add(ctx.TYPE().getText())

    def enterLetDeclear(self, ctx: coolParser.LetDeclearContext):
        self.table.openScope()
        self.scopes += 1
        self.table[ctx.ID().getText()] = getKlassByString(ctx.TYPE().getText())

    def exitLet(self, ctx: coolParser.LetContext):
        for i in range(self.scopes):
            self.table.closeScope()
        self.scopes = 0

        if ctx.let_decl() and ctx.expr():
            if ctx.let_decl()[0].TYPE().getText() != ctx.expr().type.name:
                raise letbadinit()

    def enterFormal_Expression(self, ctx: coolParser.Formal_ExpressionContext):
        self.table[ctx.ID().getText()] = getKlassByString(ctx.TYPE().getText())

    def enterAtribute(self, ctx: coolParser.AtributeContext):
        self.table[ctx.ID().getText()] = getKlassByString(ctx.TYPE().getText())
        if ctx.expr():
            if type(ctx.expr()) == coolParser.BaseContext:
                if type(ctx.expr().children[0]) == coolParser.VariableContext:
                    try:
                        self.table[ctx.expr().children[0].getText()]
                    except KeyError:
                        raise attrbadinit()

    def exitMetodo(self, ctx: coolParser.MetodoContext):
        self.table.closeScope()

    def exitProgram(self, ctx: coolParser.ProgramContext):
        ctx.table = self.table

    def exitAssign(self, ctx: coolParser.AssignContext):
        if not self.table[ctx.ID().getText()].conforms(ctx.expr().type):
            raise assignnoconform()

    def exitBase(self, ctx: coolParser.BaseContext):
        ctx.type = ctx.getChild(0).type

    def exitSubexpresion(self, ctx: coolParser.SubexpresionContext):
        ctx.type = ctx.expr().type

    def exitNew(self, ctx: coolParser.NewContext):
        try:
            ctx.type = getKlassByString(ctx.TYPE().getText())
        except KeyError:
            raise returntypenoexist()

    def enterVariable(self, ctx: coolParser.VariableContext):
        if ctx.getText() == "self":
            ctx.type = self.currentClass
            return
        if type(ctx.parentCtx.parentCtx) != coolParser.CaseStateContext:
            try:
                ctx.type = self.table[ctx.getText()]
            except KeyError:
                raise outofscope()
        else:
            ctx.type = getKlassByString(ctx.parentCtx.parentCtx.TYPE().getText())
