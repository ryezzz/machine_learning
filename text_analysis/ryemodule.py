import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.externals import joblib

def lettersToNumbers (convert):
    convert = convert.lower()
    convert = convert.replace('a','1').replace('b','2').replace('c','3').replace('d','4').replace('e','5').replace('f','6').replace('g','7').replace('h','8').replace('i','9').replace('j','10').replace('k','11').replace('l','12').replace('m','13').replace('n','14').replace('o','15').replace('p','16').replace('q','17').replace('r','18').replace('s','19').replace('t','20').replace('u','21').replace('v','22').replace('w','23').replace('x','24').replace('y','25').replace('z','26')
    convert = ''.join(filter(lambda x: x.isdigit(), convert))
    convert = int(convert)
    return pd.to_numeric(convert)
#     return pd.to_numeric(convert, errors='coerce')


def removeLetters (convert):
    convert = convert.replace('a','1').replace('b','2').replace('c','3').replace('d','4')
    convert = ''.join(filter(lambda x: x.isdigit(), convert))
    return pd.to_numeric(convert)



def testType (test):
    print(type(test))