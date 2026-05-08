// test_04: Comparador ==
sensor estado;
rutina main() {
    si estado == 1:
        ejecutar activar_robot();
    sino:
        ejecutar suspender();
}
