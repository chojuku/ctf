/***
bof.c
$ gcc -m32 -fno-stack-protector -o bof bof.c
$ python -c 'print("A"*128)' | ./bof
$ python -c 'print("A"*128)' | strace -i ./bof
***/

#include <stdio.h>

int main (int argc, char *argv[]) {
  char buffer[100];
  fgets(buffer, 128, stdin);
  return 0;
}
