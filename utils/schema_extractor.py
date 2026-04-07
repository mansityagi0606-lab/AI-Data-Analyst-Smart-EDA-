import pandas as pd

def extract_schema(file_path):
    df = pd.read_csv(file_path)

    schema_info = {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "shape": df.shape
    }

    return df, schema_info