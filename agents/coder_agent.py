from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def generate_eda_code(schema_info):
    prompt = f"""
    You are a data scientist.

    Here is dataset metadata:
    {schema_info}

    Write Python code using pandas, matplotlib, seaborn to:
    1. Summary statistics
    2. Distribution plots
    3. Correlation heatmap
    4. Missing values heatmap
    5. Use matplotlib or seaborn for plots.ALWAYS use plt.figure() before plotting. 
       DO NOT use plt.show()
    6. Do NOT use pd.read_csv. The dataset is already loaded as 'df'. Use 'df' directly

    Only return executable Python code.
    """

    return llm.invoke(prompt)