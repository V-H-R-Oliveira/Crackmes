#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#define SIZE 4108

void menu(void)
{
    puts("Welcome to my keygen...");
    puts("The key is your directory parsed by an algorithm described in the write up...");
    puts("Other weird ways to solve this are in the solution package in the file \"weird-solution.txt\"");
    puts("Fill the problem input with the key and be happy :)");
    puts("If you see a non printable string, i suggest you resize your value input, only printable keys are valid in this program :)");
    puts("Developed by Binary Newbie");
}

int main(int argc, char **argv)
{
  menu();

  size_t dir_length;
  int i = 0;
  int length;
  char directory[SIZE];
  char key[SIZE];
  
  getcwd(directory,0x1000);
  dir_length = strlen(directory);
  
  while(i < (int)dir_length) 
  {
    if(directory[(long)i] == '/') 
    {
      directory[(long)i] = '$';
    }
    else 
    {
      if((directory[(long)i] < 'a') || ('z' < directory[(long)i])) 
      {
        if(('@' < directory[(long)i]) && (directory[(long)i] < '[')) 
          directory[(long)i] += '\x1e';
      }
      else 
        directory[(long)i] += -0x1e;
    }

    i++;
  }
  
  if(argc == 2)
  {
      length = atoi(argv[1]);
      
      if(length < 0 || length > SIZE || length > dir_length)
      {
          fprintf(stderr, "Invalid length.\n");
          return 1;
      }else {
          for(int j = 0; j < length; j++)
              key[j] = directory[j];

          printf("Key: %s\n", key);
      }
  }else {
      fprintf(stderr, "usage %s <number>\n", argv[0]);
      return 1;
  }

  return 0;
}

