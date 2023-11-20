
input="503 723 961 899 766 482 237 104 62 234 491 763 924 913 762 483 212 98 76 248 514 515 702 845 901 845 640 381 156 83 130 362 600 838 972 930 744 442 185 65 246 505 715 815 699 426 121 49 125 359 610 817"

input = input.split(" ")
input = [int(i) for i in input]
import matplotlib.pyplot as plt
plt.plot(input)
plt.plot(input, 'ro')
plt.show()