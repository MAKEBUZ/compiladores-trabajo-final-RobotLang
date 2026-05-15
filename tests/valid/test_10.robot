// test_10: Programa complejo con múltiples rutinas y llamadas encadenadas
sensor proximidad;
sensor luz;
rutina evitar_obstaculo() {
    si proximidad < 8:
        ejecutar girar_izquierda();
    sino:
        ejecutar avanzar();
}
rutina ajustar_luz() {
    si luz < 20:
        ejecutar alerta_proximidad();
    sino:
        ejecutar estado_ok();
}
rutina ciclo_trabajo() {
    ejecutar evitar_obstaculo();
    ejecutar ajustar_luz();
}
rutina main() {
    ciclo_trabajo();
}
