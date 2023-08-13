#include <stdio.h>

int main() {
    int a;
    char b;
    float c;
    double d;

    printf("Size of int: %ld bytes\n", sizeof(a));
    printf("Size of char: %ld byte\n", sizeof(b));
    printf("Size of float: %ld bytes\n", sizeof(c));
    printf("Size of double: %ld bytes\n", sizeof(d));

    return 0;
}
