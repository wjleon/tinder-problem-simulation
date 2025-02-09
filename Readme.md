# 📌 Tinder Problem Simulation and Optimization

## 📝 Overview
This project simulates the **Secretary Problem**, a famous optimal stopping problem in decision theory. The goal is to determine the optimal **rejection fraction** of candidates before selecting the best one. The simulation runs multiple trials to find the most effective selection strategy, providing insights into probability-driven decision-making.

This implementation:
✅ **Simulates the problem** with a range of rejection fractions.
✅ **Uses Monte Carlo simulations** to compute success rates.
✅ **Generates a visual plot** comparing different strategies.
✅ **Outputs a tabular summary** of results.

## 🎯 Problem Explanation
The **Secretary Problem** models scenarios where a decision-maker must choose the best option without the ability to revisit past choices. Examples include:
- Hiring the best job candidate.
- Selecting the best deal when shopping.
- Choosing a parking spot in a crowded lot.

### 🔹 The Optimal Strategy
The well-known mathematical solution suggests rejecting the first **1/e (~36.8%)** of candidates and then selecting the next best one that surpasses all previous candidates.

## ⚙️ How It Works
1. Candidates are shuffled randomly.
2. A portion (defined by the rejection fraction) is **observed but not selected**.
3. The first candidate better than all previously seen ones is chosen.
4. The success rate and average rank are tracked across many iterations.

## 🚀 Features
- **Progressive candidate evaluation** based on the rejection fraction.
- **Performance evaluation** of different rejection fractions.
- **Graphical representation** of success probability vs. fraction tested.
- **Interactive visualization** using `matplotlib`.
- **Optimal fraction discovery** based on empirical simulations.

## 🛠️ Installation
Make sure you have **Python 3.7+** installed.

### Install dependencies:
```sh
pip install numpy matplotlib tqdm
```

## 📌 Usage
Run the script using:
```sh
python tinder-final.py
```

## 📊 Example Output
### 🔢 Text-Based Summary
```
--- Summary of Results ---
Rejection Fraction | Success Rate | Average Rank
-------------------|--------------|-------------
     0.00         |      5.23%    |     52.31
     0.05         |     18.46%    |     47.82
     0.10         |     25.61%    |     41.29
     ...
Optimal Rejection Fraction: 0.368
Optimal Success Rate: 37.2%
Optimal Average Rank: 78.6
Theoretical optimal fraction (1/e): 0.368
```

### 📈 Graphical Output
The script generates a **plot showing success probability** for different rejection fractions. The vertical red line represents the **theoretical optimal fraction (1/e)**.

![Secretary Problem Simulation Graph](graph_placeholder.png)

## 🏆 Key Insights
- **Empirical results align with theoretical expectations.**
- The best strategy **rejects ~36.8% of candidates** before selecting the next best option.
- Lower rejection fractions lead to poor selections, while higher ones risk missing the best candidate.

## 🔥 Future Improvements
- Extend to **real-world hiring data** for better modeling.
- Support **dynamic rejection fractions** based on past observations.
- Implement **multi-round selection strategies**.

## 💡 Contributions
Feel free to fork, submit issues, or suggest improvements! 🚀

📩 **Author:** Wilmer Leon  
🔗 **LinkedIn:** [Wilmer Leon](https://www.linkedin.com/in/wilmer-leon/)
