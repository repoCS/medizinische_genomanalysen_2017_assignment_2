#!/usr/bin/env python3

import vcf

__author__ = 'Clemens Spielvogel'

class Assignment2:
    def __init__(self):
        # Check if pyvcf is installed
        print("PyVCF version: {}".format(vcf.VERSION))
        self.vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf", "r"))


    def get_average_quality_of_son(self):
        self.sum = 0
        self.count = 0
        for record in self.vcf:
            self.sum = self.sum + record.QUAL
            self.count += 1
        print(float(self.sum) / self.count)
        return float(self.sum) / self.count


    def get_total_number_of_variants_of_son(self):
        for record in self.vcf:
            self.count += 1
        print(self.count)
        return self.count


    def get_variant_caller_of_vcf(self):
        for line in self.vcf._header_lines:
             if line.startswith("##source"):
                 return "-", str.split(line, '"')[1]


    def get_human_reference_version(self):
        for line in self.vcf._header_lines:
             if line.startswith("##reference=file://"):
                 print(str.split(line, '/')[6])
                 return str.split(line, '/')[6]


    def get_number_of_indels(self):
        self.indels = 0
        for record in self.vcf:
            if record.is_indel:
                self.indels += 1
        print(self.indels)
        return self.indels


    def get_number_of_snvs(self):
        self.snv = 0
        for record in self.vcf:
            if record.is_snp:
              self.snv += 1
        print(self.snv)
        return self.snv


    def get_number_of_heterozygous_variants(self):
        self.num_hetero = 0
        for record in self.vcf:
            self.num_hetero += record.num_hetero
        print(self.num_hetero)
        return self.num_hetero


    def print_summary(self):
        self.get_average_quality_of_son()
        self.get_total_number_of_variants_of_son()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()                   # 1823
        self.get_number_of_snvs()                     # 36703
        self.get_number_of_heterozygous_variants()    # 23819


if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
assignment1.print_summary()
