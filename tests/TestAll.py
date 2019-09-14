import os
directory = os.path.dirname(os.path.abspath(__file__))

print("-------------------- TestAll Started --------------------")

print("-------------------- Running MCEuroTest --------------------")
os.system('python {}/MCEuroTest.py'.format(directory))
print("-------------------- Running MCAmericanTest --------------------")
os.system('python {}/MCAmericanTest.py'.format(directory))
print("-------------------- Running PCATest --------------------")
os.system('python {}/PCATest.py'.format(directory))
print("-------------------- Running RegressionTest --------------------")
os.system('python {}/RegressionTest.py'.format(directory))
print("-------------------- Running ParabolicTest --------------------")
os.system('python {}/ParabolicTest.py'.format(directory))
print("-------------------- Running VannilaNetworkTest --------------------")
os.system('python {}/VannilaNetworkTest.py'.format(directory))

print("-------------------- TestAll Finished --------------------")