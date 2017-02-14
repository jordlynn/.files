# -*- coding: utf-8 -*-
"""
Display time as a "fuzzy" approximation.

Will not display exact time but rather a quick phrase.

Configuration parameters:
    - cache_timeout : How often you want time to update. 30 sec by default.

@author Jordan Lynn snake.river52@gmail.com
@license BSD
"""

import time


class Py3status:

    # available configuration parameters
    cache_timeout = 300
    
    def __init__(self):
        pass

    def kill(self, i3s_output_list, i3s_config):
        """
        This method will be called upon py3status exit.
        """
        pass

    def on_click(self, i3s_output_list, i3s_config, event):
        pass
        

    def oTime(self, i3s_output_list, i3s_config):
        currTimeStruct = time.localtime()
        phrase = ""
        hour = int(time.strftime("%-I"))
        minute = currTimeStruct[4]

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
