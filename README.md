# LLM Timeseries Forecasting for Physical Systems

#### Informal TL;DR: LLMs have been shown to be [zero-shot timeseries forecasters](https://arxiv.org/pdf/2310.07820.pdf). I show their zero-shot timeseries forecasting ability can be augmented through contextual information about the generating process (in this case, a physical process), revealing a deep structural connection between next numeric token prediction and textual pretraining.  

An open-source demonstration created by Peter Bowman-Davis for APHY 526, "Explorations in Physics and Computation", at Yale University Graduate School of Arts and Sciences.

"You are a helpful assistant that performs time series predictions on a Damped Harmonic Oscillator."            |  "You are a helpful assistant that performs time series predictions."
:-------------------------:|:-------------------------:
![Fig1](https://github.com/P-H-B-D/526_research/blob/main/READMEfigures/Figure_1.png)  |  ![Fig2](https://github.com/P-H-B-D/526_research/blob/main/READMEfigures/Figure_2.png)
![Fig3](https://github.com/P-H-B-D/526_research/blob/main/READMEfigures/Figure_3.png)  |  ![Fig4](https://github.com/P-H-B-D/526_research/blob/main/READMEfigures/Figure_4.png)



Expanding on the work of [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf), I investigate the ability of Large Language Models (LLMs) to act as Zero-Shot Time Series Forecasters within the context of physical systems modelling. In particular, I investigate the ability of LLMs to incorporate textual information about the physical system (e.g. a description of the system, its mechanics or physical attributes, etc.) for use in its forecasting. If this proves to be successful, it may be seen as a natural extension to the results of [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf), and related literature on In-Context-Learning (ICL) more broadly, (see: [Brown et al.](https://arxiv.org/pdf/2005.14165.pdf), [Min et al.](https://arxiv.org/pdf/2202.12837.pdf)).

I first set up the experiment to use the tokenization technique described by [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf) to leverage GPT-3.5+ tokenization for the positional data, ensuring each timestep maps to a single token, and all tokens are separated by space tokens (see [tokenizerTest.py](https://github.com/P-H-B-D/526_research/blob/main/tokenizerDemo/tokenizerTest.py) for a proof-of-concept of this). Next, I generate a variety of data for physical systems (see [main.py](https://github.com/P-H-B-D/526_research/blob/main/main.py) > function library – currently, a SHO and damped harmonic oscillator are implemented) for timeseries forecasting. After, I design a variety of prompts that describe each physical system in terms of its attributes. Finally, I use OpenAI's GPT-3.5-Turbo model to generate predictions for the next sequence of position tokens. After many trials, I will determine the difference in distributions between prompting strategies, which will effectively determine if the descriptor of the physical system has positive impact upon its ability to forecast next timesteps in the system.

This work is important because it not only shows that using LLMs for Zero-Shot Timeseries forecasting is advantageous due to their domain agnosticism, but also because they may be augmented with additional textual data.

TODO:
- Improve the README writeup. 
- Add more physical demonstrations (Lotka-Volterra, Replicator equations)
- Evaluate the effects of various prompting techniques (e.g. in-context natural language physical descriptors) on timeseries forecasting. 
