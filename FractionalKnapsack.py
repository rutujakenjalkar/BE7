#Fractional knapsack
# Write a program to solve a fractional Knapsack problem using a greedy method. 

def fractional(value,weight,capacity):
    ratio=[]
    for i in range(len(value)):
        ratio.append(value[i]/weight[i])


    for i in range(len(ratio)):
        for j in range(i+1,len(ratio)):
            if ratio[i]<ratio[j]:
                ratio[i],ratio[j]=ratio[j],ratio[i]
                value[i],value[j]=value[j],value[i]
                weight[i],weight[j]=weight[i],weight[j]

    
    total_value=0

    for i in range(len(value)):
        if capacity>=weight[i]:
            capacity-=weight[i]
            total_value+=value[i]

        else:
            total_value+=value[i]*(capacity/weight[i])
            print(total_value)


    return total_value





if __name__=="__main__":
    value = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50


    print(fractional(value,weight,capacity))
