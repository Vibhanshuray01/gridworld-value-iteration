# GridWorld Value Iteration

## 🚀 Overview  
This repository implements **Value Iteration** for a **4x4 GridWorld** environment.  
The agent starts at the **top-left corner** (State 0) and tries to reach the **bottom-right corner** (State 15).  
Each move incurs a **reward of -1**, and the goal state has a **reward of 0**.  

The algorithm iteratively applies the **Bellman Equation** until the **value function converges**.

---

## 📌 **Concepts Used**
- **Markov Decision Process (MDP)**
- **Value Iteration Algorithm**
- **Bellman Expectation Equation**
- **Reinforcement Learning (RL)**
- **State-Value Function Updates**

---

## 🎯 **Problem Setup**

### 🔹 **Grid Representation (4×4)**
Each cell represents a state. The agent starts at `(0,0)`, and the goal is `(3,3)`.  
The reward is **-1 for each move** until the agent reaches `(3,3)`, which has a reward of **0**.


- **S** = Start State `(0,0)`
- **G** = Goal `(3,3)`
- **.** = Other states with reward `-1`  

---

## 📖 **Mathematical Formulation**

The **Bellman Equation** updates the value of each state as:

\[
V(s) = \max_a \sum_{s'} P(s'|s, a) \left[ R + \gamma V(s') \right]
\]

Where:  
- \( V(s) \) = Value of state **s**  
- \( R \) = Reward for each move **(-1)**  
- \( \gamma \) = **Discount factor (1.0, no discounting)**  
- \( P(s'|s, a) \) = **Transition probability (1/4 for each valid move)**  

---

## ⚙️ **Implementation Steps**

### **1️⃣ Initialize**
- Set all **V(s) = 0** for all states.
- Define **reward = -1** for each move, **0 for the terminal state**.
- Define actions: **Up, Down, Left, Right**.

### **2️⃣ Value Iteration Loop**
- Repeat until **max change in V(s) < 1e-4**:
  - Compute **new values** for each state.
  - Apply the **Bellman Equation**.
  - Track the maximum change to check for **convergence**.

### **3️⃣ Output the final value function**
- The final **V(s)** represents the expected return from each state.

---

## 🔧 **How to Run the Code**
### **1️⃣ Clone the Repository**

git clone https://github.com/Vibhanshuray01/gridworld-value-iteration.git
cd gridworld-value-iteration

**Install dependency if needed,**
pip install numpy

**Run the python script**
python bellman.py



**Example Output as below:**

 -59.423  -57.423  -54.281  -51.710
 -57.423  -54.566  -49.710  -45.139
 -54.281  -49.710  -40.853  -29.997
 -51.710  -45.139  -29.997    0.000


**Future Improvements**

Implement Policy Iteration.
Extend to larger grids (e.g., 5x5, 10x10).
Add obstacles and dynamic rewards.
Train an RL agent using Q-learning.