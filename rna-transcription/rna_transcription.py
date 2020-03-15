def to_rna(dna_strand):
    rna_transcription = ''
    for nucleotides in dna_strand:
        if nucleotides is 'C': rna_transcription += 'G'
        if nucleotides is 'G': rna_transcription += 'C'
        if nucleotides is 'T': rna_transcription += 'A'
        if nucleotides is 'A': rna_transcription += 'U'

    return rna_transcription
