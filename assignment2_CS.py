#!/usr/bin/env python3

'''
Assignment 2 - Medizinische Genomanalyse
von Clemens Spielvogel

VOR DEM AUSFUEHREN muss der absolute Pfad der vcf-Datei fuer die Variable vcf (Zeile 13) angegeben werden!
'''

import vcf

__author__ = 'Clemens Spielvogel'
vcf_path = "/home/vortex/Bioinformatik/med_genomanalyse/AmpliseqExome.20141120.NA24385.vcf"

class Assignment2:
    def __init__(self, vcf_path):
        # Check if pyvcf is installed
        print("PyVCF version: {}".format(vcf.VERSION))


    def get_average_quality_of_son(self):
        print("\n---------------\nAverage quality of son:")

        sum = 0
        count = 0
        for record in vcf.Reader(open(vcf_path, "r")):
            sum = sum + record.QUAL
            count += 1
        print(round(float(sum) / count, 2))
        return float(sum) / count


    def get_total_number_of_variants_of_son(self):
        print("\n---------------\nNumber of variants (son):")

        count = 0
        for record in vcf.Reader(open(vcf_path, "r")):
            count += 1
        print(count)
        return count


    def get_variant_caller_of_vcf(self):
        for line in vcf.Reader(open(vcf_path, "r"))._header_lines:
             if line.startswith("##source"):
                 return "-", str.split(line, '"')[1]


    def get_human_reference_version(self):
        print("\n---------------\nHuman reference version:")

        for line in vcf.Reader(open(vcf_path, "r"))._header_lines:
             if line.startswith("##reference=file://"):
                 print(str.split(line, '/')[6])
                 return str.split(line, '/')[6]


    def get_number_of_indels(self):
        print("\n---------------\nNumber of indels:")

        indels = 0
        for record in vcf.Reader(open(vcf_path, "r")):
            if record.is_indel:
                indels += 1
        print(indels)
        return indels


    def get_number_of_snvs(self):
        print("\n---------------\nNumber of SNVs:")

        snv = 0
        for record in vcf.Reader(open(vcf_path, "r")):
            if record.is_snp:
              snv += 1
        print(snv)
        return snv


    def get_number_of_heterozygous_variants(self):
        print("\n---------------\nNumber of heterozygous variants:")

        num_hetero = 0
        for record in vcf.Reader(open(vcf_path, "r")):
            num_hetero += record.num_het
        print(num_hetero)
        return num_hetero


    def print_summary(self):
        self.get_average_quality_of_son()
        self.get_total_number_of_variants_of_son()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()


if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2(vcf_path)
assignment1.print_summary()
