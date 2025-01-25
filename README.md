# Smartfrog & Canary

This repository includes two Practical Part algorithms and one Theoretical Part Word document.

1: Theoretical Part: The Word(.docx) document contains the test plan.

2: Practical Part: The setup for the algorithms is provided below.

## Installation

### 1: Git

1. Download and install Git from the official website: https://git-scm.com/downloads.
2. Verify the installation by running `git --version` in your terminal. This should print the installed Git version.
3. You can also download files directly from GitHub repository https://github.com/SaadiIftikhar/Smartfrog-Canary.git.

### 2: Download and Install Python

1. Visit the official Python website (https://www.python.org/) and download the latest version
2. During installation, check the box that says "Add Python to PATH".
3. Verify installation by opening a terminal or command prompt and typing:

```bash
python --version
```

### 3: Download and Install VSCode (Optional as you can run the commands through command prompt)

1. Visit the VSCode website (https://code.visualstudio.com/) and download the latest version.
2. Install and open VSCode.

## Setting Up Project

1. Clone this repository using Git (If the zip is not downloaded directly.):

```bash
git clone https://github.com/SaadiIftikhar/Smartfrog-Canary.git
```
Note: Git will create project folder in the directory you run this command in.

2. Navigate to the Project Directory:

```bash
cd Smartfrog-Canary
```
Note: Cloning with Git sets the folder name as "Smartfrog-Canary," while downloading the zip sets it as "Smartfrog-Canary-main." Update commands accordingly. Extract the zip file before use.


3. Create a Virtual Environment

```bash
python -m venv env
```

4. Activate the Virtual Environment

```bash
env\Scripts\activate
```

## Running Algorithm Files
Once the setup is done you will be able to 

1. Run algorithm file for alphanumeric sorting using

```bash
python alphanumeric_sort.py
```
Note: It will ask you for input value to use for the alphanumeric sorting. Also you can type 'exit' to end the program.

2. Run algorithm file for file archiver using

```bash
python file_archiver.py
```
Notes: 

1: A tmp folder will be created in Smartfrog-Canary folder if not present.

2: You will need to add files to the tmp folder yourself.

3: The unique archive file will be added in the main Smartfrog-Canary folder using the current timestamp (YYYYMMDD_HHMMSS). So names will be like 'files_20250125_022815.tar.gz'



## Pictures Of Algorithm Runs

1: alphanumeric_sort.py

![Image](https://github.com/user-attachments/assets/b1a0d778-7e1b-44c9-8ccb-4e55cd92b5a4)

2: file_archiver.py

-- Constant monitoring of created tmp folder

![Image](https://github.com/user-attachments/assets/206f2d35-2e35-439e-becf-069b6e81fb23)

-- Printing of archived file names when 10 or more files are present in folder (it will only archive the first 10)

![Image](https://github.com/user-attachments/assets/31cf3bed-ec02-46a0-a460-d1aa0b743f03)

-- Making of `files.tar.gz` file

![Image](https://github.com/user-attachments/assets/64fa0ef6-ea70-48f0-8e1d-105c09141c1f)

## Overview of Design Decisions and Trade-offs

Below text outlines the design decisions and trade-offs made during the implementation of the **Alphanumeric Sorter** and **File Archiver** scripts.

---

**Text Sorter: Alphanumeric Sort**

**1. User Input for Sorting**
- **Decision:** The script prompts the user to input a string for sorting instead of hardcoding an example.
  
  - **Trade-offs:**
    - **Pros:** Provides flexibility, allowing users to input different strings for sorting each time.
    - **Cons:** Relies on user input, which may lead to human errors if the user doesn't follow the expected format.

**2. Sorting Alphanumeric Characters**
- **Decision:** The string is sorted by numbers first, followed by lowercase letters, uppercase letters, and other characters.
  
  - **Trade-offs:**
    - **Pros:** Clear and logical sorting order as per the requirements. Treats adjacent numerical characters as a single value (e.g., `11` becomes `11` rather than `1` and `1`).
    - **Cons:** The sorting logic could become complex when handling edge cases with mixed special characters.

**3. Handling Numbers as One Entity**
- **Decision:** Consecutive numerical characters are treated as a single value.
  
  - **Trade-offs:**
    - **Pros:** Ensures that numbers like `11`, `4`, and `3` are treated as individual numerical values, maintaining the integrity of multi-digit numbers.
    - **Cons:** It assumes that the user will always input well-formed numerical values, which could be problematic in cases of mixed characters and numbers.

**4. Sorting Using Built-In Python Functions**
- **Decision:** Python's built-in sorting functionality (e.g., `sorted()`) is used to sort the input string.
  
  - **Trade-offs:**
    - **Pros:** Simple, efficient, and easy to implement.
    - **Cons:** Limited to sorting only based on characters' natural order; custom sorting behavior is needed for complex cases.

---

**File Archiver: Archiving Files in `tmp` Folder**

**1. Monitoring the `tmp` Folder (Polling Approach)**
- **Decision:** The script checks the `tmp` folder every 5 seconds to see if files are present for archiving.
  
  - **Trade-offs:**
    - **Pros:** Straightforward approach with minimal complexity.
    - **Cons:** The script is not instant in detecting files, introducing a delay (5 seconds). Polling can also be inefficient for larger systems or directories.

**2. Archiving Files in Batches of 10**
- **Decision:** The script archives only the first 10 files found in the `tmp` folder and then deletes them.
  
  - **Trade-offs:**
    - **Pros:** Limits the number of files processed at once, keeping the archiving process efficient and manageable.
    - **Cons:** If more than 10 files exist, the script ignores the remaining files until the next check. It doesn't archive all files in one go.

**3. Creating Unique Archive Names**
- **Decision:** Archive filenames are based on the current timestamp to ensure uniqueness (e.g., `files_20230101_120000.tar.gz`).
  
  - **Trade-offs:**
    - **Pros:** Ensures no archive is overwritten, and each archive is uniquely identifiable.
    - **Cons:** Filenames may become long and cumbersome, especially if the script runs multiple times per day.

**4. Folder Creation Check**
- **Decision:** The script checks for the existence of the `tmp` folder and creates it if it doesn’t exist.
  
  - **Trade-offs:**
    - **Pros:** Ensures the folder is available for the script to monitor and avoids errors in case the folder is missing.
    - **Cons:** Additional checks and actions may seem unnecessary if the `tmp` folder already exists.

**5. Archiving Files in Batches of 10 (File Deletion)**
- **Decision:** After archiving the files, they are deleted from the `tmp` folder to prevent accumulation.
  
  - **Trade-offs:**
    - **Pros:** Keeps the `tmp` folder clean and prevents an overflow of files.
    - **Cons:** Risk of data loss if files are mistakenly deleted before archiving due to an error in the archiving process.

**6. Console Feedback (File Names and Status)**
- **Decision:** The script prints feedback to the console, listing the names of files being archived and their status, such as "Files collected and archived."
  
  - **Trade-offs:**
    - **Pros:** Provides clear feedback to the user, making it easy to understand the script's actions and monitor progress.
    - **Cons:** For production environments, more sophisticated logging may be required, especially for tracking errors or large-scale operations.

**7. Resetting the Folder After Archiving**
- **Decision:** After 10 files are archived and deleted, the script resets the monitoring process and starts over with a new set of files.
  
  - **Trade-offs:**
    - **Pros:** Ensures that only a fresh set of files is archived at once, and the folder doesn't become too cluttered.
    - **Cons:** Files that exceed 10 are left in the folder until the next check. This approach may cause delays in archiving if a batch isn't completed in time.

---

**Conclusion**

Both scripts are designed to be simple and easy to use, with a focus on core functionality over optimization. The design decisions prioritize user flexibility, simplicity, and clarity, while the trade-offs reflect the typical considerations for small-scale scripts. For larger systems or production environments, improvements such as optimized performance, better error handling, and more sophisticated logging could be considered.
