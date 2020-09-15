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

Now that you have all the tools you need installed, have a look at our [project setup guide](README.md#project-setup) next!
