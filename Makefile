all: cacheMeasure.c
	gcc -o cacheMeasure cacheMeasure.c

clean: 
	$(RM) cacheMeasure
