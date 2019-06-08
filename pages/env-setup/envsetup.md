# Setting up python environment

## **STEP 1**: SETTING UP PYTHON 3 and VENV (Virtual Environment)
Since I am using all linux based systems on my machines and mini-computers (RASP-PI) python2 and python3 comes pre-installed. You can enter "`python`" (without braces) in your terminal and verify whether python is installed or not. If not, then there are many tutorials and docs out on web which will help you in installing python on your linux machine.

### **Installing `pip`**
Many linux distributions give python2 as the default version when you type `python` in the terminal. We will deal with this later in the below step how `venv` can be used to solve this issue (although not).
To install `pip3` on linux systems we need to use distro's package manager.
The below table shows what package managers are used in different flavours.


| DISTRO        | PACKAGE-MANAGER |
| ------------- |:-------------:|
|**`Debian based`**  | apt, apt-get  |
| **`Red-hat`**     | yum (old), dnf (new)  |
| **`Arch, Manjaro`** | pacman, yarout     |

### **Setting the `venv`**
`venv` stands for virtual environment. Here we shall create a virtual environment for `python3`. To install `venv` on linux systems use the following commands.
