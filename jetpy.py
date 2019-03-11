"""
Utility modul
"""
import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
import Autodesk
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *

import System
from System.Collections.Generic import *

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)


class _custom_exception(Exception):
    """ My Exeption """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def raise_error(message, theme = "Title"):
	messagePop = TaskDialog(theme)
	messagePop.MainContent = message
	messagePop.Show()
	raise _custom_exception(message)
