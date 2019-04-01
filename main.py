import math
from Join import *
from Experiment import *
from ExperimentAggFunctions import *

buildSizes = [128, 256]
probeSizes = [128, 256]
memSizes = [255, 256]
F = 1.3
numPartitions = [2, 3, 4]

E = Experiment(buildSizes, probeSizes, memSizes, F, numPartitions)
E.run()

for r in E.runs:
    print(r.join.stats())

groups = ExperimentAggFunctions.groupBy(E.runs, lambda c: c.numPartitions)
print(groups)
print(ExperimentAggFunctions.select(groups, lambda c: c.buildSize / c.memSize))
