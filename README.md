  # Matrix_Search_1
  This program aims to find all the matrices for which the sum of the elements of each diagonal,
the sum of the elements of each row, the sum of the elements of each column is 13.

  The algorithm is based on the resolution of a system of linear equations: 
here are 7 free parameters change in the range(1, 7). Thus, the program has to
process 7 ^ 7 ~ 900 000 varinats to find the required matrices. 
  By the way, you do not need to check the sum values at each iteration: this condition is automatically fulfilled.

  Программа ищет все такие матрицы, для котрых сумма элеметнов каждого столбца, каждой строки и диагонали равна 13.
  
  Алгоритм основан на решении соответсвующей системы линейных уравнений: в решении есть 7 свободных параметров,
которые меняются в пределах (0, 6). Таким образом, программа должна обработать около 900 000 вариантов для отыскания
нужных матриц. При этом нет поитерационной проверки выполнения условия на суммы: оно выполнено автоматически.
