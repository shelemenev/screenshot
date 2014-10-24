import os, ftplib, json, time

def config_default():
    f = open('config')
    config = json.loads(f.read())
    f.close()
    return lambda x: config[x]

def get_filename_from_time(timestamp):
    return lambda: 'screenshot-' + str(timestamp) + '.png'

def screen_gtk(filename):
    import gtk.gdk
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save(filename(),"png")

def screen_image_magic(filename):
    os.system("import -window root "+filename())

def upload_ftp(filename, config):
    ftp = ftplib.FTP(config('server'))
    ftp.login(config('login'), config('password'))
    ftp.cwd(config('upload_dir'))
    myfile = open(filename(), 'rb')
    ftp.storbinary('STOR ' + filename(), myfile)
    myfile.close()
    os.remove(filename())
    return config('url_prefix') + filename()

def screenshot(screen, upload):
    get_filename = get_filename_from_time(time.time())
    screen(get_filename)
    return upload(get_filename, config_default())
