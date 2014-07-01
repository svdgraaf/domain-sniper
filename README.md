Domain-Sniper
=============

With this tool, you can easily check if a domain is in use or not. It uses the OpenProvider api for interaction, so you need an account there.

Example
=======
```bash
$ ./sniper example.com -u [username] --hash [hash]
example.com active Domain exists
```

You can pipe the results to do something with it:
```bash
./sniper example.com asdfsfdasfa23wdszc.com -u [username] --hash [hash] | awk '{print $1,":", $2}'
example.com : active
asdfsfdasfa23wdszc.com : free
```

Installation
============
```bash
git clone git@github.com:svdgraaf/domain-sniper.git
cd domain-sniper
pip install -r requirements.txt
# ...
echo 'profit!'
```


Options
=======
```bash
$ ./sniper -h
usage: sniper [-h] [-p password] [-u username] [--hash hash]
              domain [domain ...]

positional arguments:
  domain                domain(s) which should be checked

optional arguments:
  -h, --help            show this help message and exit
  -p password, --password password
                        password for authentication
  -u username, --username username
                        username for authentication
  --hash hash           hash for authentication
```


Todo
====
Make provider optional, and create endpoints for other registrars
