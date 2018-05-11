#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	if (argc < 2){
		printf("Provide array size in kilo bytes \n");
		exit(0);
	}
	
	int array_size_in_kilo_bytes = atoi(argv[1]);
	
	int arrayLength = array_size_in_kilo_bytes * 1024;
	int *array = (int*)malloc(arrayLength * sizeof(int));
	

	int steps = 64 * 1024 * 1024; //Arbitrary amount of steps

	for(int i = 0; i < steps; i++){
		array[(i * 16) % arrayLength]++;
	}

	free(array);

	return 0;
}