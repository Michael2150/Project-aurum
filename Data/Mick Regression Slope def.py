# https://www.youtube.com/watch?v=JvS2triCgOY&ab_channel=statisticsfun
# This video explains the formula:
# a =  (n∑(xy)−∑x∑y) / (n∑x2−(∑x)^2)
def get_regression_slope(xs,ys):
    # Get the number of points
    n = min(len(xs),len(ys))

    # Get the mean of the points
    mean_x = sum(xs)/n
    mean_y = sum(ys)/n

    reg_val1 = []
    reg_val2 = []
    for i in range(n):
        # Calculate (x - mean_x)^2 for every point
        val1 = (xs[i] - mean_x)*(xs[i] - mean_x)
        reg_val1.append(val1)
        # Calculate (x - mean_x)(y - mean_y) for every point 
        val2 = (xs[i] - mean_x)*(ys[i] - mean_y)   
        reg_val2.append(val2)

    # Gets ∑(x - mean_x)^2
    val1 = sum(reg_val1)
    # Gets ∑(x - mean_x)(y - mean_y)
    val2 = sum(reg_val2)

    # returns the final answer from the formula:
    # a =  (n∑(xy)−∑x∑y) / (n∑x2−(∑x)^2)
    a = val2/val1
    return a

inputxs = [1,2,3,4,5]
inputys = [2,4,5,4,5]
a = get_regression_slope(inputxs,inputys)
print(a)
