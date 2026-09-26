"""
pages/__init__.py - Page classes package
"""

from .basepage import BasePage
from .login import LoginPage
from .dashboard import DashboardPage

__all__ = ["BasePage", "LoginPage", "DashboardPage"]