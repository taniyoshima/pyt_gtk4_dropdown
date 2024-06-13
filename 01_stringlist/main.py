import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


APPID = 'com.github.taniyoshima.dropdown'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

    @Gtk.Template.Callback()
    def on_selected(self, dropdown, selected):
        print(f"選択した番号: {dropdown.get_selected()}")
        print(f"選択した項目: {dropdown.get_selected_item().get_string()}")


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
