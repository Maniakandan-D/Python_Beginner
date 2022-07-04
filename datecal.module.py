import time

# print(time.gmtime(0))

# print(time.localtime())

# print(time.time())

from time import time as my_timer  # time function
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()
# strf stands for string from time can be used format local time tuple into more readable from according to a
# format string
print("Started at" + time.strftime("%X", time.localtime(start_time)))
print("Ended at" + time.strftime("%X", time.localtime(end_time)))  # %X local appropriate time representation

print("Your reaction time was {} seconds".format(end_time - start_time))
