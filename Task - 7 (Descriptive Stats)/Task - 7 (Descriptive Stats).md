![image.png](attachment:image.png)

<div style="text-align: right"> $ \large \rightarrow \text{V Adithya Sai} $ </div>

### <b>Hi! Guys :) Today Lets Learn about <font color='blue'>Descriptive Stats</font> and About <font color='blue'>Latex</font> in this Tutorial</b>

## <font color = 'blue'>In Descriptive Stats We Deal & Discuss With </font>
1. Mean
2. Median
3. Mode
4. Variance
5. Standard Deviation
6. Correlation
7. Normal Distribution
8. Feature of Normal Distribution
9. Positively Skewed & Negatively Skewed Normal Distribution
10. Effect on Mean, Median and Mode due to Skewness
11. Explain QQ Plot and show the implementation of the same
12. Explain Box Cox and show the implementation of the same

### What is the use of <font color='blue'>Latex</font> and What it is?
from the Question Itself we can Say What it is, in Question we kept <font color='blue'>Question Mark '?'</font>, but 
what if we want to place the symbols like <font color='blue'>Mod, Delta, Ohm, Sigma</font> weather all these symbols available in keyboard.
No Absolutley Not Present in the Keyboard, there we deal with Latex for Placing those Symbols.

## <font color = 'red'> Ok! Let's See starting from the Descrptive Stats</font>

## <font color = 'Green'>Mean, Median and Mode are called as Measures of Central Tendency</font>

## <font color = 'blue'> 1. <u>Mean</u>: </font>
           Mean is a Descriptive Stat that Looks at the Average Value of the Data or Dataset. Most People Understand it
    as Average

How Is the Mean Calculated:
    $ \LARGE \bar{X} / \mu_x \ $ $ \Large = $ $ \ $ $ \LARGE \frac{\sum_{k=1}^{n}X}{N}$ $ \ \ \ $ $ \Huge \Rightarrow $ $ \ \ \ $ $ \Large \frac{SUM \ \ OF \ \ ALL \ \ VALUES}{TOTAL \ \ NUMBER \ \ OF \ \ VALUES} $

 ## <b> Let's see Example For Mean With and With out Using Libary Function </b> <br>
 ## With using Libary Function


```python
import numpy as np
import pandas as pd
df = pd.read_csv('data.csv')
df.head(n=3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mthly_HH_Income</th>
      <th>Mthly_HH_Expense</th>
      <th>No_of_Fly_Members</th>
      <th>Emi_or_Rent_Amt</th>
      <th>Annual_HH_Income</th>
      <th>Highest_Qualified_Member</th>
      <th>No_of_Earning_Members</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5000</td>
      <td>8000</td>
      <td>3</td>
      <td>2000</td>
      <td>64200</td>
      <td>Under-Graduate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6000</td>
      <td>7000</td>
      <td>2</td>
      <td>3000</td>
      <td>79920</td>
      <td>Illiterate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10000</td>
      <td>4500</td>
      <td>2</td>
      <td>0</td>
      <td>112800</td>
      <td>Under-Graduate</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
income = df['Mthly_HH_Income'].values
income
```




    array([  5000,   6000,  10000,  10000,  12500,  14000,  15000,  18000,
            19000,  20000,  20000,  22000,  23400,  24000,  24000,  25000,
            25000,  25000,  29000,  30000,  30500,  32000,  34000,  34000,
            35000,  35000,  39000,  40000,  42000,  43000,  45000,  45000,
            45000,  45000,  46000,  47000,  50000,  50500,  55000,  60000,
            60000,  65000,  70000,  80000,  85000,  90000,  98000, 100000,
           100000, 100000], dtype=int64)




```python
mean_income = np.mean(income)
print(' mean_income with Using Numpy Library function is ------ {}  '.format(mean_income))
```

     mean_income with Using Numpy Library function is ------ 41558.0  
    


```python
import statistics
smean = statistics.mean(income)
print(' mean_income with Using Statistics Library function is ------ {}  '.format(smean))
```

     mean_income with Using Statistics Library function is ------ 41558  
    

## With out using Library Function


```python
n = df.shape[0]
n
```




    50




```python
def mean(a,b):
    return a/b
sum = 0
for i in range(n):
    sum += df['Mthly_HH_Income'][i]
print('mean_income with Out Using Library function is ------ {}  '.format(mean(sum,n)))
```

    mean_income with Out Using Library function is ------ 41558.0  
    

##### $ \rightarrow $ HENCE WE CAN SEE THAT MEAN VALUE OF INCOME WITH AND WITH USING LIBRARY FUNCTION IS SAME

## <font color = 'blue'> 2. <u>Median</u>: </font>
       The Next Measure of Central Tendency is Median. Median also used to define the typical value in the data or dataset.
    but unlike mean it does not require any Calculation, we need to arrange all our data in asscending order. Then median 
    is the data that coincides with the middle of the data. if there are even number of data we take the mean of the middle 
    two values.


## Median is Calculated from: 

 $ \ \ \ $ $ \Huge \tilde x $ $ \Large = $ $ \Huge \frac{n+1}{2}$$ \Large ^{term}$ $ \Large \rightarrow \ for \ Odd \ Number \ of \ Observations $

$ \ \ $$ \ \ $$ \ \ $$ \ \ $$ \ \ $ $ \Large = $ $ \Huge ( $ $ \Huge ( $ $ \Huge \frac{n}{2} $$ \Huge ) $$ + $$ \Huge ( $$ \Huge \frac{n}{2}+1$ $ \Huge ) $$ \Huge ) $$\Huge /2$ $ \Large ^{term}$ $ \Large \rightarrow \ for \ Even \ Number \ of \ Observations $

![image.png](attachment:image.png)

 ## <b> Let's see Example For Median With and With out Using Libary Function </b> <br>
 ## With using Libary Function


```python
df.head(n=3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mthly_HH_Income</th>
      <th>Mthly_HH_Expense</th>
      <th>No_of_Fly_Members</th>
      <th>Emi_or_Rent_Amt</th>
      <th>Annual_HH_Income</th>
      <th>Highest_Qualified_Member</th>
      <th>No_of_Earning_Members</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5000</td>
      <td>8000</td>
      <td>3</td>
      <td>2000</td>
      <td>64200</td>
      <td>Under-Graduate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6000</td>
      <td>7000</td>
      <td>2</td>
      <td>3000</td>
      <td>79920</td>
      <td>Illiterate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10000</td>
      <td>4500</td>
      <td>2</td>
      <td>0</td>
      <td>112800</td>
      <td>Under-Graduate</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
med = df['Mthly_HH_Income'].values
```


```python
median_income = np.median(med)
print(' median_income with Using Library function is ------ {} '.format(median_income))
```

     median_income with Using Library function is ------ 35000.0 
    


```python
smedian = statistics.median(med)
print(' median_income with Using Library function is ------ {} '.format(smedian))
```

     median_income with Using Library function is ------ 35000.0 
    

## With Out using Libary Function


```python
n = df.shape[0]
ls =[]
for i in range(n):
    ls.append(df['Mthly_HH_Income'][i])
ls.sort()
if n%2 != 0:
    median = (ls[int(n/2)] + ls[int(n/2)+1])/2
else:
    median = ls[int(n/2)]
    
print('median_income with Using Library function is ------ {} '.format(float(median)))
```

    median_income with Using Library function is ------ 35000.0 
    

## <font color = 'blue'> 3. <u>Mode</u>: </font>
        The Last measure of central tendency is Mode. Mode is Defined as the value that occur Most frequently in our data. 
    if a Value Appear Repeatedly throughout the data it may influence the average towards the model value. the more the 
    value repeated in the data, the more it will influence the mean. thus mode represents the highest weighted factor to 
    mean. like median there is no Built in function for mode, but we can find it by counting the Occurences of the value.

![image.png](attachment:image.png)

##   $ \ $ $ \ $$ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $$ \ $ $ \ $  $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $$ \ $ $ \ $  $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \Large \downarrow $

##   $ \ $ $ \ $$ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $$ \ $ $ \ $  $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $$ \ $ $ \ $  $ \ $ $ \ $ $ \ $ $ \ $ $ \ $  $ \Large Mode = 67 $

## Let's see Example For Median With and With out Using Libary Function
## Lets Find out the mode for Highest_Qualified_Member Column in the Above Data


```python
df.head(n=2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mthly_HH_Income</th>
      <th>Mthly_HH_Expense</th>
      <th>No_of_Fly_Members</th>
      <th>Emi_or_Rent_Amt</th>
      <th>Annual_HH_Income</th>
      <th>Highest_Qualified_Member</th>
      <th>No_of_Earning_Members</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5000</td>
      <td>8000</td>
      <td>3</td>
      <td>2000</td>
      <td>64200</td>
      <td>Under-Graduate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6000</td>
      <td>7000</td>
      <td>2</td>
      <td>3000</td>
      <td>79920</td>
      <td>Illiterate</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
md = df['Highest_Qualified_Member'].values
```

## With using Libary Function


```python
import statistics 
smode = statistics.mode(md)
print('Mode Value with Using Library function is ------ {} '.format(smode))
```

    Mode Value with Using Library function is ------ Graduate 
    

## With Out Using Library Function


```python
n = df.shape[0]
ls =[]
for i in range(n):
    ls.append(df['Highest_Qualified_Member'][i])
mode = max(ls, key = ls.count)
print('Mode Value with Out Using Library function is ------ {} '.format(mode))
```

    Mode Value with Out Using Library function is ------ Graduate 
    

## <font color = 'Green'> Variance and Standard Deviation are called Measure of Spread</font>

## <font color = 'blue'> 4. <u>Variance</u>: </font>
            Variance is the Square of the Average Distance Between Each Quantity and the mean. It is a Square of
    Standard Deviation. it also defined as how far individual values in data from the mean or average.
    
$ \normalsize \rightarrow  \ High \ variance \ tells \ that \ the \ values \ in \ our \ data \ are \ far \ from \ the \ mean \ or \ Average $
$ \normalsize \rightarrow  \ Low \ variance \ tells \ that \ the \ values \ in \ our \ data \ are \ quite \ near \ to \ the \ mean \ or \ Average $

$ \Large \rightarrow \ variance \ is \ denoted \ By \ (S.D)^2 $ $ \Large = $ $ \Large (\sigma)^2 $ 

$ \Large \rightarrow  \ were \ ( \sigma ) \ is \ Standard \ Deviation $

$ \Large \rightarrow \ Formulea \ Of \  (\sigma)^2  = \frac{\sum (X - \mu)^2}{N} =  \frac{\sum X^2}{N} - \mu^2 $

  $ \ $ $ \ $  $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ $ $ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \Large were \ \ \ \mu = \frac{\sum X}{N} $

## Let's see Example For Variance With and With out Using Libary Function

## With Using Library Function


```python
import numpy as np
import statistics as stat
```


```python
# let's find the variance for 'Mthly_HH_Income' in our data 

vare = df['Mthly_HH_Income'].values
nvar = np.var(vare)
print('Variance with Using Library function is ------ {} '.format(nvar))
```

    Variance with Using Library function is ------ 667478836.0 
    


```python
svar = stat.pvariance(vare)
print('Variance with Using Library function is ------ {} '.format(svar))
```

    Variance with Using Library function is ------ 667478836 
    

## With out using Library Function


```python
n = df.shape[0]
ls = []
for i in range(n):
    ls.append(df['Mthly_HH_Income'][i])
def sum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
        
def var(a):
    mean = sum(a)/len(a)
    deviations = [(x - mean) ** 2 for x in a]
    variance = sum(deviations)/len(a)
    return variance
print('Variance with Out Using Library function is ------ {} '.format(var(ls)))
```

    Variance with Out Using Library function is ------ 667478836.0 
    

## <font color = 'blue'> 5. <u> Standard Deviation</u>: </font>
                The Standard deviation measures the amount of variation or dispersion of a set of numeric values. standard
    deviation is the square root of variance. if we want to calculate the standard deviation, then all we just have to 
    do is to take the square root of Variance

 $ \Large \rightarrow \ Standard \ Deviation \ is \ denoted \ as \  (\sigma) \ $

$ \Large \rightarrow $ $ \ \ \ $ $ \ \ \ $$ \ \ \ $$ \ \ \ $ $ \Large Were  \  (\sigma) = \sqrt{Variance} = \sqrt{\sigma^2} $

$ \Large \rightarrow $ $ \ \ \ $ $ \ \ \ $$ \ \ \ $$ \ \ \ $ $ \Huge \sigma = \sqrt{\frac{\sum (X - \mu)^2}{N}} $

## Let's see Example For Standard Deviation With and With out Using Libary Function

## With Using Library Function


```python
import numpy as np
import statistics as stat
```


```python
# Let's find the standard deviation for 'Mthly_HH_Expense' column in our data
st = df['Mthly_HH_Expense'].values
nst = np.std(st)
print('standard deviation with Using Library function is ------ {} '.format(nst))
```

    standard deviation with Using Library function is ------ 11968.704023410388 
    


```python
sst = stat.pstdev(st)
print('standard deviation with Using Library function is ------ {} '.format(sst))
```

    standard deviation with Using Library function is ------ 11968.704023410388 
    

## With out using Library Function


```python
n = df.shape[0]
ls = []
for i in range(n):
    ls.append(df['Mthly_HH_Expense'][i])
def sum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
        
def var(a):
    mean = sum(a)/len(a)
    deviations = [(x - mean) ** 2 for x in a]
    variance = sum(deviations)/len(a)
    return variance
def sroot(a):
    return a**(1/2)
stde = sroot(var(ls))
print('standard deviation with out Using Library function is ------ {} '.format(stde))
```

    standard deviation with out Using Library function is ------ 11968.704023410388 
    


```python
def std_deviation(data):
    length=len(data)
    sum_of_data=sum(data)
    mean=sum_of_data/length
    su=0
    for i in data:
        sum_square=(i-mean)**2
        su+=sum_square
    return (su/length)**(1/2)
print('standard deviation with out Using Library function is ------ {} '.format(std_deviation(ls)))
```

    standard deviation with out Using Library function is ------ 11968.704023410388 
    

## <font color = 'blue'> 6. <u>Correlation</u>: </font>
                A correlation is a statistical measure of the relationship between two variables. The measure is best 
    used in variables that demonstrate a linear relationship between each other. The fit of the data can be visually 
    represented in a scatterplot. Using a scatterplot, we can generally assess the relationship between the variables
    and determine whether they are correlated or not.
    
    The correlation coefficient is a value that indicates the strength of the relationship between variables. The 
    coefficient can take any values from -1 to 1. The interpretations of the values are:

 

$ \large \rightarrow \  -1 \ : \ Perfect \ negative \ correlation. \ The \ variables \ tend \ to \ move \ in \ opposite \ directions. $
$ \large \rightarrow \  0 \ : \ No \ correlation. \ The \ variables \ do \ not \ have \ a \ relationship \ with \ each \ other. $
$ \large \rightarrow \  +1 \ : \ Perfect \ positive \ correlation. \ The \ variables \ tend \ to \ move \ in \ the \ same \ direction. $

### Correlation can be found with this:

$ \Large \ Correlation \ between \ two \ Features \ is \ \ \ \LARGE r_{xy} = \frac{\sum_{i}(X_{i} - \bar X)(Y_{i} - \bar Y)}{\sqrt{\sum_{i}(X_{i} - \bar X)^2\sum_{i}(Y_{i} - \bar Y)^2}} $

$ \ $$ \ $ $ \Large \ were $ <br>
<center> $ \large \ r_{xy} \rightarrow \ correlation \ between \ features \ x \ and \ y $ </center><br>
<center> $ \large \ X_i \rightarrow \ Values \ of \ X variable \ in \ Sample $ </center> <br>
<center> $ \large \ \bar X \rightarrow \ Mean \ of \ values \ of \ X variable $ </center> <br>
<center> $ \large \ Y_i \rightarrow \ Values \ of \ Y variable \ in \ Sample $ </center> <br>
<center> $ \large \ \bar Y \rightarrow \ Mean \ of \ values \ of \ Y variable $ </center>

## Let's see Example For Correlation with and with out Library Function
### With Library Function and scatter plot


```python
df.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mthly_HH_Income</th>
      <th>Mthly_HH_Expense</th>
      <th>No_of_Fly_Members</th>
      <th>Emi_or_Rent_Amt</th>
      <th>Annual_HH_Income</th>
      <th>No_of_Earning_Members</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mthly_HH_Income</th>
      <td>1.000000</td>
      <td>0.649215</td>
      <td>0.448317</td>
      <td>0.036976</td>
      <td>0.970315</td>
      <td>0.347883</td>
    </tr>
    <tr>
      <th>Mthly_HH_Expense</th>
      <td>0.649215</td>
      <td>1.000000</td>
      <td>0.639702</td>
      <td>0.405280</td>
      <td>0.591222</td>
      <td>0.311915</td>
    </tr>
    <tr>
      <th>No_of_Fly_Members</th>
      <td>0.448317</td>
      <td>0.639702</td>
      <td>1.000000</td>
      <td>0.085808</td>
      <td>0.430868</td>
      <td>0.597482</td>
    </tr>
    <tr>
      <th>Emi_or_Rent_Amt</th>
      <td>0.036976</td>
      <td>0.405280</td>
      <td>0.085808</td>
      <td>1.000000</td>
      <td>0.002716</td>
      <td>-0.097431</td>
    </tr>
    <tr>
      <th>Annual_HH_Income</th>
      <td>0.970315</td>
      <td>0.591222</td>
      <td>0.430868</td>
      <td>0.002716</td>
      <td>1.000000</td>
      <td>0.296679</td>
    </tr>
    <tr>
      <th>No_of_Earning_Members</th>
      <td>0.347883</td>
      <td>0.311915</td>
      <td>0.597482</td>
      <td>-0.097431</td>
      <td>0.296679</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



$ \rightarrow $ Let's find the Correlation between 'Mthly_HH_Income' and 'Annual_HH_Income'


```python
np.corrcoef(df['Mthly_HH_Income'], df['Annual_HH_Income'])
```




    array([[1.        , 0.97031542],
           [0.97031542, 1.        ]])




```python
import matplotlib.pyplot as plt
x = df['Mthly_HH_Income'].values
y = df['Annual_HH_Income'].values
plt.xlabel(xlabel = "Mthly_HH_Income")
plt.ylabel(ylabel ="Annual_HH_Income")
plt.scatter(x,y)
```




    <matplotlib.collections.PathCollection at 0x1987232c850>




    
![png](output_75_1.png)
    


### With out Library Function


```python
def correlation(column_x,column_y):
    cov=covariance(column_x,column_y)  # Here I have used previously created function of covariance
    std_x=std_deviation(column_x) # Here I have used previously created function of standard deviation
    std_y=std_deviation(column_y) # Here I have used previously created function of standard deviation
    return (cov/(std_x*std_y))
def covariance(column_x,column_y):
    length=len(column_x)
    # Finding mean of x
    sum_x=sum(column_x)
    mean_x=sum_x/length
   
    #Finding mean of y
    sum_y=sum(column_y)
    mean_y=sum_y/length
    
    sum_var_x=0
    sum_var_y=0
    
    lst_x=[]
    lst_y=[]
    for i in column_x:
        var_x=i-mean_x
        lst_x.append(var_x)
    for j in column_y:
        var_y=j-mean_y
        lst_y.append(var_y)
    
    sum_corr=0
    for i in range(0,len(lst_x)):
        for j in range(0,len(lst_y)):
            if(i==j):
                corr=lst_x[i]*lst_y[j]
                sum_corr+=corr
                
    return (sum_corr/length)
correlation(df['Mthly_HH_Income'],df['Annual_HH_Income'])

```




    0.9703154166603717



## <font color = 'blue'> 7 & 8. <u> Normal Distribution, feature of Normal Distribution</u>: </font>
                 Normal distribution, also known as the Gaussian distribution, is a probability distribution that is 
    symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the
    mean. In graph form, normal distribution will appear as a bell curve.
    
    takeaway from Normal Distribution:
    1. A normal distribution is the proper term for a probability bell curve.
    2. In a normal distribution the mean is zero and the standard deviation is 1. It has zero skew and a kurtosis of 3.
    3. Normal distributions are symmetrical, but not all symmetrical distributions are normal.
    4. In reality, most pricing distributions are not perfectly normal.
    
    The standard normal distribution has two parameters: 
        the mean and the standard deviation. 
    features of Normal Distribution Include:
    The area under the curve is equal to 1.
    The sum of all the probabilities of event is equal to 1
    For a normal distribution:
        68% of the observations are within +/- one standard deviation of the mean, 
        95% are within +/- two standard deviations, 
        and 99.7% are within +- three standard deviations.
    Normal Distribution Notation is given by:

<center> $ \Huge X - \ N(\mu , \sigma^2) $ </center>


![image.png](attachment:image.png)

<center>were Normal Distribution is Given by $\Large \rightarrow f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{\frac{-(x-\mu)^{2}}{2\sigma^{2}}}$</center>


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mthly_HH_Income</th>
      <th>Mthly_HH_Expense</th>
      <th>No_of_Fly_Members</th>
      <th>Emi_or_Rent_Amt</th>
      <th>Annual_HH_Income</th>
      <th>Highest_Qualified_Member</th>
      <th>No_of_Earning_Members</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5000</td>
      <td>8000</td>
      <td>3</td>
      <td>2000</td>
      <td>64200</td>
      <td>Under-Graduate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6000</td>
      <td>7000</td>
      <td>2</td>
      <td>3000</td>
      <td>79920</td>
      <td>Illiterate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10000</td>
      <td>4500</td>
      <td>2</td>
      <td>0</td>
      <td>112800</td>
      <td>Under-Graduate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10000</td>
      <td>2000</td>
      <td>1</td>
      <td>0</td>
      <td>97200</td>
      <td>Illiterate</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12500</td>
      <td>12000</td>
      <td>2</td>
      <td>3000</td>
      <td>147000</td>
      <td>Graduate</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats as st
```


```python
nor = np.random.normal(df['Mthly_HH_Income'])
sns.distplot(nor)
```

    C:\Users\HP\anaconda3\lib\site-packages\seaborn\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
      warnings.warn(msg, FutureWarning)
    




    <AxesSubplot:ylabel='Density'>




    
![png](output_84_2.png)
    



```python
mu_normal = nor.mean()

sigma_normal= nor.std()

print(mu_normal, sigma_normal)
```

    41557.95896277037 25835.352751646617
    


```python
one_std_right = mu_normal + (1 * sigma_normal)

one_std_left = mu_normal - (1 * sigma_normal)

two_std_right = mu_normal + (2 * sigma_normal)

two_std_left = mu_normal - (2 * sigma_normal)

three_std_right = mu_normal + (3 * sigma_normal)

three_std_left = mu_normal - (3 * sigma_normal)
```


```python
plt.figure(figsize=(20,10))
sns.set_style("darkgrid")
sns.distplot(nor)

plt.axvline(mu_normal, color='coral', label='Mean')

plt.axvline(one_std_right, color='yellow', label='Mean + 1SD')
plt.axvline(one_std_left, color='yellow', label='Mean - 1SD')
plt.axvline(two_std_right, color='green', label='Mean + 2SD')
plt.axvline(two_std_left, color='green', label='Mean - 2SD')
plt.axvline(three_std_right, color='blue', label='Mean + 3SD')
plt.axvline(three_std_left, color='blue', label='Mean - 3SD')
plt.legend();
```

    C:\Users\HP\anaconda3\lib\site-packages\seaborn\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
      warnings.warn(msg, FutureWarning)
    


    
![png](output_87_1.png)
    



```python
print(((one_std_left < nor) & (nor < one_std_right)).sum()/nor.size)
print(((two_std_left < nor) & (nor < two_std_right)).sum()/nor.size)
print(((three_std_left < nor) & (nor < three_std_right)).sum()/nor.size)
```

    0.7
    0.92
    1.0
    

$ \rightarrow $ we can see this Data didn't satisfied 65-95-99.7 rule & this didn't formed an accurate bell shaped curve too se we can say this won't follow Normal Distribution

## <font color = 'Blue'> 9. <u>Positively Skewed & Negatively Skewed Normal Distribution </u>: </font>

### What is Skewness?
Skewness is a measure of the symmetry of a distribution. The highest point of a distribution is its mode. 
The mode marks the response value on the x-axis that occurs with the highest probability. it is the measure 
of asymmetry of probability distribution of a random variable about its mean. The skewness can be either 
can be positive, negative or zero. If skewness is 0 the data is perfectly symmetric

---> If the skewness is less than -1 and greater than +1, then it is highly skewed data. <br>
---> If the skewness is between -0.5 to -1 or between 0.5 to 1, then it is moderately skewed data. <br>
---> If the skewness is between -0.5 to 0.5 then, the distribution is almost symmetric. <br>


### Positively and Negatively Skewed Normal Distribution?

---> Positively-Skewed distribution also known as right-skewed distribution as it's long tails lies <br>
     in the right side of the distribution. <br>
---> Negatively-Skewed distribution also known as left-skewed distribution as it's long tail lies <br>
     in the left side of the distribution. <br>

# ![image.png](attachment:image.png) 

## <font color = 'Blue'> 10. <u>Effect on Mean, Median and Mode due to Skewness</u>:</font>

### Effect on mean, median and mode due to skewness?

if the distribution of data is skewed to the left, the mean is less than the median, which is often less than the mode.
If the distribution of data is skewed to the right, the mode is often less than the median, which is less than the mean.

Negatively-Skewed distribution: Mean <  Median < Mode <br>
Positively-Skewed distribution: Mode < Median < Mean



![image.png](attachment:image.png)

## <font color = 'blue'> 11. <u>Explain QQ Plot and show the implementation of the same</u>: </font>

#### --> The Q-Q plot, or quantile-quantile plot, is a graphical tool to help us assess if a set of data plausibly came from some theoretical distribution such as a Normal or exponential. <br>
#### --> A Q-Q plot is a scatterplot created by plotting two sets of quantiles against one another. If both sets of quantiles came from the same distribution, we should see the points forming a line that’s roughly straight. <br>

$ \rightarrow $ It checks the normality of the data. <br>
$ \rightarrow $ For the data, to be normally distributed all the point should lie on $45^{\circ}$ angle.

### we saw the first feature monthly income didn't follow Normal Distribution. let's conclude it from QQ-Plot


```python
from scipy import stats
stats.probplot(df['Mthly_HH_Income'], dist="norm",plot=plt)
plt.grid()
```


    
![png](output_100_0.png)
    


$ \large \rightarrow \ we \ can \ see \ all \ the \ points \ didn't \ fall \ on \ 45^{\circ} \ line $
$ \large \rightarrow \ so \ we \ can \ say \ monthly \ income \ won't \ follow \ normal \ distribution $

$ \large How \ can \ we \ convert \ this \ data \ to \ distribute \ Normally \ ? $

## <font color = 'blue'> 12. <u>Explain Box Cox and show the implementation of the same</u> :</font>

A Box Cox transformation is a transformation of a non-normal dependent variables into a normal shape. Normality 
is an important assumption for many statistical techniques;if your data isn’t normal, applying a Box-Cox means 
that you are able to run a broader number of tests.

$ \rightarrow \ It \ is \ used \ to \ transform \ the \ data \ into \ normal \ distribution. $


```python
ls, b = stats.boxcox(df['Mthly_HH_Income'])
print(b)
```

    0.3031376789702236
    


```python
stats.probplot(ls,plot=plt,dist='norm')
plt.grid()
```


    
![png](output_106_0.png)
    


$ \large \rightarrow \text{Analyse the two plots above, we can notice that there is an improvement in second plot towards Normal Distribution} $
$ \large \rightarrow \text{data in the second plot falls approximately on the} $$ \large \ 45^{\circ} line $
$ \large \rightarrow \text{finally using this Box-Cox Transformation the initial data which is not normally distributed is converted to Normally distributed Data} $

<font color = 'Blue'> $ \Large \rightarrow Pareto Distribution: $</font>
    
    Pareto distribution is a power law probability distribution used to model empiric phenomena such as the distribution
    of wealth, the stock price fluctuations, the occurrence of natural resources. Pareto distribution has been vulgarized
    under the name of Pareto principle (or the “80–20 rule”, the Matthew principle) stating that, for example, 80% of the
    wealth of a society is held by 20% of its population. However, the Pareto distribution only produces this result for 
    a particular power value of the input parameter alpha (α = log45 ≈ 1.16). In terms of parameters, this distribution 
    depends on location (the lower bound for the variable) and the shape controlling the variance.



![image.png](attachment:image.png)

<font color = 'Blue'> $ \Large \rightarrow Log Normal Distribution: $</font>
    
    Lognormal distribution is a good candidate for modelling positively skewed values which are ≥0. 
    For instance, normal distribution cannot be used to model stock prices because it has a negative 
    side and stock prices cannot fall below zero so lognormal distribution is a good candidate. Thus,
    if a random variable X is log-normally distributed, then Y = ln(X) has a normal distribution. 
    Likewise, if Y has a normal distribution, then the exponential function of Y, X = exp(Y), has a 
    log-normal distribution. Lognormal distribution is described by 2 parameters, the mean and the 
    standard deviation.

    


![image.png](attachment:image.png)

<font color = 'Blue'> $ \Large \rightarrow Exponential Distribution: $</font>
    
    This distribution describes the amount of time between events occurring at random moments. It is considered 
    that time has no effect on future outcomes (the future lifetime of an object has the same distribution, 
    regardless of the time it existed) which makes the exponential “memoryless”. It can be used to model situa-
    tions such as: how long do we have to wait at a crossroad until we see a car running on the red light or how 
    long it will take until someone receives the next phone call? how long will a product function before breaking
    down?Exponential distribution is related to Poisson which doesn’t describe the time lapsed but the number of
    occurrences of an event in a given time frame. The exponential distribution is parametrised only by lambda,
    the success rate.


![image.png](attachment:image.png)


```python

```
