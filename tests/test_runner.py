"""
=============================================================
 Test Runner — RobotLang
 Ejecuta los 20 casos de prueba (10 válidos + 10 inválidos)
=============================================================
"""

import os
import sys
from pathlib import Path

# Asegurar que el root del proyecto esté en el path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import RobotLangCompiler


class TestRunner:
    """Ejecuta y reporta todos los casos de prueba."""

    VALID_DIR   = Path(__file__).parent / 'valid'
    INVALID_DIR = Path(__file__).parent / 'invalid'

    GREEN  = '\033[92m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    CYAN   = '\033[96m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'

    def __init__(self):
        self.compiler = RobotLangCompiler(verbose=False)
        self.passed   = 0
        self.failed   = 0
        self.results  = []

    def run_all(self):
        print(f"\n{self.BOLD}{'='*65}{self.RESET}")
        print(f"{self.BOLD}  SUITE DE PRUEBAS — RobotLang Compiler{self.RESET}")
        print(f"{self.BOLD}{'='*65}{self.RESET}\n")

        # Tests válidos: deben compilar exitosamente
        print(f"{self.CYAN}  ── PRUEBAS VÁLIDAS (deben compilar sin errores) ──{self.RESET}")
        valid_files = sorted(self.VALID_DIR.glob('*.robot'))
        for f in valid_files:
            self._run_valid(f)

        print()
        print(f"{self.CYAN}  ── PRUEBAS CON ERRORES (deben fallar correctamente) ──{self.RESET}")
        invalid_files = sorted(self.INVALID_DIR.glob('*.robot'))
        for f in invalid_files:
            self._run_invalid(f)

        self._print_summary()
        self._save_report()

    def _run_valid(self, path: Path):
        source = path.read_text(encoding='utf-8')
        result = self.compiler.compile(source, source_name=path.name)
        passed = result['success']
        status = f"{self.GREEN}PASS{self.RESET}" if passed else f"{self.RED}FAIL{self.RESET}"
        detail = '' if passed else f" → {result['errors'][0] if result['errors'] else 'sin código generado'}"
        print(f"  [{status}] {path.name:<30} {'✔ Compilado OK' if passed else '✘ Debería compilar'}{detail}")

        if passed:
            self.passed += 1
        else:
            self.failed += 1
        self.results.append({
            'file': path.name, 'expected': 'PASS', 'got': 'PASS' if passed else 'FAIL',
            'errors': result['errors']
        })

    def _run_invalid(self, path: Path):
        source = path.read_text(encoding='utf-8')
        result = self.compiler.compile(source, source_name=path.name)
        # Para pruebas inválidas: esperamos que FALLE
        passed = not result['success']
        status = f"{self.GREEN}PASS{self.RESET}" if passed else f"{self.RED}FAIL{self.RESET}"
        first_err = result['errors'][0] if result['errors'] else '(sin error reportado)'
        # Extraer solo la parte relevante del error
        short_err = first_err.replace('[ERROR LÉXICO] ', '').replace('[ERROR SINTÁCTICO] ', '').replace('[ERROR SEMÁNTICO] ', '')
        short_err = short_err[:55] + '...' if len(short_err) > 55 else short_err
        print(f"  [{status}] {path.name:<30} {'✔ Error detectado' if passed else '✘ Debería fallar'}: {short_err}")

        if passed:
            self.passed += 1
        else:
            self.failed += 1
        self.results.append({
            'file': path.name, 'expected': 'FAIL', 'got': 'FAIL' if passed else 'PASS',
            'errors': result['errors']
        })

    def _print_summary(self):
        total = self.passed + self.failed
        print(f"\n{self.BOLD}{'='*65}{self.RESET}")
        print(f"{self.BOLD}  RESUMEN{self.RESET}")
        print(f"  Total de pruebas : {total}")
        print(f"  {self.GREEN}Exitosas{self.RESET}         : {self.passed}")
        print(f"  {self.RED}Fallidas{self.RESET}         : {self.failed}")
        pct = (self.passed / total * 100) if total > 0 else 0
        color = self.GREEN if pct == 100 else (self.YELLOW if pct >= 80 else self.RED)
        print(f"  Cobertura        : {color}{pct:.1f}%{self.RESET}")
        print(f"{self.BOLD}{'='*65}{self.RESET}\n")

    def _save_report(self):
        lines = ["REPORTE DE PRUEBAS — RobotLang\n", "="*65 + "\n\n"]
        for r in self.results:
            status = "PASS" if r['expected'] == r['got'] else "FAIL"
            lines.append(f"[{status}] {r['file']}\n")
            lines.append(f"       Esperado: {r['expected']} | Obtenido: {r['got']}\n")
            for e in r['errors']:
                lines.append(f"       {e}\n")
            lines.append("\n")
        lines.append(f"\nTotal: {self.passed + self.failed} | OK: {self.passed} | Fallidos: {self.failed}\n")

        report_path = Path(__file__).parent.parent / 'output.txt'
        report_path.write_text(''.join(lines), encoding='utf-8')
        print(f"  Reporte guardado en: output.txt\n")


if __name__ == '__main__':
    runner = TestRunner()
    runner.run_all()
