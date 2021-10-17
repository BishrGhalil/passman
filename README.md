# PassMan
A simple python password manager.
### Dependencies
* pyperclip
* cryptography
* argparse
### Install
```
git clone https://github.com/BishrGhalil/passman.git
cd passman
pip3 install -r requirements.txt
sudo make
```

### Usage
You can use it to add, search, delete and generate passwords by running.
```
passman
```
You can use the command line arguments to copy a password to the clipboard by a single command.
```
passman -us <service-name>
```
See ```passman -h``` for complete help.
