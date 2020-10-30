def to_rna(dna_strand):
    rna_transcription = ''
    for nucleotides in dna_strand:
        if nucleotides == 'C':
            rna_transcription += 'G'

        if nucleotides == 'G':
            rna_transcription += 'C'

        if nucleotides == 'T':
            rna_transcription += 'A'

        if nucleotides == 'A':
            rna_transcription += 'U'

    return rna_transcription
