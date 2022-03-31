#include <unistd.h>
#include <stdio.h>

int main(){
	setreuid(1000, 1000);
	system("/bin/sh");
	return 0;
}
