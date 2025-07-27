import os
import sys
import subprocess
import random
from datetime import datetime
import time

# Written with help from ChatGPT
print("\n=================================================\n")

# Configuration
MAX_FILE_SIZE = 10 * 1024  # 10 KB limit
SCRIPT_PATH = os.path.abspath(__file__)

# Check file size before modifying
if os.path.getsize(SCRIPT_PATH) > MAX_FILE_SIZE:
    print("File too large! Aborting modification.")
    sys.exit(1)

# Read current script content
with open(SCRIPT_PATH, "r") as f:
    lines = f.readlines()

# Generate a random harmless modification
upper_bound = str(random.randint(100,9999));
loop_bound = str(random.randint(3,99));
bound2 = str(random.randint(5,16));
modifications = [
    "\n# Auto-update tweak\nx = random.randint(1, " + upper_bound + "); print(f'Random X: {x}')\n",
    "\n# Silent change\nfor i in range(" + loop_bound + "): pass  # Loop doing nothing\n",
    "\n# Generating a new number\ny = sum([i for i in range(" + bound2 + ")]); print(f'Sum: {y}')\n"
]

new_code = random.choice(modifications)

# Prevent duplicate appends
if new_code.strip() not in "".join(lines):
    lines.append(new_code)
else:
    print("No new change needed. Avoiding redundant modification.")
    print(new_code)
    sys.exit(0)

# Generate a unique branch name based on timestamp
branch_name = f"update-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

# Create and switch to the new branch
subprocess.run(["git", "checkout", "-b", branch_name], check=True)

# Write back modified script
with open(SCRIPT_PATH, "w") as f:
    f.writelines(lines)

# Stage the updated file
subprocess.run(["git", "add", SCRIPT_PATH], check=True)

# Commit the changes with a timestamped message
commit_message = f"Automated self-update with randomness on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "commit", "-m", commit_message], check=True)

# Push the branch to remote
subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

# Switch back to main branch
subprocess.run(["git", "checkout", "main"], check=True)

# Merge the temporary branch into main
subprocess.run(["git", "merge", branch_name], check=True)

# Push the merges to main
subprocess.run(["git", "push"], check=True)  # Ensure authentication is set up

# Delete the temporary branch locally and remotely
subprocess.run(["git", "branch", "-d", branch_name], check=True)
subprocess.run(["git", "push", "origin", "--delete", branch_name], check=True)

# Automatically-generated code will be below this line...
# Silent change
for i in range(31): pass  # Loop doing nothing

# Auto-update tweak
x = random.randint(1, 9955); print(f'Random X: {x}')

# Generating a new number
y = sum([i for i in range(14)]); print(f'Sum: {y}')

# Generating a new number
y = sum([i for i in range(5)]); print(f'Sum: {y}')

# Auto-update tweak
x = random.randint(1, 7095); print(f'Random X: {x}')

# Silent change
for i in range(61): pass  # Loop doing nothing

# Silent change
for i in range(58): pass  # Loop doing nothing

# Silent change
for i in range(30): pass  # Loop doing nothing

# Generating a new number
y = sum([i for i in range(15)]); print(f'Sum: {y}')

# Silent change
for i in range(66): pass  # Loop doing nothing

# Generating a new number
y = sum([i for i in range(7)]); print(f'Sum: {y}')

# Generating a new number
y = sum([i for i in range(10)]); print(f'Sum: {y}')

# Silent change
for i in range(57): pass  # Loop doing nothing

# Auto-update tweak
x = random.randint(1, 8828); print(f'Random X: {x}')

# Auto-update tweak
x = random.randint(1, 322); print(f'Random X: {x}')

# Auto-update tweak
x = random.randint(1, 708); print(f'Random X: {x}')

# Auto-update tweak
x = random.randint(1, 5172); print(f'Random X: {x}')

# Silent change
for i in range(64): pass  # Loop doing nothing

# Silent change
for i in range(45): pass  # Loop doing nothing

# Auto-update tweak
x = random.randint(1, 1419); print(f'Random X: {x}')

# Auto-update tweak
x = random.randint(1, 6526); print(f'Random X: {x}')

# Silent change
for i in range(89): pass  # Loop doing nothing

# Silent change
for i in range(13): pass  # Loop doing nothing

# Silent change
for i in range(22): pass  # Loop doing nothing

# Auto-update tweak
x = random.randint(1, 3687); print(f'Random X: {x}')

# Auto-update tweak
x = random.randint(1, 814); print(f'Random X: {x}')

# Generating a new number
y = sum([i for i in range(6)]); print(f'Sum: {y}')

# Silent change
for i in range(41): pass  # Loop doing nothing

# Auto-update tweak
x = random.randint(1, 2236); print(f'Random X: {x}')

# Auto-update tweak
x = random.randint(1, 6227); print(f'Random X: {x}')

# Auto-update tweak
x = random.randint(1, 765); print(f'Random X: {x}')

# Silent change
for i in range(36): pass  # Loop doing nothing
