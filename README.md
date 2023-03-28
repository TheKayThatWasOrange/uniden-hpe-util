# Uniden HPE File Converter

If you want to use an [absurdly expensive Uniden brand radio scanner](https://www.zipscanners.com/products/sds100-uniden-police-scanner) that doesn't even come with its own GPS tranceiver you have to contend with some seriously asstastic Windows software known as [Sentinel](http://info.uniden.com/twiki/bin/view/UnidenMan4/BCDx36HPSentinel) to program custom channel information into it from a big boy keyboard. Sentinel's automation capabilities begin and end with the importing and exporting of opaque, undocumented `.hpe` files that look like pure binary gibberish in a hex editor. Uniden assumes that the HPE files you want are already on the internet and tells you to kick rocks if they aren't.

But what if you need to add thousands and thousands of custom channels which no unemployable boomer in the world has ever cared enough about to post on some radio dork forum for Justin Wilson lookalikes? Well you get to sit there and create them yourself one-by-friggin-one because Uniden hates people who have jobs.

You might be tempted to think that you can just clone an existing channel over and over and then type in the new frequency to speed through all that data entry tedium the way you might in an actual spreadsheet, but you'd be living in some kind of Bizarro world where Uniden hires competent product managers. Sentinel is here to guard you from socialist constructs like convenience and ease of use. What are you? Some kind of ANTIFA snowflake?

Many angry stepdads with Earthlink email addresses will smugly point out that there's a cataract-inducing [aftermarket application](https://proscan.org/) which you can PayPal some flag-waving geezer $50 for if you want more programming flexibility and less money in your pocket, but it is similar to Uniden's own offering in that it will only run on a Gateway PC your grandson set up for you 30 years ago to "thank" you for all the handmade wooden toys he threw away. Also every cent that flies through PayPal results in Peter Thiel's ego swelling faster than his prostate and I think we've all had quite enough of that.

Luckily, [this person](https://github.com/sq5bpf/hpe_open) found out that HPE files are nothing more than XORed GZip files which can be converted to/from plain text with a Little Orphan Annie secret decoder ring. Unluckily, his makefile doesn't work anymore so I just translated the basic process into reasonably modern Python. I say that having written zero Python in the last two years so my idea of "reasonably modern" may very well be "utterly laughable" to you. Why do I think it's modern? Because I used the walrus operator. Twice!

Once you get something tab-delimited to work with you can use any tool you like on any platform imaginable to modify that text and pump it back into Uniden's awful Sentinel application.

# Disclaimer

This tool is a proof-of-concept devoid of any warranty. It has no meaningful error handling of any kind and even less technical support but it's free. Just like freedom itself.

# Usage

Assuming that the executable bit is still set on the file:

### Decoding

`./hpeutil.py decode social_security_check_cashing_services.hpe`

### Encoding

`./hpeutil.py encode social_security_check_cashing_services.txt`

# What's In An HPE File Anyway?

They look like this (Who needs named columns? Guess!):

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

Since you won't know what goes where or what constitutes a valid value, your best bet is to create one of the channels you need in Sentinel manually, export that to HPE, run this tool and then write whatever you need to extend that template file.

Once you're done adding channels convert it back to HPE and go import it into Sentinel. If you're extremely lucky it'll actually work and Santa will bring you a scanner that is slightly less crippled with your Trumpy Bear this year. If it doesn't work, feel free to figure out why and send me a pull request.

# Getting Uniden Senitnel To Run Without Buying A Windows License You Have Absolutely No Use For

1. Install [CrossOver](https://www.codeweavers.com/crossover)
2. Download one of their pre-packaged ["bottles"](https://www.codeweavers.com/xfer/Dependency_archive/) that includes the .NET framework. Most Uniden executives are still running Windows 7 so no need to be even remotely up-to-date. If that page asks you for a password give it `demo`.
3. Import the bottle you downloaded
4. Install Sentinel into that same bottle
5. Profit

If you get some nonsensical, broken English error message like _"Reading hpe file was failure."_ then you probably didn't pick the right bottle. You can try to install .NET yourself if you actually know how Wine works but I don't so I didn't.
