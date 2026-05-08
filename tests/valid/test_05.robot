// test_05: Rutina con varias sentencias
sensor dist;
rutina navegar() {
    si dist < 20:
        ejecutar girar_derecha();
    sino:
        ejecutar avanzar_rapido();
}
rutina main() {
    ejecutar navegar();
    ejecutar navegar();
}
