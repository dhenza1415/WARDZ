# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Silahakan ketik kode '" + pin + "' Pin kode sudah di kirim lewat silahkan cek di akun line anda")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='or scan this QR '
        else:
            notice=''
        self.callback('Silahkan loggin token \npaling lama 2 menit sbeleum hangus \n' + url + '\nEDITOR BY DHENZA')
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
