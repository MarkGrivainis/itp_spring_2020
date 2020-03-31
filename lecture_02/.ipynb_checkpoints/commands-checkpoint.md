#### Commands we have used and some new commands

In terminal / PowerShell depending on OS

### Shell Commands:
|command                |description|
|-                      |-                                       |
|**pwd**                |List the path of the current directory|
|**cd \<path\>**        |Change directory using the provided path|
|**mkdir \<dir_name\>** |Make a new directory called \<dir_name\> in the current directory|
|**ls**                 |List the contents of the directory|
|**ll or ls -l**        |List the contents with more detailed information (MAC)|


### Conda Commands:

```sh
conda create -n <env name> python=<python version> <packages>
```
+ This command will create a new conda environment called \<env name\> using \<python version\> and then installing the listed \<packages\>
  + eg: **conda create -n test_env python=3.7 jupyterlab seaborn pandas numpy**

```sh
conda env list
```
+ This command will list all of the conda environments which are installed

```sh
conda activate <env name>
```
+ activate the conda environment called \<env name\>

```sh
conda remove -n <env name> --all
```
+ remove the environment called \<env name\> and all of the packages installed into the environment

```sh
conda install <packages>
```
+ install the \<packages\> into the currently active environment
  + eg: **conda install jupyterlab seaborn pandas numpy**


### Using Python:
|command                     |description|
|-|-|
|python                      |This will start an interactive python session in the terminal / powershell window|
|python \<python script\>.py |This will execute the script and print the output to the console|
|jupyter lab                 |This will open Jupyter Lab using the current directory as the root|

### git commands:
|command                     |description|
|-|-|
|git clone \<url\>             |Clone the git repository from url to your local system. (into the current folder)|
|git init                    |Initialize a git repository in the current directory (this will create a hidden folder called '.git' in the directory)|
|git add .                   |Add all files that have changed to the staging area. (basically this lets git know you would like to save these files later)|
|git commit -m '\<message\>'   |Take all of the files that have been staged (using git add) and save the changes. '-m' flags that you are adding a commit message within quotation marks. These messages should describe the changes. If you leave this out it will open the default system text editor and ask you to enter one.|
|git pull                    |Pull the changes from a remote repository (GitHub) to your local system|
|git push                    |Push the commited changes from your local system to the remote system (GitHub).|
|git stash                   |Make a temporary save (commit) of the changes made to your files and then revert them back to the previous save (commit). Use this when you have made changes to your files but need to pull new changes from the remote repository|
|git stash pop               |Take the last changes that were stashed and redo them.|
|git branch \<branch name\>    |Create a new branch called \<branch name\>. Branches allow you to have different versions of the same files saved. This is useful when you are working on different features, each feature would have a branch and the fact that the feature is not working does not break your code.|
|git checkout \<branch name\>  |Change the branch which is currently being worked on. This requires all new changes to be commited to the previous branch prior to running the checkout command.|
|git status                  |List the current status of the git repository. This will tell you what files are un/staged, if you are behind or ahead of the remote repository, etc...|