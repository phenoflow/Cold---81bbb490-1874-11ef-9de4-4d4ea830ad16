# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"H060.00","system":"readv2"},{"code":"H060.11","system":"readv2"},{"code":"H060D00","system":"readv2"},{"code":"H060x00","system":"readv2"},{"code":"H060300","system":"readv2"},{"code":"H060C00","system":"readv2"},{"code":"H060z00","system":"readv2"},{"code":"H302.00","system":"readv2"},{"code":"Hyu1000","system":"readv2"},{"code":"H060700","system":"readv2"},{"code":"H060600","system":"readv2"},{"code":"H060v00","system":"readv2"},{"code":"H060B00","system":"readv2"},{"code":"H06..00","system":"readv2"},{"code":"H300.00","system":"readv2"},{"code":"H060000","system":"readv2"},{"code":"H060A00","system":"readv2"},{"code":"H060100","system":"readv2"},{"code":"H060F00","system":"readv2"},{"code":"H060E00","system":"readv2"},{"code":"h060.00","system":"readv2"},{"code":"H060400","system":"readv2"},{"code":"H060w00","system":"readv2"},{"code":"H060200","system":"readv2"},{"code":"H301.00","system":"readv2"},{"code":"H060900","system":"readv2"},{"code":"H060500","system":"readv2"},{"code":"H06z.00","system":"readv2"},{"code":"466 BC","system":"readv2"},{"code":"490 T","system":"readv2"},{"code":"490 LT","system":"readv2"},{"code":"466 V","system":"readv2"},{"code":"466 FB","system":"readv2"},{"code":"490 CT","system":"readv2"},{"code":"490 WH","system":"readv2"},{"code":"466 C","system":"readv2"},{"code":"491 AC","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cold-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cold-laryngotracheobronchitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cold-laryngotracheobronchitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cold-laryngotracheobronchitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
