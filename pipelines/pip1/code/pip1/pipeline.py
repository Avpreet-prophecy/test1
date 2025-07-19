from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pip1.config.ConfigStore import *
from pip1.functions import *
from prophecy.utils import *
from pip1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Aggregate_1 = Aggregate_1(spark)
    df_Join_1 = Join_1(spark)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("pip1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pip1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pip1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
