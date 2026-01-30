from pipeline.run_pipeline import run_pipeline

if __name__ == "__main__":
    url = input("Enter webpage URL: ")

    try:
        result = run_pipeline(url)
        print("\nSummary:\n")
        print(result["summary"])
    except Exception as e:
        print(f"Error: {e}")
