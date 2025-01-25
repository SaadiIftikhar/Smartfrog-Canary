import os
import tarfile
import time


def ensure_tmp_folder():
    """Ensures the 'tmp' folder exists in the current directory."""
    if not os.path.exists("tmp"):
        os.mkdir("tmp")


def count_files_in_tmp():
    """Counts the number of files in the 'tmp' folder."""
    return len([f for f in os.listdir("tmp") if os.path.isfile(os.path.join("tmp", f))])


def archive_files():
    """Archives all files in the 'tmp' folder into a tar.gz file and empties the folder."""
    with tarfile.open("files.tar.gz", "w:gz") as archive:
        for file in os.listdir("tmp"):
            file_path = os.path.join("tmp", file)
            archive.add(file_path, arcname=file)
            os.remove(file_path)
    print("files collected")


if __name__ == "__main__":
    ensure_tmp_folder()
    print("Monitoring 'tmp' folder...")

    try:
        while True:
            file_count = count_files_in_tmp()
            if file_count >= 10:
                archive_files()
                break
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
