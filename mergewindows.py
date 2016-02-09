import sublime
import sublime_plugin


class mergewindows(sublime_plugin.WindowCommand):
    def run(self):
        for wnd in sublime.windows():
            if wnd.window_id == self.window.window_id:
                continue

            for oldview in wnd.views():
                fname = oldview.file_name()
                vname = oldview.name()
                content = oldview.substr(sublime.Region(0, oldview.size()))

                if fname is not None:
                    newview = self.window.open_file(fname)
                else:
                    newview = self.window.new_file()
                    newview.set_name(vname)
                    newview.set_syntax_file(oldview.settings().get('syntax'))
                    newview.run_command('insert', {"characters": content})

                if oldview.is_dirty() and fname is not None:
                    newview.run_command('select_all')
                    newview.run_command('left_delete')
                    newview.run_command('insert', {"characters": content})

                oldview.set_scratch(True)
                oldview.close()
