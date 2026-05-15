"""
=============================================================
 Generación de Código Intermedio — TAC (Three-Address Code)
 RobotLang — Mini-compilador para configuración de robots
 Universidad Cooperativa de Colombia — Compiladores 2026
=============================================================
"""

from typing import List
from dataclasses import dataclass, field
from generated.ast_nodes import (
    ProgramNode, DeclarationNode, RoutineNode,
    ControlNode, ActionNode, CallNode, ExprNode, ASTNode
)


# ─── Instrucciones TAC ──────────────────────────────────────

@dataclass
class TACInstruction:
    op:     str
    arg1:   str = ''
    arg2:   str = ''
    result: str = ''

    def __str__(self):
        if self.op == 'LABEL':
            return f"{self.result}:"
        if self.op == 'ASSIGN':
            return f"  {self.result} = {self.arg1}"
        if self.op == 'IF_FALSE':
            return f"  IF_FALSE {self.arg1} GOTO {self.result}"
        if self.op == 'GOTO':
            return f"  GOTO {self.result}"
        if self.op == 'CALL':
            return f"  CALL {self.arg1}"
        if self.op == 'SENSOR_DECL':
            return f"  SENSOR {self.arg1}"
        if self.op == 'FUNC_BEGIN':
            return f"\nFUNC_BEGIN {self.arg1}"
        if self.op == 'FUNC_END':
            return f"FUNC_END {self.arg1}"
        if self.op == 'CMP':
            return f"  {self.result} = {self.arg1} {self.op} {self.arg2}"
        return f"  {self.op} {self.arg1} {self.arg2} {self.result}".rstrip()


# ─── Generador TAC ──────────────────────────────────────────

class TACGenerator:
    """
    Recorre el AST y genera instrucciones TAC (Three-Address Code).
    Es una representación intermedia del programa antes de la
    traducción final a Python.
    """

    def __init__(self):
        self.instructions: List[TACInstruction] = []
        self._label_count = 0
        self._temp_count  = 0

    def _new_label(self) -> str:
        self._label_count += 1
        return f"L{self._label_count}"

    def _new_temp(self) -> str:
        self._temp_count += 1
        return f"t{self._temp_count}"

    def emit(self, op, arg1='', arg2='', result=''):
        self.instructions.append(TACInstruction(op, arg1, arg2, result))

    # ─── Generación ───────────────────────────────────────

    def generate(self, program: ProgramNode):
        # Declaraciones de sensores
        for decl in program.declarations:
            self.emit('SENSOR_DECL', arg1=decl.name)

        # Rutinas
        for routine in program.routines:
            self._gen_routine(routine)

        # Sentencias globales (si existen)
        for stmt in program.statements:
            self._gen_statement(stmt)

    def _gen_routine(self, routine: RoutineNode):
        self.emit('FUNC_BEGIN', arg1=routine.name)
        for stmt in routine.body:
            self._gen_statement(stmt)
        self.emit('FUNC_END', arg1=routine.name)

    def _gen_statement(self, stmt: ASTNode):
        if isinstance(stmt, ControlNode):
            self._gen_control(stmt)
        elif isinstance(stmt, ActionNode):
            self.emit('CALL', arg1=stmt.target)
        elif isinstance(stmt, CallNode):
            self.emit('CALL', arg1=stmt.name)

    def _gen_control(self, ctrl: ControlNode):
        # Evaluar condición
        temp   = self._new_temp()
        lbl_else = self._new_label()
        lbl_end  = self._new_label()

        expr = ctrl.condition
        self.emit('CMP', arg1=expr.left, arg2=expr.right,
                  result=f"{temp} = {expr.left} {expr.comparator} {expr.right}")
        self.emit('IF_FALSE', arg1=temp, result=lbl_else)

        # Rama then
        self._gen_statement(ctrl.then_branch)

        if ctrl.else_branch:
            self.emit('GOTO', result=lbl_end)
            self.emit('LABEL', result=lbl_else)
            self._gen_statement(ctrl.else_branch)
            self.emit('LABEL', result=lbl_end)
        else:
            self.emit('LABEL', result=lbl_else)

    # ─── Reporte ──────────────────────────────────────────

    def print_tac(self):
        print("\n" + "=" * 60)
        print("  FASE 4a — CÓDIGO INTERMEDIO (TAC)")
        print("=" * 60)
        for instr in self.instructions:
            print(str(instr))
        print("=" * 60 + "\n")

    def get_tac_string(self) -> str:
        return '\n'.join(str(i) for i in self.instructions)
