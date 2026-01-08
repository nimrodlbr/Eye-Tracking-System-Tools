"""
Eye-tracking preprocessing module.

This module provides tools for synchronizing eye-tracking data with arena videos
and Open Ephys recordings.
"""

from .BlockSync_class import BlockSync
from .OERecording import OERecording

__all__ = ['BlockSync', 'OERecording']
