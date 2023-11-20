# from openai import OpenAI
# client = OpenAI()

# completion=client.completions.create(
#   model="gpt-3.5-turbo-instruct",
#   prompt="What is the next value: 499 790 973 975 794 501 206 24 24 205 499 790 973 975 794 501 206 24 24 205",
#   max_tokens=2,
#   temperature=1
# )

# if(completion.choices[0].text[0] == "\n" or completion.choices[0].text[0] == " "):
#   print(completion.choices[0].text[1:])
# else:
#   print(completion.choices[0].text)

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant that performs time series predictions. Please continue the following sequence without producing any additional text, just return the numbers. "},
    {"role": "user", "content": "503 723 961 899 766 482 237 104 62 234 491 763 924 913 762 483 212 98 76 248 514 515 702 845 901 845 640 381 156 83 130 362 600 838 972 930 744 442 185"}
  ],
  max_tokens=25
)

print(completion.choices[0].message)


# #tokenizer verification

# import tiktoken
# enc = tiktoken.encoding_for_model("gpt-3.5-turbo-instruct")
# for token in enc.encode("499 790 973 975 794 501 206 24 24 205 499 790 973 975 794 501 206 24 24 205"):
#     print(enc.decode_single_token_bytes(token))


