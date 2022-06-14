# Generated from C:/Users/X220/Desktop/round4/cool/antlr\cool.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .coolParser import coolParser
else:
    from coolParser import coolParser

# This class defines a complete listener for a parse tree produced by coolParser.
class coolListener(ParseTreeListener):

    # Enter a parse tree produced by coolParser#program.
    def enterProgram(self, ctx:coolParser.ProgramContext):
        pass

    # Exit a parse tree produced by coolParser#program.
    def exitProgram(self, ctx:coolParser.ProgramContext):
        pass


    # Enter a parse tree produced by coolParser#klass.
    def enterKlass(self, ctx:coolParser.KlassContext):
        pass

    # Exit a parse tree produced by coolParser#klass.
    def exitKlass(self, ctx:coolParser.KlassContext):
        pass


    # Enter a parse tree produced by coolParser#metodo.
    def enterMetodo(self, ctx:coolParser.MetodoContext):
        pass

    # Exit a parse tree produced by coolParser#metodo.
    def exitMetodo(self, ctx:coolParser.MetodoContext):
        pass


    # Enter a parse tree produced by coolParser#atribute.
    def enterAtribute(self, ctx:coolParser.AtributeContext):
        pass

    # Exit a parse tree produced by coolParser#atribute.
    def exitAtribute(self, ctx:coolParser.AtributeContext):
        pass


    # Enter a parse tree produced by coolParser#formal_Expression.
    def enterFormal_Expression(self, ctx:coolParser.Formal_ExpressionContext):
        pass

    # Exit a parse tree produced by coolParser#formal_Expression.
    def exitFormal_Expression(self, ctx:coolParser.Formal_ExpressionContext):
        pass


    # Enter a parse tree produced by coolParser#add.
    def enterAdd(self, ctx:coolParser.AddContext):
        pass

    # Exit a parse tree produced by coolParser#add.
    def exitAdd(self, ctx:coolParser.AddContext):
        pass


    # Enter a parse tree produced by coolParser#new.
    def enterNew(self, ctx:coolParser.NewContext):
        pass

    # Exit a parse tree produced by coolParser#new.
    def exitNew(self, ctx:coolParser.NewContext):
        pass


    # Enter a parse tree produced by coolParser#minus.
    def enterMinus(self, ctx:coolParser.MinusContext):
        pass

    # Exit a parse tree produced by coolParser#minus.
    def exitMinus(self, ctx:coolParser.MinusContext):
        pass


    # Enter a parse tree produced by coolParser#parentCall.
    def enterParentCall(self, ctx:coolParser.ParentCallContext):
        pass

    # Exit a parse tree produced by coolParser#parentCall.
    def exitParentCall(self, ctx:coolParser.ParentCallContext):
        pass


    # Enter a parse tree produced by coolParser#while.
    def enterWhile(self, ctx:coolParser.WhileContext):
        pass

    # Exit a parse tree produced by coolParser#while.
    def exitWhile(self, ctx:coolParser.WhileContext):
        pass


    # Enter a parse tree produced by coolParser#call.
    def enterCall(self, ctx:coolParser.CallContext):
        pass

    # Exit a parse tree produced by coolParser#call.
    def exitCall(self, ctx:coolParser.CallContext):
        pass


    # Enter a parse tree produced by coolParser#division.
    def enterDivision(self, ctx:coolParser.DivisionContext):
        pass

    # Exit a parse tree produced by coolParser#division.
    def exitDivision(self, ctx:coolParser.DivisionContext):
        pass


    # Enter a parse tree produced by coolParser#equal.
    def enterEqual(self, ctx:coolParser.EqualContext):
        pass

    # Exit a parse tree produced by coolParser#equal.
    def exitEqual(self, ctx:coolParser.EqualContext):
        pass


    # Enter a parse tree produced by coolParser#negative.
    def enterNegative(self, ctx:coolParser.NegativeContext):
        pass

    # Exit a parse tree produced by coolParser#negative.
    def exitNegative(self, ctx:coolParser.NegativeContext):
        pass


    # Enter a parse tree produced by coolParser#not.
    def enterNot(self, ctx:coolParser.NotContext):
        pass

    # Exit a parse tree produced by coolParser#not.
    def exitNot(self, ctx:coolParser.NotContext):
        pass


    # Enter a parse tree produced by coolParser#isVoid.
    def enterIsVoid(self, ctx:coolParser.IsVoidContext):
        pass

    # Exit a parse tree produced by coolParser#isVoid.
    def exitIsVoid(self, ctx:coolParser.IsVoidContext):
        pass


    # Enter a parse tree produced by coolParser#lessThan.
    def enterLessThan(self, ctx:coolParser.LessThanContext):
        pass

    # Exit a parse tree produced by coolParser#lessThan.
    def exitLessThan(self, ctx:coolParser.LessThanContext):
        pass


    # Enter a parse tree produced by coolParser#let.
    def enterLet(self, ctx:coolParser.LetContext):
        pass

    # Exit a parse tree produced by coolParser#let.
    def exitLet(self, ctx:coolParser.LetContext):
        pass


    # Enter a parse tree produced by coolParser#block.
    def enterBlock(self, ctx:coolParser.BlockContext):
        pass

    # Exit a parse tree produced by coolParser#block.
    def exitBlock(self, ctx:coolParser.BlockContext):
        pass


    # Enter a parse tree produced by coolParser#lessEqual.
    def enterLessEqual(self, ctx:coolParser.LessEqualContext):
        pass

    # Exit a parse tree produced by coolParser#lessEqual.
    def exitLessEqual(self, ctx:coolParser.LessEqualContext):
        pass


    # Enter a parse tree produced by coolParser#multiply.
    def enterMultiply(self, ctx:coolParser.MultiplyContext):
        pass

    # Exit a parse tree produced by coolParser#multiply.
    def exitMultiply(self, ctx:coolParser.MultiplyContext):
        pass


    # Enter a parse tree produced by coolParser#if.
    def enterIf(self, ctx:coolParser.IfContext):
        pass

    # Exit a parse tree produced by coolParser#if.
    def exitIf(self, ctx:coolParser.IfContext):
        pass


    # Enter a parse tree produced by coolParser#case.
    def enterCase(self, ctx:coolParser.CaseContext):
        pass

    # Exit a parse tree produced by coolParser#case.
    def exitCase(self, ctx:coolParser.CaseContext):
        pass


    # Enter a parse tree produced by coolParser#base.
    def enterBase(self, ctx:coolParser.BaseContext):
        pass

    # Exit a parse tree produced by coolParser#base.
    def exitBase(self, ctx:coolParser.BaseContext):
        pass


    # Enter a parse tree produced by coolParser#assign.
    def enterAssign(self, ctx:coolParser.AssignContext):
        pass

    # Exit a parse tree produced by coolParser#assign.
    def exitAssign(self, ctx:coolParser.AssignContext):
        pass


    # Enter a parse tree produced by coolParser#caseState.
    def enterCaseState(self, ctx:coolParser.CaseStateContext):
        pass

    # Exit a parse tree produced by coolParser#caseState.
    def exitCaseState(self, ctx:coolParser.CaseStateContext):
        pass


    # Enter a parse tree produced by coolParser#letDeclear.
    def enterLetDeclear(self, ctx:coolParser.LetDeclearContext):
        pass

    # Exit a parse tree produced by coolParser#letDeclear.
    def exitLetDeclear(self, ctx:coolParser.LetDeclearContext):
        pass


    # Enter a parse tree produced by coolParser#subexpresion.
    def enterSubexpresion(self, ctx:coolParser.SubexpresionContext):
        pass

    # Exit a parse tree produced by coolParser#subexpresion.
    def exitSubexpresion(self, ctx:coolParser.SubexpresionContext):
        pass


    # Enter a parse tree produced by coolParser#variable.
    def enterVariable(self, ctx:coolParser.VariableContext):
        pass

    # Exit a parse tree produced by coolParser#variable.
    def exitVariable(self, ctx:coolParser.VariableContext):
        pass


    # Enter a parse tree produced by coolParser#int.
    def enterInt(self, ctx:coolParser.IntContext):
        pass

    # Exit a parse tree produced by coolParser#int.
    def exitInt(self, ctx:coolParser.IntContext):
        pass


    # Enter a parse tree produced by coolParser#string.
    def enterString(self, ctx:coolParser.StringContext):
        pass

    # Exit a parse tree produced by coolParser#string.
    def exitString(self, ctx:coolParser.StringContext):
        pass


    # Enter a parse tree produced by coolParser#boolTrue.
    def enterBoolTrue(self, ctx:coolParser.BoolTrueContext):
        pass

    # Exit a parse tree produced by coolParser#boolTrue.
    def exitBoolTrue(self, ctx:coolParser.BoolTrueContext):
        pass


    # Enter a parse tree produced by coolParser#boolFalse.
    def enterBoolFalse(self, ctx:coolParser.BoolFalseContext):
        pass

    # Exit a parse tree produced by coolParser#boolFalse.
    def exitBoolFalse(self, ctx:coolParser.BoolFalseContext):
        pass



del coolParser