// test_09: Comparador mayor que
sensor presion;
rutina aliviar() {
    si presion > 200:
        ejecutar apagar_motor();
    sino:
        ejecutar continuar();
}
rutina main() {
    aliviar();
}
