# Generated from C:/Users/X220/Desktop/round4/cool/antlr\cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete generic visitor for a parse tree produced by coolParser.

class coolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by coolParser#program.
    def visitProgram(self, ctx:coolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#klass.
    def visitKlass(self, ctx:coolParser.KlassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#metodo.
    def visitMetodo(self, ctx:coolParser.MetodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#atribute.
    def visitAtribute(self, ctx:coolParser.AtributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#formal_Expression.
    def visitFormal_Expression(self, ctx:coolParser.Formal_ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#add.
    def visitAdd(self, ctx:coolParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#new.
    def visitNew(self, ctx:coolParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#minus.
    def visitMinus(self, ctx:coolParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#parentCall.
    def visitParentCall(self, ctx:coolParser.ParentCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#while.
    def visitWhile(self, ctx:coolParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#call.
    def visitCall(self, ctx:coolParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#division.
    def visitDivision(self, ctx:coolParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#equal.
    def visitEqual(self, ctx:coolParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#negative.
    def visitNegative(self, ctx:coolParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#not.
    def visitNot(self, ctx:coolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#isVoid.
    def visitIsVoid(self, ctx:coolParser.IsVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#lessThan.
    def visitLessThan(self, ctx:coolParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#let.
    def visitLet(self, ctx:coolParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#block.
    def visitBlock(self, ctx:coolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#lessEqual.
    def visitLessEqual(self, ctx:coolParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#multiply.
    def visitMultiply(self, ctx:coolParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#if.
    def visitIf(self, ctx:coolParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#case.
    def visitCase(self, ctx:coolParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#base.
    def visitBase(self, ctx:coolParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#assign.
    def visitAssign(self, ctx:coolParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#caseState.
    def visitCaseState(self, ctx:coolParser.CaseStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#letDeclear.
    def visitLetDeclear(self, ctx:coolParser.LetDeclearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#subexpresion.
    def visitSubexpresion(self, ctx:coolParser.SubexpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#variable.
    def visitVariable(self, ctx:coolParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#int.
    def visitInt(self, ctx:coolParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#string.
    def visitString(self, ctx:coolParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#boolTrue.
    def visitBoolTrue(self, ctx:coolParser.BoolTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by coolParser#boolFalse.
    def visitBoolFalse(self, ctx:coolParser.BoolFalseContext):
        return self.visitChildren(ctx)



del coolParser