from antlr4 import *
from cool.antlr.coolLexer import coolLexer
from cool.antlr.coolParser import coolParser

# from listeners.tree import TreePrinter

from cool.listeners.Checks01Listener import Checks01Listener
from cool.listeners.Checks02Listener import Checks02Listener
from cool.listeners.HierarchyListener import HierarchyListener
from cool.listeners.SymbolTableListener import SymbolTableListener
from cool.listeners.TreePrinterListener import TreePrinter
from cool.util.KlassRegistry import clearKlassTree


def compile(file):
    clearKlassTree()
    parser = coolParser(CommonTokenStream(coolLexer(FileStream(file))))
    tree = parser.program()

    walker = ParseTreeWalker()
    walker.walk(Checks01Listener(), tree)
    walker.walk(HierarchyListener(), tree)
    walker.walk(SymbolTableListener(), tree)
    walker.walk(Checks02Listener(), tree)
    walker.walk(TreePrinter(), tree)


def dummy():
    raise SystemExit(1)

if __name__ == '__main__':
    compile('cool/resources/semantic/input/anattributenamedself.cool')
