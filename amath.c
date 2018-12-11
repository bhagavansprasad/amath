
#include "stdio.h"

int get_factorial_value(int n)
{
	int t = 1, i = 0;
	printf ("-->%s, %s, %d\n", __FILE__, __FUNCTION__, __LINE__);

	if (n < 0)
		return -1;

	printf ("-->%u\n", i);
	printf ("-->%u\n", i);

	for (i = 1; i <= n; i++)
	{
		printf ("-->%u\n", i);
		t = t * i;
	}

	return t;
}
