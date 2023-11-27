import asyncio
from openai import AsyncOpenAI
from dataGenerator import dataGenerator
import numpy as np


client = AsyncOpenAI()

# Function 'library'
damped_harmonic_oscillator=lambda x: np.exp(-x)*np.sin(2*np.pi*x)
sine_wave=lambda x: np.sin(2*np.pi*x)

# Generate input sequence
dg=dataGenerator(t_max=2, samples=31, noise=0.0,fxn=damped_harmonic_oscillator)


prompt=dg.generateStringOutput()

sysPrompt="You are a helpful assistant that performs time series predictions. Please continue the following sequence without producing any additional text, just return the numbers. "

async def make_chat_completion(semaphore, sysPrompt,prompt):
    async with semaphore:
        chat_completion = await client.chat.completions.create(
            messages=[

                {"role": "system", "content": sysPrompt},
                {"role": "user", "content": prompt}
                
                ],
            model="gpt-3.5-turbo",
        )
        print(chat_completion.choices[0].message.content)



async def main():
    N=2 #Number of concurrent requests for API safety
    semaphore = asyncio.Semaphore(N)

    print("Starting, prompt is: " + prompt + "")
   
    await asyncio.gather(
        make_chat_completion(semaphore, sysPrompt,prompt),
        make_chat_completion(semaphore, sysPrompt,prompt),
    )

asyncio.run(main())




# from openai import OpenAI
# import matplotlib.pyplot as plt
# import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Author: Peter Bowman-Davis, Nov 20, 2023                          #
# # Version 1 of Timeseries Prediction for Physical Systems Demo      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# client = OpenAI()

# # Function 'library'
# damped_harmonic_oscillator=lambda x: np.exp(-x)*np.sin(2*np.pi*x)
# sine_wave=lambda x: np.sin(2*np.pi*x)

# # Generate input sequence
# dg=dataGenerator(t_max=2, samples=31, noise=0.0,fxn=damped_harmonic_oscillator)
# input=dg.generateStringOutput()
# def genNextSequence(inputSeq):
    
#     prompt=inputSeq

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": sysPrompt},
#         {"role": "user", "content": prompt}
#     ],
#     max_tokens=50
#     )
#     return completion


# try:
#     generatedNumbers = genNextSequence(input).choices[0].message.content
# except:
#     print("Error in response from OpenAI API.")
#     exit(1)


# try:
#     generatedSamples=[int(stringNumber) for stringNumber in generatedNumbers.split(" ") if stringNumber != ""]
#     plt.plot(range(0,len(input.split(" "))),[int(y) for y in input.split(" ")], 'r')
#     plt.plot(range(0,len(input.split(" "))),[int(y) for y in input.split(" ")], 'ro')
#     plt.plot(range(len(input.split(" ")), len(input.split(" ")) + len(generatedSamples)), generatedSamples, 'b')
#     plt.plot(range(len(input.split(" ")), len(input.split(" ")) + len(generatedSamples)), generatedSamples, 'bo')
#     plt.xlabel("Time")
#     plt.ylabel("Amplitude")
#     plt.title("Damped Harmonic Oscillator")
#     plt.legend(["","Actual","","Forecast without System Descriptor"])
#     plt.show()

# except:
#     print("Error: Generated numbers do not match expected format.")
#     print("Expected: ['number', ' ', 'number', ' ', 'number', ' ', ... etc], got: " + generatedNumbers)
#     #TODO: Add retry logic.
#     exit(1)


