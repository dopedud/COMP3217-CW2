# COMP3217-CW2

This project is the coursework 2 of Security of Cyber Physical Systems (COMP3217). This coursework is about building a machine learing (ML) pipeline to estimate labels of a given training data, which contains system traces of a power system.

## Setup

The programming language to use is Python, since it has many libraries to assist in building a ML pipeline, particularly libraries provided by Scikit-Learn.

To use these libraries, you need to create a python virtual environment and install the libraries into the environment. This will make the libraries we used are local only to this project. The steps to do this are shown below:
1. install Python 3.8 or above
2. open `cmd` with this project folder's directory as working directory
3. check python version is correct by typing `py --version` into `cmd`
4. create a python virtual environment by typing `py -m venv venv` into `cmd`; this will create a new folder called `venv`
5. activate python environment by typing `venv\Scripts\activate`

From here you can install any packages you want. Most common ones are:
1. `numpy`
2. `pandas`
3. `matplotlib`
4. `scikit-learn`

To install packages, type the command `pip install <name of package>` into `cmd` (NOTE: venv must be activated first).
`pip list` to check installed packages.

From here you can use jupyter notebook to use these libraries and code in the ML pipeline.