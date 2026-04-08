# sample_action.py - A custom action plugin for Ansible.
# Author: Your Name
# License: GPL-3.0-or-later
# pylint: disable=E0401

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.plugins.action import ActionBase  # type: ignore


class ActionModule(ActionBase):  # type: ignore[misc]
    """
    Custom Ansible action plugin: sample_action
    A custom action plugin for Ansible.
    """

    def run(
        self,
        tmp=None,
        task_vars=None,
    ):
        """
        Executes the action plugin.

        Args:
            tmp: Temporary path provided by Ansible for the module execution. Defaults to None.
            task_vars: Dictionary of task variables available to the plugin. Defaults to None.

        Returns:
            dict: Result of the action plugin execution.
        """
        if task_vars is None:
            task_vars = {}

        result = super(ActionModule, self).run(tmp, task_vars)
        result.setdefault("changed", False)
        return result
