#include <stdio.h>
 
int main()
{
    int i = 100, j = 200;
    
    for (i; i < j; i++) {
    	if (i % 2 == 0) {
    	  printf("%d%s", i," ��ż��\n");
    	  if (i == 2) {
			printf("%s%d%s", "isPrime:", i, "\n");
		  }
		} else {
    	  printf("%d%s", i," ������\n");
			
			int isPrime = 1;
			int n;
			for (n = 2; n < i; n++) {
			    if (i % n == 0) {
			    	isPrime = 0;
			    }
			}
			
			if (i != 1 && isPrime == 1) {
				printf("%s%d%s", "isPrime:", i, "\n");
			}
		
		}
	} 

    return 0;
}
