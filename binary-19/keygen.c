#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#define SIZE 1000

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
    unsigned long username_ascii_sum, password;
    char first_username_char;
    char password_string[SIZE];

    if(argc == 2)
    {
        username = argv[1];
        first_username_char = *username;
        username_ascii_sum = sum_ascii(username);
        password = (unsigned long)((username_ascii_sum ^ (int)first_username_char * 3) << 10);
        printf("Username: %s\nPassword: %ld\n", username, password);
        sprintf(password_string, "%ld", password);
        char *args[4] = {"./keygenme", username, password_string, NULL};
        execve(args[0], args, NULL);
    }else
    {
        fprintf(stderr, "Invalid or insufficent arguments");
        return 1;
    }

    return 0;
}
