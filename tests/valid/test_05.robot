// test_05: Rutina con varias sentencias
sensor dist;
rutina navegar() {
    si dist < 20:
        ejecutar girar_izquierda();
    sino:
        ejecutar avanzar();
}
rutina main() {
    ejecutar navegar();
    ejecutar navegar();
}
