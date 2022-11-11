#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - functions an infinite loop
 *
 * Return: 0 in success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie process
 *
 * Return: 0 in success
 */
int main(void)
{
	int itr = 5;

	while (itr > 0)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
		itr--;
	}
	infinite_while();
	return (0);
}
