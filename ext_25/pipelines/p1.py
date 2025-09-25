Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    all_type_databricks_0 = SourceTask(
        task_id = "all_type_databricks_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "databricks_1", oAuthType = "m2m"), 
        format = DATABRICKSFormat(
          schema = {
            "fields": [{"name" : "id", "dataType" : {"type" : "int32"}},                         {"name" : "tiny_value", "dataType" : {"type" : "int8"}},                         {"name" : "small_value", "dataType" : {"type" : "int16"}},                         {"name" : "big_value", "dataType" : {"type" : "int64"}},                         {"name" : "name", "dataType" : {"type" : "utf8"}},                         {"name" : "is_active", "dataType" : {"type" : "bool"}},                         {"name" : "salary", "dataType" : {"type" : "decimal128"}},                         {"name" : "float_value", "dataType" : {"type" : "float32"}},                         {"name" : "double_value", "dataType" : {"type" : "float64"}},                         {"name" : "binary_data", "dataType" : {"type" : "binary"}},                         {"name" : "created_at", "dataType" : {"type" : "timestamp"}},                         {"name" : "created_at_ntz", "dataType" : {"type" : "timestamp"}},                         {"name" : "birth_date", "dataType" : {"type" : "date64"}},                         {"name" : "interval_value", "dataType" : {"type" : "utf8"}},                         {"name" : "interval_seconds", "dataType" : {"type" : "utf8"}},                         {
                          "name": "metadata", 
                          "dataType": {"keyType" : {"type" : "utf8"}, "type" : "Map", "valueType" : {"type" : "utf8"}}
                        },                         {"name" : "int_array", "dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}},                         {"name" : "float_array", "dataType" : {"dataType" : {"type" : "float32"}, "type" : "Array"}},                         {"name" : "boolean_array", "dataType" : {"dataType" : {"type" : "bool"}, "type" : "Array"}},                         {"name" : "decimal_array", "dataType" : {"dataType" : {"type" : "decimal128"}, "type" : "Array"}},                         {"name" : "timestamp_array", "dataType" : {"dataType" : {"type" : "timestamp"}, "type" : "Array"}},                         {"name" : "date_array", "dataType" : {"dataType" : {"type" : "date64"}, "type" : "Array"}},                         {
                          "name": "struct_array", 
                          "dataType": {
                            "dataType": {
                              "fields": [{"dataType" : {"type" : "utf8"}, "name" : "type"},                                           {"dataType" : {"type" : "int32"}, "name" : "value"}], 
                              "type": "Struct"
                            }, 
                            "type": "Array"
                          }
                        },                         {
                          "name": "array_of_arrays", 
                          "dataType": {"dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}, "type" : "Array"}
                        },                         {
                          "name": "struct_of_array", 
                          "dataType": {
                            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "name"},                                         {"dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}, "name" : "values"}], 
                            "type": "Struct"
                          }
                        },                         {
                          "name": "struct_of_array_of_structs", 
                          "dataType": {
                            "fields": [{"dataType" : {"type" : "int32"}, "name" : "id"},                                         {
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{"dataType" : {"type" : "utf8"}, "name" : "key"},                                                           {"dataType" : {"type" : "int32"}, "name" : "val"}], 
                                              "type": "Struct"
                                            }, 
                                            "type": "Array"
                                          }, 
                                          "name": "details"
                                        }], 
                            "type": "Struct"
                          }
                        }], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_automation"}
    )
    all_type_databricks_0 = Task(
        task_id = "all_type_databricks_0", 
        component = "Dataset", 
        label = "all_type_databricks_0", 
        table = {"name" : "{{ prophecy_tmp_source('p1', 'all_type_databricks_0') }}", "sourceType" : "UnreferencedSource"}
    )
    xlxs_file = Task(
        task_id = "xlxs_file", 
        component = "Dataset", 
        table = {"name" : "xlxs_file", "sourceType" : "Table", "sourceName" : "avpreet_random_prophecy_io_team.dummy", "alias" : ""}
    )
    p1__Reformat_1 = Task(task_id = "p1__Reformat_1", component = "Model", modelName = "p1__Reformat_1")
    all_type_databricks_0.out0 >> all_type_databricks_0.input_port_0
    all_type_databricks_0.output_port_0 >> p1__Reformat_1.in_0
