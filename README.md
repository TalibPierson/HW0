# HW0: Galaxy Explorers
Talib Pierson  
September 2020

## Part 1
### a.
|total number of objects|mean update time per coordinate (us)|
|-----------------------|------------------------------------|
|1|0.6996703739176741|
|2|0.4364231691363768|
|4|0.3315281772615919|
|8|0.2759401807796852|
|16|0.2525712289817156|
|32|0.23780252265959145|
|64|0.25457546234085304|
|128|0.2585264053337616|
|256|0.26059476947865035|
|512|0.2664582805633059|
|1024|0.2757434844971596|
|2048|0.2872345275881788|
|4096|0.2877296104430993|
|8192|0.28505723190241916|
|16384|0.32059593009850507|
|32768|0.4464829473482118|
|65536|0.5078680925356405|
|131072|0.5062201404570227|
|262144|0.47883055305508737|
|524288|0.40485972023149297|
|1048576|0.4079532003389841|

(for graph see `plot.svg`)

I picked sizes and iterations such that their product is 2^16 because I thought that if I multuply the size of a problem by some number, I should divide the number of iterations of it by that same number so that my computer doesn't take too long to process the test, and to get a feel for how different balances between size and iterations affect mean time per coordinate.

### b.
I measured only once each time since it takes so long to process and my results seem consistent. Rather than running `update_locations` many times it's better to just run it using more iterations to increase my sampling. The second time I ran it to check for consistency I generated `plot1.svg`
