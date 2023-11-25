import numpy as np

def npv(benefit: np.ndarray, cost: np.ndarray, discount_rate=0.05) -> float:
    time = np.arange(1, len(benefit) + 1)
    discount = (1 + discount_rate) ** time
    return np.sum((benefit - cost) / discount)

benefit_data = np.array([100, 200, 300, 400, 500])
cost_data = np.array([50, 100, 150, 200, 250])

result = npv(benefit_data, cost_data)
print(result)
