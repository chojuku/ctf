/***
 $ gcc -m32 -o format format.c
 $ ./format
"%x,%x,%x,%x,%x,%x,%x,%x,%x
 ***/
#include <stdio.h>

int main(int argc, char *argv[]) {
  char str[128];
  fgets(str, 128, stdin);
  printf("Hello, ");
  printf(str);
  return 0;
}
