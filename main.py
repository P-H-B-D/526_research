from dataGenerator import dataGenerator
from openai import OpenAI
import matplotlib.pyplot as plt

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Author: Peter Bowman-Davis, Nov 20, 2023                          #
# Version 1 of Timeseries Prediction for Physical Systems Demo      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

client = OpenAI()
dg = dataGenerator()
input=dg.generateStringOutput()




sysPrompt="You are a helpful assistant that performs time series predictions. Please continue the following sequence without producing any additional text, just return the numbers. "
prompt=input 

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": sysPrompt},
    {"role": "user", "content": prompt}
  ],
  max_tokens=25
)

generatedNumbers=completion.choices[0].message.content

generatedSamples=[int(stringNumber) for stringNumber in generatedNumbers.split(" ")]

plt.plot(range(0,len(input.split(" "))),[int(y) for y in input.split(" ")], 'r')
plt.plot(range(0,len(input.split(" "))),[int(y) for y in input.split(" ")], 'ro')
plt.plot(range(len(input.split(" ")), len(input.split(" ")) + len(generatedSamples)), generatedSamples, 'b')
plt.plot(range(len(input.split(" ")), len(input.split(" ")) + len(generatedSamples)), generatedSamples, 'bo')
plt.show()

# try:
#     generatedSamples=[int(stringNumber) for stringNumber in generatedNumbers.split(" ")]

#     plt.plot(range(0,len(input.split(" "))),[int(y) for y in input.split(" ")], 'ro')
#     plt.plot(range(len(input.split(" ")), range(len(input.split(" ")) + len(generatedSamples))), generatedNumbers, 'bo')


# except:
#     print("Error: Generated numbers do not match expected format.")
#     print("Expected: ['number', ' ', 'number', ' ', 'number', ' ', ... etc], got: " + generatedNumbers)
#     #TODO: Add retry logic.
#     exit(1)


