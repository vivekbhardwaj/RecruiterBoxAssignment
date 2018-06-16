import unittest
import glob
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

test_file_strings = glob.glob('Test*.py')
module_strings = [str[0:len(str)-3] for str in test_file_strings]

for module in module_strings:
    mod = __import__(module)
    test_names =loader.getTestCaseNames(mod.Test)
    for test in test_names:
        suite.addTest(mod.Test(test,"chrome"))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner()
result = runner.run(suite)