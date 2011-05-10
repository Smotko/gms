#!/usr/bin/python
import pygtk
pygtk.require("2.0")

import gtk
import appindicator

from threading import Thread

class AppIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator ("example-simple-client", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-new")
        self.ind.set_icon("distributor-logo")


        # create a menu
        self.menu = gtk.Menu()

        # create items for the menu - labels, checkboxes, radio buttons and images are supported:
        
        settings = gtk.MenuItem("Settings")
        settings.show()
        settings.connect("activate", self.settings)
        self.menu.append(settings)

        quit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        quit.connect("activate", self.quit)
        quit.show()
        self.menu.append(quit)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)
        
        self.bg = Thread(target=self.start_log)
        self.bg.start()

    def quit(self, widget, data=None):
        gtk.main_quit()
        
    def settings(self, widget, data=None):
        
        from settingsFrame import SettingsFrame
        
        SettingsFrame()
        
    def settings_start(self):
        from settingsFrame import SettingsFrame
        from wx import App
        app = App(False)
        frame = SettingsFrame(None, 'GMS Settings')
        app.MainLoop()
        
        
    def start_log(self):
        from gms import setup_hookers
        
        setup_hookers()
        
    def main(self):
        """
            This function starts GTK drawing the GUI and responding to events
            like button clicks
        """
 
        gtk.main()


def main():
    
    return 0

if __name__ == "__main__":
    indicator = AppIndicator()
    gtk.gdk.threads_init()
    gtk.gdk.threads_enter()
    indicator.main()    
    gtk.gdk.threads_leave()

