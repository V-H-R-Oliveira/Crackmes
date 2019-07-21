#include <stdio.h>
#include <string.h>
#define SIZE 11
#define USER_LENGTH 13

int main(void)
{
    char buffer[SIZE], username[USER_LENGTH];
    char password_input[] = "M-f=j-b=f-P="; // random string
    char s[] = "THEPIRATEISZ", s2[] = "?*-/597$=#&@";
    char username_copy[USER_LENGTH];
    int i = 0, j = 0, k = 0, offset = 0;

    printf("Enter username, with length 12: ");
    fgets(username, USER_LENGTH, stdin);
    
    username[13] = '\0';
    strncpy(username_copy, username, 12);
    username_copy[13] = '\0';
    
    if(strlen(username) == 12)
    {
         while (i < SIZE)
         {
            offset = (int)(char)username[(long)i] ^ (int)s[(long)i] + 0x32U;
            buffer[(long)i] = (char)offset + (char)(offset / 100) * -100 + 'A';
            k = i * 9 + 5;
            buffer[(long)(i + 1)] = s2[(long)(k + ((k / 6 + (k >> 0x1f) >> 1) - (k >> 0x1f)) * -0xc)];
 
            if(((j == i) && (buffer[(long)i] == password_input[(long)i])) && (buffer[(long)(i + 1)] == password_input[(long)(i + 1)])) 
            {
                j += 2;
            }
 
            i += 2;
        }

        buffer[12] = '\0';
        printf("Username: %sPassword: %s\n", username_copy, buffer);
    }else
    {
        fprintf(stderr, "Invalid length\n");
        return 1;
    }

    return 0;
}
