import time
from tqdm import tqdm

for i in tqdm(range(2500), ncols=150, desc="Please wait to run the ProgressBar!!", initial=5, miniters=10, colour="yellow"):
    time.sleep(.1)

print("***Thanks for your time!!!***")