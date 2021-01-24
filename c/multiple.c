#include <stdio.h>
 
int main()
{
    int i, j;
    int max = 10;
    char s; 
    for (i = 1; i < max; i++) {
    	printf("\n");
    	for (j= 1; j < max; j++) {
    		if (i <= j) {
    			printf("%d%s%d%s%d%s", i, " x ", j, " = ", i * j, "   ");
    	    }
		}
	}
    return 0;
}
