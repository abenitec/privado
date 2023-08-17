#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// define a structure named 'person'
struct person {
    char name[20];
    int age;
};

int main() {
    // declare a variable of type 'person'
    struct person bob;

    // declare a pointer to a 'person' structure
    struct person *ptr;

    // assign the address of 'bob' to 'ptr'
    ptr = &bob;

    // assign values to the members of 'bob' using 'ptr'
    strcpy(ptr->name, "Bob");
    ptr->age = 25;

    // print the values of the members of 'bob' using 'ptr'
    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);

    return 0;
}
