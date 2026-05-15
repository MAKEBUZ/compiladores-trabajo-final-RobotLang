"""
Análisis semántico — Visitor/Verificador
Contiene `SemanticError` y `SemanticAnalyzer` (alias `SemanticVisitor`).
"""
from typing import Dict, List, Optional
from .SymbolTable import SymbolTable
from generated.ast_nodes import (
    ProgramNode, DeclarationNode, RoutineNode,
    ControlNode, ActionNode, CallNode, ExprNode, ASTNode
)


class SemanticError(Exception):
    def __init__(self, message: str, line: int = 0):
        self.line = line
        super().__init__(f'[ERROR SEMÁNTICO] {message} (línea {line})')


class SemanticAnalyzer:
    """
    Realiza las siguientes verificaciones:
      1. Sensores deben estar declarados antes de usarse en expresiones.
      2. La rutina main() es obligatoria.
      3. Las rutinas/acciones llamadas deben estar definidas.
      4. No se permiten rutinas duplicadas.
      5. No se permiten sensores duplicados.
    """

    def __init__(self):
        self.global_table = SymbolTable()
        self.errors:   List[str] = []
        self.warnings: List[str] = []
        self._current_scope: Optional[SymbolTable] = None

    def analyze(self, program: ProgramNode) -> bool:
        """Retorna True si no hay errores semánticos."""
        self._first_pass(program)
        self._second_pass(program)
        self._check_main()
        return len(self.errors) == 0

    def _first_pass(self, program: ProgramNode):
        # Registrar sensores
        for decl in program.declarations:
            if self.global_table.lookup(decl.name):
                self._error(f'Sensor "{decl.name}" ya fue declarado', decl.line)
            else:
                self.global_table.define(decl.name, 'sensor', decl.line)

        # Registrar rutinas
        for routine in program.routines:
            if self.global_table.lookup(routine.name):
                self._error(f'Rutina "{routine.name}" ya fue declarada', routine.line)
            else:
                self.global_table.define(routine.name, 'rutina', routine.line)

    def _second_pass(self, program: ProgramNode):
        # Verificar sentencias globales
        for stmt in program.statements:
            self._check_statement(stmt, self.global_table)

        # Verificar cuerpo de rutinas
        for routine in program.routines:
            scope = SymbolTable(parent=self.global_table)
            self._current_scope = scope
            for stmt in routine.body:
                self._check_statement(stmt, scope)
            self._current_scope = None

    def _check_statement(self, stmt: ASTNode, scope: SymbolTable):
        if isinstance(stmt, ControlNode):
            self._check_expr(stmt.condition, scope)
            self._check_statement(stmt.then_branch, scope)
            if stmt.else_branch:
                self._check_statement(stmt.else_branch, scope)

        elif isinstance(stmt, ActionNode):
            sym = self.global_table.lookup(stmt.target)
            if sym is not None:
                self.global_table.mark_used(stmt.target)

        elif isinstance(stmt, CallNode):
            sym = self.global_table.lookup(stmt.name)
            if sym is None:
                self._error(
                    f'Rutina "{stmt.name}" no está definida', stmt.line
                )
            elif sym['kind'] != 'rutina':
                self._error(
                    f'"{stmt.name}" no es una rutina, es un {sym["kind"]}', stmt.line
                )
            else:
                self.global_table.mark_used(stmt.name)

    def _check_expr(self, expr: ExprNode, scope: SymbolTable):
        """Verifica que el sensor usado en la expresión esté declarado."""
        sym = self.global_table.lookup(expr.left)
        if sym is None:
            self._error(
                f'Sensor "{expr.left}" no ha sido declarado', expr.line
            )
        elif sym['kind'] != 'sensor':
            self._error(
                f'"{expr.left}" no es un sensor, es un {sym["kind"]}', expr.line
            )
        else:
            self.global_table.mark_used(expr.left)

    def _check_main(self):
        sym = self.global_table.lookup('main')
        if sym is None or sym['kind'] != 'rutina':
            self._error('Rutina "main()" es obligatoria pero no fue definida', 0)

    def _error(self, msg: str, line: int):
        err = SemanticError(msg, line)
        self.errors.append(str(err))

    def print_report(self):
        print("\n" + "=" * 60)
        print("  FASE 3 — ANÁLISIS SEMÁNTICO")
        print("=" * 60)
        self.global_table.print_table("Tabla de Símbolos Global")

        if self.errors:
            print("\n  *** ERRORES SEMÁNTICOS ***")
            for e in self.errors:
                print(f"  {e}")
        else:
            print("\n  ✔ Análisis semántico completado sin errores.")

        if self.warnings:
            print("\n  *** ADVERTENCIAS ***")
            for w in self.warnings:
                print(f"  {w}")
        print("=" * 60 + "\n")


# Alias para mantener compatibilidad con el nombre sugerido
SemanticVisitor = SemanticAnalyzer

__all__ = ["SemanticAnalyzer", "SemanticVisitor", "SemanticError"]
