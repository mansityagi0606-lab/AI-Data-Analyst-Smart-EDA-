from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def generate_insights(summary):
    prompt = f"""
    You are a senior data scientist.

    Here are dataset statistics:
    {summary}

    Provide:
    - Key patterns
    - Data quality issues
    - Correlations
    - ML recommendations
    """

    return llm.invoke(prompt)