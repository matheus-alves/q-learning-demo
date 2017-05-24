# q-learning-demo

Master's coursework containing a Python demo for the Q-Learning reinforcement learning algorithm.

This demo presents the results of applying Q-Learning to solve the Cliff-walking problem.

## Requirements

- Python 3.x
- WxPython

## Setup

First you need to install WxPython requirements, please refer to the following link: https://github.com/wxWidgets/Phoenix#prerequisites

After that, to install the requirements simply run the following command:

    pip install -r requirements.txt
    
Note: if pip does not find the wxPython requirement you can find it here: https://wxpython.org/Phoenix/snapshot-builds/
    
## Execution

To run this solution use the following command:

    python demo.py NUM_OF_EPISODES

Where the NUM_OF_EPISODES param is optional and defines the number of episodes that the Q-Learning algorithm is going to use.
It defaults to 250.

## Results

The results are presented in two UIs:

- Q-Learning best path (S = Start, G = Goal)
- Q values (state, action)
