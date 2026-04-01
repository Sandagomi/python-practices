import os
import subprocess
from datetime import datetime, timedelta
import random

# Work in the main repository (parent directory)
REPO_PATH = "."
FILE_NAME = "contribution_data.txt"

# Start date - May 25 to November 25 (184 days)
start_date = datetime(2025, 5, 25)
end_date = datetime(2025, 11, 25)
days_diff = (end_date - start_date).days

for i in range(days_diff + 1):
    current_date = start_date + timedelta(days=i)

    # Random number of commits per day
    commits_per_day = random.randint(1, 5)

    for _ in range(commits_per_day):
        with open(FILE_NAME, "a") as f:
            f.write(f"Commit on {current_date}\n")

        subprocess.run(["git", "add", FILE_NAME])

        date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        subprocess.run(["git", "commit", "-m", f"Commit for {date_str}"], env=env)


print("Commits created successfully! Now pushing to GitHub...")
subprocess.run(["git", "push"])