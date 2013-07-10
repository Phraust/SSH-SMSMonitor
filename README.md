SSH-SMSMonitor
==============

A simple python script to test a remote server's uptime by trying to make an SSH connection.  If the server cannot be reached, it'll send an SMS Message.

This is a blatant rip-off of Motoma's [elegantly simple monitoring script](http://motoma.io/basic-server-monitoring-with-python/) which I could have never put together myself.  I pulled out his emailer, and replaced it with the same pygooglevoice that is used in the [BFGMiner-SMSMonitor](https://github.com/Phraust/BFGMiner-SMSMonitor).

*I use this script as a cron job on a different server, to make sure that it's always up.  With my [BFGMiner-SMSMonitor](https://github.com/Phraust/BFGMiner-SMSMonitor) script, I've had issues where there would be a power failure, and the server would be down without me knowing about it.  This is my first stab at trying to fix that.*

REQUIREMENTS
------------

* Python (I'm using 2.7.5 on ArchLinux)
* [pygooglevoice](https://code.google.com/p/pygooglevoice/)
* [Google Voice Account](https://voice.google.com)

*[There is a fix](https://code.google.com/r/bwpayne-pygooglevoice-auth-fix/source/checkout) needed to get Google Voice working.*


SETUP
-----

Download the script wherever you want.

You can make it executable by running:

    chmod +x STATUS.py


RUNNING
-------

Just call it using either:

    python STATUS.py host:port phone-number

or:

    ./STATUS.py host:port phone-number
    
All you need to do is enter in the IP or HOSTNAME of the server you want to monitor, the port the service is running on, and the phone number you want texted.

If the host cannot be reached, you'll recieve a text message saying:

    HOST:PORT NEEDS HELP. :(
    
You can customize this on line 34 if you want.
