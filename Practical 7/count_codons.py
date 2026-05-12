def parse_fasta(filename):
    genes = {}
    with open(filename) as f:
        gid = None
        seq = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if gid:
                    genes[gid] = "".join(seq)
                gid = line[1:].split()[0]
                seq = []
            else:
                seq.append(line)
        if gid:
            genes[gid] = "".join(seq)
    return genes

def longest_orf_for_stop(seq, stop_codon):
    seq = seq.upper()
    start = "ATG"
    max_len = 0
    best_orf = ""

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start:
            frame = i % 3
            for j in range(i + 3, len(seq) - 2, 3):
                if j % 3 == frame and seq[j:j+3] == stop_codon:
                    orf_len = j + 3 - i
                    if orf_len > max_len:
                        max_len = orf_len
                        best_orf = seq[i:j+3]
                    break
            break

    return best_orf

from collections import Counter

def count_codons(orf_seq):
    codons = [orf_seq[i:i+3] for i in range(0, len(orf_seq) - 2, 3)]
    return Counter(codons)

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def plot_pie(counter, stop_codon):
    labels = counter.keys()
    sizes = counter.values()
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, labeldistance=1.05, pctdistance=0.75, wedgeprops={'linewidth': 0})
    circle=Circle((0, 0), radius=1, fill=False, edgecolor='black', linewidth=1)
    plt.gca().add_patch(circle)
    plt.title(f"Codon Usage Upstream of {stop_codon}")
    plt.axis("equal")

    filename = f"codon_distribution_{stop_codon}.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.show()
    print(f"Pie chart saved as {filename}")

def main():
    stop_codon = input("Input a stop codon (TAA, TAG, or TGA): ").upper()
    if stop_codon not in {"TAA", "TAG", "TGA"}:
        print("Invalid stop codon.")
        return

    genes = parse_fasta("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")

    total_counter = Counter()

    for gene_id, seq in genes.items():
        orf = longest_orf_for_stop(seq, stop_codon)
        if orf:
            total_counter.update(count_codons(orf))

    if not total_counter:
        print("No valid ORFs found for this stop codon.")
        return

    plot_pie(total_counter, stop_codon)

if __name__ == "__main__":
    main()

input("Press enter to exit.")