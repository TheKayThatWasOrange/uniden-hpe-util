# Uniden HPE File Converter

If you want to use an absurdly expensive Uniden brand radio scanner that doesn't even come with its own GPS tranceiver you have to contend with some seriously asstastic Windows software known as [Sentinel](http://info.uniden.com/twiki/bin/view/UnidenMan4/BCDx36HPSentinel) to program custom channel information into it. Sentinel's automation capabilities begin and end with the importing/exporting of opaque, undocumented `.hpe` files. Uniden assumes that the HPE files you want are already on the internet and tells you to kick rocks if they aren't.

Need to add thousands and thousands of custom channels which no unemployable boomer in the world has ever cared enough about to post on some radio dork forum for radio dorks? Well you get to sit there and create them yourself one-by-friggin-one because Uniden hates you.

You can't even clone an existing channel and just type in the new frequency to speed through the tedium. Sentinel is every bit as bad as Robotech II: The Sentinels. Probably worse.

Some angry stepdads will smugly point out that there's an [aftermarket application](https://proscan.org/) you can PayPal some flag-waving geezer $50 for if you want more automation capabilities, but it is similar to Uniden's own offering in that it will only run on a Gateway PC your grandson set up for you 30 years ago to get you to stop making him wooden toys he had to throw away. Also every cent that flies through PayPal results in Peter Thiel's ego getting bigger and I think we've all had quite enough of that.

Luckily, [this person](https://github.com/sq5bpf/hpe_open) found out that `.hpe` files are nothing more than XORed GZip files which can be converted to/from plain text pretty easily. Once you get something tab-delimited to work with, you can use any tool you like on any platform imaginable to modify that text and pump it back into Uniden's awful Sentinel application.

This tool is a proof-of-concept in Python 3. It has no meaningful error handling of any kind and even less technical support but it's free.

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

Your best bet is to create one of the channels you need in Sentinel manually, export that to HPE, run this tool and then write whatever you need to extend that example file. Once you're done, convert it back to HPE and go import it into Sentinel. If you're extremely lucky, it'll actually work and Santa will bring you a scanner that is slightly less crippled with your Trumpy Bear this year.
