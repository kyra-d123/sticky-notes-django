#!/usr/bin/env python3
"""Provide Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run administrative tasks for the Django project."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sticky_notes.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Confirm that it is installed and "
            "that the virtual environment is active."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()