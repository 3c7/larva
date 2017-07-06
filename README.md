# Larva

Larva is a simple TheHive commandline client. Right now it is capable of... nothing. Well it can list cases, but if I find some time, I'll add some features.
![What it looks like atm...](https://s4.postimg.org/77nconswt/Screenshot_from_2017-07-06_20.56.56.png)
## Installation
```bash
$ git clone git@github.com:3c7/larva.git
$ cd larva
$ virtualenv .
$ . bin/activate 
$ pip install .
```

or in case of developing without re-installs

```bash
$ git clone git@github.com:3c7/larva.git
$ cd larva
$ virtualenv .
$ . bin/activate
$ pip install --editable .
```
## Configuration
```bash
# Set username
$ larva config username --set MyUsernameOrEmail@example.com
# Set TheHive URL
$ larva config url --set https://myinstance.ofthehive.com
```

## Usage
```bash
$ larva
Usage: larva [OPTIONS] COMMAND [ARGS]...

  The commandline client to TheHive.

  If you find any bugs, please make sure to report them on
  https://github.com/3c7/larva/issues

Options:
  --help  Show this message and exit.

Commands:
  config  Manage larva configuration
  list    This lists all cases.
```
