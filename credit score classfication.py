def classify_credit_score(score):
    if score < 300 or score > 850:
        return "Invalid score. Credit score must be between 300 and 850."
    elif 300 <= score < 580:
        return "Poor"
    elif 580 <= score < 670:
        return "Fair"
    elif 670 <= score < 740:
        return "Good"
    elif 740 <= score <= 850:
        return "Excellent"
    return "Unknown category"  

def main():
    try:
        score = int(input("Enter credit score (300-850): "))
        category = classify_credit_score(score)
        print("Credit Score Classification:", category)
    except ValueError:
        print("Please enter a valid integer for the credit score.")

if __name__ == "__main__":
    main()
