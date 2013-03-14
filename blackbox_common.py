
import os
import sublime
import subprocess
import tempfile


def can_run_blackbox(view): 
    log("Testing wether or not blackbox can be run on this machine")
    # We don't support running this plugin on windows yet
    if sublime.platform() == "windows":
      sublime.error_message("Unfortunately Windows is unsupported at this time.")
      return False
    # Make sure the user has the ghci binary installed
    if not which('ghci'):
      sublime.error_message("Please ensure you have ghci installed")
      return False  
    # Make sure the user has the blackbox binary installed
    if not which('/Users/darren/Library/Haskell/bin/cabal'):
      sublime.error_message("Please ensure you have cabal installed")
      return False       # Make sure the user has the blackbox binary installed
    if not which('/Users/darren/Library/Haskell/bin/blackbox'):
      sublime.error_message("Please ensure you have the blackbox binary installed. It can be installed via Cabal: `cabal install blackbox`")
      return False   
    # Ensure we have been passed haskell source
    syntax_file_for_view = view.settings().get('syntax').lower()
    if 'haskell' not in syntax_file_for_view:
        sublime.error_message("This plugin only works with Haskell source files")
        return False
    # We need the file to be saved to disk before we can work on it
    # This is required so a copy of the working directory can be made
    # So we can edit it on the fly. Fo example to plug errors
    file_name = view.file_name()
    if not file_name:
      sublime.error_message("Please save the file before continuing")
      return False      
    return True

def which(program):
    cmd = 'which ' + program 
    exit_code, out, err = call_and_wait(cmd)
    if exit_code == 0:
      return out.strip()
    return None

def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

def run_blackbox(infile, markupfile):
    blackbox = which('/Users/darren/Library/Haskell/bin/blackbox')
    cmd = blackbox + ' -f \'' + infile + '\' -m \'' + markupfile + '\''
    log("About to fork blackbox: " + cmd)
    exit_code, out, err = call_and_wait(cmd)
    log(exit_code)
    log(out)
    log(err)
    return exit_code, out, err

def call_and_wait(command):
    return call_and_wait_with_input(command, None)

def call_and_wait_with_input(command, input_string):
    # For the subprocess, extend the env PATH to include the 'add_to_PATH' setting.
    extended_env = dict(os.environ)
    PATH = os.getenv('PATH') or ""
    extended_env['PATH'] = PATH

    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        env=extended_env)
    stdout, stderr = process.communicate(input_string)
    exit_code = process.wait()
    return (exit_code, stdout, stderr)

def log(message):
    print(u'Blackbox: {0}'.format(message))
