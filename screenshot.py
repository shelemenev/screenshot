import os, ftplib, json, time

class screenshot:
    config = {}
    filename = '';

    def __init__(self):
        f = open('config')
        self.config = json.loads(f.read())
        f.close()
        try:
            import gtk.gtk
            self.screen = self.screenGtk
        except ImportError:
            self.screen = self.screenImageMagic
        self.upload = self.uploadFTP

    def getFilename(self):
        self.filename = 'screenshot-' + str(time.time()) + '.png'
            
    def screenGtk(self):
        import gtk.gdk
        self.getFilename()
        w = gtk.gdk.get_default_root_window()
        sz = w.get_size()
        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
        pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
        if (pb != None):
            pb.save(self.filename,"png")

    def screenImageMagic(self):
        self.getFilename();
        os.system("import -window root "+self.filename)

    def uploadFTP(self):
        ftp = ftplib.FTP(self.config['ftp']['server'])
        ftp.login(self.config['ftp']['login'], self.config['ftp']['password'])
        ftp.cwd(self.config['ftp']['upload_dir'])
        myfile = open(self.filename, 'rb')
        ftp.storbinary('STOR ' + self.filename, myfile)
        myfile.close()
        os.remove(self.filename)
        print(self.config['ftp']['url_prefix'] + self.filename)

scr = screenshot()
scr.screen()
scr.upload()
