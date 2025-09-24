Config = {"c_string" : "'hey'", "c_int" : "'123'"}

with DAG(Config = Config):
    pip2__age_21_and_above_employees = Task(
        task_id = "pip2__age_21_and_above_employees", 
        component = "Model", 
        modelName = "pip2__age_21_and_above_employees"
    )
