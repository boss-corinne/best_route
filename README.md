best_route
==========
This is a python package which can be used as a command-line 
tool to find the best route between two specified points.

Installation
------------
To install the package, clone or download it from this 
repository, enter the top level of the directory and 
execute the following command:

```bash
pip install best_route
```
or (if you don't have access to pip):
```bash
python setup.py install
```

To install for development purposes, again in the top level:
```bash
pip install -e .
```
or:
```bash
python setup.py develop --user
```

Usage
-----
You will need three input arguments:
<network-filename>
<origin>
<destination>

These should be used in a bash terminal as follows:
```bash
best_route <network-filename> <origin> <destination>
```

The returned value is the shortest route between the origin 
and destination according to the specified network file.
