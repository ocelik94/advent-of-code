"""Utility & CLI functions"""  # pylint:disable-msg=C0415

import importlib.util
import subprocess
import sys
from glob import glob

import pylint
import pylint.lint


def exit_on_result(success: bool):
    """Shutdown with correct exit code"""
    return sys.exit(0) if success else sys.exit(1)


def run_lint():
    """run linting using pylint"""
    exit_on_result(pylint.lint.Run(["./2022"]) == pylint.ExitCode.OK)
    exit_on_result(pylint.lint.Run(["./2024"]) == pylint.ExitCode.OK)


def run_black(check_only: bool = True):
    """run black"""
    args = ["black", "./"]
    if check_only:
        args.append("--check")
    return subprocess.run(args, check=False)


def run_isort(check_only: bool = True):
    """run isort"""
    args = ["isort", "."]
    if check_only:
        args.append("--diff")
    return subprocess.run(args, check=False)


def check_format():
    """Invoke Black to check formatting"""
    exit_on_result(run_black(check_only=True).returncode == 0)


def check_isort():
    """Invoke Black to check formatting"""
    exit_on_result(run_isort(check_only=True).returncode == 0)


def run_format():
    """Invoke isort and Black to apply formatting"""
    print("Running isort\n")
    run_isort(check_only=False)
    print("Running Black\n")
    exit_on_result(run_black(check_only=False).returncode == 0)
