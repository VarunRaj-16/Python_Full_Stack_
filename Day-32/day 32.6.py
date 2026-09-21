import numpy as np
# 12. COPYING AND VIEWS
arr = np.array([10, 20, 30])
# Shallow copy / View
view_arr = arr.view()
view_arr[0] = 100
print(arr)
# Deep copy
copy_arr = arr.copy()
copy_arr[0] = 200
print(arr)