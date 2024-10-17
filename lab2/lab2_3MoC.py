import numpy as np

# Hardcoded coefficients as per provided data
coefficients = [
    (0.375, 0.0),  # C0
    (0.0, -0.125), # C1
    (-0.12499999999999994, -0.25),  # C2
    (-1.3877787807814457e-16,0.1250000000000001),  # C3
    (-0.125,-6.123233995736766e-17),  # C4
]

# Function to calculate the signal based on coefficients
def calculate_signal(coefficients):
    N = len(coefficients)
    extended_coefficients = coefficients + [(A, -B) for A, B in coefficients[1:-1][::-1]]  # Extend coefficients symmetrically

    signal = []
    
    for n in range(len(extended_coefficients)):
        s_n_real = 0
        for k, coeff in enumerate(extended_coefficients):
            real_part = coeff[0] * np.cos(2 * np.pi * k * n / len(extended_coefficients))
            imag_part = coeff[1] * np.sin(2 * np.pi * k * n / len(extended_coefficients))
            s_n_real += real_part - imag_part
        
        signal.append(s_n_real)
    
    return signal

# Function to display coefficients
def display_coefficients(coefficients):
    for i, (A, B) in enumerate(coefficients[1:], start=1):
        print(f"C{i} = {A} + i*{B}")

# Main function to execute
def main():
    display_coefficients(coefficients)
    
    signal_values = calculate_signal(coefficients)
    
    print("------------------------")
    
    print("Signal:")
    for value in signal_values:
        print(value)
    
    print("------------------------")
    print(f"s(0T_delta) = {signal_values[0]:.5f}")
    print(f"s(1T_delta) = {signal_values[1]:.5f}")

if __name__ == "__main__":
    main()
