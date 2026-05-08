"""
=============================================================
 Análisis Sintáctico — RobotLang
 Mini-compilador para configuración de robots
 Universidad Cooperativa de Colombia — Compiladores 2026
=============================================================
"""

from typing import List, Optional
from generated.lexer import Token
from generated.ast_nodes import (
    ProgramNode, DeclarationNode, RoutineNode,
    ControlNode, ActionNode, CallNode, ExprNode, ASTNode
)


class ParseError(Exception):
    def __init__(self, message: str, line: int = 0):
        self.line = line
        super().__init__(f'[ERROR SINTÁCTICO] {message} (línea {line})')


class Parser:
    """
    Analizador sintáctico descendente recursivo para RobotLang.

    Gramática implementada:
        program    : (declaration | routine | statement)+ EOF
        declaration: 'sensor' ID ';'
        routine    : 'rutina' ID '(' ')' '{' statement+ '}'
        statement  : control | action | call
        control    : 'si' expr ':' statement ('sino' ':' statement)?
        action     : 'ejecutar' ID '(' ')' ';'
        call       : ID '(' ')' ';'
        expr       : ID comparator NUMBER
        comparator : '<' | '>' | '=='
    """

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.errors: List[str] = []

    # ─── Utilidades ────────────────────────────────────────

    def current(self) -> Token:
        return self.tokens[self.pos]

    def peek(self, offset: int = 1) -> Token:
        idx = self.pos + offset
        return self.tokens[idx] if idx < len(self.tokens) else self.tokens[-1]

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return tok

    def expect(self, ttype: str) -> Token:
        tok = self.current()
        if tok.type != ttype:
            raise ParseError(
                f'Se esperaba "{ttype}" pero se encontró "{tok.value}" ({tok.type})',
                tok.line
            )
        return self.advance()

    def match(self, *types: str) -> bool:
        return self.current().type in types

    # ─── Reglas gramaticales ───────────────────────────────

    def parse(self) -> ProgramNode:
        """Punto de entrada: parse programa completo."""
        declarations = []
        routines     = []
        statements   = []

        while not self.match('EOF'):
            try:
                if self.match('SENSOR'):
                    declarations.append(self.parse_declaration())
                elif self.match('RUTINA'):
                    routines.append(self.parse_routine())
                else:
                    statements.append(self.parse_statement())
            except ParseError as e:
                self.errors.append(str(e))
                self._sync()   # recuperación de errores

        node = ProgramNode(declarations, routines, statements)
        return node

    def parse_declaration(self) -> DeclarationNode:
        line = self.current().line
        self.expect('SENSOR')
        name = self.expect('ID').value
        self.expect('SEMI')
        return DeclarationNode(name=name, line=line)

    def parse_routine(self) -> RoutineNode:
        line = self.current().line
        self.expect('RUTINA')
        name = self.expect('ID').value
        self.expect('LPAREN')
        self.expect('RPAREN')
        self.expect('LBRACE')
        body = []
        while not self.match('RBRACE', 'EOF'):
            try:
                body.append(self.parse_statement())
            except ParseError as e:
                self.errors.append(str(e))
                self._sync()
                # Si _sync paró en RBRACE, salir del loop
                if self.match('RBRACE', 'EOF'):
                    break
        if self.match('RBRACE'):
            self.advance()
        elif self.match('EOF'):
            raise ParseError(
                f'Se esperaba "RBRACE" para cerrar rutina "{name}" pero se encontró fin de archivo',
                line
            )
        return RoutineNode(name=name, body=body, line=line)

    def parse_statement(self) -> ASTNode:
        if self.match('SI'):
            return self.parse_control()
        elif self.match('EJECUTAR'):
            return self.parse_action()
        elif self.match('ID'):
            return self.parse_call()
        else:
            tok = self.current()
            raise ParseError(
                f'Sentencia inválida: "{tok.value}"', tok.line
            )

    def parse_control(self) -> ControlNode:
        line = self.current().line
        self.expect('SI')
        condition = self.parse_expr()
        self.expect('COLON')
        then_branch = self.parse_statement()
        else_branch = None
        if self.match('SINO'):
            self.advance()
            self.expect('COLON')
            else_branch = self.parse_statement()
        return ControlNode(condition=condition, then_branch=then_branch,
                           else_branch=else_branch, line=line)

    def parse_action(self) -> ActionNode:
        line = self.current().line
        self.expect('EJECUTAR')
        target = self.expect('ID').value
        self.expect('LPAREN')
        self.expect('RPAREN')
        self.expect('SEMI')
        return ActionNode(target=target, line=line)

    def parse_call(self) -> CallNode:
        line = self.current().line
        name = self.expect('ID').value
        self.expect('LPAREN')
        self.expect('RPAREN')
        self.expect('SEMI')
        return CallNode(name=name, line=line)

    def parse_expr(self) -> ExprNode:
        line = self.current().line
        left = self.expect('ID').value
        comp = self.parse_comparator()
        right = self.expect('NUMBER').value
        return ExprNode(left=left, comparator=comp, right=right, line=line)

    def parse_comparator(self) -> str:
        tok = self.current()
        if self.match('LT', 'GT', 'EQ'):
            return self.advance().value
        raise ParseError(f'Comparador inválido: "{tok.value}"', tok.line)

    # ─── Recuperación de errores ──────────────────────────

    def _sync(self):
        """Avanza hasta un punto de sincronización seguro."""
        sync_tokens = {'SEMI', 'RBRACE', 'RUTINA', 'SENSOR', 'EOF'}
        while not self.match(*sync_tokens) and self.current().type != 'EOF':
            self.advance()
        if self.match('SEMI'):
            self.advance()

    # ─── Reporte ──────────────────────────────────────────

    def print_ast(self, node: ASTNode, indent: int = 0):
        prefix = "  " * indent
        name   = type(node).__name__
        if isinstance(node, ProgramNode):
            print(f"{prefix}ProgramNode")
            for d in node.declarations:
                self.print_ast(d, indent + 1)
            for r in node.routines:
                self.print_ast(r, indent + 1)
            for s in node.statements:
                self.print_ast(s, indent + 1)
        elif isinstance(node, DeclarationNode):
            print(f"{prefix}DeclarationNode  sensor={node.name}")
        elif isinstance(node, RoutineNode):
            print(f"{prefix}RoutineNode  name={node.name}")
            for s in node.body:
                self.print_ast(s, indent + 1)
        elif isinstance(node, ControlNode):
            print(f"{prefix}ControlNode  cond={node.condition.left} {node.condition.comparator} {node.condition.right}")
            self.print_ast(node.then_branch, indent + 1)
            if node.else_branch:
                print(f"{prefix}  [else]")
                self.print_ast(node.else_branch, indent + 1)
        elif isinstance(node, ActionNode):
            print(f"{prefix}ActionNode  target={node.target}")
        elif isinstance(node, CallNode):
            print(f"{prefix}CallNode  name={node.name}")
        elif isinstance(node, ExprNode):
            print(f"{prefix}ExprNode  {node.left} {node.comparator} {node.right}")
        else:
            print(f"{prefix}{name}")
