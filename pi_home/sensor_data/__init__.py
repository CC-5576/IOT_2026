# this module will define and gather the raw sensor data from the CROWPI device.
# This module can be called to get and return data in a dict format for processing
import RPi.GPIO as gp

from ._export import bulk_data as read
from ._button import window
from ._hts import HumidTemp
from ._motion import motion
from ._sonic import sonics
from ._sound import sound

gp.setmode(gp.BCM)

__all__ = ["window", "HumidTemp", "motion", "sonics", "sound"]
