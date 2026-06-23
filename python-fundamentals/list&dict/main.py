# You have this list of AI model info
models = [
    {"name": "gpt-4", "company": "OpenAI", "context_window": 128000},
    {"name": "claude-3", "company": "Anthropic", "context_window": 200000},
    {"name": "gemini-pro", "company": "Google", "context_window": 100000}
]

# Task 1: Print only the model names

# Task 2: Print name + context_window for models with context_window > 100000

for model in models:
    print(model["name"])

for model in models:
    if model["context_window"] > 100000:
        print(f"{model["name"]} has a context window of {model["context_window"]}")

# Task 1: Use a list comprehension to get a list of just the "company" values
# Task 2: Use a list comprehension to get model names where company is "Anthropic" or "OpenAI"

companies = [model["company"] for model in models]
print(companies)
expectedCompanies = ["OpenAI", "Anthropic"]
theCompanies = [model["name"] for model in models if model["company"] in expectedCompanies]
print(theCompanies)

# Task: Build a dict comprehension mapping company -> context_window
# (so {"OpenAI": 128000, "Anthropic": 200000, "Google": 100000})

context_window_dict = {model["company"]: model["context_window"] for model in models}
print(context_window_dict)