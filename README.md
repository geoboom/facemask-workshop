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

You may find the detailed installation instructions for your operating system (Linux/Mac/Windows) via the links below. We know the instructions might look pretty lengthy but it won't take more than 20 minutes! :pray::pray::pray:

If you use a **Windows** machine, click [here](windows.md).

If you use a **Mac**, click [here](mac.md).

If you use **Linux**, click [here](linux.md).

Please only follow **ONE** of the installation guides e.g. if you're using Mac please don't follow the Linux guide by accident. We can't help you with troubleshooting issues otherwise.

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
