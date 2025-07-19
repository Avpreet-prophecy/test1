from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pip1.config.ConfigStore import *
from pip1.functions import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.agg()
