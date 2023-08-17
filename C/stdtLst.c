#include <stdio.h>

int main(){
	
	struct Stdts{
		char name[20];
		int age;
		int grade;
	};
	struct Stdts s2 = {"Alice", 19, 90};
	printf("Name = %s , Age = %d , Grade = %d" , s2.name,s2.age,s2.grade);

	return 0;

};

