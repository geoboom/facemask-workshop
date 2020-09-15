# Welcome to NUS Statistics Society Facemask Detector Workshop!

The purpose of this repository is to **help you get started with the basic tools :hammer: and code :computer:** needed to follow along in the workshop. It will also serve as the single source of truth, hosting the latest version of our facemask :mask: detector workshop material :books:.

We hope that you will find great joy and meaning in our workshop! :joy: Consider giving this repository a star :star: if you found it helpful!

# Table of contents:

- [Pre-workshop installation guide](#pre-workshop-installation-guide)
  - [Windows](windows.md)
  - [Mac](mac.md)
  - [Linux](linux.md)
- [Project setup](#project-setup)
  - [Cloning this repo](#cloning-this-repo)
  - [Launching jupyter notebook](#launching-jupyter-notebook)
  - [Running the website](#running-the-frontend-website)
  - [Running the FastAPI server](#running-the-backend-fastapi-server)
- [Credits](#credits)

# Pre-workshop installation guide

This guide covers the installation of:

- Anaconda - a distribution of python which comes with a lot of data science packages :package:.
- `jupyter notebook` - a live python execution environment typically used for exploratory :mag: data analysis.
- `nodejs` and `npm` - nodejs is a js (javascript) runtime built on chrome's V8 engine :car: and npm is a package manager for nodejs.

You may find the detailed installation instructions for your favorite operating system (Linux/Mac/Windows) below. We know it looks pretty lengthy but it won't take more than 20 minutes! :pray::pray::pray:

If you use a **Windows** machine, click [here](#windows-installation-guide).

If you use a **Mac**, click [here](#mac-installation-guide).

If you use **Linux**, click [here](#linux-installation-guide).

Please only follow **ONE** of the installation guides e.g. if you're using Mac please don't follow the Linux guide by accident. We can't help you with troubleshooting issues otherwise.

## Mac installation guide

### 0.1 Pre-req: installing Homebrew

Please follow the steps [here](https://treehouse.github.io/installation-guides/mac/homebrew) to install Homebrew for Mac. It's a package manager and installer for Mac.

### 0.2 Pre-req: installing `wget`

Type `brew install wget` to install `wget`. `wget` is a tool that helps you download files from the internet to your machine.

### 0.3 Pre-req: installing `python3`

Ensure you have a working installation of `python3` (in terminal, type `python3` and hit enter to check). If you do not have a working installation of `python3`, we advice you to search [mac python3 install](https://www.google.com/search?q=mac+python3+install) on Google and follow the instructions there :thumbsup:.

### 1. Installing Anaconda

You can install Anaconda EITHER via the GRAPHICAL installer (clicky with mouse) OR the TERMINAL (type with keyboard). We've got you covered for both.

1. (GRAPHICAL install) follow the steps listed on the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/mac-os/) under **Installing on macOS > macOS graphical install**.
   - After you're done with **step 10**, open up terminal and type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal. You may close the terminal afterwards.
   - Please **go to bullet point 3** below and **ignore** bullet point 2.
2. (TERMINAL install) follow the steps listed on the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/mac-os/) under **Installing on macOS > Using the command-line install**.
   - At **step 7**, select "yes" when prompted "Do you wish the installer to initialize Anaconda3 by running conda init?". We'll need this for **step 11**.
   - At **step 11**, type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal. You may close the terminal now.
3. Wow, must've been a lot of steps and a lot of work :sweat:... BUT we're not yet done - we need to verify that your installation is working. Please open a new terminal and run `conda activate base`. You should see a `(base)` pop up beside your name in terminal if your installation was successful.
4. **Congratulations**, you've installed Anaconda! :tada::tada::tada:

**Why is there a `(base)` beside my name?**

`(base)` beside your name means you've activated the Anaconda's `base` environment, where you have access to many data science packages (`pip list` to view).

**Where are the `jupyter notebook` installation instructions?**

By default, Anaconda's base environment ships with `jupyter notebook`. Run `jupyter notebook` in terminal to run the jupyter notebook server. Your local jupyter notebook website should automatically pop up in your favorite browser. To stop the server, press CTRL+C in terminal to terminate the running program.

### 2. Installing `nodejs` and `npm`

Yay, you're done with the hardest :muscle: part of installing Anaconda :snake:. This part will be suuper easy in comparison! :smile: All you have to do is open up terminal and run this command by copying the whole command into your terminal and pressing enter ([source](https://nodejs.org/en/download/package-manager/#macos)):

```
curl "https://nodejs.org/dist/latest/node-${VERSION:-$(wget -qO- https://nodejs.org/dist/latest/ | sed -nE 's|.*>node-(.*)\.pkg</a>.*|\1|p')}.pkg" > "$HOME/Downloads/node-latest.pkg" && sudo installer -store -pkg "$HOME/Downloads/node-latest.pkg" -target"/"
```

Now if you run `npm --verson` and `node --version` in terminal, your versions of `npm` and `nodejs` will be printed. This indicates a successful installation. See, I said it would be easy didn't I? :wink:

**What do I do now?**

Now that you have all the tools you need installed, have a look at our [project setup guide](#project-setup) next!

## Linux installation guide

### 0.1. Pre-req: installing `wget`

Type `sudo apt install wget` to install `wget`. `wget` is a tool that helps you download files from the internet to your machine.

### 0.2. Pre-req: installing `python3`

Ensure you have a working installation of `python3` (in terminal, type `python3` and hit enter to check). Most linux distributions come with `python3` already installed. If you do not have a working installation of `python3`, we advice you to search [linux python3 install](https://www.google.com/search?q=linux+python3+install) on Google and follow the instructions there :thumbsup:.

### 1. Installing Anaconda

1. Download the [conda installer](https://repo.Anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh). Verify that the downloaded conda installer is in your Downloads folder i.e. there is a file called `~/Downloads/Anaconda3-2020.07-Linux-x86_64.sh`.
2. Next, follow the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/linux/), starting from **Installing on Linux > Installation > step 3** (the step which begins with "Enter the following to install Anaconda for Python 3.7") all the way to **step 11**. Please take note of following points during installation:
   - At **step 3**, when typing `bash ~/Downloads/Anaconda3` you can press the TAB key to autocomplete the filepath for you. You might need this as the version of their Anaconda3 installer on their installation instructions might not be the same as the one you've downloaded.
   - At **step 7**, choose "yes" when prompted "Do you wish the installer to initialize Anaconda3 by running conda init?". We'll need this for **step 11**.
   - At **step 11**, type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal.
3. Wow, must've been a lot of steps and a lot of work :sweat:... BUT we're not yet done - we need to verify that your installation is working. Please restart (close and re-open) your terminal and run `conda activate base`. You should see a `(base)` pop up beside your name in terminal if your installation was successful.
4. **Congratulations**, you've installed Anaconda! :tada::tada::tada:

**Why is there a `(base)` beside my name?**

`(base)` beside your name means you've activated the Anaconda's `base` environment, where you have access to many data science packages (`pip list` to view).

**Where are the `jupyter notebook` installation instructions?**

By default, Anaconda's base environment ships :ship: with `jupyter notebook`. Run `jupyter notebook` in terminal to run the jupyter notebook server. Your local jupyter notebook website should automatically pop up in your favorite browser. To stop the server, press CTRL+C in terminal to terminate the running program.

### 2. Installing `nodejs` and `npm`

Yay, you're done with the hardest :muscle: part of installing Anaconda :snake:. This part will be suuper easy in comparison! :smile: All you have to do is open up terminal and run these commands by copying them one line at a time into your terminal and hitting enter ([source](https://github.com/nodesource/distributions/blob/master/README.md#debinstall)):

```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Now if you run `npm --verson` and `node --version` in terminal, your versions of `npm` and `nodejs` will be printed. This indicates a successful installation. See, I said it would be easy didn't I? :wink:

**What do I do now?**

Now that you have all the tools you need installed, have a look at our [project setup guide](#project-setup) next!

# Project setup

Follow the instructions below to get familiarized with the project repository. You may make reference to this section during the workshop itself to perform certain tasks :book:.

Note that the **backend code is incomplete** - you'll be filling in the blanks during the workshop!

## Cloning this repo

1. Open up terminal (wsl terminal for Windows) and type `sudo apt update && sudo apt upgrade`. This ensures you have the **latest system packages**.
2. Run `git clone --depth 1 https://github.com/geoboom/facemask-workshop.git` to **clone this repo**.
3. Run `ls` and you should see a folder called `facemask-workshop`.

## Launching `jupyter notebook`

1. In terminal, type `cd facemask-workshop` to navigate to the project's root folder.
1. In the root folder, navigate to the **notebook subdirectory** by typing `cd notebook`.
1. Type `conda activate base` to **activate Anaconda's base environment**. You should see `(base)` beside your name in terminal.
1. Now run `jupyter notebook` and this notebook folder should open in Jupyter Notebook on your browser.

## Running the frontend (website)

1. Open up a new terminal and type `cd facemask-workshop` to navigate to the project's root folder.
1. In the root folder, navigate to the **frontend subdirectory** by typing `cd frontend`.
1. Type `npm install` to **install the frontend project dependencies**. This might take a while so grab a coffee :coffee:.
1. Once the dependencies have finished installing, type `npm run dev` to **run the website's server** (`nextjs`).
1. Visit `localhost:3000` in your browser to **see the website live!**

## Running the backend (FastAPI server)

1. Open up a new terminal and type `cd facemask-workshop` to navigate to the project's root folder.
1. In the root folder, navigate to the **backend subdirectory** by typing `cd backend`.
1. Type `python3 -m venv venv` to create a `python3` virtual environment in the backend directory.
1. Type `source venv/bin/activate` to **activate this virtual environment**. You should see `(venv)` beside your name, indicating that the `venv` environment is activated.
1. Run `pip install -r requirements.txt` to **install the dependencies** to this virtual environment. This might take a while so grab a coffee :coffee:.
1. Once dependencies have finished installing, type `./run.sh` to **run the FastAPI** server and hit enter.

# Credits

This section is under construction.

| Name    | Role                                        | Github                      |
| ------- | ------------------------------------------- | --------------------------- |
| Jet     | NUS Statistics Society Workshop Director    | https://github.com/jetnew   |
| Rama    | Presenter, guide writing, and material prep | https://github.com/ramav111 |
| Georgie | Presenter, guide writing, and material prep | https://github.com/geoboom  |

[Dataset](https://github.com/prajnasb/observations/tree/master/experiements/dest_folder) for masked/no-masked.
