# Uniden HPE File Converter

If you want to use an [absurdly expensive Uniden brand radio scanner](https://www.zipscanners.com/products/sds100-uniden-police-scanner) you have to contend with some seriously asstastic Windows software known as [Sentinel](http://info.uniden.com/twiki/bin/view/UnidenMan4/BCDx36HPSentinel) to program custom channel information into it on a big boy keyboard. Sentinel's automation capabilities begin and end with the importing and exporting of opaque, undocumented `.hpe` files that look like pure binary gibberish in a hex editor. Uniden assumes that the HPE files you want are already on the internet and tells you to kick rocks if they aren't.

![hpehex](https://user-images.githubusercontent.com/129024004/228378228-a6015a04-5131-4752-987d-b4c712207f7a.jpg)

But what if you need to add thousands and thousands of custom channels with specific CTCSS tones which no unemployable boomer in the world has ever cared enough about to post on some radio dork forum for Justin Wilson lookalikes who drive Jeeps? Well you get to sit there and give yourself carpal tunnel syndrome cilcking through billions and billions of individual settings fields one-by-friggin-one because Uniden hates anyone who has a job.

Now you might be tempted to think that you can just clone a "template" channel over and over and then proceed to edit the frequencies en-masse to speed through all that data entry tedium the way you might in an actual spreadsheet, but then you'd be living in some kind of Bizarro world where Uniden hires competent product managers that care about their users. Even Sony's never done that. No folks, The Sentinel is here to guard you from hippie socialist constructs like productivity and ease of use. Don't like it? What are you? Some kind of ANTIFA snowflake?

![boomer-computer-monsters](https://user-images.githubusercontent.com/129024004/228384261-88177861-9ee9-4076-9f3f-a2490f7f75bc.gif)

Many angry stepdads with Earthlink email addresses will smugly point out that there's a cataract-inducing [aftermarket application](https://proscan.org/) which you can PayPal some flag-waving geezer $50 for if you want more programming flexibility and less money in your pocket, but it is similar to Uniden's own offering in that it will only run on a Gateway PC your grandson set up for you 30 years ago to "thank" you for all the handmade wooden toys he threw away. Also every cent that flies through PayPal results in Peter Thiel's ego swelling faster than his prostate and I think we've all had quite enough of that.

Luckily, [this person](https://github.com/sq5bpf/hpe_open) found out that HPE files are nothing more than XORed GZip files which can be converted to/from plain text with the computational sophistication of a Little Orphan Annie secret decoder ring. Unluckily, his makefile doesn't work anymore so I just translated the basic process into reasonably modern Python. I say that having written zero Python in the last two years so my idea of "reasonably modern" may very well be "utterly laughable" to you. Why do I think it's modern? Because I used the walrus operator. Twice!

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

They look like this after you unpack them (Who needs named columns? Guess!):

![hpeexample](https://user-images.githubusercontent.com/129024004/228380496-4a2f8a51-164c-4c5d-b02c-99bf87dce44a.gif)

Since you won't know what goes where or what constitutes a valid value, your best bet is to create one of the channels you need in Sentinel manually, export that to HPE, run this tool and then write whatever you need to extend that template file.

Once you're done adding channels convert it back to HPE and go import it into Sentinel. If you're extremely lucky it'll actually work and Santa will bring you a scanner that is slightly less crippled with your Trumpy Bear this year. If it doesn't work, feel free to figure out why and send me a pull request.

# Getting Uniden Senitnel To Run Without Buying A Windows License You Have Absolutely No Use For

Current versions of Sentinel seem to have introduced some bizarre new requirement in that they will only read and write scanner data to a drive which identifies itself as "Removable." Wine does not seem to support creating this kind of drive, so even if you explicity map your SD card in and can see it just fine, Sentinel will pretend it's not there. Long story short, don't waste your time unless you know a whole lot about Wine.

1. Install [CrossOver](https://www.codeweavers.com/crossover)
2. Download one of their pre-packaged ["bottles"](https://www.codeweavers.com/xfer/Dependency_archive/) that includes the .NET framework. Most Uniden executives are still running Windows 7 so no need to be even remotely up-to-date. If that page asks you for a password give it `demo`.
3. Import the bottle you downloaded
4. Install Sentinel into that same bottle
5. Map your drive in (if that's even possible anymore)
6. Profit

![sentineled](https://user-images.githubusercontent.com/129024004/228398643-d992458f-fbd4-4e93-8b47-5fb35819d0eb.jpg)

If you get some nonsensical, broken English error message like _"Reading hpe file was failure."_ then you probably didn't pick the right bottle. You can try to install .NET yourself if you actually know how Wine works but I don't so I didn't.

![UnidenError](https://user-images.githubusercontent.com/129024004/228379961-894d5854-4efa-4378-8c55-6530de5e05ff.gif)
