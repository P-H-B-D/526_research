# LLM Timeseries Forecasting for Physical Systems



Code demonstration for APHY 526, "Explorations in Physics and Computation", Yale GSAS. 
c/o Peter Bowman-Davis, Fall 2023.

#### *Abstract*: 
LLMs have been shown to be [zero-shot timeseries forecasters](https://arxiv.org/pdf/2310.07820.pdf). I show their zero-shot timeseries forecasting ability can be augmented through contextual information about the generating process (in this case, a physical process), revealing a deep structural connection between next numeric token prediction and textual pretraining.  

"You are a helpful assistant that performs time series predictions on a Damped Harmonic Oscillator."            |  "You are a helpful assistant that performs time series predictions."
:-------------------------:|:-------------------------:
![Fig1](https://github.com/P-H-B-D/526_research/blob/main/READMEfigures/Figure_1.png)  |  ![Fig2](https://github.com/P-H-B-D/526_research/blob/main/READMEfigures/Figure_2.png)
Average MAE:  52.35185  |  Average MAE:  77.82245000000002
Average MSE:  4960.373449999999 | Average MSE:  12778.02805
Min MAE:  17.85 | Min MAE:  16.65
Min MSE:  423.75 | Min MSE:  449.55
Fraction of samples with values outside of bounds:  0.002 | Fraction of samples with values outside of bounds:  0.029
Fraction of samples with values outside of true bounds:  0.349 | Fraction of samples with values outside of true bounds:  0.666


### [Code Example 1 (Underdamped Harmonic Oscillator)](https://github.com/P-H-B-D/526_research/blob/main/dampedHarmonic.ipynb) | [Code Example 2 (Noisy Sinusoid)](https://github.com/P-H-B-D/526_research/blob/main/sineWave.ipynb)

Expanding on the work of [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf), I investigate the ability of Large Language Models (LLMs) to act as Zero-Shot Time Series Forecasters within the context of physical systems modelling. In particular, I measure the ability of LLMs to incorporate textual information about the physical system (e.g. a description of the system, its mechanics or physical attributes, etc.) for use in its forecasting. This demonstration may be seen as a natural extension to the results of [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf), and related literature on In-Context-Learning (ICL) more broadly, (see: [Brown et al.](https://arxiv.org/pdf/2005.14165.pdf), [Min et al.](https://arxiv.org/pdf/2202.12837.pdf)), given that the process of integrating physical descriptions into the forecasted sequence is done entirely in-context.

I first set up the experiment to use the tokenization technique described by [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf) to leverage GPT-3.5-Turbo tokenization for the in-context "training" data (e.g. the given tokens), ensuring each timestep maps to a single token, and all tokens are separated by space tokens (see [tokenizerTest.py](https://github.com/P-H-B-D/526_research/blob/main/tokenizerDemo/tokenizerTest.py) for a proof-of-concept of this). 

Next, I demonstrate the process of augmenting zero-shot timeseries forecasting using physical descriptors on two systems: An underdamped harmonic oscillator and a noisy sinusoidal signal. In doing so with significant sample and sequence size (n=1000 and generation length = 20) for each physical descriptor, I measure the effect of various physical descriptors on statistical outcomes of the models, such as the average error and variance in sequence generation.

In doing so, I find that the integration of different physical information into the prompt may either increase or decrease the error and index-wise standard deviation of the generated sequences. Somewhat predictably, this means that not all physical information is integrated equally into the timeseries forecasting process. It is thus described that further research is needed to better understand the relation of various descriptors and their resulting effects on statistical outcomes.

This work demonstrates strong empirical evidence for the possible benefit of incorporating physical descriptors into the zero-shot forecasting prompt. In turn, this reveals a nontrivial insight into transformers: zero-shot timeseries forecasting ability can be augmented through textual descriptors about the generating process, revealing a deep structural connection between next numeric token prediction and textual pretraining. That is to say, the LLM appears to be capable of effectively integrating contextual information about processes which generate timeseries data into next-token prediction, even when the contextual information pertains to abstract concepts such as an "underdamped harmonic oscillator". Even more impressive is that this entire process takes place in-context and without the use of techniques such as [Chain-of-Thought (Wei et al.)](https://arxiv.org/abs/2201.11903), which would likely be able to even further boost performance through a textual description generation process. 

Use of ChatGPT/Generative AI Statement: Github Copilot was used to generate print statements and matplotlib graphs, but not in the core algorithmic development or logical implementations.

Collaboration Statement: All work was conducted by Peter Bowman-Davis.