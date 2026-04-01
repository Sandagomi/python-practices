import os
import subprocess
from datetime import datetime, timedelta
import random

REPO_PATH = "github-fill"
FILE_NAME = "data.txt"

# Create repo if not exists
if not os.path.exists(REPO_PATH):
    os.makedirs(REPO_PATH)
    os.chdir(REPO_PATH)
    subprocess.run(["git", "init"])
else:
    os.chdir(REPO_PATH)

# Start date (e.g., last 90 days)
start_date = datetime.now() - timedelta(days=90)

for i in range(90):
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

# Add remote and push
subprocess.run(["git", "remote", "add", "origin", "https://github.com/Sandagomi/python-practices.git"])
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "push", "-u", "origin", "main"])