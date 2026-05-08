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

import sys
import os
from pathlib import Path

from generated.lexer           import Lexer, LexerError
from generated.parser          import Parser, ParseError
from semantic_analyzer         import SemanticAnalyzer
from codegen.tac_generator     import TACGenerator
from codegen.python_generator  import PythonCodeGenerator


# ─── Colores para terminal ──────────────────────────────────

class C:
    GREEN  = '\033[92m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    CYAN   = '\033[96m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'

def ok(msg):    return f"{C.GREEN}✔ {msg}{C.RESET}"
def err(msg):   return f"{C.RED}✘ {msg}{C.RESET}"
def info(msg):  return f"{C.CYAN}→ {msg}{C.RESET}"
def bold(msg):  return f"{C.BOLD}{msg}{C.RESET}"


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
            'source':      source_name,
            'tokens':      None,
            'ast':         None,
            'tac':         None,
            'python_code': None,
            'errors':      [],
            'success':     False,
        }

        banner = f"\n{'='*60}\n  COMPILADOR RobotLang — {source_name}\n{'='*60}"
        if self.verbose:
            print(banner)

        # ── FASE 1: Análisis Léxico ──────────────────────
        if self.verbose:
            print(info("Fase 1: Análisis Léxico..."))
        lexer = Lexer(source)
        tokens = lexer.tokenize()

        if lexer.errors:
            for e in lexer.errors:
                result['errors'].append(e)
            if self.verbose:
                lexer.print_tokens()
                print(err("Errores léxicos encontrados. Abortando."))
            return result

        result['tokens'] = tokens
        if self.verbose:
            lexer.print_tokens()
            print(ok("Análisis léxico completado."))

        # ── FASE 2: Análisis Sintáctico ──────────────────
        if self.verbose:
            print(info("Fase 2: Análisis Sintáctico..."))
        parser = Parser(tokens)
        ast = parser.parse()

        if parser.errors:
            for e in parser.errors:
                result['errors'].append(e)
            if self.verbose:
                print(f"\n  {'='*56}")
                print("  FASE 2 — ANÁLISIS SINTÁCTICO")
                print(f"  {'='*56}")
                for e in parser.errors:
                    print(f"  {e}")
                print(err("Errores sintácticos. Abortando."))
            return result

        result['ast'] = ast
        if self.verbose:
            print(f"\n{'='*60}")
            print("  FASE 2 — ÁRBOL SINTÁCTICO ABSTRACTO (AST)")
            print(f"{'='*60}")
            parser.print_ast(ast)
            print(f"{'='*60}\n")
            print(ok("Análisis sintáctico completado."))

        # ── FASE 3: Análisis Semántico ───────────────────
        if self.verbose:
            print(info("Fase 3: Análisis Semántico..."))
        semantic = SemanticAnalyzer()
        sem_ok = semantic.analyze(ast)

        if self.verbose:
            semantic.print_report()

        if not sem_ok:
            for e in semantic.errors:
                result['errors'].append(e)
            if self.verbose:
                print(err("Errores semánticos. Abortando."))
            return result

        if self.verbose:
            print(ok("Análisis semántico completado."))

        # ── FASE 4a: Código Intermedio TAC ───────────────
        if self.verbose:
            print(info("Fase 4a: Generando código intermedio (TAC)..."))
        tac_gen = TACGenerator()
        tac_gen.generate(ast)
        result['tac'] = tac_gen.get_tac_string()

        if self.verbose:
            tac_gen.print_tac()
            print(ok("TAC generado."))

        # ── FASE 4b: Generación de código Python ─────────
        if self.verbose:
            print(info("Fase 4b: Generando código Python final..."))
        py_gen = PythonCodeGenerator()
        python_code = py_gen.generate(ast)
        result['python_code'] = python_code

        if self.verbose:
            py_gen.print_python(python_code)
            print(ok("Código Python generado."))

        result['success'] = True
        if self.verbose:
            print(f"\n{C.GREEN}{C.BOLD}  ✔ COMPILACIÓN EXITOSA{C.RESET}\n")

        return result


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
        print(ok(f"Código Python guardado en: {out_py}"))

    # Guardar output.txt (log de fases)
    log_lines = [f"Compilación de: {input_file}\n"]
    if result['success']:
        log_lines.append("ESTADO: EXITOSO\n")
        log_lines.append("\n--- TAC ---\n")
        log_lines.append(result['tac'] or '')
        log_lines.append("\n\n--- PYTHON GENERADO ---\n")
        log_lines.append(result['python_code'] or '')
    else:
        log_lines.append("ESTADO: FALLIDO\n")
        log_lines.append("\n--- ERRORES ---\n")
        for e in result['errors']:
            log_lines.append(f"{e}\n")

    Path('output.txt').write_text(''.join(log_lines), encoding='utf-8')
    print(ok("Log guardado en: output.txt"))

    sys.exit(0 if result['success'] else 1)


def run_test_suite():
    """Ejecuta todos los archivos de prueba."""
    from tests.test_runner import TestRunner
    runner = TestRunner()
    runner.run_all()


if __name__ == '__main__':
    main()
