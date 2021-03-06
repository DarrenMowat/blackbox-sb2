import sublime_plugin
import sublime
import tempfile 
import os

from blackbox_common import can_run_blackbox, run_blackbox, log


class SplitPatternsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Check if we can run blackbox on this machine
    if not can_run_blackbox(self.view):
      return
    # Check that the user has selected a pattern/patterns
    # Ensure the user has selected an argument to split
    selections = self.view.sel()
    if not selections:
      sublime.error_message("Please select an argument(s) to split")
      return       
    # Store the current viewport 
    vpos = self.view.viewport_position()
    # Start to modify the buffer
    self.tag_regions(edit, self.view)    
    # self.view.end_edit(edit)
    # Save this modified buffer as a temp file
    body = self.view.substr(sublime.Region(0, self.view.size()))
    temp_fd, temp_path = tempfile.mkstemp()
    os.write(temp_fd, body)
    os.close(temp_fd)
    # Run Blackbox
    exit_code, out, err = run_blackbox(self.view.file_name(), temp_path)
    if exit_code == 0: 
      self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    else:
      sublime.error_message("An error occurred: " + err)
      self.view.replace(edit, sublime.Region(0, self.view.size()), body)
    # Reset viewport
    self.view.set_viewport_position(vpos)
    # Tidy Up
    os.remove(temp_path)

  def tag_regions(self, edit, view):
    for region in view.sel():
      if not region.empty():
        view.insert(edit, region.begin(), '{-SPLIT-}')
    
    return None

class InsertTypeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if not can_run_blackbox(self.view):
      return
    selections = self.view.sel()
    if not selections:
      sublime.error_message("Please select a function to insert type line to")
      return       
    vpos = self.view.viewport_position()
    self.tag_regions(edit, self.view)    
    body = self.view.substr(sublime.Region(0, self.view.size()))
    temp_fd, temp_path = tempfile.mkstemp()
    os.write(temp_fd, body)
    os.close(temp_fd)
    exit_code, out, err = run_blackbox(self.view.file_name(), temp_path)
    if exit_code == 0: 
      self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    else:
      sublime.error_message("An error occurred: " + err)
      self.view.replace(edit, sublime.Region(0, self.view.size()), body)
    self.view.set_viewport_position(vpos)
    # Tidy Up
    os.remove(temp_path)

  def tag_regions(self, edit, view):
    for region in view.sel():
      if not region.empty():
        view.insert(edit, region.end(), '{-TYPELINE-}')
    
    return None

class InScopeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if not can_run_blackbox(self.view):
      return
    selections = self.view.sel()
    if not selections:
      sublime.error_message("Please highlight the binding right hand side of the expression you want to know the scope of")
      return       
    vpos = self.view.viewport_position()
    self.tag_regions(edit, self.view)    
    body = self.view.substr(sublime.Region(0, self.view.size()))
    temp_fd, temp_path = tempfile.mkstemp()
    os.write(temp_fd, body)
    os.close(temp_fd)
    exit_code, out, err = run_blackbox(self.view.file_name(), temp_path)
    if exit_code == 0: 
      self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    else:
      sublime.error_message("An error occurred: " + err)
      self.view.replace(edit, sublime.Region(0, self.view.size()), body)
    self.view.set_viewport_position(vpos)
    os.remove(temp_path)

  def tag_regions(self, edit, view):
    for region in view.sel():
      if not region.empty():
        view.insert(edit, region.begin(), '{-SCOPE-}')
    
    return None

class DummyProcessCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if not can_run_blackbox(self.view):
      return     
    vpos = self.view.viewport_position()
    body = self.view.substr(sublime.Region(0, self.view.size()))
    temp_fd, temp_path = tempfile.mkstemp()
    os.write(temp_fd, body)
    os.close(temp_fd)
    exit_code, out, err = run_blackbox(self.view.file_name(), temp_path)
    if exit_code == 0: 
      self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    else:
      sublime.error_message("An error occurred: " + err)
      self.view.replace(edit, sublime.Region(0, self.view.size()), body)
    self.view.set_viewport_position(vpos)
    os.remove(temp_path)
    return None

