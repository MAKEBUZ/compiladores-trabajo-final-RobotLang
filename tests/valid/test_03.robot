// test_03: Llamada a rutina propia (call) dentro de main
sensor temperatura;
rutina verificar_temp() {
    si temperatura > 90:
        ejecutar apagar_sistema();
    sino:
        ejecutar operar_normal();
}
rutina main() {
    verificar_temp();
}
