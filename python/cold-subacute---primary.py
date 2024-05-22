# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"H023z00","system":"readv2"},{"code":"F520300","system":"readv2"},{"code":"H023100","system":"readv2"},{"code":"H022.00","system":"readv2"},{"code":"F510z00","system":"readv2"},{"code":"H013.00","system":"readv2"},{"code":"H040300","system":"readv2"},{"code":"H012.00","system":"readv2"},{"code":"H051.00","system":"readv2"},{"code":"F510000","system":"readv2"},{"code":"H050.00","system":"readv2"},{"code":"H040x00","system":"readv2"},{"code":"H010.00","system":"readv2"},{"code":"H041100","system":"readv2"},{"code":"F520100","system":"readv2"},{"code":"H04..00","system":"readv2"},{"code":"H00..12","system":"readv2"},{"code":"H040600","system":"readv2"},{"code":"F510200","system":"readv2"},{"code":"F510400","system":"readv2"},{"code":"F520.00","system":"readv2"},{"code":"H042z00","system":"readv2"},{"code":"H020.00","system":"readv2"},{"code":"H01y000","system":"readv2"},{"code":"H02..00","system":"readv2"},{"code":"F510600","system":"readv2"},{"code":"H041z00","system":"readv2"},{"code":"H023.00","system":"readv2"},{"code":"F526.00","system":"readv2"},{"code":"H010.11","system":"readv2"},{"code":"H042000","system":"readv2"},{"code":"H01y.00","system":"readv2"},{"code":"H04z.00","system":"readv2"},{"code":"F525.00","system":"readv2"},{"code":"H040500","system":"readv2"},{"code":"H00..00","system":"readv2"},{"code":"H024.00","system":"readv2"},{"code":"H011.00","system":"readv2"},{"code":"H042100","system":"readv2"},{"code":"H01..00","system":"readv2"},{"code":"H043.00","system":"readv2"},{"code":"H00..14","system":"readv2"},{"code":"H05..00","system":"readv2"},{"code":"H043z00","system":"readv2"},{"code":"F520000","system":"readv2"},{"code":"F520z00","system":"readv2"},{"code":"H040200","system":"readv2"},{"code":"H040w00","system":"readv2"},{"code":"F510500","system":"readv2"},{"code":"H02z.00","system":"readv2"},{"code":"H021.00","system":"readv2"},{"code":"F510100","system":"readv2"},{"code":"F528.00","system":"readv2"},{"code":"H043200","system":"readv2"},{"code":"H040100","system":"readv2"},{"code":"H040.00","system":"readv2"},{"code":"H01yz00","system":"readv2"},{"code":"FyuP000","system":"readv2"},{"code":"H040z00","system":"readv2"},{"code":"H01z.00","system":"readv2"},{"code":"H041.00","system":"readv2"},{"code":"H043000","system":"readv2"},{"code":"H041000","system":"readv2"},{"code":"H040000","system":"readv2"},{"code":"H042.00","system":"readv2"},{"code":"H023000","system":"readv2"},{"code":"F510300","system":"readv2"},{"code":"F510011","system":"readv2"},{"code":"H043100","system":"readv2"},{"code":"f528.00","system":"readv2"},{"code":"H00..16","system":"readv2"},{"code":"3810TP","system":"readv2"},{"code":"462 CT","system":"readv2"},{"code":"3810ML","system":"readv2"},{"code":"3810","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cold-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cold-subacute---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cold-subacute---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cold-subacute---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
