# ============================================================
# Código generado automáticamente por RobotLang Compiler
# Universidad Cooperativa de Colombia — Compiladores 2026
# ============================================================

# --- Sensores (variables globales) ---
proximidad = 0
temperatura = 0

# --- Acciones primitivas del robot ---
def girar_izquierda():
    print("Robot girando a la izquierda")

def avanzar():
    print("Robot avanzando")

def apagar_motor():
    print("Motor apagado")

def continuar():
    print("Robot continuando")

# --- Rutinas generadas ---

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
if __name__ == "__main__":
    main()