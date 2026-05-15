// test_02: Dos sensores, dos rutinas con sino
sensor proximidad;
sensor velocidad;
rutina frenar() {
    si proximidad < 5:
        ejecutar apagar_motor();
    sino:
        ejecutar continuar();
}
rutina main() {
    ejecutar frenar();
}
