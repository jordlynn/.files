# -*- coding: utf-8 -*-

# This is an example module to be used as a template.
# See https://github.com/ultrabug/py3status/wiki/Write-your-own-modules
# for more details.
#
# NOTE: py3status will NOT execute:
#     - methods starting with '_'
#     - methods decorated by @property and @staticmethod
#
# NOTE: reserved method names:
#     - 'kill' method for py3status exit notification
#     - 'on_click' method for click events from i3bar (read below please)
#
# WARNING:
#
# Do NOT use print on your modules: py3status will catch any output and discard
# it silently because this would break your i3bar (see issue #20 for details).
# Make sure you catch any output from any external program you may call
# from your module. Any output from an external program cannot be caught and
# silenced by py3status and will break your i3bar so please, redirect any
# stdout/stderr to /dev/null for example (see issue #20 for details).
#
# CONTRIBUTORS:
#
# Contributors are kindly requested to agree to contribute their code under
# the BSD license to match py3status' one.
#
# Any contributor to this module should add his/her name to the @author
# line, comma separated.
#
# DOCSTRING:
#
# Fill in the following docstring: it will be parsed by py3status to document
# your module from the CLI.
"""
Quicly display time

Will not display exact time ifyouknowwhatImean.

Configuration parameters:
    - cache_timeout : 300

@author Jordan Lynn snake.river52@gmail.com
@license BSD
"""

# import your useful libs here
import time


class Py3status:
    """
    The Py3status class name is mendatory.

    Below you list all the available configuration parameters and their
    default value for your module which can be overwritten by users
    directly from their i3status config.

    This examples features only one parameter which is 'cache_timeout'
    and is set to 10 seconds (0 would mean no cache).
    """
    # available configuration parameters
    cache_timeout = 300

    def __init__(self):
        """
        This is the class constructor which will be executed once.
        """
        pass

    def kill(self, i3s_output_list, i3s_config):
        """
        This method will be called upon py3status exit.
        """
        pass

    def on_click(self, i3s_output_list, i3s_config, event):
        """
        This method should only be used for ADVANCED and very specific usages.

        Read the 'Handle click events directly from your i3status config'
        article from the py3status wiki:
            https://github.com/ultrabug/py3status/wiki/

        This method will be called when a click event occurs on this module's
        output on the i3bar.

        Example 'event' json object:
        {'y': 13, 'x': 17, 'button': 1, 'name': 'example', 'instance': 'first'}
        """
        pass

    def oTime(self, i3s_output_list, i3s_config):
        currTimeStruct = time.localtime()
        phrase = ""
        hour = int(time.strftime("%-I"))
        minute = 3

        if minute <= 2:
            phrase = str(hour) + " o'clock"

        elif 3 <= minute <= 7:
            phrase = "five past " + str(hour)

        elif 8 <= minute <= 11:
            phrase = "ten past " + str(hour)

        elif 12 <= minute <= 17:
            phrase = "quarter after " + str(hour)

        elif 18 <= minute <= 21:
            phrase = "twenty past " + str(hour)

        elif 22 <= minute <= 36:
            phrase = "half past " + str(hour)

        elif 37 <= minute <= 40:
            phrase = "fourty past " + str(hour)

        elif 41 <= minute <= 49:
            hour += 1
            phrase = "quarter to " + str(hour)

        elif 50 <= minute <= 53:
            hour += 1
            phrase = "ten to " + str(hour)

        elif 54 <= minute:
            hour +=1
            phrase = "five to " + str(hour)


        elif minute >= 50:
            hour += 1
            phrase = "almost " + str(hour)
        else:
            phrase = "time exception!"

        response = {
            #'cached_until': time() + self.cache_timeout,
            'full_text': ''.join(phrase)
        }
        return response

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    This SHOULD work before contributing your module please.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_bad': '#FF0000',
        'color_degraded': '#FFFF00',
        'color_good': '#00FF00'
    }
    while True:
        print(x.oTime([], config))
        sleep(180)
