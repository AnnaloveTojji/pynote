


for r1=0->n_rows
   for c1=0->n_cols
       r2 = r1 + height - 1
       c2 = c1 + width - 1
       if valid(r1,c1,r2,c2) // doesn't exceed the original matrix
            sum_sub = ... // formula mentioned above
            best = max(sum_sub, best)
return best

calculating sum of submatrix (r1 ... r2 , c1 ... c2)
sum_sub = cumulative_sum(r2,c2) - cumulative_sum(r1-1,c2) - cumulative_sum(r2,c1-1) + cumulative_sum(r1-1,c1-1)