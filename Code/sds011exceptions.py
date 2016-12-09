"""Moduel holding the exceptions for use in SDS011 class"""
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class WorkStateError(Error):
    """Exception raised for errors in the workingmode."""
    pass
class GetStatusError(Error):
    """Exception raised when initial getting the current sensor status won't work."""
    pass
class ReportModeError(Error):
    """Exception raised when sensor is in wrong reportmode for requested operation."""
    pass
