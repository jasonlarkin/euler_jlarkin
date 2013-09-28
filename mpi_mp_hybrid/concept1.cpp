#include <omp.h>
#include "mpi.h"
#include <stdio.h>
#define _NUM_THREADS 4

int main (int argc, char *argv[]) {
  int p,my_rank,c;
  c = 0;
  /* set number of threads to spawn */
  omp_set_num_threads(_NUM_THREADS);
  /* initialize MPI stuff */
  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD,&p);
  MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
  /* the following is a parallel OpenMP
   * executed by each MPI process
   */
  #pragma omp parallel
  {
    #pragma omp master
    {
      if ( 0 == my_rank) {
         // some MPI_ call as ROOT process
         c = 1; printf("%d\n",my_rank);}
      else {
         // some MPI_ call as non-ROOT process
         c = 2; printf("%d\n",my_rank);}
    }
  }
  /* expect a number to get printed for each MPI process */
  printf("%d\n",c);
  /* finalize MPI */
  MPI_Finalize();
  return 0;
}
