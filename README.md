# buckwalter_transliterate_arabic
Buckwalter transliteration for Arabic language using [lang-trans](https://github.com/kariminf/lang-trans.git) package, moreover this code allows us to transliterate on any text you want and save your result as you want.

</br>


## What it does
these scripts help to transliterate from utf8 format to buckwalter format and vice versa.

## System requirements
- Python 2.7 or 3
- python package lang-trans 

## Installation 

- installl lang-trans from source

```
git clone https://github.com/kariminf/lang-trans.git
cd lang-trans
sudo python setup.py install
```
- install lang-trans with pip or pip3

```
pip install lang-trans
pip3 install lang-trans
```
## Usage
from utf8 format to buckwater format and vice versa
```
python buckwalter_to_utf8.py <text_name_path> <file result>
python utf8_to_buckwalter.py <text_name_path> <file result>
```
## Example of use

```
python buckwalter_to_utf8.py  test/test2.txt result.txt
python utf8_to_buckwalter.py  test/test1.txt result.txt
```








