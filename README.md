# HW0: Galaxy Explorers
Talib Pierson  
September 2020

## Part 1
### a.
| size | iterations | mean time per coordinate |
|------|------------|--------------------------|
| 1 | 16777216 | 0.5013454386592047us |
| 255 | 65536 |  0.2060186279895455us |
| 65536 | 255 |  0.24303742843327183us |
| 16777216 | 1 | 0.2227190853953671us |

MIN:  0.2060186279895455us  
MEDI: 0.23287825691431946us  
MEAN: 0.2932801451193473us  
MAX:  0.5013454386592047us

I picked sizes and iterations such that their product is 2^24 because I thought that if I multuply the size of a problem by some number, I should divide the number of iterations of it by that same number so that my computer doesn't take too long to process the test, and to get a feel for how different balances between size and iteratiosn affects mean time per coordinate.

### b.
I measured three times and picked the middle number each time.
