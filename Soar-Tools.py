import sublime, sublime_plugin

# Basic build commands; just figure out the correct arguments to use
# and call the exec default plugin


# run soarunit on current file
class SoarunitOneFileCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        args = get_settings()
        args.append(sublime.active_window().active_view().file_name())
        run_soarunit(args)

# run all tests found in project
class SoarunitProjectCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        args = get_settings()
        import os.path
        project_file = sublime.active_window().project_file_name()
        args.extend(["--recursive", os.path.dirname(project_file)])
        run_soarunit(args)

def get_settings():
    settings = sublime.load_settings('Soar-Tools.sublime-settings')
    soarunit = settings.get('soarunit_path', 'soarunit')
    callargs = [soarunit]
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

    return callargs

def run_soarunit(args):
    sublime.active_window().run_command("exec", {
        "cmd": args,
        # also, Running test case '[^']+' from '([^']+)'
        # TODO: if SoarUnit updates output line number, update this too
        # github.com/soartech/jsoar/issues/103
        "file_regex": "Test Case: .* \\(([^)]+)\\)"
    })