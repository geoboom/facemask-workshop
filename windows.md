# Windows installation guide

When you see the word **terminal**, we mean the **wsl terminal** that can be launched by typing Ubuntu in the Windows start menu and selecting the Ubuntu app. You'll have this app by the end of step **0.1. Pre-req**.

## 0.1. Pre-req: installing Windows Subsystem for Linux (wsl)

We will be covering the install of wsl1 in this section. We won't cover nor support wsl2 in this workshop because of the issues associated with connecting to a local server hosted on wsl2. You don't have to worry about the wsl2 issues if you:

- don't currently have wsl installed; or
- have wsl1 installed (in which case you can skip the 0.1. Pre-req);
- have wsl2 installed and know what you're doing :wink: (in which case you can skip the 0.1. Pre-req).

Fret not if you don't know what we're talking about - just follow the instructions below.

1. To enable wsl, open PowerShell :rocket: as Administrator and run (copy the entire command and press CTRL+V in PowerShell):
   ```
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   ```
   Here's how to open PowerShell as Administrator:
   1. Press the WINDOWS key on your keyboard OR click the Windows start icon at the bottom left of your screen. This will open up the start menu.
   2. Now, type "powershell", right click the PowerShell program, and choose "Run as Administrator". Accept the confirmation prompt. This will open up PowerShell (looks like a blue terminal).
2. After enabling wsl1, please restart :curly_loop: your computer. This step is mandatory.
3. When your computer has restarted, you need to install the Ubuntu :penguin: distribution from the Microsoft Store :shopping_cart: (it's free). You may find it [here](https://www.microsoft.com/store/apps/9N9TNGVNDL3Q).
4. Once your Ubuntu has finished installing, follow the **Create a user account and password for your new Linux distribution** and **Update and upgrade packages** steps [here](https://docs.microsoft.com/en-us/windows/wsl/user-support). You may launch the Ubuntu terminal by pressing the WINDOWS key on your keyboard to bring up the start menu, typing "ubuntu", and selecting the Ubuntu app.
5. **Congratulations!** :tada::tada::tada: You have successfully installed Ubuntu 18.04 wsl terminal.

## 0.2. Pre-req: enabling copy-paste in wsl terminal

1. Open wsl terminal by typing "ubuntu" in start menu and selecting the Ubuntu app.
2. Right-click an empty part of the title bar and select "Properties".
3. Select the "Use Ctrl + Shift + C / V as Copy/Paste" option, and then click the "OK" button.

You can now press CTRL+SHIFT+V in wsl terminal to paste what you've copied into your clipboard. This will come in handy :hand: later when needing to paste in commands.

## 0.3. Pre-req: installing `wget`

Type `sudo apt install wget` to install `wget`. `wget` is a tool that helps you download files from the internet to your machine.

## 0.4. Pre-req: installing `python3`

1. Type `sudo apt install python3 python3-pip ipython3` in terminal. If prompted for password, type in the password you created your user account with in **0.1. Pre-req bullet point 4** and hit enter.
2. Verify that `python3` has been successfully installed by typing `python3 --version` in terminal. You should see your `python3` version information printed. This means all is well. :smiley:

## 1. Installing Anaconda

1. Open wsl terminal by typing "ubuntu" in start menu and selecting the Ubuntu app.
2. When terminal opens, you should be in your `home` :house: directory. Verify this by typing `pwd`. You should see `/home/<user>` printed. If you see something apart from `/home/<user>`, it means you're not in the `home` directory. Type `cd ~` and hit enter to go to the home directory.
3. Make a downloads folder by running `mkdir ~/Downloads`.
4. Go into the downloads folder by running `cd ~/Downloads`.
5. Download the conda installer by running `wget https://repo.Anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh`.
6. Next, follow the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/linux/), starting from **Installing on Linux > Installation > step 3** (the step which begins with "Enter the following to install Anaconda for Python 3.7") all the way to **step 11**. Please take note of following points during installation:
   - At **step 3**, when typing `bash ~/Downloads/Anaconda3` you can press the TAB key to autocomplete the filepath for you. You might need this as the version of their Anaconda3 installer on their installation instructions might not be the same as the one you've downloaded.
   - At **step 7**, choose "yes" when prompted "Do you wish the installer to initialize Anaconda3 by running conda init?". We'll need this for **step 11**.
   - At **step 11**, type `conda config --set auto_activate_base False` to prevent the conda base environment from being automatically activated each time you launch terminal.
7. Wow, must've been a lot of steps and a lot of work :sweat:... BUT we're not yet done - we need to verify that your installation is working. Please restart (close and re-open) your terminal and run `conda activate base`. You should see a `(base)` pop up beside your name in terminal if your installation was successful.
8. **Congratulations**, you've installed Anaconda! :tada::tada::tada:

**Why is there a `(base)` beside my name?**

`(base)` beside your name means you've activated the Anaconda's `base` environment, where you have access to many data science packages (`pip list` to view).

**Where are the `jupyter notebook` installation instructions?**

By default, Anaconda's base environment ships :ship: with `jupyter notebook`. Run `jupyter notebook` in terminal to run the jupyter notebook server. Your local jupyter notebook website should automatically pop up in your favorite browser. To stop the server, press CTRL+C in terminal to terminate the running program.

## 2. Installing `nodejs` and `npm`

Yay, you're done with the hardest :muscle: part of installing Anaconda :snake:. This part will be suuper easy in comparison! :smile: All you have to do is open up terminal and run these commands by copying them one line at a time into your terminal and hitting enter ([source](https://github.com/nodesource/distributions/blob/master/README.md#debinstall)):

```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Now if you run `npm --verson` and `node --version` in terminal, your versions of `npm` and `nodejs` will be printed. This indicates a successful installation. See, I said it would be easy didn't I? :wink:

**What do I do now?**

Now that you have all the tools you need installed, have a look at our [project setup guide](README.md#project-setup) next!
