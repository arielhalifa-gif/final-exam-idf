class Sort:
    def sort_by_distance(soldiers_mat):
        n = len(soldiers_mat)
    
    # Traverse through all soldiers_mat elements
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is smaller
                # than the next element
                if soldiers_mat[j][-1] < soldiers_mat[j+1][-1]:
                    soldiers_mat[j], soldiers_mat[j+1] = soldiers_mat[j+1], soldiers_mat[j]
                    swapped = True
            if (swapped == False):
                break
