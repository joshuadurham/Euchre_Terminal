import urwid
import main
class TextInput(urwid.Filler):
    
    def onKeyPress(self, size, key):
        if key != 'q':
            return super(TextInput, self).keypress(size, key)
        self.original_widget = urwid.Text(
            u"Nice to meet you,\n%s.\n\nPress Q to exit." %
            main.edit.edit_text)

     