#include <stdio.h>
#include "circleArea.h"

/*
*main - area of the circle
*
*Return: always 0
*/

int main(){
	
	int r= 5;
	double area = Square(r) * Pi;
	printf("%lf", area);
	return 0;
}
