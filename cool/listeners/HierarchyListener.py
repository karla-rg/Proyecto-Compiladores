from cool.antlr.coolListener import coolListener
from cool.antlr.coolParser import coolParser
from cool.util.Klass import Klass
from cool.util.KlassRegistry import klassRepeats, getKlassByString
from cool.util.Method import Method
from cool.util.exceptions import *
from cool.util.exceptions import attroverride, dupformals, signaturechange


class HierarchyListener(coolListener):
    def __init__(self):
        self.currentKlass = None

    def enterKlass(self, ctx: coolParser.KlassContext):
        mainType = ctx.TYPE(0).getText()
        inheritance = None
        if ctx.TYPE(1):
            inheritance = ctx.TYPE(1).getText()

        if inheritance:
            if inheritance == 'SELF_TYPE':
                raise inheritsselftype()
            if inheritance == 'Bool':
                raise inheritsbool()
            if inheritance == 'String':
                raise inheritsstring()
        else:
            if mainType == 'Int':
                raise badredefineint()
            if mainType == 'Object':
                raise redefinedobject()
            if mainType == 'SELF_TYPE':
                raise selftyperedeclared()
        if klassRepeats(mainType):
            raise redefinedclass()

        if ctx.TYPE(1) is not None:
            klass = Klass(mainType, inheritance)
        else:
            klass = Klass(mainType)
        ctx.type = klass
        self.currentKlass = klass

    def enterAtribute(self, ctx: coolParser.AtributeContext):
        try:
            variablename = ctx.ID().getText()
            self.currentKlass.lookupAttribute(variablename)
            if not self.currentKlass.getOwnAttribute(variablename):
                raise attroverride()
        except KeyError:
            pass
        attrtype = ctx.TYPE().getText()
        self.currentKlass.addAttribute(ctx.ID().getText(), attrtype)
        ctx.type = getKlassByString(attrtype)

    def exitMetodo(self, ctx: coolParser.MetodoContext):
        parsedparams = set()
        if ctx.params:
            seen_param_names = set()
            for param in ctx.params:
                if type(param) == coolParser.Formal_ExpressionContext:
                    if param.ID().getText() in seen_param_names:
                        raise dupformals()
                    parsed = frozenset([param.TYPE().getText(), param.ID().getText()])
                    seen_param_names.add(param.ID().getText())
                    parsedparams.add(parsed)
        parsedMethod = Method(ctx.TYPE(), parsedparams)
        try:
            overridenmethod = self.currentKlass.lookupMethod(ctx.ID().getText())
            if len(parsedMethod.params) != len(overridenmethod.params):
                raise signaturechange()
        except KeyError:
            pass
        try:
            overridenmethod1 = self.currentKlass.lookupMethod(ctx.ID().getText())
            if parsedMethod.params.values() != overridenmethod1.params.values():
                pass
        except KeyError:
            pass
        self.currentKlass.addMethod(ctx.ID().getText(), parsedMethod)
