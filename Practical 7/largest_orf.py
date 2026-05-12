seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon = "AUG"
stop_codons = ["UAA", "UAG", "UGA"]

max_orf_length = 0
for i in range(len(seq)):
    if seq[i:i+3] == start_codon:
        for j in range(i+3, len(seq), 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                orf_length = j+3-i
                if orf_length > max_orf_length:
                    max_orf_length = orf_length
                break

print(f"The longest ORF is {max_orf_length} nucleotides long.")

input("Press enter to exit.")