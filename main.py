from shell import *
from display import *

home_dp()

while True:
    ish = input("-> ")
    if (ish == "exit"):
        print("期待与你的下次相见 (^ω^)  ")
        break
    shell(ish)