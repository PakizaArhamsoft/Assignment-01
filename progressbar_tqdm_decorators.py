import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

"""
    This program show the progressBar using tqdm with decorator function
"""

## decorator function
def show_progressbar(func):
        def inner(iterable=None, desc=None, total=None, leave=True,
                  file=None, ncols=None, mininterval=0.1,maxinterval=10.0,
                  miniters=None, ascii=None, disable=False, unit='it', unit_scale=False,
                  dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                  position=None, postfix=None,unit_divisor=1000, write_bytes=None,
                  lock_args=None, nrows=None, colour=None, delay=0,
                  gui=False, **kwargs):
            iterable = iterable
            desc = desc
            total = total
            leave = leave
            file = file
            ncols = ncols
            mininterval = mininterval
            maxinterval = maxinterval
            miniters = miniters
            ascii = ascii
            disable = disable
            unit = unit
            unit_scale = unit_scale
            dynamic_ncols = dynamic_ncols
            smoothing = smoothing
            bar_format = bar_format
            initial = initial
            position = position
            postfix = postfix
            unit_divisor = unit_divisor
            write_bytes = write_bytes
            lock_args = lock_args
            nrows = nrows
            colour = colour
            delay = delay
            gui = gui
            return func(iterable, desc, total, leave, file, ncols, mininterval, maxinterval,
                        miniters, ascii, disable, unit, unit_scale, dynamic_ncols, smoothing,
                        bar_format, initial, position, postfix, unit_divisor, write_bytes, lock_args,
                        nrows, colour, delay, gui)
        return inner


if __name__ == '__main__':
    def prog_bar(iterable=range(2500), desc="Please wait to  run the "
                                            "ProgressBar!!", total=None, leave=True,
                 file=None, ncols=150, mininterval=5,
                 maxinterval=0.1, miniters=10, ascii=None, disable=False, unit='it',
                 unit_scale=False, dynamic_ncols=False, smoothing=0.3, bar_format=None,
                 initial=0, position=None, postfix=None, unit_divisor=1000, write_bytes=None,
                 lock_args=None, nrows=None, colour="yellow", delay=0, gui=False):
        for i in tqdm(iterable=iterable, desc=desc, ncols=ncols, mininterval=mininterval,
                      maxinterval=maxinterval,
                      miniters=miniters, unit=unit,  colour=colour):
            time.sleep(.1)

    prog_bar = show_progressbar(prog_bar)

    print("""
    Enter the tqdm parameters while you want......
    If you want to add press 'y' ,otherwise enter 'n'
    """)
    option = input("Want to add? ")
    parameters = []
    while option.casefold() == 'y':
        # parameters are e.g: iterable=range(2500), desc="Please wait to "
        #                               "run the ProgressBar!!", ncols=150, mininterval=5,
        #             maxinterval=0.1, miniters=10, unit='it', colour="yellow"
        parameters .append(input("Enter parameter: "))      
        option = input("Want to add? ")
        
    prog_bar(parameters)
    print("***Thanks for your time!!!***")

