"""Utility & CLI functions"""  # pylint:disable-msg=C0415

import subprocess
import sys

import pylint
import pylint.lint


def exit_on_result(success: bool):
    return sys.exit(0) if success else sys.exit(1)


def run_lint():
    exit_on_result(pylint.lint.Run(["./2024"]) == pylint.ExitCode.OK)


def run_black(check_only: bool = True):
    args = ["black", "./"]
    if check_only:
        args.append("--check")
    return subprocess.run(args, check=False)


def run_isort(check_only: bool = True):
    args = ["isort", "."]
    if check_only:
        args.append("--diff")
    return subprocess.run(args, check=False)


def check_format():
    exit_on_result(run_black(check_only=True).returncode == 0)


def check_isort():
    exit_on_result(run_isort(check_only=True).returncode == 0)


def run_format():
    print("Running isort\n")
    run_isort(check_only=False)
    print("Running Black\n")
    exit_on_result(run_black(check_only=False).returncode == 0)
