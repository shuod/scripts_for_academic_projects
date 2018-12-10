/*
Function: Initiate ten-thread calculations, each run a shell script.
Usage: replace the filename with the shell script you want to run.
Version: 20131231
Author: Shuo Dai

Environment: Centos 6 

Others: This program for Top-1000 calculation and used as step4. 

*/


#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

int nthreads,tid,i;

/* fork a team of thread */
#pragma omp parallel private(nthreads,tid)
{

tid=omp_get_thread_num();
nthreads=omp_get_num_threads();

if (tid==1)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish1");
}

if (tid==2)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish2");
}

if (tid==3)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish3");
}

if (tid==4)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish4");
}

if (tid==5)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish5");
}


if (tid==6)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish6");
}

if (tid==7)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish7");
}


if (tid==8)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish8");
}

if (tid==9)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish9");
}


if (tid==10)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system("~/Template/top1000/generate_octopus_abs_finish10");
}



if (tid==0)
{
printf ("Total threads are %d and you are using thread %d) \n",nthreads, tid);
system(" The current starts.");
}



}

return 0;

}

