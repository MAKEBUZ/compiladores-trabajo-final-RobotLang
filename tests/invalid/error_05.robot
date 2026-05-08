// error_05: [SEMÁNTICO] Sensor duplicado
sensor temperatura;
sensor temperatura;
rutina main() {
    si temperatura > 50:
        ejecutar enfriar();
}
