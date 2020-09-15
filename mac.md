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
