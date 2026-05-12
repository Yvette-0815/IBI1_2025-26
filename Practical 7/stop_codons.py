input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

def parse_fasta(filename):
    sequences = {}
    with open(filename, 'r') as f:
        current_id = None
        current_seq = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_id is not None:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id is not None:
            sequences[current_id] = ''.join(current_seq)
    return sequences

def inframe_stop(seq):
    seq = seq.upper().replace('T', 'U')
    stop_codons = ['UAA', 'UAG', 'UGA']
    found_stops = set()
    for frame in range(3):
        for i in range(frame, len(seq) - 2,3):
            codon = seq[i:i+3]
            if codon in stop_codons:
                found_stops.add(codon)
    return found_stops

all_genes = parse_fasta(input_file)
with open(output_file, 'w') as out_f:
    for gene_id, sequence in all_genes.items():
        stops = inframe_stop(sequence)
        if stops:
            stop_str=''.join(sorted(stops))
            out_f.write(f">{gene_id}; {stop_str}\n")
            out_f.write(f"{sequence}\n")

input("Press enter to exit.")