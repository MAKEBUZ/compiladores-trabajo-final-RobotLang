// test_04: Comparador ==
sensor estado;
rutina main() {
    si estado == 1:
        ejecutar alerta_proximidad();
    sino:
        ejecutar continuar();
}
