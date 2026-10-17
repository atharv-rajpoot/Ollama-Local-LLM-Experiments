"""
Name: Atharv Anil Rajpoot
Roll no.: 25f20000553
Workshop Assignment on: Ollama for Beginners: Running Open-Source LLMs Locally
"""

# ============================================================
# TASK 1: Download and run qwen2.5:3b using Ollama CLI
# ============================================================
# Command used to download the model:
# ollama pull qwen2.5:3b

# Command used to run the model:
# ollama run qwen2.5:3b

# Prompt entered: Explain machine learning in simple language.

"""
Output:
Sure! Imagine you have a computer program that can learn and improve from experience, without being explicitly
programmed to do so. This is what machine learning is all about.

In simple terms, machine learning is a way for computers to learn and make decisions based on data. Here's a
breakdown:

1. **Data**: Machines use lots and lots of data to learn. This data could be anything - numbers, text, images,
videos, etc.

2. **Learning Algorithms**: These are like recipes or rules that machines use to understand patterns in the data.
There are many types of learning algorithms, such as regression (which is used for predicting continuous values),
classification (which is used for predicting discrete categories), and clustering (which is used for grouping
similar data together).

3. **Training**: The machine takes the data, uses the learning algorithms, and "learns" to recognize patterns.
This is called "training."

4. **Prediction and Decision Making**: Once the machine has learned from the data, it can then make predictions or
decisions based on new data it hasn't seen before.

Machine learning is all about teaching computers to perform tasks without being explicitly programmed to do so. It
can be used in many different fields, from making recommendations on e-commerce websites (like which products you
might like based on your previous purchases), to predicting weather conditions, or even helping doctors diagnose
diseases.
"""

# ============================================================
# TASK 2: Interact with Ollama using Python
# ============================================================

from ollama import chat

response_task_2 = chat(
    model="qwen2.5:3b",
    messages=[{
        "role": "user",
        "content": (
            "Explain the difference between supervised and unsupervised learning in three bullet points"
        )
    }]
)

print(response_task_2["message"]["content"])

"""
Output:
- Supervised learning involves training a model on a labeled dataset, where the algorithm learns to map inputs to outputs. The dataset includes both input features and corresponding correct output labels, allowing the model to generalize to new, unseen data.
- In contrast, unsupervised learning deals with unlabeled data, where the model must find structure or patterns within the data without any predefined correct answers. This technique is used for tasks like clustering, where the goal is to group similar data points together.
- Supervised learning can be further divided into regression (for predicting continuous values) and classification (for predicting discrete categories), while unsupervised learning includes methods such as clustering and association rule learning.
"""


# ============================================================
# TASK 3: Experiment with another prompt using Ollama
# ============================================================
from ollama import chat

response_task_3 = chat(
    model="qwen2.5:3b",
    messages=[{
        "role": "user",
        "content": "Explain neural networks as if you were teaching a 12-year-old."
    }]
)

print(response_task_3["message"]["content"])

"""
Output:
Sure! Imagine you have a really big puzzle, and you want to solve it without looking at all the pieces at once. That's kind of what a neural network does, but instead of a puzzle, we're dealing with information from the internet or from images or sounds.

### How It Works
Let's start with something simple. Think of a neural network like a bunch of friends who are good at solving puzzles. These friends all work together to solve big puzzles. We call these friends "neurons" in a neural network.
Each neuron knows a bit about the puzzle. For example, one might be really good at recognizing blue squares, another might be good at recognizing the color red, and so on.

### The Input
When we give a neural network a picture or a sound, it doesn’t understand what it is. It’s like having a friend who doesn’t know what colors are. So, we need to tell the network what to look for first. We do this by giving the network something to start with, like giving a clue for the puzzle.

### Processing Information
Once we give the network a clue, it goes to work. Each neuron looks at the clue and decides if it matches what they know well. If it does, they "pass the information" on to the next neuron. It’s like passing a ball around a group of friends. Each friend gets a little piece of the information and decides how to pass it along.

### Learning
To get better at recognizing colors or shapes, these friends need practice. We give them more clues over and over again. Each time they get better at recognizing the puzzle pieces. It's like practicing a sport: the more you practice, the better you get!

### Making Decisions
After all the neurons have finished their part, they decide together what the whole picture looks like. They use their combined knowledge to make a final decision. It's like all the friends working together to solve the puzzle and figuring out what the whole picture looks like.

### That's It!
That's the basic idea of a neural network! It's a bunch of friendly, smart helpers that work together to solve problems, much like how your friends help you when you’re playing games or solving puzzles. They learn from the clues you give them and get better at understanding the information you provide them with.
"""
