def calculate_protein_mass(amino_acid_sequence):
    amino_acid_masses = {
        'G': 57.02,
        'A': 71.04,
        'S': 87.03,
        'P': 97.05,
        'V': 99.07,
        'T': 101.05,
        'C': 103.01,
        'I': 113.08,
        'L': 113.08,
        'N': 114.04,
        'D': 115.03,
        'Q': 128.06,
        'K': 128.09,
        'E': 129.04,
        'M': 131.04,
        'H': 137.06,
        'F': 147.07,
        'R': 156.10,
        'Y': 163.06,
        'W': 186.08
     }
    
    total_mass = 0.0
    for i in amino_acid_sequence:
        if i in amino_acid_masses:
            total_mass += amino_acid_masses[i]
        else:
            raise ValueError(f"Error:'{i}'.")
    return total_mass

if __name__ == "__main__":
    example_sequence = "GASP"
    try:
        mass = calculate_protein_mass(example_sequence)
        print(f"The mass of {example_sequence} is {mass:.2f} amu.")
    except ValueError as e:
        print(e)

    invalid_sequence = "GASX"
    try:
        mass = calculate_protein_mass(invalid_sequence)
        print(f"The mass of {invalid_sequence} is {mass:.2f} amu.")
    except ValueError as e:
        print(f"Invalid sequence {e}")

    input("Press enter to exit.")
