"""Q1.A sorted array is rotated at some unknown point, find the minimum element in
it.
Following solution assumes that all elements are distinct.
Examples:
Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1"""

def finmin(arr,low,high):
    if high < low:
        return arr[0]
    if high ==low:
        return arr[low]
    mid = int((low + high)/2)
    if mid <high and arr[mid+1]<arr[mid]:
        return arr[mid+1]
    if mid>low and arr[mid] < arr[mid - 1]:
        return arr[mid]
    if arr[high] > arr[mid]:
        return finmin(arr, low, mid-1)
    return finmin(arr, mid+1, high)
arr = [5,6,1,2,3,4]
N =len(arr)
print("minimum element is " + str(finmin(arr, 0, N-1)))

"""
Q2.Given two strings str1 and str2 and below operations that can
performed on str1. Find minimum number of edits (operations) required to
convert ‘str1′ into ‘str2′.
Operation :- replace

** replacement cost =1

Examples:
Input :

Str1= Quantom
Str2= Quantum

Output:
1
As Quantom can be changed to Quantum by replacing o with
u Examples 2:
Input :

Str1= Week Experience
Str2= Work Experience

Output:
2
"""
def dist(str, str1 ,m,n):

    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j] =j
            elif j==0:
                dp[i][j] = i
            elif str[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

    return dp[m][n]
str = "week experience"
str1 ="work experience"
print(dist(str,str1,len(str),len(str1)))



"""Q3.

Write a sudo code To explain your approach
Given: An Image with rectangular Boxes and labels associated to those Boxes. Index of every Box
and its Coordinates.
Problem Statement: Group together Boxes by labels and Neighboring Criteria and return the
Coordinates of the New Boxes formed.
Input: Index, Label and Coordinate of the Box(x0,y0,x1,y1) where (x0,y0) represents top-left corner
and (x1,y1) represents bottom-right corner of box with origin at top-left corner of image

Neighboring Criteria: Make a new Box that is 0.5 units away from the boundary of a selected original
box for all the sides. Now if the original boxes intersect with this new box, we consider them as
neighbors.

If label of the Neighbor Boxes matches within the newly formed Box we group them all together and
re-calculate the new Box using the same method that we used in Neighboring Criteria (0.5 units"""


coordinates = vis_util.return_coordinates(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.80)

for coordinate in coordinates:
            print(coordinate)
            (y1, y2, x1, x2, accuracy, classification) = coordinate




"""Q4. Predict the below image with Machine Learning Algorithm and Check can you apply PCA?
i) check the accuracy.
ii) if accuracy level is low then how can we increase the accuracy ."""
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd

mnist = fetch_openml('mnist_784')
mnist.data.shape
mnist.target.shape
train_img, test_img, train_lbl, test_lbl = train_test_split(
    mnist.data, mnist.target, test_size=1/7.0, random_state=0)
    
from sklearn.preprocessing import StandardScaler

scaler.fit(train_img)


train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)
from sklearn.decomposition import PCA


pca = PCA(.95)


pca.fit(train_img)
PCA(copy=True, iterated_power='auto', n_components=0.95, random_state=None,
    svd_solver='auto', tol=0.0, whiten=False)
pca.n_components_


train_img = pca.transform(train_img)
test_img = pca.transform(test_img)
from sklearn.linear_model import LogisticRegression

logisticRegr = LogisticRegression(solver = 'lbfgs')




logisticRegr.fit(train_img, train_lbl)

logisticRegr.predict(test_img[0].reshape(1,-1))
array(['0'], dtype=object)

logisticRegr.predict(test_img[0:10])
score = logisticRegr.score(test_img, test_lbl)
print(score)

