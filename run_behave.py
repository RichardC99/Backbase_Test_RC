from behave.__main__ import main as behave_main
import sys

print("hack way of running behave, works if running under python 2.6")
features = "ControlPanel//features"
if len(sys.argv) > 1:
    features = features + "//" + sys.argv[1]
behave_main(features)
