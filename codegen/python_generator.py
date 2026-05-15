"""
=============================================================
 Generación de Código Final — Python
 RobotLang — Mini-compilador para configuración de robots
 Universidad Cooperativa de Colombia — Compiladores 2026
=============================================================
"""

from typing import List
from generated.ast_nodes import (
    ProgramNode,
    DeclarationNode,
    RoutineNode,
    ControlNode,
    ActionNode,
    CallNode,
    ExprNode,
    ASTNode
)


class PythonCodeGenerator:
    """
    Traduce el AST de RobotLang a un script Python ejecutable.

    Mapeo de construcciones:
      sensor X       →  X = 0
      rutina F()     →  def F():
      si E : S       →  if E: ...
      sino : S       →  else: ...
      ejecutar F()   →  F()
      F()            →  F()
    """

    INDENT = "    "

    def __init__(self):
        self._lines: List[str] = []

    # =========================================================
    # Generación principal
    # =========================================================

    def generate(self, program: ProgramNode) -> str:
        self._lines = []

        # -----------------------------------------------------
        # Encabezado
        # -----------------------------------------------------

        self._emit("# ============================================================")
        self._emit("# Código generado automáticamente por RobotLang Compiler")
        self._emit("# Universidad Cooperativa de Colombia — Compiladores 2026")
        self._emit("# ============================================================")
        self._emit("")

        # -----------------------------------------------------
        # Sensores → variables globales
        # -----------------------------------------------------

        if program.declarations:
            self._emit("# --- Sensores (variables globales) ---")

            for decl in program.declarations:
                self._emit(f"{decl.name} = 0")

            self._emit("")

        # -----------------------------------------------------
        # Acciones primitivas del robot
        # -----------------------------------------------------

        self._emit("# --- Acciones primitivas del robot ---")

        primitive_actions = [
            ("girar_izquierda", "Robot girando a la izquierda"),
            ("avanzar",         "Robot avanzando"),
            ("apagar_motor",    "Motor apagado"),
            ("continuar",       "Robot continuando"),
            ("alerta_proximidad", "ALERTA: objeto detectado a menos de 10 unidades"),  # nuevo
            ("estado_ok",       "Estado del robot: todo en orden"),                    # nuevo
        ]

        for action_name, message in primitive_actions:
            self._emit(f"def {action_name}():")
            self._emit(f'print("{message}")', 1)
            self._emit("")

        # -----------------------------------------------------
        # Rutinas → funciones Python
        # -----------------------------------------------------

        self._emit("# --- Rutinas generadas ---")
        self._emit("")

        for routine in program.routines:
            self._gen_routine(routine)
            self._emit("")

        # -----------------------------------------------------
        # Punto de entrada
        # -----------------------------------------------------

        self._emit("# --- Punto de entrada ---")
        self._emit('if __name__ == "__main__":')
        self._emit("main()", 1)

        return "\n".join(self._lines)

    # =========================================================
    # Generación de rutinas
    # =========================================================

    def _gen_routine(self, routine: RoutineNode, depth: int = 0):
        self._emit(f"def {routine.name}():", depth)

        # Rutina vacía
        if not routine.body:
            self._emit("pass", depth + 1)
            return

        for stmt in routine.body:
            self._gen_statement(stmt, depth + 1)

    # =========================================================
    # Generación de sentencias
    # =========================================================

    def _gen_statement(self, stmt: ASTNode, depth: int = 1):

        # ---------------------------------------------
        # if / else
        # ---------------------------------------------

        if isinstance(stmt, ControlNode):
            self._gen_control(stmt, depth)

        # ---------------------------------------------
        # ejecutar accion();
        # ---------------------------------------------

        elif isinstance(stmt, ActionNode):
            self._emit(f"{stmt.target}()", depth)

        # ---------------------------------------------
        # llamada rutina();
        # ---------------------------------------------

        elif isinstance(stmt, CallNode):
            self._emit(f"{stmt.name}()", depth)

        # ---------------------------------------------
        # nodo desconocido
        # ---------------------------------------------

        else:
            raise TypeError(
                f"Nodo no soportado en generación Python: "
                f"{type(stmt).__name__}"
            )

    # =========================================================
    # Generación de estructuras de control
    # =========================================================

    def _gen_control(self, ctrl: ControlNode, depth: int):

        expr = ctrl.condition

        # Generar condición
        condition = f"{expr.left} {expr.comparator} {expr.right}"

        # if
        self._emit(f"if {condition}:", depth)

        self._gen_statement(ctrl.then_branch, depth + 1)

        # else opcional
        if ctrl.else_branch:
            self._emit("else:", depth)
            self._gen_statement(ctrl.else_branch, depth + 1)

    # =========================================================
    # Utilidad de escritura
    # =========================================================

    def _emit(self, line: str, depth: int = 0):
        self._lines.append(self.INDENT * depth + line)

    # =========================================================
    # Pretty print del código generado
    # =========================================================

    def print_python(self, code: str):

        print("\n" + "=" * 60)
        print("  FASE 4b — CÓDIGO FINAL (Python)")
        print("=" * 60)

        for i, line in enumerate(code.split("\n"), 1):
            print(f"  {i:3}  {line}")

        print("=" * 60 + "\n")