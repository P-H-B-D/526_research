# LLM Timeseries Forecasting for Physical Systems
APHY 526 Yale University
Peter Bowman-Davis, 2023

<!-- You should have (1) a first-pass of one of your code’s 2+ examples, and (2) a draft of the 1-page cheat sheet that intros and explains your project. If your scope has changed from your abstract, you should also indicate this to me, just so I know what is going on. You should very obviously have a working code, or be able to understand and build on prior code you are working with.
The intent behind this demo is essentially just to make sure that I won't have to give you a bad grade for the final project. The goal is that you (and I) should feel like you will obviously be able to complete the project by the end of the month, and I should be able to easily see this from your demo. -->

Expanding on the work of [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf), I investigate the ability of Large Language Models (LLMs) to act as Zero-Shot Time Series Forecasters within the context of physical systems modelling. In particular, I investigate the ability of LLMs to incorporate textual information about the physical system (e.g. a description of the system, its mechanics or physical attributes, etc.) for use in its forecasting. If this proves to be successful, it may be seen as a natural extension to the results of [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf), and related literature on In-Context-Learning (ICL) more broadly, (see: [Brown et al.](https://arxiv.org/pdf/2005.14165.pdf), [Min et al.](https://arxiv.org/pdf/2202.12837.pdf)).

I first set up the experiment to use the tokenization technique described by [Gruver et al.](https://arxiv.org/pdf/2310.07820.pdf) to leverage GPT-3.5+ tokenization for the positional data, ensuring each timestep maps to a single token, and all tokens are separated by space tokens (see ./tokenizerdemo/tokenizerTest.py for a proof-of-concept of this). Next, I generate a variety of data for physical systems (see main.py > function library – currently, a SHO and damped harmonic oscillator are implemented) for timeseries forecasting. After, I design a variety of prompts that describe each physical system in terms of its attributes. Finally, I use OpenAI's GPT-3.5-Turbo model to generate predictions for the next sequence of position tokens. After many trials, I will determine the difference in distributions between prompting strategies, which will effectively determine if the descriptor of the physical system has positive impact upon its ability to forecast next timesteps in the system.

This work is important because it not only shows that using LLMs for Zero-Shot Timeseries forecasting is advantageous due to their domain agnosticism, but also because they may be augmented with additional textual data.

TODO:
- Data integrity verification on over n>1 calls, try "generate next n samples" prompt.
- Generate summary statistics for forecasted data – distribution visualization. Statistics: MAE, distribution distances (KL), geometric properties (curvature estimations, etc).
- Evaluate the effects of various prompting techniques (e.g. in-context natural language physical descriptors) on timeseries forecasting.
