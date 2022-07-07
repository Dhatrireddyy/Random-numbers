#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

int main()
{
    printf("Mean=%lf\n",mean("uni.dat"));

    printf("Variance=%lf",var("uni.dat"));
    return 0;
}
