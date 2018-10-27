#!/usr/bin/env python3

"""
Author: Jakob Beckmann

Copyright 2018 ChainSecurity AG

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from . import command

class TruffleCommand(command.Command):
    """A command that uses the truffle development environment to compile the project."""
    def __init__(self, project_root):
        super().__init__(project_root)

    def compile_(self):
        print(f"Compiling using truffle in root {self.get_project_root()}")

    def report(self):
        print("Reporting using truffle")
