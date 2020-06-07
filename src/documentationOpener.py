import webbrowser
import os

def openDocumentationFile():
    cwd = os.getcwd()
    webbrowser.open_new(cwd + "/src/doc/documentation.pdf")

