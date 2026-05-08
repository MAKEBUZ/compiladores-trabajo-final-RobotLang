// test_09: Comparador mayor que
sensor presion;
rutina aliviar() {
    si presion > 200:
        ejecutar abrir_valvula();
    sino:
        ejecutar cerrar_valvula();
}
rutina main() {
    aliviar();
}
