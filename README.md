# Uniden HPE File Converter

If you want to use a Uniden brand radio scanner you have to contend with some seriously horrible Windows software to program custom channel information and its automation capabilities begin and end with the importing/exporting of `.hpe` files. Need to add thousands and thousands of channels which no unemployable boomer in the world has ever cared about enough to post on some radio dork forum? Well you get to sit there and enter them one-by-one. There's an aftermarket application you can PayPal some flag-waving geezer $50 for if you want more capabilities, but it is similar to Uniden's own offering in that it will only run on a Gateway PC your grandson set up for you 30 years ago.

Luckily, [this person](https://github.com/sq5bpf/hpe_open) found out that `.hpe` files are nothing more than XORed GZip files which can be converted to/from plain text pretty easily. Once you get something tab-delimited to work with, you can use pretty much any tool you like on any platform imaginable to modify that text and pump it back into Uniden's awful Sentinel application.

This tool is a proof-of-concept in Python 3. It has no meaningful error handling of any kind but it's free.

# Usage

## Decoding

`./hpeutil.py decode test.hpe`

## Encoding

`./hpeutil.py encode test.txt`

## What's In An HPE File Anyway?

They look like this:

```
TargetModel	HomePatrol-1
FormatVersion	2.00
Conventional			Federal 163-165 MHz	Off		Conventional
C-Group			Analog Search	Off	0.000000	0.000000	0.0	Circle
C-Freq			163.0000	Off	163000000	FM	TONE=Srch	208	Off	2	0	Off	Auto
C-Freq			163.0125	Off	163012500	FM	TONE=Srch	208	Off	2	0	Off	Auto
C-Freq			163.0250	Off	163025000	FM	TONE=Srch	208	Off	2	0	Off	Auto
C-Freq			163.0375	Off	163037500	FM	TONE=Srch	208	Off	2	0	Off	Auto
C-Freq			163.0500	Off	163050000	FM	TONE=Srch	208	Off	2	0	Off	Auto
C-Freq			163.0625	Off	163062500	FM	TONE=Srch	208	Off	2	0	Off	Auto
File	HomePatrol Export File
```

If you know what Python is then you can probably figure out how to do something useful with that.
