#include "stdio.h"

int test_num[] = {2, 5, 8, 9};
main(int argc, char *argv[])
{
	int n = 5, retval = 0, i = 0;
	char *p = 100;

	if (argc == 1)
	{
		retval = get_factorial_value(5);
		printf ("-->Test case%d: factorial value of %d, is :%d\n", i+1, n, retval);

		return 1;
	}

	if (strcasecmp(argv[1] , "test2") == 0)
	{
		for (i = 0; i < 2; i++)
		{
			retval = get_factorial_value(test_num[i]);
			printf ("-->Test case%d: factorial value of %d, is :%d\n", i+1, test_num[i], retval);
		}
		return 1;
	}
	else if (strcasecmp(argv[1] , "test3") == 0)
	{
		for (i = 0; i < 3; i++)
		{
			retval = get_factorial_value(test_num[i]);
			printf ("-->Test case%d: factorial value of %d, is :%d\n", i+1, test_num[i], retval);
		}
		return 1;
	}

	printf ("-->INVALID TEST CASE :***%s***\n", argv[1]);
}
