# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Author: Peter Bowman-Davis, Nov 20, 2023                    #
# Demonstration of tokenizer for up to triple digit numbers   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import tiktoken

baseString="499 790 973 975 794 501 206 24 24 205 499 790 973 975 794 501 206 24 24 205"
enc = tiktoken.encoding_for_model("gpt-3.5-turbo-instruct")
tokenList=[]
for token in enc.encode(baseString):
    tokenList.append(enc.decode_single_token_bytes(token).decode("utf-8"))

split=baseString.split(" ")
decomposed=[]


for i in range(len(split)-1):
    decomposed.append(split[i])
    decomposed.append(" ")
decomposed.append(split[-1])

assert tokenList == decomposed  # = ['499', ' ', '790', ' ', '973', ' ', ... etc]



