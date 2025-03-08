import os
import sys
import subprocess
import random
from datetime import datetime

# Written with ChatGPT

# Configuration
MAX_FILE_SIZE = 5 * 1024  # 5 KB limit
SCRIPT_PATH = os.path.abspath(__file__)

# Check file size before modifying
if os.path.getsize(SCRIPT_PATH) > MAX_FILE_SIZE:
    print("File too large! Aborting modification.")
    sys.exit(1)

# Read current script content
with open(SCRIPT_PATH, "r") as f:
    lines = f.readlines()

# Generate a random harmless modification
upper_bound = random.randint(100,9999);
loop_bound = str(random.randint(3,99));
modifications = [
    "\n# Auto-update tweak\nx = random.randint(1, upper_bound); print(f'Random X: {x}')\n",
    "\n# Self-learning script\nimport time; print(f'Time now: {time.time()}')\n",
    "\n# Silent change\nfor i in range(" + loop_bound + "): pass  # Loop doing nothing\n",
    "\n# Generating a new number\ny = sum([i for i in range(5)]); print(f'Sum: {y}')\n"
]

new_code = random.choice(modifications)

# Prevent duplicate appends
if new_code.strip() not in "".join(lines):
    lines.append(new_code)
else:
    print("No new change needed. Avoiding redundant modification.")
    print(new_code)
    sys.exit(0)

# Write back modified script
with open(SCRIPT_PATH, "w") as f:
    f.writelines(lines)

# Git commands
subprocess.run(["git", "add", SCRIPT_PATH], check=True)
commit_message = f"Automated self-update with randomness on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "commit", "-m", commit_message], check=True)
subprocess.run(["git", "push"], check=True)  # Ensure authentication is set up



# Generating a new number
y = sum([i for i in range(5)]); print(f'Sum: {y}')

# Self-learning script
import time; print(f'Time now: {time.time()}')

# Silent change
for i in range(78): pass  # Loop doing nothing

# Silent change
for i in range(69): pass  # Loop doing nothing
