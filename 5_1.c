#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "/Users/dhatrireddy/Desktop/gvv/header.h"

int main() {
	FILE *fp = fopen("ber.dat", "w");

	for (int i = 0; i < 1000000; i++) {
		fprintf(fp, "%lf\n", randomBernoulli());
	}
	fclose(fp);
	return 0;	
}