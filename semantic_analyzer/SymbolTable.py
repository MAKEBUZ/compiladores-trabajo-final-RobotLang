"""
Tabla de símbolos con soporte de ámbitos anidados.
"""
from typing import Dict, Optional


class SymbolTable:
    """Tabla de símbolos con soporte de ámbitos anidados."""

    def __init__(self, parent: Optional['SymbolTable'] = None):
        self._table: Dict[str, dict] = {}
        self.parent = parent

    def define(self, name: str, kind: str, line: int):
        self._table[name] = {'kind': kind, 'line': line, 'used': False}

    def lookup(self, name: str) -> Optional[dict]:
        if name in self._table:
            return self._table[name]
        if self.parent:
            return self.parent.lookup(name)
        return None

    def mark_used(self, name: str):
        if name in self._table:
            self._table[name]['used'] = True
        elif self.parent:
            self.parent.mark_used(name)

    def all_symbols(self) -> Dict[str, dict]:
        return dict(self._table)

    def print_table(self, title: str = "Tabla de Símbolos"):
        print(f"\n  {'─'*50}")
        print(f"  {title}")
        print(f"  {'─'*50}")
        print(f"  {'NOMBRE':<20} {'TIPO':<12} {'LÍNEA':>6} {'USADO':>6}")
        print(f"  {'─'*50}")
        for name, info in self._table.items():
            used = "sí" if info['used'] else "no"
            print(f"  {name:<20} {info['kind']:<12} {info['line']:>6} {used:>6}")
        print(f"  {'─'*50}")

__all__ = ["SymbolTable"]
