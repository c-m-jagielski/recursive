import subprocess
import random

# Define weighted probabilities for execution counts
execution_options = [0, 1, 2, 3, 4, 5]  # Possible execution counts
weights = [0.10, 0.72, 0.10, 0.05, 0.02, 0.01]  # Corresponding probabilities

# Choose how many times to run the script
num_executions = random.choices(execution_options, weights, k=1)[0]

print(f"Executing upload_to_git.py {num_executions} times.")

# Execute the script the selected number of times
for _ in range(num_executions):
    subprocess.run(["python3", "upload_to_git.py"])

