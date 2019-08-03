#!/usr/bin/python3

import string
import random

def pickSerial():
    key, charset = "", string.digits
    blocks, block_sum_list = [], []
    s1, s2, sum_each_block = 0, 0, 0

    while True:
        for x in range(19):
            if x == 4 or x == 9 or x == 14:
                key += '-'
            else:
                key += random.choice(charset)

        blocks = key.split('-')

        for x in blocks:
            for c in x:
                sum_each_block += int(c)
            block_sum_list.append(sum_each_block)
            sum_each_block = 0

        s1 = block_sum_list[0] + block_sum_list[1]
        s2 = block_sum_list[2] + block_sum_list[3]

        # verify constrains below

        if s1 == (s2 + s2):
            if block_sum_list[1] > block_sum_list[2]:
                if (block_sum_list[0] + block_sum_list[3]) & 1 == 0:
                    if block_sum_list[0] > 5:
                        if block_sum_list[0] <= 24:
                            if block_sum_list[3] & 1 != 0:
                                return key
                            else:
                                key = ""
                                #sum_each_block = 0
                                s1 = 0
                                s2 = 0
                                blocks.clear()
                                block_sum_list.clear()
                        else:
                            key = ""
                            #sum_each_block = 0
                            s1 = 0
                            s2 = 0
                            blocks.clear()
                            block_sum_list.clear()
                    else:
                        key = ""
                        #sum_each_block = 0
                        s1 = 0
                        s2 = 0
                        blocks.clear()
                        block_sum_list.clear()
                else:
                    key = ""
                    #sum_each_block = 0
                    s1 = 0
                    s2 = 0
                    blocks.clear()
                    block_sum_list.clear()
            else:
                key = ""
                #sum_each_block = 0
                s1 = 0
                s2 = 0
                blocks.clear()
                block_sum_list.clear()
        else:
            key = ""
            #sum_each_block = 0
            s1 = 0
            s2 = 0
            blocks.clear()
            block_sum_list.clear()

print("Welcome to my keygen, it's ugly and not-optimized, but the purpose is not performance.")
print("Developed by: Binary Newbie")
print()
print("Key:", pickSerial())
