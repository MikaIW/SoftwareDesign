# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle
from load import load_seq

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:


        output = output + s
    return output
    
def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    aminoacids = []
    
    for i in range (0,len(dna)/3):
        start = 3*i
        stop = 3*i + 3
        dna3 = dna[start:stop]
        
        for n in range (0,len(aa)):
            if dna3 in codons[n]:
                aminoacids.append(aa[n])
                
    return collapse(aminoacids)
        

def get_amino_acid_for_codon(codon):
    if codon == 'TTT' or codon == 'TTC':
        return 'F'


def coding_strand_to_AA_unit_tests(inp,expout):
    """ Unit tests for the coding_strand_to_AA function """
    """ inp = input, expout = expected output"""
    print 'input: ' + inp + ', expected output: ' + expout + ', actual output: ' + coding_strand_to_AA(inp)

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    reversedna = ""

    for i in range (0,len(dna)):
        x = dna[len(dna)-i-1]
        if x == 'A':
            reversedna += 'T'
        elif x == 'T':
            reversedna += 'A'
        elif x == 'G':
            reversedna += 'C'
        elif x == 'C':
            reversedna += 'G'
                
    return reversedna
    
def get_reverse_complement_unit_tests(inp,expout):
    """ Unit tests for the get_complement function """
    """ inp = input, expout = expected output"""
        
    print 'input: ' + inp + ', expected output: ' + expout + ', actual output: ' + get_reverse_complement(inp)

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    openref = ""
    
    for i in range (0,len(dna)/3):
        start = 3*i
        stop = 3*i + 3
        dnaopen = dna[start:stop]
        if dnaopen in codons[10]:
            openref += dna[0:start]
    
    if openref == "":
        return dna
    else:
        return openref
            
        
def rest_of_ORF_unit_tests(inp, expout):
    """ Unit tests for the rest_of_ORF function """
        
    print 'input: ' + inp + ', expected output: ' + expout + ', actual output: ' + rest_of_ORF(inp)
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    oneframe = []
    
    i = 0
    
    while i < len(dna)/3:
        start = 3*i
        stop = 3*i + 3
        dna2 = dna[start:stop]
        if dna2 == 'ATG':
            oneframe.append(rest_of_ORF(dna[start:]))
            i = i + len(oneframe[len(oneframe)-1])/3
        i += 1
            
    return oneframe
     
    
def find_all_ORFs_oneframe_unit_tests(inp,expout):
    """ Unit tests for the find_all_ORFs_oneframe function """

    print 'input: ' + inp + ', expected output: ' 
    print expout
    print ', actual output: '
    print find_all_ORFs_oneframe(inp)

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    allORFs = []
    
    i = 0
    
    while i < len(dna)-2:
        start = i
        stop = i + 3
        dna2 = dna[start:stop]
        if dna2 == 'ATG':
            allORFs.append(rest_of_ORF(dna[start:]))
            i = i + len(allORFs[len(allORFs)-1]) - 2
        i += 1
            
    return allORFs

def find_all_ORFs_unit_tests(inp,expout):
    """ Unit tests for the find_all_ORFs function """
        
    print 'input: ' + inp + ', expected output: ' 
    print expout
    print ', actual output: '
    print find_all_ORFs(inp)

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    A = find_all_ORFs(dna)
    B = find_all_ORFs(get_reverse_complement(dna))
    A.extend(B)

    return A


def find_all_ORFs_both_strands_unit_tests(inp,expout):

    """ Unit tests for the find_all_ORFs_both_strands function """

    print 'input: ' + inp + ', expected output: ' 
    print expout
    print ', actual output: '
    print find_all_ORFs_both_strands(inp)

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    if len(find_all_ORFs_both_strands(dna)) == 0:
        return ""
    A = max(find_all_ORFs_both_strands(dna),key=len)
    return A

def longest_ORF_unit_tests(inp,expout):
    """ Unit tests for the longest_ORF function """

    print 'input: ' + inp + ', expected output: ' 
    print expout
    print ', actual output: '
    print longest_ORF(inp)

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    x = list(dna)
    longestORF = ''
    longestORFlength = 0
    
    for i in range (0,num_trials):
        shuffle(x)
        orf = longest_ORF(x)
        if len(orf)>longestORFlength:
            longestORFlength = len(orf)
            longestORF = orf
     
    return len(longestORF)/3
    

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    genefinder = []
    
    a = find_all_ORFs_both_strands(dna) #list of ORFs
    A = max(find_all_ORFs_both_strands(dna),key=len) #max value from a
    
    if len(a) == 0:
        return [] #in case of empty list
    if len(A) < threshold:
        return [] #in case the max value is still smaller than the threshold
        
    for i in range (0,len(a)):
        x = a[i] #ith element of list a
        if len(x) > threshold:
            genefinder.append(coding_strand_to_AA(x))
            
    return genefinder