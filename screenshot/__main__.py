import os
from screenshot.lib.screenshot import *

def main():
    config = config_default()
    url = screenshot(screen_imagemagic, upload_ftp)
    os.system(config('browser') + ' ' + url)

if __name__ == "__main__":
    main()
