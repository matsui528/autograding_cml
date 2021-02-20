#include <stdio.h>
#include <stdlib.h>

int multiply (int a, int b) {
    // この関数内部を編集してください
    return a * b;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Error\n");
        return -1;
    }
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    printf("%d\n", multiply(a, b));
    return 0;
}