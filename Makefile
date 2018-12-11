CFLAGS := -Wall -g 
math.out : amath.o main.o
	gcc $(CFLAGS) amath.o main.o -o math.out

amath.o: amath.c defs.h
	gcc -c $(CFLAGS) amath.c

main.o: main.c defs.h
	gcc -c $(CFLAGS) main.c

clean:
	rm -rf math.out
	rm -rf *.o
	rm -rf a.out
	rm -rf build.log
	rm -rf t.txt
