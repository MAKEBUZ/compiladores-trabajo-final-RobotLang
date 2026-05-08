// test_10: Programa complejo con múltiples rutinas y llamadas encadenadas
sensor proximidad;
sensor luz;
rutina evitar_obstaculo() {
    si proximidad < 8:
        ejecutar retroceder();
    sino:
        ejecutar avanzar();
}
rutina ajustar_luz() {
    si luz < 20:
        ejecutar encender_faro();
    sino:
        ejecutar apagar_faro();
}
rutina ciclo_trabajo() {
    ejecutar evitar_obstaculo();
    ejecutar ajustar_luz();
}
rutina main() {
    ciclo_trabajo();
}
