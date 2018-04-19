#
# lebab.py
# Transforms codes to ES6 using Lebab
#
# Written by unibtc
# Copyright (c) 2018 Uni Sayo
#
# License: MIT 
# See LICENSE file in the project root for license information
#

import sublime, sublime_plugin
import platform
import os, sys, traceback
from subprocess import Popen, PIPE

PLUGIN_NAME = "LebabTransform"
SETTINGS_FILE = PLUGIN_NAME + ".sublime-settings"
BIN_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),"bin")
USER_OS = platform.system()


class LebabtransformCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:            
            transforms = get_pref("transforms",self.view)
            lebab_exec = get_lebab_exec()
            command = [lebab_exec, self.view.file_name(), "-o", self.view.file_name(), "--transform", ",".join(transforms)]            
            cdir = os.path.dirname(self.view.file_name())
            p = execute(command, cdir, self.view)
        except:
            # Something bad happened.
            # Print traceback on sublime's console
            traceback.print_exc()
            # Print and show the error message on sublime's error window
            sublime.error_message(str(sys.exc_info()[1]))

class LebabtransformEventListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        if (get_pref("format_on_save",view) and isJavascript(view)):
            view.window().run_command("lebabtransform")

def clear_status(view):
    view.window().destroy_output_panel("Lebab_Warning")

def show_status_msg(proc,view):
    clear_status(view)
    if(get_pref("show_warnings",view)):
        msg = proc.stderr.read()
        if(msg == ''):            
            return
        wnd = view.window()
        panel_view = wnd.create_output_panel("Lebab_Warning", True)
        wnd.run_command("show_panel", {"panel": "output.Lebab_Warning"})
        panel_view.set_read_only(False)
        panel_view.run_command('insert', {'characters': ''.join(msg.split('  '))})
        panel_view.set_read_only(True)
    else:
        print(proc.stdout.read())

def get_pref(key,view):
    global_settings = sublime.load_settings(SETTINGS_FILE)
    value = global_settings.get(key)
    
    project_settings = view.settings()

    if project_settings.has(PLUGIN_NAME):
        value = project_settings.get(PLUGIN_NAME).get(key, value)

    return value

def isJavascript(view):
    name = view.file_name()
    project_settings = view.settings()
    if (name and os.path.splitext(name)[1][1:] in ["js"]):
        return True

    syntax = project_settings.get("syntax")
    if (syntax and "javascript" in syntax.split("/")[-1].lower()):
        return True

    return False

def get_lebab_exec():
    platform = "win.exe" if (USER_OS == 'Windows') else USER_OS
    lebabexec = "lebab-" + platform.lower()
    lebab = os.path.join(BIN_DIR, lebabexec)
    print("Lebab executable is: " + lebab)
    return lebab

def execute(cmd, cdir, view):
    try:
        with Popen(cmd,stdout=PIPE, stdin=PIPE,
            stderr=PIPE, cwd=cdir, shell=USER_OS == 'Windows',universal_newlines=True) as proc:
            show_status_msg(proc,view)

    except OSError as e:
        raise Exception(e)



