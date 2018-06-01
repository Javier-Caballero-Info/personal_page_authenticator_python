# Personal Page Authenticator - Python

> Python API REST Full with [Flask](http://flask.pocoo.org/), [Connexion](https://github.com/zalando/connexion) and [Firebase database](https://firebase.google.com/)

## Table of Contents

-   [Overview](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master/README.md#overview)
-   [API Description](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master/README.md#api_description)
-   [Clone](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master/README.md#clone)
- [Requirements](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#requirements)
- [Installation](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#installation)
	- [Pyhton 3](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#nodejs-and-npm)
	- [Virtual environments - pyenv (Linux/MacOS)](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#nodejs-and-npm)
	- [Creation of virtualenv (Linux/Mac)](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#nodejs-and-npm)
	- [Dependencies (All)](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#dependencies)
- [Environment](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#environment)
- [Developing](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#developing)
- [Test](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#test)
- [Build](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#build)
- [Running with Docker](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#running-with-docker)
	- [Building the image](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#building-the-image)
	- [Starting up a container](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#starting-up-a-container)
- [Contributing](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#contributing)
- [Author](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#author)
- [License](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/tree/master#license)

## Overview

This API has the responsibility of manage all the user information and control the authentication process and methods. 

## API Description

For more information about the endpoints of the API please check the [apiary doc](https://personalpageadminnodejs.docs.apiary.io).

## Clone

```bash
git clone https://github.com/Javier-Caballero-Info/personal_page_authenticator_python.git
git remote rm origin
git remote add origin <your-git-path>
```

## Requirements

* **Python:** 3.6.5 or above

## Installation

The installation is recommended made by python virtual environments (Linux and Mac users). For that reason, the following instruction includes the installation of virtualenv.

1. ### Pyhton 3

    - Debian / Ubuntu
    
        - Ubuntu 16.04
        
        ```Bash
        sudo add-apt-repository ppa:jonathonf/python-3.6
        sudo apt update
        sudo apt install python3.6
        ```
            
        - Ubuntu 16.10 or above
    
        ```bash
        sudo apt update
        sudo apt install python3.6
        ```
    
    - MacOS
    
        - Installer
        
        Install Python 3.6.x from [https://www.python.org/downloads/](https://www.python.org/downloads/).
        
        - Brew
        ```bash
        brew install python3
        ```
    
    - Windows
    
        - Installer
        
        Install Python 3.6.x from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. ### Virtual environments - pyenv (Linux/MacOS) 

    - Debian / Ubuntu
    
    ```bash
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    ```
    
    - MacOS
    
        - Bash
        
        ```bash
        curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
        ```
        
        - Brew
        ```bash
        brew install pyenv
        ```
    
3. ### Creation of virtualenv (Linux/Mac)
    
    Creation of virtualenv:
    
    ```bash
    virtualenv -p python3 <desired-path>
    ```
    Activate the virtualenv:
    
    ```bash
    source <desired-path>/bin/activate
    ```
    
    Deactivate the virtualenv:
    
    ```bash
    deactivate
    ```

4. ### Dependencies (All)

    This will install all dependencies from requirements.txt
    
    ```bash
    pip install -r requirements.txt
    ```

## Environment

Export the following environment variables:

```bash
PORT=3000
SECRET=secret # Secret key for JWT

# Firebase Credentials
DATABASE_URL=db.firebase.com # Url for Firebase database
DB_PRIVATE_KEY_ID=secret_id # Firebase private key id
DB_PRIVATE_KEY=secret # Firebase private key
DB_CLIENT_EMAIL=email@firebase.com # Firebase client email
DB_CLIENT_ID=some_client_id # Firebase client id
```

## Developing

>Setup the environment variables

After every change in the code you must stop the server and build the app again.

```
python setup.py install && python -m swagger_server
```

## Test

>Setup the environment variables before run the command.

```
tox
```

## Build

```
python setup.py install
```


## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

### Building the image
```bash
docker build -t personal_page_authenticator_python .
```
### Starting up a container
```bash
docker run -p 3000:3000 -d \
-e SECRET_KEY="some-secret-string" \
-e JWT_SECRET_KEY="jwt-secret-string" \
-e DATABASE_URL="db.firebase.com" \
-e DB_PRIVATE_KEY_ID="secret_id" \
-e DB_PRIVATE_KEY="secret" \
-e DB_CLIENT_EMAIL="email@firebase.com" \
-e DB_CLIENT_ID="some_client_id" \
personal_page_authenticator_python
```
## Contributing

Contributions welcome! See the  [Contributing Guide](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/blob/master/CONTRIBUTING.md).

## Author

Created and maintained by [Javier Hernán Caballero García](https://javiercaballero.info)).

## License

GNU General Public License v3.0

See  [LICENSE](https://github.com/Javier-Caballero-Info/personal_page_authenticator_python/blob/master/LICENSE)