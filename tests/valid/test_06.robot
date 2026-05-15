// test_06: Tres sensores, tres rutinas coordinadas
sensor proximidad;
sensor luz;
sensor temperatura;
rutina esquivar() {
    si proximidad < 15:
        ejecutar girar_izquierda();
    sino:
        ejecutar avanzar();
}
rutina iluminar() {
    si luz < 30:
        ejecutar alerta_proximidad();
    sino:
        ejecutar estado_ok();
}
rutina controlar_calor() {
    si temperatura > 75:
        ejecutar apagar_motor();
    sino:
        ejecutar continuar();
}
rutina main() {
    ejecutar esquivar();
    ejecutar iluminar();
    ejecutar controlar_calor();
}
