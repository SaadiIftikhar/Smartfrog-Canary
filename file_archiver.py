import os
import tarfile
import time
from datetime import datetime

def ensure_tmp_folder():
    """Ensure that the 'tmp' folder exists."""
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

def count_files_in_tmp():
    """Count the number of files in the 'tmp' folder."""
    return [name for name in os.listdir("tmp") if os.path.isfile(os.path.join("tmp", name))]

def create_archive_name():
    """Generate a unique archive name based on the current timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"files_{timestamp}.tar.gz"

def archive_files(files_to_archive):
    """Create an archive from the specified files in the 'tmp' folder."""
    archive_name = create_archive_name()
    with tarfile.open(archive_name, "w:gz") as tar:
        for file in files_to_archive:
            tar.add(os.path.join("tmp", file), arcname=file)
    # Remove archived files after archiving
    for file in files_to_archive:
        os.remove(os.path.join("tmp", file))

if __name__ == "__main__":
    print("Welcome to the File Archiver!")
    ensure_tmp_folder()
    print("Monitoring the 'tmp' folder for files...")

    while True:
        files_in_tmp = count_files_in_tmp()
        if len(files_in_tmp) >= 10:
            print(f"Found {len(files_in_tmp)} files, archiving the first 10...")
            # Archive the first 10 files
            archive_files(files_in_tmp[:10])
            print("Files archived. Resetting folder...")
        elif len(files_in_tmp) > 0:
            print(f"Files in 'tmp': {len(files_in_tmp)}/10")
        else:
            print("No files in 'tmp'.")

        time.sleep(5)  # Check every 5 seconds
