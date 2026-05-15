"""
=============================================================
 main.py — Punto de Integración del Compilador RobotLang
 Mini-compilador para configuración de robots
 Universidad Cooperativa de Colombia — Compiladores 2026
=============================================================

Uso:
    python main.py                    # compila input.txt
    python main.py archivo.robot      # compila archivo específico
    python main.py --tests            # ejecuta suite de pruebas
"""

import os
import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream, Token
from antlr4.error.ErrorListener import ErrorListener

from generated.RobotLangLexer import RobotLangLexer
from generated.RobotLangParser import RobotLangParser
from generated.RobotLangVisitor import RobotLangVisitor
from generated.ast_nodes import (
    ActionNode,
    CallNode,
    DeclarationNode,
    ExprNode,
    ProgramNode,
    RoutineNode,
    ControlNode,
)
from semantic_analyzer import SemanticAnalyzer
from semantic_analyzer.tac_generator import TACGenerator
from codegen.python_generator import PythonCodeGenerator


# ─── Colores para terminal ──────────────────────────────────

class C:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def ok(msg):
    return f"{C.GREEN}✔ {msg}{C.RESET}"


def err(msg):
    return f"{C.RED}✘ {msg}{C.RESET}"


def info(msg):
    return f"{C.CYAN}→ {msg}{C.RESET}"


def bold(msg):
    return f"{C.BOLD}{msg}{C.RESET}"


class CollectingErrorListener(ErrorListener):
    def __init__(self, phase: str):
        super().__init__()
        self.phase = phase
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(
            f"[ERROR {self.phase}] {msg} (línea {line}, columna {column + 1})"
        )


class ASTBuilder(RobotLangVisitor):
    def visitProgram(self, ctx):
        declarations = []
        routines = []
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, RobotLangParser.DeclarationContext):
                declarations.append(self.visit(child))
            elif isinstance(child, RobotLangParser.RoutineContext):
                routines.append(self.visit(child))
            elif isinstance(child, RobotLangParser.StatementContext):
                statements.append(self.visit(child))

        return ProgramNode(declarations=declarations, routines=routines, statements=statements)

    def visitDeclaration(self, ctx):
        return DeclarationNode(name=ctx.ID().getText(), line=ctx.start.line)

    def visitRoutine(self, ctx):
        body = [self.visit(stmt) for stmt in ctx.statement()]
        return RoutineNode(name=ctx.ID().getText(), body=body, line=ctx.start.line)

    def visitStatement(self, ctx):
        if ctx.control():
            return self.visit(ctx.control())
        if ctx.action():
            return self.visit(ctx.action())
        return self.visit(ctx.call())

    def visitControl(self, ctx):
        statements = ctx.statement()
        else_branch = self.visit(statements[1]) if len(statements) > 1 else None
        return ControlNode(
            condition=self.visit(ctx.expr()),
            then_branch=self.visit(statements[0]),
            else_branch=else_branch,
            line=ctx.start.line,
        )

    def visitAction(self, ctx):
        return ActionNode(target=ctx.ID().getText(), line=ctx.start.line)

    def visitCall(self, ctx):
        return CallNode(name=ctx.ID().getText(), line=ctx.start.line)

    def visitExpr(self, ctx):
        return ExprNode(
            left=ctx.ID().getText(),
            comparator=ctx.comparator().getText(),
            right=ctx.NUMBER().getText(),
            line=ctx.start.line,
        )


# ─── Compilador principal ───────────────────────────────────

class RobotLangCompiler:
    """Orquesta todas las fases del compilador."""

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def compile(self, source: str, source_name: str = '<stdin>') -> dict:
        """
        Ejecuta el pipeline completo.
        Retorna un dict con resultados de cada fase.
        """
        result = {
            'source': source_name,
            'tokens': None,
            'ast': None,
            'tac': None,
            'python_code': None,
            'errors': [],
            'success': False,
        }

        banner = f"\n{'=' * 60}\n  COMPILADOR RobotLang — {source_name}\n{'=' * 60}"
        if self.verbose:
            print(banner)

        # ── FASE 1: Análisis Léxico ──────────────────────
        if self.verbose:
            print(info('Fase 1: Análisis Léxico...'))
        input_stream = InputStream(source)
        lexer = RobotLangLexer(input_stream)
        lexer_errors = CollectingErrorListener('LÉXICO')
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_errors)

        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        tokens = [token for token in token_stream.tokens if token.type != Token.EOF]
        result['tokens'] = tokens

        if lexer_errors.errors:
            result['errors'].extend(lexer_errors.errors)
            if self.verbose:
                self._print_tokens(tokens)
                for error in lexer_errors.errors:
                    print(f'  {error}')
                print(err('Errores léxicos encontrados. Abortando.'))
            return result

        if self.verbose:
            self._print_tokens(tokens)
            print(ok('Análisis léxico completado.'))

        # ── FASE 2: Análisis Sintáctico ──────────────────
        if self.verbose:
            print(info('Fase 2: Análisis Sintáctico...'))
        parser = RobotLangParser(token_stream)
        parser_errors = CollectingErrorListener('SINTÁCTICO')
        parser.removeErrorListeners()
        parser.addErrorListener(parser_errors)
        tree = parser.program()

        if parser_errors.errors:
            result['errors'].extend(parser_errors.errors)
            if self.verbose:
                print(f"\n  {'=' * 56}")
                print('  FASE 2 — ANÁLISIS SINTÁCTICO')
                print(f"  {'=' * 56}")
                for error in parser_errors.errors:
                    print(f'  {error}')
                print(err('Errores sintácticos. Abortando.'))
            return result

        builder = ASTBuilder()
        ast = builder.visit(tree)
        result['ast'] = ast

        if self.verbose:
            self._print_ast(ast)
            print(ok('Análisis sintáctico completado.'))

        # ── FASE 3: Análisis Semántico ───────────────────
        if self.verbose:
            print(info('Fase 3: Análisis Semántico...'))
        semantic = SemanticAnalyzer()
        sem_ok = semantic.analyze(ast)

        if self.verbose:
            semantic.print_report()

        if not sem_ok:
            result['errors'].extend(semantic.errors)
            if self.verbose:
                print(err('Errores semánticos. Abortando.'))
            return result

        if self.verbose:
            print(ok('Análisis semántico completado.'))

        # ── FASE 4a: Código Intermedio TAC ───────────────
        if self.verbose:
            print(info('Fase 4a: Generando código intermedio (TAC)...'))
        tac_gen = TACGenerator()
        tac_gen.generate(ast)
        result['tac'] = tac_gen.get_tac_string()

        if self.verbose:
            tac_gen.print_tac()
            print(ok('TAC generado.'))

        # ── FASE 4b: Generación de código Python ─────────
        if self.verbose:
            print(info('Fase 4b: Generando código Python final...'))
        py_gen = PythonCodeGenerator()
        python_code = py_gen.generate(ast)
        result['python_code'] = python_code

        if self.verbose:
            py_gen.print_python(python_code)
            print(ok('Código Python generado.'))

        result['success'] = True
        if self.verbose:
            print(f"\n{C.GREEN}{C.BOLD}  ✔ COMPILACIÓN EXITOSA{C.RESET}\n")

        return result

    def _token_label(self, token_type: int) -> str:
        if token_type == Token.EOF:
            return 'EOF'

        if 0 <= token_type < len(RobotLangLexer.literalNames):
            literal = RobotLangLexer.literalNames[token_type]
            if literal and literal != '<INVALID>':
                return literal.strip("'")

        if 0 <= token_type < len(RobotLangLexer.symbolicNames):
            symbolic = RobotLangLexer.symbolicNames[token_type]
            if symbolic and symbolic != '<INVALID>':
                return symbolic

        return str(token_type)

    def _print_tokens(self, tokens):
        print(f"\n{'=' * 60}")
        print('  FASE 1 — TOKENS LÉXICOS')
        print(f"{'=' * 60}")
        for token in tokens:
            text = (token.text or '').replace('\n', '\\n').replace('\t', '\\t')
            label = self._token_label(token.type)
            print(f"  {token.line}:{token.column + 1:<3} {label:<12} {text}")
        print(f"{'=' * 60}\n")

    def _print_ast(self, ast):
        print(f"\n{'=' * 60}")
        print('  FASE 2 — ÁRBOL SINTÁCTICO ABSTRACTO (AST)')
        print(f"{'=' * 60}")
        self._print_ast_node(ast)
        print(f"{'=' * 60}\n")

    def _print_ast_node(self, node, depth: int = 0):
        indent = '  ' * depth
        if isinstance(node, ProgramNode):
            print(f'{indent}Program')
            for declaration in node.declarations:
                self._print_ast_node(declaration, depth + 1)
            for routine in node.routines:
                self._print_ast_node(routine, depth + 1)
            for statement in node.statements:
                self._print_ast_node(statement, depth + 1)
        elif isinstance(node, DeclarationNode):
            print(f'{indent}Declaration(name={node.name}, line={node.line})')
        elif isinstance(node, RoutineNode):
            print(f'{indent}Routine(name={node.name}, line={node.line})')
            for statement in node.body:
                self._print_ast_node(statement, depth + 1)
        elif isinstance(node, ControlNode):
            print(f'{indent}Control(line={node.line})')
            self._print_ast_node(node.condition, depth + 1)
            print(f'{indent}  Then:')
            self._print_ast_node(node.then_branch, depth + 2)
            if node.else_branch:
                print(f'{indent}  Else:')
                self._print_ast_node(node.else_branch, depth + 2)
        elif isinstance(node, ActionNode):
            print(f'{indent}Action(target={node.target}, line={node.line})')
        elif isinstance(node, CallNode):
            print(f'{indent}Call(name={node.name}, line={node.line})')
        elif isinstance(node, ExprNode):
            print(
                f'{indent}Expr(left={node.left}, comparator={node.comparator}, '
                f'right={node.right}, line={node.line})'
            )
        else:
            print(f'{indent}{node}')


# ─── Ejecución por línea de comandos ────────────────────────

def main():
    # Determinar archivo de entrada
    if '--tests' in sys.argv:
        run_test_suite()
        return

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

    if not os.path.exists(input_file):
        print(err(f'Archivo no encontrado: {input_file}'))
        sys.exit(1)

    source = Path(input_file).read_text(encoding='utf-8')
    compiler = RobotLangCompiler(verbose=True)
    result = compiler.compile(source, source_name=input_file)

    # Guardar output_program.py
    if result['success'] and result['python_code']:
        out_py = Path('output_program.py')
        out_py.write_text(result['python_code'], encoding='utf-8')
        print(ok(f'Código Python guardado en: {out_py}'))

    # Guardar output.txt (log de fases)
    log_lines = [f'Compilación de: {input_file}\n']
    if result['success']:
        log_lines.append('ESTADO: EXITOSO\n')
        log_lines.append('\n--- TAC ---\n')
        log_lines.append(result['tac'] or '')
        log_lines.append('\n\n--- PYTHON GENERADO ---\n')
        log_lines.append(result['python_code'] or '')
    else:
        log_lines.append('ESTADO: FALLIDO\n')
        log_lines.append('\n--- ERRORES ---\n')
        for error in result['errors']:
            log_lines.append(f'{error}\n')

    Path('output.txt').write_text(''.join(log_lines), encoding='utf-8')
    print(ok('Log guardado en: output.txt'))

    sys.exit(0 if result['success'] else 1)


def run_test_suite():
    """Ejecuta todos los archivos de prueba."""
    from tests.test_runner import TestRunner

    runner = TestRunner()
    runner.run_all()


if __name__ == '__main__':
    main()
