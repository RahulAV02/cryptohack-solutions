n = 2048
threshold = 0.75
for i in range(1, n):
    probability = (i / n) ** 2  
    if probability > threshold:
        print(f"Threshold exceeded at iteration: {i}")
        break
