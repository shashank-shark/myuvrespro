# Setting up python environment

> ### Software packages and requirements
### **Basic TOOLS required for implementation and visualization**
* networkx python module
* matplotlib
* numpy
* algorithms and data structures

#### Concepts that I would and may use to **develop** this system include:
- Operating System Concepts.
- IPC (Interprocess Communications).
- Socket Programming
- Multipoint client-server programming.
- OpenCV (Computer Vision)
- Robotics and few electronic and circuit boards.


## **STEP 1**: SETTING UP PYTHON 3 and VENV (Virtual Environment)
Since I am using all linux based systems on my machines and mini-computers (RASP-PI) python2 and python3 comes pre-installed. You can enter "`python`" (without braces) in your terminal and verify whether python is installed or not. If not, then there are many tutorials and docs out on web which will help you in installing python on your linux machine.

### **Installing `pip`**
Many linux distributions give python2 as the default version when you type `python` in the terminal. We will deal with this later in the below step how `venv` can be used to solve this issue (although not).
To install `pip3` on linux systems we need to use distro's package manager.
The below table shows what package managers are used in different flavours.


| DISTRO        | PACKAGE-MANAGER | COMMAND |
| ------------- |:-------------:| -------------|
|**`Debian based`**  | apt, apt-get  | sudo apt-get install python3-pip |
| **`Red-hat`**     | yum (old), dnf (new)  |   sudo dnf install python3-pip    |
| **`Arch, Manjaro`** | pacman, yarout     |    sudo pacman -S python-pip   |

### **Setting the `venv`**
`venv` stands for virtual environment. Here we shall create a virtual environment for `python3`. To install `venv` on linux systems use the following commands.

| Command for installing `venv` for python  |
|:-----------------------------------------:|
|   `sudo apt-get install python3-venv`   |

### **Creating first python3 virtual environment**
- Use the below command to create the virtual environment.
- `python3 -m venv shashank`

- After executing this command python3 virtual environment named **shashank** will be created.

### **Activating the virtual environment created**
- Navigate to the `shashank/bin` directory.
- Use the below command to activate the environment.
- `source activate`
- In furthur updates and coding I would create many python virtual environments as such.
