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

def alerta_proximidad():
    print("ALERTA: objeto detectado a menos de 10 unidades")

def estado_ok():
    print("Estado del robot: todo en orden")

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

def reportar():
    if proximidad < 10:
        alerta_proximidad()
    else:
        estado_ok()

def main():
    reportar()
    esquivar()
    monitorear()

# --- Punto de entrada ---
if __name__ == "__main__":
    main()