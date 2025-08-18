
- [1. Goal](#1-goal)
  - [1.1. Set Up](#11-set-up)
- [2. Python](#2-python)
  - [2.1. What is Python?](#21-what-is-python)
  - [2.2. Why uses Python?](#22-why-uses-python)
  - [2.3. Before you start](#23-before-you-start)
- [3. Container technology](#3-container-technology)
  - [3.1. What/Why?](#31-whatwhy)
  - [3.2. Installation](#32-installation)
    - [3.2.1. Windows](#321-windows)
- [4. Visual Studio Code (vscode)](#4-visual-studio-code-vscode)
- [5. Docker](#5-docker)
  - [5.1. What is Docker?](#51-what-is-docker)
  - [5.2. Base Image](#52-base-image)
  - [5.3. Customizing Image](#53-customizing-image)
  - [5.4. Build](#54-build)
  - [5.5. Create a container](#55-create-a-container)
  - [5.6. Tedious?](#56-tedious)
- [6. Docker Compose](#6-docker-compose)
- [7. Using our Python container](#7-using-our-python-container)
  - [7.1. `Remote - Containers` method](#71-remote---containers-method)
  - [7.2. `.Devcontainer`](#72-devcontainer)
- [8. Ensure the migration (Bonus)](#8-ensure-the-migration-bonus)
  - [8.1. Buy a new machine](#81-buy-a-new-machine)
  - [8.2. Python Environment](#82-python-environment)
    - [8.2.1. Put it in the .Dockerfile](#821-put-it-in-the-dockerfile)
    - [8.2.2. Use virtual environment](#822-use-virtual-environment)
  - [8.3. Your code](#83-your-code)
    - [8.3.1. GIT](#831-git)
    - [8.3.2. GitHub](#832-github)
  - [8.4. Your data](#84-your-data)
  - [8.5. Execution](#85-execution)
  - [8.6. GitHub Desktop](#86-github-desktop)
  - [8.7. Gitignore](#87-gitignore)
  - [8.8. Publishing the repository](#88-publishing-the-repository)
  - [8.9. Syncing and Collaborating](#89-syncing-and-collaborating)
  - [8.10. What else?](#810-what-else)

# 1. Goal
The goal here is to has a Python environment that is providion from Docker container.


## 1.1. Set Up
1. Any relatively modern laptop/PC with at least 8 GB
   - Windows 10/11: Intel/AMD-based is preferred
   - macOS: Apple Silicon-based CPU is preferred
   - Ubuntu/Other linux: Good luck. You are on your own.
2. Internet
3. VSCode that installs according to your OS. [link](https://code.visualstudio.com/)


# 2. Python

## 2.1. What is Python? 
[quote](https://www.w3schools.com/python/python_intro.asp)

> Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
> 
> It is used for:
> 
> - web development (server-side),
> - software development,
> - mathematics,
> - system scripting.

## 2.2. Why uses Python?
[quote](https://www.w3schools.com/python/python_intro.asp)
> - Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
> - Python has a simple syntax similar to the English language.
> - Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
> - Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
> - Python can be treated in a procedural way, an object-orientated way or a - functional way.

## 2.3. Before you start
1. There are two major versions of Python, which are `Python2` and `Python3`. You must be aware of which major/minor version you are using.
2. There are some differences in syntax between the two versions. We recommend that you use version 3 throughout the course.

# 3. Container technology

## 3.1. What/Why?

There are many reasons why we should use containerization technology.
At the core of `container`, it is a virtualization. 
To the user, it looks like there is another computer running inside their computer. 
That `computer` running inside is virtualized, which is just software; thus, we can simply build/rebuild/discard this virtualized computer at any time we want.

What does this mean to you?

Reproducible is probably the correct word to use. 
When you use your computer for development, you will install this/that/those over time. 
If your computer is suddenly broken, how long do you need to take in order to get back on track again?
If you are afraid of this, it means your development is tied closely to your machine. 
We want to decouple your project from the machine.
If we achieved that, the time it takes for you to get back on track should be just to buy a new computer and rebuild the `virtualized computer`.

`Docker` is one of, if not the most famous, container solutions. 
It is free for non-commercial use, and it is widely adopted.

## 3.2. Installation

The easiest way to get `Docker` running in your machine is through [`Docker Desktop`](https://www.docker.com/products/docker-desktop/).

There are many great tutorials available online to help you with the installation process.

### 3.2.1. Windows

*I happen to write this guide since I was a Windows user (since 2020). So take this with a grain of salt.*

1. Install the `Docker Desktop` from <a href="https://www.docker.com/products/docker-desktop/">link</a>
2. Once the installation is done you may need to restart your OS.
3. Upon a startup, the `Docker Desktop` will launch up. It won't successfully to do so because you do not have WSL2. In the error box, there will be a link to *WSL2 installation guide* from Microsoft. Now, run this command to install WSL2 `wsl --install` in your cmd/terminal.
4. Check the result with this command.
```
> wsl -l -v
  NAME                   STATE           VERSION
* docker-desktop-data    Running         2
  docker-desktop         Running         2
```
This command shows you the kernel and version. If you are not going to use WSL anymore, this is all we need.
1. Launch `Docker Desktop` again.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/docker-desktop.png)

Tips:
If you take a look in the `Task Manager`, there is a process named `Vmmem` running. This is the Docker process. Once the `Docker Desktop` is started, `Vmmem` will always be there. To fully shut the Docker, use `wsl --shutdown` command in the cmd/terminal. 

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/vmmem.png)


# 4. Visual Studio Code (vscode)

Code is simply a text. 
This means you can write code with any text editor in the world, including Notepad. 
That is doable until you have to write a bigger project with many modules plus libraries. 
At this stage, having some help would be nice. 

Here comes the `Integrated Development Environment (IDE)`.

[quote](https://en.wikipedia.org/wiki/Integrated_development_environment)
> a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger. Some IDEs, such as NetBeans and Eclipse, contain the necessary compiler, interpreter, or both; others, such as SharpDevelop and Lazarus, do not.
>
> The boundary between an IDE and other parts of the broader software development environment is not well-defined; sometimes a version control system or various tools to simplify the construction of a graphical user interface (GUI) are integrated. Many modern IDEs also have a class browser, an object browser, and a class hierarchy diagram for use in object-oriented software development.

In my words, in order to enjoy developing code more, a good code development software is a must; otherwise, you will spend more time fixing basic bugs than creating magic.

Basic bug??

Yes, basic bugs, such as syntax errors, wrong variable name, undefined blah blah blah. Basic bugs.
These are avoidable or, at least, can be mitigated by using a better editor.

Enter `Visual Studio Code`. 
To define VScode, it is difficult. 

[quote](https://en.wikipedia.org/wiki/Visual_Studio_Code)
>Visual Studio Code, also commonly referred to as VS Code,[9] is a source-code editor made by Microsoft for Windows, Linux and macOS.[10] Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. Users can change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality.
>
>In the Stack Overflow 2021 Developer Survey, Visual Studio Code was ranked the most popular developer environment tool, with 70% of 82,000 respondents reporting that they use it.[11]

In my words, it is a versatile code editor. 
From a fresh installation, it is pretty lightweight.
The amazing thing about VSCode is the `Extension`.
It lets VSCode adapt itself to whatever you want it to be (and it starts to not be lightweight here LOL).


# 5. Docker

Let's get back to `Docker` because we only install it without learning about it.

Do we really need to understand `Docker` before we can use it? No. But should we? Yes.

## 5.1. What is Docker?

[quote](https://en.wikipedia.org/wiki/Docker_(software))
>Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine. It was first started in 2013 and is developed by Docker, Inc. Wikipedia

The key is `virtualization`. 
It is a form of simulation just like VM, but instead of emulating the entire machine, it only simulates kernels. 
In a more basic word, I can have Ubuntu 20.04, 18.04, 16.04, CentOS, and Red Hat running on my Windows/Mac. 
It does not end here; instead of running just a bare-bones OS, it can has an application pre-installed. 
This means I can run MySQL, PostgreSQL, Redis, Java, Python, C#, C++, Golang, ... in just a matter of minutes. 
**Using Docker will shorten installation steps and ensure that anyone who uses the same image will have the same environment.**

Wow, that's simply the same benefit as VM, but no, Docker is not a VM, as it does not emulate hardware. 
Instead, Docker sees all of your hardware. 
This comes with both pros and cons. 
We can discuss this elsewhere.

In Docker, `Docker image` and `Container` are two confusing words for a newcomer. 
To understand this, let's think about how we install Windows on a fresh machine.

1. Download ISO and create a bootable USB
2. Install Windows 
3. Configure and install the software we want to use
4. If the PC crashes, we restart it.
5. If the PC is broken, we reinstall it and repeat from step 2.

For Docker, if you want to have Ubuntu 24.04, we do the following:

1. Download the Docker Image of Ubuntu 24.04.
2. Run the image. It yields a container that runs Ubuntu 24.04. 
3. We install the software we want to use.
4. If we stop the container, we can start to restart it.
5. If we destroy the container, we have to recreate it, thus repeat from step 2.

Therefore, `Docker Image` is what we want to start with, and `Container` is an instance of what we start. 
This means you can create multiple Ubuntu 24.04 containers that consist of different software for different purposes, hence reducing the chance of library conflicts.

While it is true that we can use Docker as a VM solution (create the container and install the software that we want to use), we often want the container to do just one thing.
If you want to run a Web Application, the container should start and right away serve the web. 
Because of this practice, we create an image for each project separately.
Thus, every project environment is isolated because they are simply running in a separate virtualized environment.

This means you, the developer, have to create the `Docker Image` of your project.
And if you do it correctly, the image can be built/rebuilt and your project will still be functioning not only on your computer but anywhere. 

Here is the summary and simple workflow of Docker.

```
Base Image -> *customize* *build* -> My Image -> *run* -> container
```

For our purpose, we want to use Python and some libraries like `numpy` and `pandas` on Ubuntu 24.04, then here is what we will do next.

```
Ubuntu 24.04 -> *customize* *build* -> Python Image -> *run* -> Python Container
```

Sure, you can find the base image with Python3, but for the sake of learning, we will proceed with my plan.


## 5.2. Base Image

To find what you want to start with, you have to search from the [DockerHub](https://hub.docker.com). 
Simply search for Ubuntu and find what you want. Here is the [Ubuntu official Image](https://hub.docker.com/_/ubuntu).

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/docker-hub-ubuntu.png)

If you just want an Ubuntu image, 

```sh
docker pull ubuntu
```

But we want a specific version of Ubuntu. Click `Tags`.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/docker-hub-ubuntu-tags.png)

```sh
docker pull ubuntu:<tag>
```

Tag is a section to specify the version we want. 
What version do you want? That is where you need to read and research.
But now I want Ubuntu 24.04.

*Note: Since an image is simply an application. Some image has a specific way to use. You must read the manual/description in order to use them correctly.*

```sh
docker pull ubuntu:24.04
```

Okay, so run the command? What is this `pull` command anyway?

Pull is to download the image into your computer, but you don't really need to do that since Docker, when built/run, will `pull` automatically when the image is not found on the machine.

For now, we remember the image name and continue with customizing.

## 5.3. Customizing Image

To customize the image we have to create a `Dockerfile` file. 

```docker
FROM ubuntu:24.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
CMD tail -f /dev/null
```

- `FROM`: will use the `ubuntu:24.04` as a base image. 
- `WORKDIR`: is like `cd`, but it will also create a folder when the path does not exist.
- `RUN`: will execute the command in the terminal. 
- And, `CMD`: is what the container will do (remember that it is designed to be a process for one purpose).

## 5.4. Build 

We can build the image from a `Dockerfile` using the following command.

```sh
docker build .
```

## 5.5. Create a container

Once we have the image that we want to use, we will create a container (which is an instance of the image) using the following command.

```sh
docker run IMAGE[:TAG|@DIGEST]
```

and now we have the container.


## 5.6. Tedious?

One thing that does not appeal to me is a bunch of commands I have to remember in order to create a container. 
We have not yet opened the port, mapped the volume, assigned hardware, or limited the resources. 
There are a bunch of options we have to specify in the `run` command.

Now, we will be more civilized and use `Docker Compose`

# 6. Docker Compose

In a nutshell, Docker Compose helps you craft your `run` command in the `yml` format. 
In addition, Docker Compose helps to manage multiple containers when your app consists of multiple services. 

In our case, we will use it in place of the `docker run` command.

Create a file `docker-compose.yml`

```yml
version: '3.9'
services:
  python: # service/container name
    image: python # image name
    build: 
      context: .
      dockerfile: dockerfile
```

Now, instead of doing all those `docker <this/that/those>`, you just run `docker compose up`.

# 7. Using our Python container

## 7.1. `Remote - Containers` method

*I want to say it is obsolete but the truth is it still works quite well for accessing containers.*

Now, we want to access the Python in the container using VSCode. Luckily, things are already simplified. We have to install `Remote - Containers` extension in VSCode.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/vscode-remote-ext.png)

Once we installed that, we can go to Docker menu, right-click on the target container, and select `Attach Visual Studio Code`.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/vscode-remote-container.png)


Now we have Python running. You are ready for this course.

## 7.2. `.Devcontainer`

The amazing `.devcontainer` folder allows you to define your development environment in a more granular way. 
You can specify the exact tools, libraries, and settings you need for your project, and VSCode will automatically set up the container for you.

*I don't have time to write this down, so I skip. 
I show this in class; if you are missing the class, you can still find this knowledge online. 
Good luck!.*

# 8. Ensure the migration (Bonus)

*Me from 2025: I just realized how much effort I put into this. The latter part is not relevant, but it is still a good read. Therefore, I left them untouched.*

As said in the beginning, my goal is to have as clean as possible set up and easily migrating to new machine. For the past topics, we have achieved **clean set up**. When you want to work, you start Docker, start container, and code. When you are finished, you close everything and kill the **vmmem** process. No process is hogging your resources. Finally, when you are done with any project, you just delete Docker image and destroy containers. **Clean~~!!**

Now, let's establish a plan when your current machine decides to give you up and stop working. What will you do?

First, let's decompose the project into components. What does it need in order to develop a project?

1. A machine: subject to break
2. Python Environment: .Dockerfile, docker-compose.yml -> if you have these two files, you can always create a copy of your environment.
3. Your code: ...
4. Your data: ...

## 8.1. Buy a new machine

Surely, if the current machine is broken, get a new one. Set up Docker and VScode, and we are half way there.

## 8.2. Python Environment

Currently, our `.Dockerfile` has Python3. Along the course of development, you will surely need other library such as `numpy` and `pandas`. So, when we are migrating to another machine, we have to have these libraries too.

Currently, our `.Dockerfile` looks like this.
```
FROM ubuntu:20.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
CMD tail -f /dev/null
```

This means there are no libraries when we build and run the image. Sure, once the container is initiated, you can run `pip3 install` inside the container to get library and never destroy your container. But we are planning for **Machine is gone** scenario, so there are ways you can ensure your container will have the libraries it needs.

### 8.2.1. Put it in the .Dockerfile

You can specify the list of libraries you need in the `.Dockerfile`. This way, every time you build the image, it will always have the libraries. The only downside is you have to keep track of the libraries you are using in the project and put it in the `.Dockerfile`.

```
FROM ubuntu:20.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
RUN pip3 install numpy
RUN pip3 install pandas
CMD tail -f /dev/null
```

### 8.2.2. Use virtual environment

Virtual Environment is a concept of managing project-level environment. Before the existing of Docker, when you are developing multiple projects and want to ensure conflict free, you use virtual environment. We do not need it in the Docker since we should build one image for one project, but that does not mean there is no benefit of virtual environment when paring with container set up.

When you use virtual environment, there will be a folder consisting of a copy of python and libraries. This is created per project, and you can always create a list of libraries you are using in each project.

Base on the above information, you have two benefits.

1. You can map the volume of that **copy of python and libraries** to the machine disk. Every time you create a new container, just map the volume, and you are good to go.
2. You can save the **list of libraries** as a file and put it in the `.Dockerfile`.

For this approach, I will have my `.Dockerfile` and `docker-compose.yml` as followings

```
FROM ubuntu:20.04
WORKDIR /root/projects
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
RUN pip3 install pipenv
CMD tail -f /dev/null
```

```
version: '3.9'
services:
  python:
    image: python
    build: 
      context: .
      dockerfile: .Dockerfile
    volumes:
      - .venv/:/root/projects/.venv
    environment:
      # `pipenv` will create an environment in the working directory
      - PIPENV_VENV_IN_PROJECT=1
```

There are couples of virtual environment module for Python. I use `pipenv` for its ability to create Pipfile (list of libraries) for me automatically.

## 8.3. Your code

If the machine is broken, you may be able to retrieve the code in the HDD/SSD. But, what if the HDD/SSD is also destroyed? Then you would need to have a second copy of your code somewhere else. Here we talk about backup. You will have multiple options and workflows to choose. You might save your code in the Google Drive, OneDrive, and other Drive from other cloud storage provider. You might have your own USB drive and remember to copy the code to the Drive. All of above are fine. However, I want to introduce you to Git and GitHub.

Here is my analogy.
- Youtube - GitHub
- Channel - Repository
- Videos - Files

The two things are similar in managing/hosting/publishing a bunch of objects. However, the similarity end there, but it is good to know some term and compare to the known word.

### 8.3.1. GIT
Git is a protocol. It solves the problem of *versioning*. When you have a project, you want to create one repository for that project. Within the repository, Git will **keep track of the changes** and save each change in a node and form a tree. Each node called `commit`. You can have multiple branches (tree) and merge branches to sync up the changes. Because it keeps track of the changes, you can always go back in history for referencing, or even revert the entire project the previous version (back to the future~~).

### 8.3.2. GitHub
GitHub is a website that support Git protocol. You can sync up your local repository with the remote (repo in the GitHub) via the Git protocol. This enables easy collaborating with peers and backup.

Now, if you use GitHub, you code + .Dockerfile + docker-compose.yml + Pipfile can all be saved to GitHub. This means if you have to migrate the project, it just a simple pull from the GitHub.

Great, this mean no more manually backup? Sadly, no. GitHub has a limit of how big your file can be uploaded. (Git can keep track of any file size, but GitHub disallowed the big file to be uploaded). Thus means you can not upload your Data to the GitHub and you need to manually back up yourself.

## 8.4. Your data

Well, manually back up your data. A database, dataset, and other binary files are usually discarded from GitHub repository. You can use OneDrive and Google Drive to back up these data.

## 8.5. Execution

Here our plan is to put everything into GitHub except some confidential/big data. Our repository will look like this.

```
repository
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--docker-compose.yml
```

When we build the image, it will map the volume `./projects` into the container so that we have access to the source code (you can change to name of the folder). Here we update the `docker-compose.yml` to do that.

```
version: '3.9'
services:
  python:
    image: python
    build: 
      context: .
      dockerfile: .Dockerfile
    volumes:
      - ./projects/:/root/projects
    environment:
      # `pipenv` will create an environment in the working directory
      - PIPENV_VENV_IN_PROJECT=1
```

Now, how do we initiate Git in our local machine?, and sync this repository with GitHub? If you have never used Git before, my suggestion would be to install GitHub Desktop. What I am about to show you will be hated by Git enthusiast around the world and many hardcore Git users will always say "use the command line is a must" which is true in some situations (also applied to Docker). Eventually, you should learn how to use Git in the command line/terminal environment. However, for all people who are not familiar with terminal environment, it usually scared them of. Moreover, in a daily basis, I would spend my time writing code rather than recalling the command for Git's routine. Not to mention that I have to install Git for Windows to have the Git command in my machine.

## 8.6. GitHub Desktop

Visit <a href="https://desktop.github.com/">GitHub Desktop</a> and download the installer according to your operating system. After all the installation. You will have to have a GitHub account (well, we are about to upload and use GitHub service). Therefore, visit <a href="https://github.com/">GitHub</a> and create yourself an account. Here I would suggest you to create your own personal account using your **personal email address**. Nowadays, GitHub has become another way for the company to know you. Then, to get **GitHub Pro** plan, you have to bind AIT email address once you have created your account.

Once you have an account and login to it in the GitHub Desktop, click menu **File > New repository**

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/github-desktop-new-repo.png)

- **Name**: The repository name. This is the same name as your folder if you already created one.
- **Description**: Can leave as blank.
- **Local path**: This is where your repository/folder exist. Read more below.
- **Initialize this repository with a README**: Well, it will just create README.md. If you already have one, you can ignore.
- **Git ignore**: If you want to exclude anything of the repository, you put it in the `.gitignore`. Here, you select a template base on the programming language you about to use which normally have the same list of ignored files. 
- **License**: By default, your project is publicly available. To allow anyone else to use your project legally, you need to specify a term of use through the license file. Right now you can ignore this, but in the future, you should take sometime to choose the license you want to use.

Now, about the local path. GitHub Desktop does not expect you to point the destination to the already exist project/folder. Thus, it will create a new folder if the folder/path is not exist. For us and our situation, we already have a folder with our code on it. Therefore, we have to be more specific. For my case, I have all of my projects/code in `D:\MyProjects`. Inside this folder, I have a bunch of folders for different project I am/was working on. My new repository is here to. Here is the structure of my machine.

```
D:\
|--**MyOtherFolders**/
|--MyProjects/
  |--**Project1**/
  |--**Project2**/
  |--repository <<<< My new project
      |--projects/
          |--.venv/
          |--Dataset/
              |--Train/
                  |--data1
                  |--data2
              |--Test/
                  |--data3
                  |--data4
          |--**folders**/
          |--**files**
          |--Pipfile
          |--Pipfile.lock 
      |--.Dockerfile
      |--docker-compose.yml
  |--**Project3**/
  |--**Project4**/
|--**MyOtherFiles**
```

Now, I should name my `repository`. I will name it `DSAI-python` to reflex that this is the repository for this course.

```
D:\
|--**MyOtherFolders**/
|--MyProjects/
  |--**Project1**/
  |--**Project2**/
  |--DSAI-python <<<< My new project
      |--projects/
          |--.venv/
          |--Dataset/
              |--Train/
                  |--data1
                  |--data2
              |--Test/
                  |--data3
                  |--data4
          |--**folders**/
          |--**files**
          |--Pipfile
          |--Pipfile.lock 
      |--.Dockerfile
      |--docker-compose.yml
  |--**Project3**/
  |--**Project4**/
|--**MyOtherFiles**
```

In the menu of create new repository, the `Name` is `DSAI-python` and `Local path` is `D:\MyProjects`. I will leave other fields as default. Then, `Create repository`.

Back to my `DSAI-python`, I will have one new folder on the root path. If you can not see it, you have to enable Hidden folder.

```
DSAI-python
|--.git/ <<<<< new
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--.gitattributes
|--docker-compose.yml
```

## 8.7. Gitignore

If we go back to the GitHub Desktop, we will notice that GitHub Desktop already commit one change with message "Initial commit" and in the commit, our `Dataset` has already *added* into the repository. For my purpose, we want to exclude this from the repository.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/github-desktop-init-commit.png)


To fix this, we have to revert the commit and exclude the `Dataset` from the git using `.gitignore`.

1. Revert the `Initial commit` by right-click on the commit and select `Undo commit...`
![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/github-desktop-undo-commit.png)

2. Create a file `.gitignore` in the root path.

```
DSAI-python
|--.git/
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--.gitattributes
|--.gitignore
|--docker-compose.yml
```

3. Add `Dataset` into the `.gitignore` and save the file

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/github-desktop-ignore.png)

Notice that all files in the Dataset folder is gone from the changes tab.

4. Commit to **main**

Now, Git will ignore the entire of Dataset folder even the assistance of the folder. This causes one thing, when you publish this to GitHub, there will be no sign of Dataset folder. Thus, when anyone clones the repository, they will have to create a folder themselves. 

Okay, if I want to keep my folder but not my files, I have to change the `.gitignore` from folder name to filename, is not it? No.

Even though you have spent your time listing all the files you want to exclude, if, in the end, the folder is empty, it won't appear in the repository. **Any folder that is empty will not appear in the repository**. Thus, if you wish to have a folder in your repository, you need to have at least one file. In the convention of Git, we put `.keep`, `.keeps` or `.gitkeep` in any folder we want to keep it existence in the repository. Then, we add `!.keep`, `!.keeps`, or `!.gitkeep` in the last line of `.gitignore` to exclude the ignoring of the file. Finally, we change from ignoring `Dataset` folder to ignoring files in the folder using `Dataset/*`

Here is my `.gitignore`

```
Dataset/*
!.keep
```

Here is my folder structure

```
DSAI-python
|--.git/
|--projects/
    |--.venv/
    |--Dataset/
        |--Train/
            |--data1
            |--data2
        |--Test/
            |--data3
            |--data4
        |--.keep
    |--**folders**/
    |--**files**
    |--Pipfile
    |--Pipfile.lock 
|--.Dockerfile
|--.gitattributes
|--.gitignore
|--docker-compose.yml
```

Note that this will not work with any file that is already added to repository. You can only ignore files that is not included in the repository only. If you make a mistake and want to ignore a file after many commits, there is a way and I will leave it to you to figure it out.

## 8.8. Publishing the repository

Now you have a repository running in your local machine. You can make changes and create commits or make a new branch and merge as many as you desire. When you are ready, you can publish this repository to GitHub. To do that, click `Publish repository`.

![alt](https://raw.githubusercontent.com/chaklam-silpasuwanchai/Machine-Learning/master/.0%20-%20installation_image/github-desktop-new-repo.png)

Here you can change the name of the repository (this will not affect the folder name in your local machine) and an option whether to make this repository a private or not. Once done choosing, just click `Publish repository`. Done~~!!

## 8.9. Syncing and Collaborating

Now, you have two repositories (local and remote/GitHub), and you wish that both repositories will look the same. To achieve you have to push and pull. Here is a diagram.

![alt](https://greenido.files.wordpress.com/2013/07/git-local-remote.png?w=696&h=570)

Every time you are committing, you are only interacting with the local repository. To sync the local repository, you have to `push` the changes/commits to the remote (GitHub) one. 

Now, if you have a second machine or your friend are also working on the same project using the same repository, that means there is another local repository in that another machine. Are you confusing? Let's imagine you have a PDF file you want to share with your friend. You choose to upload the PDF to Google Drive and share the link to your friend (`push`). Your friends see the file exist in the Google Drive. They will have to download in to their machine (`pull`). In this context, I map to the following analogy.

- PDF - commit
- You machine - Local Repository
- Google Drive - GitHub/Remote Repository
- Upload PDF - Push
- Your friend machine - Another local Repository
- Download PDF - Pull

`fetch` is to check for new commits but not push or pull.

In summary, you will have to push and pull consistently to make sure that both repositories are in sync.

## 8.10. What else?

There is no rule in GitHub. There is only `main` branch and other branches. The meaning of branch is up to you and your team.

Conflict is not an error but rather Git is asking you to help decide what you want. Remember that Git is only tracking changes of files. Conflict happens because in one line of one file is changed from both persons (commit). Conflict can and will happen if more than one person are working on the same file. If you want to avoid this, you have to plan your project structure out and breakdown your code into multiple files and each team member working on different files. Anyhow, it just my suggestion and my best practice. You can always adapt and make your own practice.
