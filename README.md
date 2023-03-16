# verb tampering
two Scripts for checking  HTTP verb tampering vulnerability on websites
that coded in python and bash script languages.

with this scripts, you can send HTTP Request with below verbs
      ```GET POST PUT DELETE HEAD OPTIONS PATH TRACE CONNECT```
to find which HTTP Method is allowd on the server.

## Usage

### Python
``` 
pip instal -r requirements.txt
python verb-tamper.py <host>
```
### bash

```
bash ./verb-tamper.sh <host>

```
