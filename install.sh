#!/bin/bash
TMPNAME=`pwd`
echo cd $TMPNAME > /usr/bin/screenshot
echo "URL=\`python start.py\`" >> /usr/bin/screenshot
echo "google-chrome-stable \$URL" >> /usr/bin/screenshot
chmod 755 /usr/bin/screenshot
