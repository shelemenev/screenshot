import os
from screenshot.lib.screenshot import *

def main():
    config = config_default()
    if config('upload'):
        url = screenshot(screen_imagemagic, upload_ftp)
        os.system(config('browser') + ' ' + url)
    else:
        screenshot(screen_imagemagic, no_upload)

if __name__ == "__main__":
    main()
