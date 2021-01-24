#include <stdio.h>
 
int main()
{
    int i = 5, j = 10;
    int result = 0;
    
	int min = i, max = j;
	int out = (min + max) * (max - min + 1) / 2;
	printf("%s%d", "out:", out);
    
    for (i; i <= j; i++) {
    	result += i;
		printf("%s%d", "\nstep:", result);
	}
	
	printf("%s%d", "\nresult:", result);


    return 0;
}
