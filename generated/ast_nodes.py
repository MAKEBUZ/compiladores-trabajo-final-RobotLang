"""
=============================================================
 Nodos del AST — RobotLang
 Mini-compilador para configuración de robots
=============================================================
"""

from dataclasses import dataclass, field
from typing import List, Optional


# ─── Nodo base ──────────────────────────────────────────────

class ASTNode:
    pass


# ─── Nodos concretos ────────────────────────────────────────

@dataclass
class ProgramNode(ASTNode):
    declarations: List['DeclarationNode']
    routines:     List['RoutineNode']
    statements:   List['StatementNode']


@dataclass
class DeclarationNode(ASTNode):
    name: str
    line: int


@dataclass
class RoutineNode(ASTNode):
    name:       str
    body:       List['StatementNode']
    line:       int


@dataclass
class ControlNode(ASTNode):
    condition:    'ExprNode'
    then_branch:  'StatementNode'
    else_branch:  Optional['StatementNode']
    line:         int


@dataclass
class ActionNode(ASTNode):
    target: str
    line:   int


@dataclass
class CallNode(ASTNode):
    name: str
    line: int


@dataclass
class ExprNode(ASTNode):
    left:       str
    comparator: str
    right:      str
    line:       int


# Alias para tipado
StatementNode = ASTNode
