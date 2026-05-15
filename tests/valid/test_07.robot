// test_07: Solo rama si (sin sino)
sensor ruido;
rutina silenciar() {
    si ruido > 100:
    ejecutar continuar();
}
rutina main() {
    ejecutar silenciar();
}
