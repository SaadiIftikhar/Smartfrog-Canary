# Mercari Playwright Tests

This repository contains Playwright tests for the Expo https://expo.dev/ React-Native website.

## System requirements / Prerequisites

* Git
* Node.js 18+
* Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL).
* macOS 13 Ventura, or later.
* Debian 12, Ubuntu 22.04, Ubuntu 24.04, on x86-64 and arm64 architecture.


## Installation

### Git

1. Download and install Git from the official website: https://git-scm.com/downloads.
2. Verify the installation by running `git --version` in your terminal. This should print the installed Git version.
3. You can also download files directly from github repository https://github.com/SaadiIftikhar/Mercari.git.

### Node.js and npm

1. Download and install Node.js `Node.js 18+` from the official website: https://nodejs.org/
2. npm (Node Package Manager) will be bundled with your Node.js installation. Verify the installation by running `npm -v` in your terminal. This should print the installed npm version.

## Setting Up Playwright

1. Clone this repository using Git:

```bash
git clone https://github.com/SaadiIftikhar/Mercari.git
```

2. Navigate to the Project Directory:

```bash
cd Mercari
```

3. Install Playwright

```bash
npm init playwright@latest
```
It will ask the following
  * Do you want to use TypeScript or JavaScript? (Select JavaScript)
  * Where to put your end-to-end tests? (Enter value = tests)
  * Add a GitHub Actions workflow? (Select False)
  * Install Playwright browsers (can be done manually via 'npx playwright install')? (Select True)
  * Then it will ask you that some files already exists. Do you want to override it? (Select false for all)
  * Delete 'example.spec.js' file from tests folder (Optional) 
  * You are all set :)


## Running Tests
Once you are in the Mercari directory, you will be able to run these tests

1. Running tests in headless format

```bash
npx playwright test --reporter=line
```

2. Running tests through UI

```bash
npx playwright test --ui
```

3. Report can be generated using

```bash
npx playwright test --reporter=html
```

4. Report can be viewed using 
```bash
npx playwright show-report
```

The report can also be found in the playwright-report folder, the report file name will be index.html

## Videos Of Test Runs Through UI



## Generated Report Example

  ![Image](https://github.com/user-attachments/assets/9944e587-b83d-414e-a24e-24631b92f5d4)



