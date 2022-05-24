```
usage: steganophy.py [-h] [-i INFILE] [-o OUTFILE] [-s SECRET] [-e] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        audio file need to be stegano
  -o OUTFILE, --outfile OUTFILE
                        out file to exported
  -s SECRET, --secret SECRET
                        secret
  -e, --encrypt
  -d, --decrypt
```

```
$python3 steganophy.py -e -i audio/audio.wav -o audio/out.wav -s "Le Thanh Trung Nhom 7 - LSB"
Success
```

```
$python3 steganophy.py -d -i audio/out.wav 
Secret : Le Thanh Trung Nhom 7 - LSB
```


