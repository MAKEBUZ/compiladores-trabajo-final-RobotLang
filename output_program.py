# ============================================================
# Código generado automáticamente por RobotLang Compiler
# Universidad Cooperativa de Colombia — Compiladores 2026
# ============================================================

# --- Sensores (variables globales) ---
proximidad = 0
temperatura = 0

def esquivar():
    if proximidad < 10:
        girar_izquierda()
    else:
        avanzar()

def monitorear():
    if temperatura > 80:
        apagar_motor()
    else:
        continuar()

def main():
    esquivar()
    monitorear()

# --- Punto de entrada ---
main()