
rnaToAminoAcid = {"UUU":"Phenylalanine", "UUC":"Phenylalanine", "UUA":"Leucine", 
    "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine",
    "UAU":"Tyrosine", "UAC":"Tyrosine", "UAA":"STOP", "UAG":"STOP",
    "UGU":"Cysteine", "UGC":"Cysteine", "UGA":"STOP", "UGG":"Tryptophan",
    "CUU":"Leucine", "CUC":"Leucine", "CUA":"Leucine", "CUG":"Leucine",
    "CCU":"Proline", "CCC":"Proline", "CCA":"Proline", "CCG":"Proline",
    "CAU":"Histidine", "CAC":"Histidine", "CAA":"Glutamine", "CAG":"Glutamine",
    "CGU":"Arginine", "CGC":"Arginine", "CGA":"Arginine", "CGG":"Arginine",
    "AUU":"Isoleucine", "AUC":"Isoleucine", "AUA":"Isoleucine", "AUG":"Methionine",
    "ACU":"Threonine", "ACC":"Threonine", "ACA":"Threonine", "ACG":"Threonine",
    "AAU":"Asparagine", "AAC":"Asparagine", "AAA":"Lysine", "AAG":"Lysine",
    "AGU":"Serine", "AGC":"Serine", "AGA":"Arginine", "AGG":"Arginine",
    "GUU":"Valine", "GUC":"Valine", "GUA":"Valine", "GUG":"Valine",
    "GCU":"Alanine", "GCC":"Alanine", "GCA":"Alanine", "GCG":"Alanine",
    "GAU":"Aspartic Acid", "GAC":"Aspartic Acid", "GAA":"Glutamic Acid", 
    "GAG":"Glutamic Acid", "UUG":"Leucine",
    "GGU":"Glycine", "GGC":"Glycine", "GGA":"Glycine", "GGG":"Glycine",}

def ribosomeSM(input):
    state = "NotReadingYet"
    firstround=0
    result = []
    done = 0
    old = ''
    older = ''
    temp = ''

    for i in input:

        if i=='G' and old=='U' and older=='A'and firstround == 0:
            state = "Start"
            temp = 'AU'
            done = 0
            firstround = 1
        
        if state == "NotReadingYet":
            result.append(None)
        
        if done>0:
            result.append(None)
        
        if state == "Start":
            temp = temp + i
            if len(temp)==3 :
                if rnaToAminoAcid[temp] != 'STOP':
                    result.append(rnaToAminoAcid[temp])
                    temp = ''
                else: 
                    done = 1
        
        older = old
        old = i
    
    return result
    
    
    
    
    
print(ribosomeSM("AGUUAUGCCGCAUAGCCGAAACUAGAAAAAAA"))










"""
Ribosomes
by skylargordon
"""
