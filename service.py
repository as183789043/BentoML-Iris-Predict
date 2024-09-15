from pydantic import BaseModel, Field
import typing as t
import pandas as pd
import numpy as np
import bentoml

class IrisFeatures(BaseModel):
    sepal_length_cm: float = Field(alias="sepal length (cm)", description="Length of the sepal in cm")
    sepal_width_cm: float = Field(alias="sepal width (cm)", description="Width of the sepal in cm")
    petal_length_cm: float = Field(alias="petal length (cm)", description="Length of the petal in cm")
    petal_width_cm: float = Field(alias="petal width (cm)", description="Width of the petal in cm")
    request_id: t.Optional[int] = Field(description="Optional request ID")

    class Config:
        populate_by_name = True


species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

@bentoml.service(
    resources={"cpu": "2"},
    traffic={"timeout": 10},
)
class IrisPredict:
    bento_model = bentoml.models.get("clf:latest")

    def __init__(self):
        self.model = bentoml.sklearn.load_model(self.bento_model)

    @bentoml.api
    def predict(self, input_data: IrisFeatures) -> t.List[str]:
        if input_data.request_id is not None:
            print(f"Received request id: {input_data.request_id}")
        
        # Create DataFrame with correct column names
        input_df = pd.DataFrame([{
            "sepal length (cm)": input_data.sepal_length_cm,
            "sepal width (cm)": input_data.sepal_width_cm,
            "petal length (cm)": input_data.petal_length_cm,
            "petal width (cm)": input_data.petal_width_cm
        }])
        
        prediction = self.model.predict(input_df).tolist()
        # Define a lambda function for mapping
        map_function = lambda label: species_map.get(label, "unknown")

        # Example list of numerical predictions

        # Apply the lambda function to the list of predictions using map
        species_predictions = list(map(map_function, prediction))

        
        return species_predictions