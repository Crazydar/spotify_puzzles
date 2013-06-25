#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

uint32_t reverse_binary(uint32_t num) {
  int i = 0, rot_back = 0;
  uint32_t res = 0;
  
  while (i < 32) {
    res = res << 1;
    if (num & 1) {
      res = res | 1;
      rot_back = 0;
    }
    else
      rot_back++;
    num = num >> 1;
    i++;
  }  

  while (rot_back) {
    res = res >> 1;
    rot_back--;
  }

  return res;
}


int main(void) {

	uint32_t num = 0;
	scanf("%u", &num);

	num = reverse_binary(num);

	printf("%u\n", num);

	return EXIT_SUCCESS;
}
