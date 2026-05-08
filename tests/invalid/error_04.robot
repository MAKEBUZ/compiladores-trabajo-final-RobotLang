// error_04: [SEMÁNTICO] Rutina duplicada
sensor luz;
rutina main() {
    ejecutar encender();
}
rutina main() {
    ejecutar apagar();
}
