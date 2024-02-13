def averages():
     
    with open("/Users/zyh/Desktop/2-data-munging-YuhaoZ22/data/clean_data.csv", "r") as file:
        next(file)  
        
        # Initialize variables
        data = []
        for line in file:
            parts = line.strip().split(',')
            data.append(float(parts[1]))  # Assuming anomalies are in 2nd column

    # Process data
    start = 1880
    sum_temp, count = 0, 0

    for i, temp in enumerate(data):
        sum_temp += temp
        count += 1

        if (i + 1) % 10 == 0 or i + 1 == len(data):
            avg_temp = sum_temp / count
            print(f"{start} to {start + 9}: {round(avg_temp, 2)}")
            
            # Update for next decade
            start += 10
            sum_temp, count = 0, 0

averages()