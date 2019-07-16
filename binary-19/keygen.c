#include <stdio.h>
#include <string.h>
#include <stdbool.h>

unsigned long sum_ascii(char *username)
{
  size_t username_length = strlen(username);
  unsigned long sum_ascii_each_char = 0, i = 0;
  
  while(i <= username_length) 
  {
    sum_ascii_each_char += (int)username[i];
    i++;
  }

  return sum_ascii_each_char;
}

int main(int argc, char ** argv)
{
    char *username;
    unsigned long username_ascii_sum;
    char first_username_char;

    if(argc == 2)
    {
        username = argv[1];
        first_username_char = *username;
        username_ascii_sum = sum_ascii(username);
        printf("Your password: %ld\n",(unsigned long)((username_ascii_sum ^ (int)first_username_char * 3) << 10));
    }else
    {
        fprintf(stderr, "Invalid or insufficent arguments");
        return 1;
    }

    return 0;
    //printf("%u\n", ((unsigned int)564 ^ (int)chr * 3) << 10);
}
