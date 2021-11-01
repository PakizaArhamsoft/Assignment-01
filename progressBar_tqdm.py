import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

"""
    This program show the progressBar using tqdm
"""

class ProgressBar:
    def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None,
                 ncols=None, mininterval=0.1,maxinterval=10.0, miniters=None,
                 ascii=None, disable=False, unit='it', unit_scale=False,
                 dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                 position=None, postfix=None,
                 unit_divisor=1000, write_bytes=None, lock_args=None, nrows=None,
                 colour=None, delay=0, gui=False, **kwargs) -> None:
        self.iterable = iterable
        self.desc = desc
        self.total = total
        self.leave = leave
        self.file = file
        self.ncols = ncols
        self.mininterval = mininterval
        self.maxinterval = maxinterval
        self.miniters = miniters
        self.ascii = ascii
        self.disable = disable
        self.unit = unit
        self.unit_scale = unit_scale
        self.dynamic_ncols = dynamic_ncols
        self.smoothing = smoothing
        self.bar_format = bar_format
        self.initial = initial
        self.position = position
        self.postfix = postfix
        self.unit_divisor = unit_divisor
        self.write_bytes = write_bytes
        self.lock_args = lock_args
        self.nrows = nrows
        self.colour = colour
        self.delay = delay
        self.gui = gui

    def show_progressbar(self, iterable=None, desc=None, total=None, leave=True,
                         file=None, ncols=None, mininterval=0.1,maxinterval=10.0,
                         miniters=None, ascii=None, disable=False, unit='it', unit_scale=False,
                         dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                         position=None, postfix=None,unit_divisor=1000, write_bytes=None,
                         lock_args=None, nrows=None, colour=None, delay=0,
                         gui=False, **kwargs):
        self.iterable = iterable
        self.desc = desc
        self.total = total
        self.leave = leave
        self.file = file
        self.ncols = ncols
        self.mininterval = mininterval
        self.maxinterval = maxinterval
        self.miniters = miniters
        self.ascii = ascii
        self.disable = disable
        self.unit = unit
        self.unit_scale = unit_scale
        self.dynamic_ncols = dynamic_ncols
        self.smoothing = smoothing
        self.bar_format = bar_format
        self.initial = initial
        self.position = position
        self.postfix = postfix
        self.unit_divisor = unit_divisor
        self.write_bytes = write_bytes
        self.lock_args = lock_args
        self.nrows = nrows
        self.colour = colour
        self.delay = delay
        self.gui = gui
        return tqdm(self.iterable, self.desc, self.total, self.leave, self.file, self.ncols
                    , self.mininterval, self.maxinterval, self.miniters, self.ascii,
                    self.disable, self.unit, self.unit_scale, self.dynamic_ncols,
                    self.smoothing, self.bar_format, self.initial, self.position,
                    self.postfix, self.unit_divisor, self.write_bytes, self.lock_args,
                    self.nrows, self.colour, self.delay, self.gui)


if __name__ == '__main__':
    prog_bar = ProgressBar()
    try:
        for i in prog_bar.show_progressbar(iterable=range(2500), desc="Please wait to "
                                                                     "run the ProgressBar!!",total= None,
                                           leave=True, file=None, ncols=150, mininterval=5,
                                           maxinterval=0.1, miniters=10, ascii=None, disable=False,
                                           unit='it', unit_scale=False, dynamic_ncols=False,
                                           smoothing=0.3, bar_format=None, initial=0, position
                                           =None, postfix=None, unit_divisor=1000, write_bytes=None,
                                           lock_args=None, nrows=None, colour="yellow",
                                           delay=0, gui=False):
            time.sleep(.1)
        print("***Thanks for your time!!!***")
    except Exception as e:
        print("Error: ", e)

