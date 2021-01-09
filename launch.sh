#!/bin/bash

set -e

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------
roscore &
sleep 5
#rosrun my_package readbagfile.py
rosrun my_package bag2yaml.py
