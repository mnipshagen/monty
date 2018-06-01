# there was one more temperature value than months, so we added 'August'
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
temperatures = [3.8, -1.7, 2.5, 12.4, 14.2, 18, 18.1, 17.9]

# make dictionary mapping months to average temperatures
month_temp_dict = {months[i] : temperatures[i] for i in range(len(temperatures))}

print(month_temp_dict)
