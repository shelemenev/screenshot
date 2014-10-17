#!/bin/bash
TMPNAME=`pwd`
echo cd $TMPNAME > /usr/bin/screenshot
echo "URL=\`python screenshot.py\`" >> /usr/bin/screenshot
echo "firefox \$URL" >> /usr/bin/screenshot
chmod 755 /usr/bin/screenshot
