"""
pages/__init__.py - Page classes package
"""

from .pagebase import PageBase
from .loginpage import LoginPage
from .dashboard import DashboardPage

__all__ = ["PageBase", "LoginPage", "DashboardPage"]