#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define BUFFER_SIZE 1024

// Función de utilidad para manejar errores
void handle_error(const char *message) {
    fprintf(stderr, "Error: %s\n", message);
    if (errno != 0) {
        fprintf(stderr, "Errno: %d\n", errno);
        fprintf(stderr, "Descripción: %s\n", strerror(errno));
    }
    exit(EXIT_FAILURE);
}

int main() {
    FILE *file = NULL;
    char buffer[BUFFER_SIZE];
    size_t bytes_read;

    // 1. Siempre verifica el valor de retorno de fopen
    file = fopen("ejemplo.txt", "r");
    if (file == NULL) {
        handle_error("No se pudo abrir el archivo");
    }

    // 2. Usa fread con comprobación de errores y EOF
    bytes_read = fread(buffer, 1, sizeof(buffer), file);
    if (bytes_read == 0) {
        if (feof(file)) {
            printf("Archivo vacío o se alcanzó el final del archivo\n");
        } else if (ferror(file)) {
            handle_error("Error al leer el archivo");
        }
    } else {
        printf("Se leyeron %zu bytes\n", bytes_read);
    }

    // 3. Siempre cierra los archivos, incluso si hay un error
    if (fclose(file) != 0) {
        handle_error("Error al cerrar el archivo");
    }

    return EXIT_SUCCESS;
}