# Nim Game with AI Training (Python)

This is a Python implementation of the classic game of **Nim**, where you play against an **AI opponent that learns over time**. The AI improves its strategy through self-play and simple reinforcement learning.

##  Objective

Take turns removing objects from heaps. On each turn, you may remove any number of objects from a single heap. The player who removes the last object **loses** (misère play).

## AI Training

- **Self-play** (simulated AI vs AI games)
- **Reinforcement learning** (adjusting move values based on game outcomes)
- **State-value memory** for better future decisions

The more the AI trains, the harder it becomes to beat.

## Requirements

- Python 3.9 or higher
- No external dependencies (pure Python)

## Additional Implemenations

- Using pygame for GUI 

## Getting Started

Clone the repository

```bash
git clone https://github.com/joey727/Nim.git
cd nim-ai-python

