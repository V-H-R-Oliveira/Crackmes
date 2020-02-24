#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <elf.h>
#include <sys/mman.h>

void *mapFile(const char *path, long *filesize)
{
    FILE *file = fopen(path, "rb");
    int fd;
    void *content;

    if (!file)
    {
        perror("fopen error:");
        exit(EXIT_FAILURE);
    }

    if (fseek(file, 0, SEEK_END) == -1)
    {
        fclose(file);
        perror("fseek error:");
        exit(EXIT_FAILURE);
    }

    fd = fileno(file);

    if (fd == -1)
    {
        fclose(file);
        perror("fileno error:");
        exit(EXIT_FAILURE);
    }

    *filesize = ftell(file);
    rewind(file);

    if (content = mmap(NULL, *filesize, PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0), content == MAP_FAILED)
    {
        fclose(file);
        perror("mmap error:");
        exit(EXIT_FAILURE);
    }

    fclose(file);
    printf("[+] %s was mapped into memory.\n", path);
    return content;
}

void freeContent(void *content, long filesize)
{
    if (munmap(content, filesize) == 0)
        printf("[+] The block memory of size %ld bytes was deallocated from the memory.\n", filesize);
}

void writeNewFile(char *content, long filesize)
{
    FILE *file;
    file = fopen("crackme-debuggable", "wb");

    if (!file)
    {
        freeContent(content, filesize);
        perror("fopen error:");
        exit(EXIT_FAILURE);
    }

    fwrite(content, filesize, 1, file);
    puts("[+] The new file was created.");
    fclose(file);
}

void parseElf(char *content, long filesize)
{
    Elf32_Ehdr *elf_headers = (Elf32_Ehdr *)content;
    elf_headers->e_shoff = 0x1734;
    elf_headers->e_shnum = 34;
    Elf32_Shdr *shdr = (Elf32_Shdr *)(content + elf_headers->e_shoff);
    shdr[31].sh_offset = 0x160a; // fim é 0x1730
    shdr[31].sh_size = 0x126;
    writeNewFile(content, filesize);
    freeContent(content, filesize);
}

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage %s <file>\n", *argv);
        return 1;
    }

    const char *path = argv[1];
    char *content;
    long filesize = 0;

    content = mapFile(path, &filesize);
    parseElf(content, filesize);

    return 0;
}
