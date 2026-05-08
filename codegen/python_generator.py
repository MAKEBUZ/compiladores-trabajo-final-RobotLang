"""
=============================================================
 Generación de Código Final — Python
 RobotLang — Mini-compilador para configuración de robots
 Universidad Cooperativa de Colombia — Compiladores 2026
=============================================================
"""

from typing import List
from generated.ast_nodes import (
    ProgramNode, DeclarationNode, RoutineNode,
    ControlNode, ActionNode, CallNode, ExprNode, ASTNode
)


class PythonCodeGenerator:
    """
    Traduce el AST de RobotLang a un script Python ejecutable.

    Mapeo de construcciones:
      sensor X       →  X = 0          (variable global inicializada en 0)
      rutina F()     →  def F():
      si E : S       →  if E: ...
      sino : S       →  else: ...
      ejecutar F()   →  F()
      F()            →  F()
    """

    INDENT = '    '  # 4 espacios

    def __init__(self):
        self._lines: List[str] = []

    def generate(self, program: ProgramNode) -> str:
        self._lines = []

        # Encabezado
        self._emit("# ============================================================")
        self._emit("# Código generado automáticamente por RobotLang Compiler")
        self._emit("# Universidad Cooperativa de Colombia — Compiladores 2026")
        self._emit("# ============================================================")
        self._emit("")

        # Sensores → variables globales
        if program.declarations:
            self._emit("# --- Sensores (variables globales) ---")
            for decl in program.declarations:
                self._emit(f"{decl.name} = 0")
            self._emit("")

        # Rutinas → funciones Python
        for routine in program.routines:
            self._gen_routine(routine)
            self._emit("")

        # Punto de entrada: llamar a main()
        self._emit("# --- Punto de entrada ---")
        self._emit("main()")

        return '\n'.join(self._lines)

    # ─── Generación de rutinas ────────────────────────────

    def _gen_routine(self, routine: RoutineNode, depth: int = 0):
        self._emit(f"def {routine.name}():", depth)
        for stmt in routine.body:
            self._gen_statement(stmt, depth + 1)

    # ─── Generación de sentencias ─────────────────────────

    def _gen_statement(self, stmt: ASTNode, depth: int = 1):
        if isinstance(stmt, ControlNode):
            self._gen_control(stmt, depth)
        elif isinstance(stmt, ActionNode):
            self._emit(f"{stmt.target}()", depth)
        elif isinstance(stmt, CallNode):
            self._emit(f"{stmt.name}()", depth)

    def _gen_control(self, ctrl: ControlNode, depth: int):
        expr = ctrl.condition
        comp = expr.comparator
        self._emit(f"if {expr.left} {comp} {expr.right}:", depth)
        self._gen_statement(ctrl.then_branch, depth + 1)
        if ctrl.else_branch:
            self._emit("else:", depth)
            self._gen_statement(ctrl.else_branch, depth + 1)

    # ─── Utilidad ─────────────────────────────────────────

    def _emit(self, line: str, depth: int = 0):
        self._lines.append(self.INDENT * depth + line)

    def print_python(self, code: str):
        print("\n" + "=" * 60)
        print("  FASE 4b — CÓDIGO FINAL (Python)")
        print("=" * 60)
        for i, line in enumerate(code.split('\n'), 1):
            print(f"  {i:3}  {line}")
        print("=" * 60 + "\n")
