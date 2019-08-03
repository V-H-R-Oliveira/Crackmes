#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

int parse(int current_seed,int new_seed,int current_interation)
{
  unsigned int offset;
  int new_seed_copy;
  int i = 0;
  int offset2 = 1;
  
  if((new_seed < -0x1000) || (new_seed_copy = new_seed, 0x1000 < new_seed)) 
  {
    offset = (unsigned int)(new_seed >> 0x1f) >> 0x14;
    new_seed_copy = -((new_seed + offset & 0xfff) - offset);
  }
  
  while (i < 3) 
  {
    offset2 = offset2 ^ new_seed_copy << ((char)i & 0x1f);
    i++;
  }

  return (int)(current_seed + ((current_interation + current_seed) - 1U ^ new_seed_copy) + offset2 - 0xf);
}

int bruteForce(void)
{
    int links, seed_cpy, new_seed, seed, i = 0, z = -1;
    
    while(z > -214748367)
    {
    
        seed = z;

        links = (((seed ^ 0x141) + (seed ^ 0x7b)) * 0x533d) % 100;

        if(links < 0) 
        {
            links = -links;
        }else 
        {
            if(links == 0) 
            {
                links = 10;
            }
        }
    
        seed_cpy = seed;

        while((i < 100 && (i < links))) 
        {
            seed_cpy = parse(seed, seed_cpy, i);
            new_seed = seed_cpy;
      
            if(seed_cpy < 0) 
            {
                new_seed = 0;
            }

            i++;
        }
    
        if(i == 99) 
        {
            puts("ERROR\nMaximum allowed iterations reached");
            return 1;
        }
    
        if((seed == seed_cpy) && (i == links)) 
        {
            return seed;
        }

        seed_cpy = 0;
        links = 0;
        i = 0;
        z--;
    }
    
    puts("Nothing founded.");
    return 1;
}

void menu(void)
{
    puts("Welcome to my fancy brute forcer algorithm.");
    puts("I've tried with positive integers and nothing was founded, so why not try with negative integers...");
    puts("Developed by: Binary Newbie");
    puts("");
}

int main(void)
{
    menu();
    
    int res = bruteForce();
    char seed[10000];

    if(res == 1)
    {
        fprintf(stderr, "Seed not founded.\n");
        return 1;
    }
    
    usleep(1000000);
    sprintf(seed, "%d", res);
    puts("=============================");
    puts("Auto exec with the valid seed");
    char *args[3] = {"./chainbreaker", seed, NULL};
    execve(args[0], args, NULL);

    return 0;
}
