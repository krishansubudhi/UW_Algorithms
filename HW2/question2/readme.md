```
                                                expected partitions expected comparisons expected runtime
    n       algorithm
    1000    Quick select random pivot                              7.2               2.17 n   0.0033 seconds
            Quick select middle index                             10.0               1.98 n   0.0018 seconds
            Quick select Median from sorting                      10.0               1.98 n   0.0027 seconds
            Quick select Median from quick select                  9.0               1.98 n   0.0085 seconds
    10000   Quick select random pivot                              9.9               2.15 n   0.0165 seconds
            Quick select middle index                             14.0               2.00 n   0.0105 seconds
            Quick select Median from sorting                      14.0               2.00 n   0.0100 seconds
            Quick select Median from quick select                 13.0               2.00 n   0.0273 seconds
    100000  Quick select random pivot                             11.9               2.63 n   0.0663 seconds
            Quick select middle index                             17.0               2.00 n   0.0524 seconds
            Quick select Median from sorting                      17.0               2.00 n   0.0715 seconds
            Quick select Median from quick select                 16.0               2.00 n   0.2158 seconds
    1000000 Quick select random pivot                             13.7               1.83 n   0.4618 seconds
            Quick select middle index                             20.0               2.00 n   0.4855 seconds
            Quick select Median from sorting                      20.0               2.00 n   0.6923 seconds
            Quick select Median from quick select                 19.0               2.00 n   2.0908 seconds
```