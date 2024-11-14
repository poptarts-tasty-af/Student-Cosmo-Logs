import subprocess
import os

# Path to your repo
repo_path = r"C:\Users\tacot\OneDrive\Desktop\CosmoStuff"
# Path to your folder to track
folder_to_track = "Student_logs"

# Change to the repo directory
os.chdir(repo_path)

# Function to run git commands and capture output
def run_git_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result

# Check if the folder exists
if os.path.isdir(folder_to_track):
    print(f"'{folder_to_track}' folder found.")

    # Add all untracked files (including the folder) to the staging area
    add_result = run_git_command(['git', 'add', '.'])  # Add all files, not just the folder
    if add_result.returncode != 0:
        print(f"Error adding files: {add_result.stderr}")
    else:
        print("Successfully added all untracked files to staging.")

    # Check the status of the repository to ensure there are changes to commit
    status_result = run_git_command(['git', 'status', '--porcelain'])
    print(f"Git status output: {status_result.stdout}")

    if status_result.stdout.strip() == "":
        print("No changes to commit.")
    else:
        # Commit changes if there are staged files
        commit_result = run_git_command(['git', 'commit', '-m', f"Add {folder_to_track} folder and other changes"])
        if commit_result.returncode != 0:
            print(f"Error committing changes: {commit_result.stderr}")
        else:
            print(f"Successfully committed changes.")

        # Push changes to the correct remote repository
        push_result = run_git_command(['git', 'push'])
        if push_result.returncode != 0:
            print(f"Error pushing to remote: {push_result.stderr}")
        else:
            print("Successfully pushed changes to the remote repository.")
else:
    print(f"Error: '{folder_to_track}' folder does not exist.")
