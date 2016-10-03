import os, ftplib, json, time

def config_default():
    f = open(os.path.expanduser('~') + '/.config/screenshot')
    config = json.loads(f.read())
    f.close()
    return lambda x: config[x]

def get_filename():
    return 'screenshot-' + str(time.time()) + '.png'

def screen_gtk(filename):
    import gtk.gdk
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    return (filename if pb!=None and (pb.save(filename, 'png') or True) else None)

def screen_imagemagic(filename):
    return (None if os.system("import -window root "+filename)>0 else filename)

def upload_ftp(filename, config):
    def perform_upload_ftp(filename, config):
        ftp = ftplib.FTP(config('server'))
        ftp.login(config('login'), config('password'))
        ftp.cwd(config('upload_dir'))
        myfile = open(filename, 'rb')
        ftp.storbinary('STOR ' + filename, myfile)
        myfile.close()
        os.remove(filename)
        return config('url_prefix') + filename
    return (perform_upload_ftp(filename, config) if filename!=None else None)

def screenshot(screen, upload):
    return upload(screen(get_filename()), config_default())
