# This is a template file you can use to add Python code to a mode.

# To use it, and it to <your_machine>/modes/<your_mode>/code/<your_mode>.py

# Also, add a blank file called __init__.py to your machine folder root, and
# to your "modes" folder, and to your mode's "code" folder. (3 total)

# Also add a "code: your_mode.YourMode" (or whatever you call it) to the
# "mode:" section of your mode's <mode_name>.yaml configuration file.

from mpf.core.mode import Mode as m

class Custom(m):
    def mode_init(self):
        pass

    def mode_start(self, **kwargs):
        del kwargs

    def mode_stop(self, **kwargs):
        #self.machine.coils.c_kicker_gun.pulse()
        pass