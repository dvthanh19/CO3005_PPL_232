# update: 6/04/2019
from abc import ABC
from dataclasses import dataclass
from AST import *


class Kind(ABC):
    pass


class Identifier(Kind):
    def __str__(self):
        return "Identifier"


class Variable(Kind):
    def __str__(self):
        return "Variable"


class Function(Kind):
    def __str__(self):
        return "Function"


class Parameter(Kind):
    def __str__(self):
        return "Parameter"


class StaticError(Exception):
    pass


class Redeclared(StaticError):
    # kind: Kind
    # name: str

    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Redeclared {str(self.kind)}: {self.name})"


class Undeclared(StaticError):
    # kind: Kind
    # name: str

    def __str__(self):
        return f"Undeclared {str(self.kind)}: {self.name})"


class TypeMismatchInExpression(StaticError):
    # expr: Expr

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return "Type Mismatch In Expression: " + str(self.expr)


class TypeMismatchInStatement(StaticError):
    # stmt: Stmt

    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "Type Mismatch In Statement: " + str(self.stmt)


class TypeCannotBeInferred(StaticError):
    # stmt: Stmt

    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return "Type Cannot Be Inferred: " + str(self.stmt)


class NoDefinition(StaticError):
    # name: str

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "No Function Definition: " + str(self.name)


class MustInLoop(StaticError):
    # stmt: Stmt

    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return str(self.stmt) + " Not In Loop"


class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"
