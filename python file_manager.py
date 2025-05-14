import os
import shutil
from pathlib import Path
import argparse

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".apk"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def organize_files(directory, dry_run=False):
    for file in os.listdir(directory):
        file_path = directory / file
        if file_path.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_path.suffix.lower() in extensions:
                    target_folder = directory / category
                    if dry_run:
                        print(f"[DRY RUN] Would move: {file} -> {target_folder}")
                    else:
                        target_folder.mkdir(exist_ok=True)
                        shutil.move(str(file_path), str(target_folder / file))
                    moved = True
                    break
            if not moved:
                other_folder = directory / "Others"
                if dry_run:
                    print(f"[DRY RUN] Would move: {file} -> {other_folder}")
                else:
                    other_folder.mkdir(exist_ok=True)
                    shutil.move(str(file_path), str(other_folder / file))

def main():
    parser = argparse.ArgumentParser(description="Organize files by type.")
    parser.add_argument(
        "-d", "--directory",
        type=str,
        default=str(Path.home() / "Downloads"),
        help="Directory to organize (default: Downloads folder)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the organization without moving files"
    )
    args = parser.parse_args()
    target_dir = Path(args.directory)

    if not target_dir.exists():
        print(f"Directory does not exist: {target_dir}")
        return

    organize_files(target_dir, dry_run=args.dry_run)
    if not args.dry_run:
        print(f"Organized files in: {target_dir}")
    else:
        print("Dry run complete. No files were moved.")

if __name__ == "__main__":
    main()