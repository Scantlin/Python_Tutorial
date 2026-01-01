from scipy.stats import t
import math

def calculate_p_value(r_value, sample_size):
    """
    Calculate the p-value from the correlation coefficient (r_value)
    and the sample size (sample_size).
    """
    if abs(r_value) == 1.0:
        return 0.0
    
    # Calculate the degrees of freedom
    df = sample_size - 2

    # Calculate the t-statistic
    t_statistic = r_value * math.sqrt(df / (1 - r_value**2))

    # Calculate the p-value
    p_value = 2 * (1 - t.cdf(abs(t_statistic), df))
    
    return p_value

def determine_significance(p_value, alpha=0.05):
    """
    Determine if the correlation is significant based on the p-value.
    """
    if p_value < alpha:
        return "Significant"
    else:
        return "Not Significant"

def main():
    r_value = float(input("Enter the correlation coefficient (R value): "))
    sample_size = int(input("Enter the sample size: "))

    p_value = calculate_p_value(r_value, sample_size)
    significance = determine_significance(p_value)

    print("P-value:", p_value)
    print("Relationship is", significance)

if __name__ == "__main__":
    main()