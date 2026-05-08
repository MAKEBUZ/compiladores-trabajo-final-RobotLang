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
        ejecutar encender_faro();
    sino:
        ejecutar apagar_faro();
}
rutina controlar_calor() {
    si temperatura > 75:
        ejecutar activar_ventilador();
    sino:
        ejecutar desactivar_ventilador();
}
rutina main() {
    ejecutar esquivar();
    ejecutar iluminar();
    ejecutar controlar_calor();
}
