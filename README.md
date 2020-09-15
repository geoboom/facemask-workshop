# Welcome to NUS Statistics Society Facemask Detector Workshop!

The purpose of this repository is to **help you get started with the basic tools :hammer: and code :computer:** needed to follow along in the workshop. It will also serve as the single source of truth, hosting the latest version of our facemask :mask: detector workshop material :books:.

We hope that you will find great joy and meaning in our workshop! :joy:

# Table of contents:

- [Pre-workshop installation guide](#pre-workshop-installation-guide)
  - [Linux](#linux-installation-guide)
  - [Mac](#mac-installation-guide)
  - [Windows](#windows-installation-guide)
- [Projects setup guide](#projects-setup-guide)

# Pre-workshop installation guide

This guide covers the installation of:

- Anaconda/`conda` - a distribution of python which comes with a lot of data science packages :package:.
- `jupyter notebook` - a live python execution environment typically used for exploratory :mag: data analysis.
- `nodejs` and `npm` - nodejs is a js (javascript) runtime built on chrome's V8 engine :car: and npm is a package manager for nodejs.

You may find the detailed installation instructions for your favorite operating system (Linux/Mac/Windows) below. We know it looks pretty lengthy but it won't take more than 20 minutes! :pray::pray::pray:

## Linux installation guide

### 0. Pre-req: installing `python3`

Ensure you have a working installation of `python3` (in terminal, type `python3` and hit enter to check). If you do not have a working installation of `python3`, we advice you to search [linux python3 install](https://www.google.com/search?q=linux+python3+install) on Google and follow the instructions there :thumbsup:.

### 1. Installing Anaconda

1. Download the [conda installer](https://repo.Anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh). Verify that the downloaded conda installer is in your Downloads folder i.e. there is a file called `~/Downloads/Anaconda3-2020.07-Linux-x86_64.sh`.
2. Next, follow the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/linux/), starting from **Installing on Linux > Installation > step 3** (the step which begins with "Enter the following to install Anaconda for Python 3.7") all the way to **step 11**. [Please](Please) take note of following points during installation:
   - At **step 7**, select "yes" when prompted "Do you wish the installer to initialize Anaconda3 by running conda init?". We'll need this for **step 11**.
   - At **step 11**, type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal.
3. Wow, must've been a lot of steps and a lot of work :sweat:... BUT we're not yet done - we need to verify that your installation is working. Please restart (close and re-open) your terminal and run `conda activate base`. You should see a `(base)` pop up beside your name in terminal if your installation was successful.

If so, then...

:tada::tada::tada: Congratulations, you've installed Anaconda! :tada::tada::tada:

**Why is there a `(base)` beside my name?**

`(base)` beside your name means you've activated the Anaconda's `base` environment, where you have access to many data science packages (`pip list` to view).

**Where are the `jupyter notebook` installation instructions?**

By default, Anaconda's base environment ships with `jupyter notebook`. Run `jupyter notebook` in terminal to run the jupyter notebook server. Your local jupyter notebook website should automatically pop up in your favorite browser. To stop the server, press CTRL+C in terminal to terminate the running program.

### 2. Installing `nodejs` and `npm`

Yay, you're done with the hardest :muscle: part of installing Anaconda :snake:. This part will be suuper easy in comparison! :smile:

All you have to do is open up terminal and run these commands by copying them one line at a time into your terminal and hitting enter ([source](https://github.com/nodesource/distributions/blob/master/README.md#debinstall)):

```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Now if you run `npm --verson` and `node --version` in terminal, your versions of `npm` and `nodejs` will be printed. This indicates a successful installation.

See, I said it would be easy didn't I? :wink:

## Mac installation guide

### 0. Pre-req: installing `python3`

Ensure you have a working installation of `python3` (in terminal, type `python3` and hit enter to check). If you do not have a working installation of `python3`, we advice you to search [mac python3 install](https://www.google.com/search?q=mac+python3+install) on Google and follow the instructions there :thumbsup:.

### 1. Installing Anaconda

You can install Anaconda EITHER via the graphical installer (clicky with mouse) OR the terminal (type with keyboard). We've got you covered for both.

1. (GRAPHICAL install) follow the steps listed on the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/mac-os/) under **Installing on macOS > macOS graphical install**.
   - After you're done with **step 10**, open up terminal and type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal. You may close the terminal afterwards.
   - Please **go to bullet point 3** below and **ignore** bullet point 2.
2. (TERMINAL install) follow the steps listed on the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/mac-os/) under **Installing on macOS > Using the command-line install**.
   - At **step 7**, select "yes" when prompted "Do you wish the installer to initialize Anaconda3 by running conda init?". We'll need this for **step 11**.
   - At **step 11**, type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal. You may close the terminal now.
3. Wow, must've been a lot of steps and a lot of work :sweat:... BUT we're not yet done - we need to verify that your installation is working. Please open a new terminal and run `conda activate base`. You should see a `(base)` pop up beside your name in terminal if your installation was successful.

If so, then...

:tada::tada::tada: Congratulations, you've installed Anaconda! :tada::tada::tada:

**Why is there a `(base)` beside my name?**

`(base)` beside your name means you've activated the Anaconda's `base` environment, where you have access to many data science packages (`pip list` to view).

**Where are the `jupyter notebook` installation instructions?**

By default, Anaconda's base environment ships with `jupyter notebook`. Run `jupyter notebook` in terminal to run the jupyter notebook server. Your local jupyter notebook website should automatically pop up in your favorite browser. To stop the server, press CTRL+C in terminal to terminate the running program.

### 2. Installing `nodejs` and `npm`

Yay, you're done with the hardest :muscle: part of installing Anaconda :snake:. This part will be suuper easy in comparison! :smile:

All you have to do is open up terminal and run this command by copying the whole command into your terminal and pressing enter ([source](https://nodejs.org/en/download/package-manager/#macos)):

```
curl "https://nodejs.org/dist/latest/node-${VERSION:-$(wget -qO- https://nodejs.org/dist/latest/ | sed -nE 's|.*>node-(.*)\.pkg</a>.*|\1|p')}.pkg" > "$HOME/Downloads/node-latest.pkg" && sudo installer -store -pkg "$HOME/Downloads/node-latest.pkg" -target"/"
```

Now if you run `npm --verson` and `node --version` in terminal, your versions of `npm` and `nodejs` will be printed. This indicates a successful installation.

See, I said it would be easy didn't I? :wink:

## Windows installation guide

# Projects setup guide
