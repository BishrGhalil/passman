# PassMan
A simple python password manager.
### Install
```
git clone https://github.com/BishrGhalil/passman.git
cd passman
pip3 install -r requirements.txt
sudo make
```

### Usage
```
passman
```
Or using cli interface
```
usage: passman.py [-h] [-n NEW] [-u USERNAME] [-s SERVICE] [-v] [-d DELETE]

options:
  -h, --help            show this help message and exit
  -n NEW, --new NEW     add a new service.
  -u USERNAME, --username USERNAME
                        username for the new service.
  -s SERVICE, --service SERVICE
                        get a stored password of a service.
  -v, --visable         print output.
  -d DELETE, --delete DELETE
                        delete a service.
```
