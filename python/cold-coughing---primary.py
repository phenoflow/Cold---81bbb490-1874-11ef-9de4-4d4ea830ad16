# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"171J.00","system":"readv2"},{"code":"171G.00","system":"readv2"},{"code":"1712.00","system":"readv2"},{"code":"R062000","system":"readv2"},{"code":"171A.00","system":"readv2"},{"code":"171H.00","system":"readv2"},{"code":"171..00","system":"readv2"},{"code":"171E.00","system":"readv2"},{"code":"171Z.00","system":"readv2"},{"code":"R062.00","system":"readv2"},{"code":"171..11","system":"readv2"},{"code":"7833CH","system":"readv2"},{"code":"7833AP","system":"readv2"},{"code":"7833PT","system":"readv2"},{"code":"7833HP","system":"readv2"},{"code":"7833PE","system":"readv2"},{"code":"7833AR","system":"readv2"},{"code":"7833DP","system":"readv2"},{"code":"7833DF","system":"readv2"},{"code":"7833CD","system":"readv2"},{"code":"7833A","system":"readv2"},{"code":"7834AH","system":"readv2"},{"code":"7833DB","system":"readv2"},{"code":"791 CH","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cold-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cold-coughing---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cold-coughing---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cold-coughing---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
