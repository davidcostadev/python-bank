# Diego Bank

### Requerimentos

 - python3
 - py.test

### Instalação

No ubuntu 18.04 precisa instalar o python3-distutils

`sudo apt-get install python3-distutils -y`

1. `pip install virtualenv` 
2. `virtualenv --python=python3 venv`
3. `source ./venv/bin/activate`
4. `pip install pytest` 


### Como usar

**Testando todos os arquivos**

`py.test`

**Testando apenas um arquivo**

`py.test test/test_diego-bank.py`


**Exemplo de test funcionando**

`py.test test/test_exemplo.py`