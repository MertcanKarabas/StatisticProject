import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#Mean of data
def mean(data):
    return round((sum(data) / len(data)), 3)  #Ortalaması (Verilen dataların toplamı / Veri sayısı)

#Median of data
def median(data):
    sorted_data = sorted(data)
    middle = (len(data) - 1) // 2
    if middle % 2:
        return round(sorted_data[middle], 3)
    else:
        return round(((sorted_data[middle] + sorted_data[middle + 1]) / 2.0), 3)

#Deviation of data
def deviations(data):
    return [(x-mean(data)) ** 2 for x in data]

#Variance of data
def variance(data):
    return  round(sum(deviations(data)) / len(data), 3)

#Standart Deviation of data
def stdev(data):
    return round(math.sqrt(variance(data)), 3)

#Standart Error of data
def ste(data):
    return round(stdev(data) / math.sqrt(len(data)), 3)

def quantiles(data):
    return [round(np.quantile(data, .25), 3), round(np.quantile(data , .75), 3)]

def outliers(data):
    quan = quantiles(data)
    IQR = quan[1] - quan[0]
    interval = [round((quan[0] - (1.5 * IQR)), 3), round((quan[1] + (1.5 * IQR)), 3)]
    print("                   Outliers Interval: ", interval)
    listOfOutliers = list()
    for dt in data:
        if dt < interval[0] or dt > interval[1]:
            listOfOutliers.append(round(dt, 2))

    counter = 0
    for item in sorted(listOfOutliers):
        if counter == 8:
            print(f"    \n    {item},", end= " ")
            counter += 1

        elif counter == 0:
            print(f"    [{item},", end = " ")
            counter += 1

        elif counter == len(listOfOutliers)-1:
            print(f"{item}]")

        else:
            print(f"{item},", end= " ")
            counter += 1

#Confidence Interval Calculation
def confidenceInterval(data, interval):
    if interval == 95:
        zNumber = 1.96 #Tablo A4
    elif interval == 90:
        zNumber = 1.645 #Tablo A4
    else:
        zNumber = 0

    minimumInterval = round(mean(data) - (zNumber * (stdev(data) / math.sqrt(len(data)))),3)
    maximumInterval = round(mean(data) + (zNumber * (stdev(data) / math.sqrt(len(data)))),3)

    return [minimumInterval, maximumInterval]

#Estimate Calculation
def estimateCalculation(data, interval):
    margin = 0.1

    if interval == 95:
        zNumber = 1.96 #Tablo A4
    elif interval == 90:
        zNumber = 1.645 #Tablo A4
    else:
        zNumber = 0

    return (f"N >= {round(zNumber * stdev(data) / margin )}")

#Main Method
def main():
    data = pd.read_csv("TSLA.csv")
    openCoulmn = data["Open"]

    print(f"--------------------------------------------------------------------")
    print(f"                           Calculations")
    print(f"--------------------------------------------------------------------")
    print(f"              Mean of Opening Prices of Tesla: {mean(openCoulmn)}")
    print(f"              Median of Opening Prices of Tesla: {median(openCoulmn)}")
    print(f"            Variance of Opening Prices of Tesla: {variance(openCoulmn)}")
    print(f"       Standart Deviation of Opening Prices of Tesla: {stdev(openCoulmn)}")
    print(f"         Standart Error of Opening Prices of Tesla: {ste(openCoulmn)}")
    print(f"%95 Confidence Interval for the Mean and Variance: {confidenceInterval(openCoulmn, 95)}")
    print(f"       %90 Confidence Estimate the Population Mean: {estimateCalculation(openCoulmn, 90)} ")
    print(f"--------------------------------------------------------------------")
    print(f"                Shape of Distribution: Right-skewed")
    print(f"--------------------------------------------------------------------")
    print(f"                            Outliers")
    print(f"--------------------------------------------------------------------")
    outliers(openCoulmn)
    print(f"--------------------------------------------------------------------")

    #Drawing Dataset Histogram
    plt.hist(openCoulmn, bins= 10, color = 'purple', ec = 'black')
    plt.title("Opening Price")
    plt.xlabel("Price")
    plt.ylabel("Total Months")
    plt.show()

    #Drawing Box Plot
    plt.boxplot(openCoulmn)
    plt.title("Open Column Box Plot")
    plt.show()

if __name__ == '__main__':
    main()
