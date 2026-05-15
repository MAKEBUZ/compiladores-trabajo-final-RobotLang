// test_08: Número decimal en expresión
sensor voltaje;
rutina controlar() {
    si voltaje < 3.7:
        ejecutar avanzar();
    sino:
        ejecutar estado_ok();
}
rutina main() {
    ejecutar controlar();
}
