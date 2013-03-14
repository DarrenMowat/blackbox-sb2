import sublime_plugin
import sublime
import urllib2 
import tempfile 
import shutil
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
    self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    # Tidy Up
    os.remove(temp_path)

  def tag_regions(self, edit, view):
    tag = '{-SPLIT-} '
    for region in view.sel():
      if not region.empty():
        view.insert(edit, region.begin(), tag)
    
    return None

class InsertTypeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Check if we can run blackbox on this machine
    if not can_run_blackbox(self.view):
      return
    # Check that the user has selected a pattern/patterns
    # Ensure the user has selected an argument to split
    selections = self.view.sel()
    if not selections:
      sublime.error_message("Please select a function to insert type line to")
      return       
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
    self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    # Tidy Up
    os.remove(temp_path)

  def tag_regions(self, edit, view):
    tag = ' {-TYPELINE-}'
    for region in view.sel():
      if not region.empty():
        view.insert(edit, region.end(), tag)
    
    return None

class InScopeTypeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Check if we can run blackbox on this machine
    if not can_run_blackbox(self.view):
      return
    # Check that the user has selected a pattern/patterns
    # Ensure the user has selected an argument to split
    selections = self.view.sel()
    if not selections:
      sublime.error_message("Please select a function to insert type line to")
      return       
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
    self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    # Tidy Up
    os.remove(temp_path)

  def tag_regions(self, edit, view):
    tag = ' {-SCOPETYPE-}'
    for region in view.sel():
      if not region.empty():
        view.insert(edit, region.end(), tag)
    
    return None

class InScopeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # Check if we can run blackbox on this machine
    if not can_run_blackbox(self.view):
      return
    # Check that the user has selected a pattern/patterns
    # Ensure the user has selected an argument to split
    selections = self.view.sel()
    if not selections:
      sublime.error_message("Please select a function to insert type line to")
      return       
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
    self.view.replace(edit, sublime.Region(0, self.view.size()), out)
    # Tidy Up
    os.remove(temp_path)

  def tag_regions(self, edit, view):
    tag = ' {-SCOPE-}'
    for region in view.sel():
      if not region.empty():
        view.insert(edit, region.end(), tag)
    
    return None
