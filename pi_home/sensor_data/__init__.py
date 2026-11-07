# this module will define and gather the raw sensor data from the CROWPI device.
# This module can be called to get and return data in a dict format for processing

from sensor_data.export import bulk_data as read

__all__ = ["read"]