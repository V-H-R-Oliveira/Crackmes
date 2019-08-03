#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int parse(int current_seed,int new_seed,int current_interation)
{
  unsigned int offset;
  int new_seed_copy;
  int i = 0;
  int offset2 = 1;
  
  if(new_seed == 0) 
  {
  //  puts("ERROR\nInvalid chain produced!");
    //exit(0);
  }
  
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

int main(int argc, char **argv)
{
    int links;
    int i = 0;
    int seed_cpy;
    int new_seed;
    int seed;

    string argv1_to_cpp_string = argv[1];
    
    seed = stoi(argv1_to_cpp_string, nullptr, 10);

    links = (int)(((seed ^ 0x141) + (seed ^ 0x7b)) * 0x533d) % 100;

    if((int)links < 0) 
    {
      links = -links;
    }else 
    {
      if(links == 0) 
      {
        links = 10;
      }
    }

    
    printf("Seed %s requires %d links\n\n",argv[1],(unsigned long)links);
    seed_cpy = seed;

    while((i < 100 && (i < links))) 
    {
      printf("LINK %d\t\t%d\t->\t",(unsigned long)(i + 1),(unsigned long)seed_cpy);
      seed_cpy = parse(seed,seed_cpy,i);
      new_seed = seed_cpy;
      
      if(seed_cpy < 0) 
      {
        new_seed = 0;
      }

      printf("%d\t Sleeping for %dms\n",(unsigned long)seed_cpy,(unsigned long)new_seed);
      i++;
    }
    
    if(i == 99) 
    {
      puts("ERROR\nMaximum allowed iterations reached");
      exit(1);
    }
    
    printf("%u == %u && %u == %u\n", seed, seed_cpy, i, links);

    if((seed == seed_cpy) && (i == links)) 
    {
      puts("You have broken the chain!");
      exit(0);
    }

    puts("ERROR\nStarting seed doesnt match final output");
    return 0;
}
