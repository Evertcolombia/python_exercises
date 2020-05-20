from scipy import stats
import numpy as np

# Calculate CORRELATION between two data

array_1 = np.array([1, 2, 3, 4, 5, 6]) # create a numpy array
array_2 = array_1

print(stats.pearsonr(array_1, array_2))

# Normal distribuition
""" La distribución normal es una que es simétrica alrededor
de la media y para la cual los valores más cercanos a la media
son más comunes. Es la distribución estándar de la "curva de campana".

Say you needed to generate data from a normal distribution
with a mean of 0 and a standard deviation of 10;
here is how you would do that:"""

x = stats.norm.rvs(loc=0, scale=10, size=10)  # Generate 10 values randomly sampled from a normal distribution with mean 0 and standard deviation of 10

print(x)

# Probability density function 

"""Another common operation on distributions is to
calculate the probability density function. This function
will give you the relative likelihood that you would
sample a particular value. Let’s look at a few:"""
# ensena probabilidad relativa de que muestre un valor determinado
p1 = stats.norm.pdf(x=-100, loc=0, scale=10)  # Get probability of sampling a value of -100
p2 = stats.norm.pdf(x=0, loc=0, scale=10)     # Get probability of sampling a value of 0

print(p1)
print(p2)

# Cumulative distribution function 
"""Another common calculation is the cumulative distribution 
function, the probability of sampling a value less 
than or equal to x."""

p1 = stats.norm.cdf(x=0, loc=0, scale=10)  # Get probability of sampling a value less than or equal to 0

print(p1)


""" calculates some functions of 
numpy library"""
import numpy as np

def perform_calculations(array):
  nparray = np.array(array)
  _max = np.max(nparray)
  std_deviation = np.std(nparray)
  _sum = np.sum(nparray)
  dot = np.dot(nparray, nparray)

  return _max, std_deviation, _sum, dot # Replace with max, std, sum, and dot product