# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"2DB6.00","system":"readv2"},{"code":"H030.00","system":"readv2"},{"code":"H035000","system":"readv2"},{"code":"H031.00","system":"readv2"},{"code":"H032.00","system":"readv2"},{"code":"A340300","system":"readv2"},{"code":"H140.00","system":"readv2"},{"code":"AA1z.12","system":"readv2"},{"code":"H036.00","system":"readv2"},{"code":"H14y500","system":"readv2"},{"code":"Hyu0200","system":"readv2"},{"code":"h03..00","system":"readv2"},{"code":"A383000","system":"readv2"},{"code":"H03..12","system":"readv2"},{"code":"H035100","system":"readv2"},{"code":"H035z00","system":"readv2"},{"code":"H03..11","system":"readv2"},{"code":"H03..00","system":"readv2"},{"code":"H033.00","system":"readv2"},{"code":"H143.00","system":"readv2"},{"code":"H037.00","system":"readv2"},{"code":"H034.00","system":"readv2"},{"code":"H035.00","system":"readv2"},{"code":"H14y600","system":"readv2"},{"code":"H03z.00","system":"readv2"},{"code":"0340BT","system":"readv2"},{"code":"463 AP","system":"readv2"},{"code":"501 PD","system":"readv2"},{"code":"463 A","system":"readv2"},{"code":"463 MP","system":"readv2"},{"code":"463 NF","system":"readv2"},{"code":"463 B","system":"readv2"},{"code":"101 TN","system":"readv2"},{"code":"463 BC","system":"readv2"},{"code":"500 CH","system":"readv2"},{"code":"500 B","system":"readv2"},{"code":"463","system":"readv2"},{"code":"0340T","system":"readv2"},{"code":"463 AL","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cold-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cold-tonsil---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cold-tonsil---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cold-tonsil---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
