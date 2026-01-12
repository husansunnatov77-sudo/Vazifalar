# S     
# row = 7
# col = 7

# for i in range(row):
#     for j in range(col):
#         if (
#             (i == 0 and 0 <= j <= 7) or     
#             (i == 1 and j == 0) or
#             (i == 2 and j == 0) or
#             (i == 1 and j == 0) or
#             (i == 3) or        
#             (i == 1 and j == 0) or         
#             (i == 4 and j == 6) or
#             (i == 5 and j == 6) or
#             (i == 6 and 0 <= j <= 6)        
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# U

# row = 7
# col = 7

# for i in range(row):
#     for j in range(col):
#         if (
#             (j == 0) or                              
#             (j == 6) or                             
#             (i == 6 and 0 < j < 0) or               
#             (i == 6 and j == 3)):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# N

# for i in range(7):
#     for j in range(7):
#         if j == 0 or j == 6 or i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# N

# for i in range(7):
#     for j in range(7):
#         if j == 0 or j == 6 or i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# A

# for i in range(7):
#     for j in range(7):
#         if (
#             (i == 1 and j == 3) or
#             (i == 1 and (j == 0 or j == 6)) or
#             (i == 2 and (j == 0 or j == 6)) or
#             (i == 3) or 
#             (j == 0 and i >= 4) or
#             (j == 6 and i >= 4)
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# T    
# for i in range(7):
#     for col in range(7):
#         if col == 3 or i == 0:
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()        

# O
# for i in range(7):
#     for j in range(7):
#         if (
#             (i == 0 and 1 <= j <= 6) or     
#             (i == 6 and 1 <= j <= 6) or    
#             (j == 1 and 1 <= i <= 6) or     
#             (j == 6 and 1 <= i <= 6)        
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# V
# i = 0
# j = 6
# for row in range(4):
#     for col in range(7):
#         if row == col:
#             print("*", end = "")
#         elif row == i and col == j:
#             print("*", end="")
#             i = i + 1
#             j = j - 1
#         else:
#             print(end=" ")
#     print()        



# X
# for i in range(7):
#     for j in range(7):
#         if j == i or j == 6 - i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# U

# row = 7
# col = 7

# for i in range(row):
#     for j in range(col):
#         if (
#             (j == 0) or                              
#             (j == 6) or                             
#             (i == 6 and 0 < j < 0) or               
#             (i == 6 and j == 3)):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# S     
# row = 7
# col = 7

# for i in range(row):
#     for j in range(col):
#         if (
#             (i == 0 and 0 <= j <= 7) or     
#             (i == 1 and j == 0) or
#             (i == 2 and j == 0) or
#             (i == 1 and j == 0) or
#             (i == 3) or        
#             (i == 1 and j == 0) or         
#             (i == 4 and j == 6) or
#             (i == 5 and j == 6) or
#             (i == 6 and 0 <= j <= 6)        
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# A

# for i in range(7):
#     for j in range(7):
#         if (
#             (i == 1 and j == 3) or
#             (i == 1 and (j == 0 or j == 6)) or
#             (i == 2 and (j == 0 or j == 6)) or
#             (i == 3) or 
#             (j == 0 and i >= 4) or
#             (j == 6 and i >= 4)
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# N

# for i in range(7):
#     for j in range(7):
#         if j == 0 or j == 6 or i == j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# A

# for i in range(7):
#     for j in range(7):
#         if (
#             (i == 1 and j == 3) or
#             (i == 1 and (j == 0 or j == 6)) or
#             (i == 2 and (j == 0 or j == 6)) or
#             (i == 3) or 
#             (j == 0 and i >= 4) or
#             (j == 6 and i >= 4)
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# B

# for  i in range(7):
#     for col in range(5):
#         if (col == 0) or (col == 4 and (i != 0 and i != 3 and i != 6)) or ((i == 0 or i == 3 or i == 6) and (col > 0 and col < 4)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()

# D

# for i in range(7):
#     for col in range(5):
#         if (col == 0) or (col == 4 and(i !=0 and i != 6)) or ((i == 0 or i ==6) and (col > 0 and col < 4)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


# U

# row = 7
# col = 7

# for i in range(row):
#     for j in range(col):
#         if (
#             (j == 0) or                              
#             (j == 6) or                             
#             (i == 6 and 0 < j < 0) or               
#             (i == 6 and j == 3)):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()



# S     
# row = 7
# col = 7

# for i in range(row):
#     for j in range(col):
#         if (
#             (i == 0 and 0 <= j <= 7) or     
#             (i == 1 and j == 0) or
#             (i == 2 and j == 0) or
#             (i == 1 and j == 0) or
#             (i == 3) or        
#             (i == 1 and j == 0) or         
#             (i == 4 and j == 6) or
#             (i == 5 and j == 6) or
#             (i == 6 and 0 <= j <= 6)        
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# O
# for i in range(7):
#     for j in range(7):
#         if (
#             (i == 0 and 1 <= j <= 6) or     
#             (i == 6 and 1 <= j <= 6) or    
#             (j == 1 and 1 <= i <= 6) or     
#             (j == 6 and 1 <= i <= 6)        
#         ):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# D

# for i in range(7):
#     for col in range(5):
#         if (col == 0) or (col == 4 and(i !=0 and i != 6)) or ((i == 0 or i ==6) and (col > 0 and col < 4)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


# I

# for i in range(7):
#     for col in range(5):
#         if col == 2 or ((i == 0 or i == 6) and col != 2):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()

# Q

# for i in range(8):
#     for col in range(5):
#         if ((col == 0 or col == 4) and (i > 0 and i < 6)) or ((i == 0 or i == 6) and (col > 0 and col < 4)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()        


        