# zbpypkg
A simple python test package


# Prepare:
```shell
## The following code installs the 'zbpypkg' package into your python's site-packages directory.
mkdir /tmp/install_zbpypkg
cd /tmp/install_zbpypkg
rm -rf zbpypkg  # The directory may not be present, though.
git clone https://github.com/zzdrazil/zbpypkg.git
mv zbpypkg/setup.py .
```

# Install (for yourself only):
```shell
python3 setup.py install --user
```

# Install system wide (login as root):
```shell
python3 setup.py install
```

# Test:
```shell
python3
```
```python3
from zbpypkg import *
m = Animals.Mammals()
m.printMembers()
```
# Output:
```
Printing members of the Mammals class
        Tiger
        Elephant
        Wild Cat
```


# Clean:
```shell
rm -rf /tmp/install_zbpypkg
```
