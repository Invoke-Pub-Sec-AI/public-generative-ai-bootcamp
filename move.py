import os
import shutil
from pathlib import Path

def copy_all_notebooks():
    # Repo root = where the script lives
    repo_root = Path(__file__).parent.resolve()
    target_dir = repo_root / "notebooks"
    target_dir.mkdir(exist_ok=True)

    # Walk through all subdirectories under repo root
    for root, _, files in os.walk(repo_root):
        # Skip the notebooks folder itself to avoid re-copying
        if root.startswith(str(target_dir)):
            continue

        for file in files:
            if file.endswith(".ipynb"):
                source = Path(root) / file
                destination = target_dir / file

                # Handle duplicate filenames
                counter = 1
                while destination.exists():
                    destination = target_dir / f"{source.stem}_{counter}{source.suffix}"
                    counter += 1

                shutil.copy2(source, destination)
                print(f"✅ Copied {source} -> {destination}")

if __name__ == "__main__":
    copy_all_notebooks()
