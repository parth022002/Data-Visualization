import os
import subprocess
import sys

repo_dir = r"C:\Users\parth\OneDrive\Desktop\Data Visualization\Tableau-Data-Analytics-Portfolio"
os.chdir(repo_dir)

def execute(cmd_list):
    print("Executing:", " ".join(cmd_list))
    res = subprocess.run(cmd_list, capture_output=True, text=True)
    if res.stdout:
        print("STDOUT:\n", res.stdout)
    if res.stderr:
        print("STDERR:\n", res.stderr)
    return res.returncode

execute(["git", "add", "."])
execute(["git", "commit", "-m", "Initial release: Tableau data visualization and analytics portfolio"])
execute(["git", "branch", "-M", "main"])
execute(["git", "remote", "remove", "origin"])
execute(["git", "remote", "add", "origin", "https://github.com/parth022002/Data-Visualization.git"])
rc = execute(["git", "push", "-u", "origin", "main"])
sys.exit(rc)
