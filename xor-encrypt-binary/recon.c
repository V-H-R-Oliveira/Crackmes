#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/syscall.h>

int main(int argc, char **argv) {
    if(argc == 2) 
    {
        printf("%ld\n", *(int64_t *)argv[1]);
        if (*(int64_t *)argv[1] == 0x212164656e7770) {
            puts("parabens, voce conseguiu ^.^");
            return 0;
        }
    }

    puts("nao foi dessa vez ...");
    return 1;
}
