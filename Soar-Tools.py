import sublime, sublime_plugin

class SoarunitOneFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        run_soarunit([self.view.file_name()])

# run all tests found in project
class SoarunitProjectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        import os.path
        file_name = sublime.active_window().project_file_name()
        run_soarunit(["--recursive", os.path.dirname(file_name)])

def run_soarunit(args):
    settings = sublime.load_settings('Soar-Tools.sublime-settings')
    jsoar = settings.get('soarunit_path', 'soarunit')
    callargs = [jsoar]
    if settings.get('ui', False):
        callargs.append('--ui')
    if settings.get('c_soar', False):
        callargs.append('--sml')
    if settings.has('SOAR_HOME'):
        import os
        os.environ["SOAR_HOME"] = settings.get('SOAR_HOME')
    if settings.has('threads'):
        threads = settings.get('threads')
        import re
        compiled = re.compile("^(\d+|cpus|cached)$")
        if not compiled.match(threads):
            sublime.error_message('"%s" is not a valid value for option "threads". Please check the documentation and fix your settings.' % threads)
            return
        else:
            callargs.extend(["--threads", threads])

    callargs.extend(args)
    sublime.set_timeout_async(lambda: run_in_background(callargs, None), 0)

# run the given args via the system shell, in the background, rerouting
# STDOUT to ST console.
def run_in_background(args, current_dir):
    import subprocess
    import platform
    startupinfo = None
    if platform.system() == 'Windows':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
    # from subprocess import Popen, PIPE
    # for whatever reason, we also PIPEing stderr leads to a freeze
    with subprocess.Popen(args, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, startupinfo=startupinfo) as proc:
        for line in proc.stdout:
            print(line, end='')
    # proc.wait() # don't bother waiting for exit
    return