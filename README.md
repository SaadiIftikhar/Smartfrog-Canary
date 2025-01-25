# Smartfrog & Canary

This repository contains the two Practical Part algorithms and one Theoretical Part word file.

1: Theoretical Part word file contains the test plan.

2: For the Practical Part algorithms, setup is mentioned below.

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

### 3: Download and Install VSCode (Optional as you can run the command through commands prompt)

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

Run the following command to create a virtual environment:

```bash
python -m venv env
```

4. Activate the Virtual Environment

Run the following command to create a virtual environment:

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
