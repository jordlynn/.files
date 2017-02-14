# -*- coding: utf-8 -*-
"""
Display system RAM and CPU utilization.

Configuration parameters:
    - format: output format string
    - high_threshold: percent to consider CPU or RAM usage as 'high load'
    - med_threshold: percent to consider CPU or RAM usage as 'medium load'

Format of status string placeholders:
    {cpu_temp}         - cpu temperature
    {cpu_usage}        - cpu usage percentage
    {mem_total}        - total memory
    {mem_used}         - used memory
    {mem_used_percent} - used memory percentage

NOTE: If using the {cpu_temp} option, the 'sensors' command should
be available, provided by the 'lm-sensors' or 'lm_sensors' package.

@author Shahin Azad <ishahinism at Gmail>, shrimpza
"""

import re
import subprocess
from time import time


class GetData:
    """
    Get system status
    """

    def execCMD(self, cmd, arg):
        """
        Take a system command and its argument, then return the result.

        Arguments:
        - `cmd`: system command.
        - `arg`: argument.
        """
        result = subprocess.check_output([cmd, arg])
        result = result.decode('utf-8')
        return result


    def memory(self):
        """
        Execute 'free -m' command, grab the memory capacity and used size
        then return; Memory size 'total_mem', Used_mem, and percentage
        of used memory.
        """
        # Run 'free -m' command and make a list from output.
        mem_data = self.execCMD('free', '-m').split()
        mem_index = mem_data.index('Mem:')
        total_mem = int(mem_data[mem_index + 1]) / 1024.
        used_mem = int(mem_data[mem_index + 2]) / 1024.

        # Caculate percentage
        used_mem_percent = int(used_mem / (total_mem / 100))

        # Results are in kilobyte.
        return total_mem, used_mem, used_mem_percent



class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 10
    format = "Mem: {mem_used}/{mem_total}, {mem_used_percent}%"
    high_threshold = 75
    med_threshold = 40

    def __init__(self):
        self.data = GetData()


    def sysData(self, i3s_output_list, i3s_config):
        # get RAM usage info
        mem_total, mem_used, mem_used_percent = self.data.memory()

        response = {
            'cached_until': time() + self.cache_timeout,
            'full_text': self.format.format(
                mem_used='%.2f' % mem_used,
                mem_total='%.2f' % mem_total,
                mem_used_percent='%.2f' % mem_used_percent,
            )
        }

        if mem_used_percent/100 <= self.med_threshold / 100.0:
            response['color'] = i3s_config['color_good']
        elif mem_used_percent/100 <= self.high_threshold / 100.0:
            response['color'] = i3s_config['color_degraded']
        else:
            response['color'] = i3s_config['color_bad']

        return response

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_bad': '#FF0000',
        'color_degraded': '#FFFF00',
        'color_good': '#9f9f9f',
    }

    while True:
        print(x.sysData([], config))
        sleep(1)