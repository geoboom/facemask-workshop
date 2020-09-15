# Welcome to NUS Statistics Society Facemask Detector Workshop!
The purpose of this repository is to **help you get started with the basic tools and code** needed to follow along in the workshop. It will also serve as the single source of truth, hosting the latest version of our facemask detector workshop material. We hope that you will find great joy and meaning in our workshop!

# Table of contents:
- [Pre-workshop installation guide](#pre-workshop-installation-guide)
    - [Linux](#linux-installation-guide)
    - [Windows](#windows-installation-guide)
    - [Mac](#mac-installation-guide)
- [Projects setup guide](#projects-setup-guide)

## Pre-workshop installation guide
This guide covers the installation of:
* Anaconda/`conda` - a distribution of python which comes with a lot of data science packages.
* `jupyter notebook` - a live python execution environment typically used for exploratory data analysis.
* `nodejs` and `npm` - nodejs is a js (javascript) runtime built on chrome's V8 engine and npm is a package manager for nodejs.

You may find the detailed installation instructions for your respective operating system (Mac/Windows/Linux) below.

### Linux installation guide
#### Prerequisite Step: `python3` installation
Ensure you have a working installation of `python3` (in terminal, type `python3` and hit enter to check). If you do not have a working installation of `python3`, we advice you to search [linux python3 install](https://www.google.com/search?q=linux+python3+install) on Google and follow the instructions there. 
#### Installing Anaconda
1. Download the [conda installer](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh). Verify that the downloaded conda installer is in your Downloads folder i.e. there is a file called `~/Downloads/Anaconda3-2020.07-Linux-x86_64.sh`. 
2. Next, follow the official anaconda installation guide [here](https://docs.anaconda.com/anaconda/install/linux/#), starting from **step 3** (the step which begins with "Enter the following to install Anaconda for Python 3.7") all the way to **step 11**. Please take note of following points during installation:
    * At **step 7**, select "yes" when prompted "Do you wish the installer to initialize Anaconda3 by running conda init?". We'll need this for **step 11**.
    * At **step 11**, type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal.
3. Wow, must've been a lot of steps and a lot of work! But we're not yet done - we need to verify that your installation is working. Please restart (close and re-open) your terminal and run `conda activate base`. You should see a `(base)` pop up beside your name in terminal if your installation was successful.

Congratulations, you're done with installing Anaconda!

`(base)` beside your name means you've activated the Anaconda's `base` environment, where you have access to many data science packages (`pip list` to view)!

#### Installing `jupyter notebook`


### Windows installation guide
### Mac installation guide

## Projects setup guide
