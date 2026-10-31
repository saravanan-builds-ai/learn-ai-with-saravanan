import numpy as np

def num_properties(scores:np.ndarray):
    print("Array:", scores)
    #Shape of array (6,)
    print("Shape:", scores.shape)
    #Dimension of array 1
    print("Dimensions:", scores.ndim)
    #Type of array int64
    print("Data type:", scores.dtype)
    #Size of array 6
    print("Total elements:", scores.size)

def num_operations(scores:np.ndarray):
    # Calculate average
    average = np.mean(scores)
    # Find maximum
    maximum = np.max(scores)
    # Find minimum
    minimum = np.min(scores)
    # Calculate median
    median = np.median(scores)
    # Calculate standard deviation
    std_deviation = np.std(scores)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Median:", median)
    print("Standard Deviation:", std_deviation)

def num_filter(scores:np.ndarray):
    scores=scores[scores>=70]
    print("More than 70", scores)

def num_broadcasting(scores:np.ndarray):
    bonus=7
    scores=scores+bonus
    print("Bonus:", scores)

if __name__=="__main__":

    scores = np.array([45, 55, 65, 75, 85, 95])
    num_properties(scores)
    num_operations(scores)
    num_filter(scores)
    num_broadcasting(scores)
