// error_02: [SEMÁNTICO] Rutina main() faltante
sensor luz;
rutina encender() {
    si luz > 50:
        ejecutar led_on();
}
