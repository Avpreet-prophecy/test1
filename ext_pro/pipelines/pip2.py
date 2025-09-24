with DAG():
    pip2__selected_employee_columns = Task(
        task_id = "pip2__selected_employee_columns", 
        component = "Model", 
        modelName = "pip2__selected_employee_columns"
    )
