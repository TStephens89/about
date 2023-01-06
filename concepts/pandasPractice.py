import pandas as pd

unitedStates = {'State': ["California", "Texas", "Florida", "New York", "Pennsylvania", "Illinois", "Ohio", "Georgia", "North Carolina", "Michigan"], 'Population': [9600500, 29700300, 21900500, 1990500, 12800100, 12500300, 11700600, 10800000, 10700000, 9900400], 'Capital': ["Sacramende", "Austin", "Tallahassee", "Albany", "Harrisburg", "Springfield", "Columbus", "Atlanta", "Raleigh", "Lansing"]}

df = pd.DataFrame(unitedStates)
print(df)

df.to_csv("unitedStates.csv")

new_df = pd.read_csv("unitedStates.csv")
population = sum(unitedStates["Population"])
print("The population of the United States is: " + str(population))