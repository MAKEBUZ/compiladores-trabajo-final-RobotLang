"""
=============================================================
 Análisis Léxico — RobotLang
 Mini-compilador para configuración de robots
 Universidad Cooperativa de Colombia — Compiladores 2026
=============================================================
"""

import re
from dataclasses import dataclass
from typing import List, Optional


# ─── Tipos de tokens ────────────────────────────────────────

TOKEN_TYPES = [
    # Palabras reservadas
    ('SENSOR',    r'\bsensor\b'),
    ('RUTINA',    r'\brutina\b'),
    ('SI',        r'\bsi\b'),
    ('SINO',      r'\bsino\b'),
    ('EJECUTAR',  r'\bejecutar\b'),
    # Literales
    ('NUMBER',    r'\d+(\.\d+)?'),
    ('ID',        r'[a-zA-Z_][a-zA-Z_0-9]*'),
    # Operadores de comparación
    ('EQ',        r'=='),
    ('LT',        r'<'),
    ('GT',        r'>'),
    # Delimitadores
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('LBRACE',    r'\{'),
    ('RBRACE',    r'\}'),
    ('SEMI',      r';'),
    ('COLON',     r':'),
    # Espacios y comentarios (ignorar)
    ('COMMENT',   r'//[^\n]*'),
    ('NEWLINE',   r'\n'),
    ('SKIP',      r'[ \t\r]+'),
]

MASTER_PATTERN = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)


@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int

    def __repr__(self):
        return f'Token({self.type}, {self.value!r}, L{self.line}:C{self.column})'


class LexerError(Exception):
    def __init__(self, char: str, line: int, col: int):
        self.char = char
        self.line = line
        self.col = col
        super().__init__(
            f'[ERROR LÉXICO] Carácter inesperado "{char}" en línea {line}, columna {col}'
        )


class Lexer:
    """Analizador léxico para RobotLang."""

    SKIP_TYPES = {'SKIP', 'COMMENT', 'NEWLINE'}

    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self._errors: List[str] = []

    def tokenize(self) -> List[Token]:
        """Recorre el código fuente y genera la lista de tokens."""
        line = 1
        line_start = 0
        pos = 0

        compiled = re.compile(MASTER_PATTERN)

        while pos < len(self.source):
            match = compiled.match(self.source, pos)
            if match is None:
                char = self.source[pos]
                col = pos - line_start + 1
                err = LexerError(char, line, col)
                self._errors.append(str(err))
                pos += 1
                continue

            kind = match.lastgroup
            value = match.group()

            if kind == 'NEWLINE':
                line += 1
                line_start = match.end()
            elif kind not in self.SKIP_TYPES:
                col = match.start() - line_start + 1
                self.tokens.append(Token(kind, value, line, col))

            pos = match.end()

        self.tokens.append(Token('EOF', '', line, 0))
        return self.tokens

    @property
    def errors(self) -> List[str]:
        return self._errors

    def print_tokens(self):
        """Muestra la tabla de tokens en pantalla."""
        print("\n" + "=" * 60)
        print("  FASE 1 — ANÁLISIS LÉXICO")
        print("=" * 60)
        print(f"  {'TIPO':<15} {'VALOR':<20} {'LÍNEA':>6} {'COL':>5}")
        print("-" * 60)
        for tok in self.tokens:
            if tok.type != 'EOF':
                print(f"  {tok.type:<15} {tok.value:<20} {tok.line:>6} {tok.column:>5}")
        print("-" * 60)
        print(f"  Total tokens: {len(self.tokens) - 1}")
        if self._errors:
            print("\n  *** ERRORES LÉXICOS ***")
            for e in self._errors:
                print(f"  {e}")
        print("=" * 60 + "\n")
