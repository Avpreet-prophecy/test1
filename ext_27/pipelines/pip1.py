with DAG():
    pip1__rides_with_fare = Task(
        task_id = "pip1__rides_with_fare", 
        component = "Model", 
        modelName = "pip1__rides_with_fare"
    )
