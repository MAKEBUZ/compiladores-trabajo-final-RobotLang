// test_08: Número decimal en expresión
sensor voltaje;
rutina controlar() {
    si voltaje < 3.7:
        ejecutar cargar_bateria();
    sino:
        ejecutar operar();
}
rutina main() {
    ejecutar controlar();
}
