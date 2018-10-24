open $fh,'<','assembler.py';
open $fw,'>','assembler2.py';
while ($line = <$fh>){

    $line =~ s/\[(\d?),(\d?),(\d?),(\d?),(\d?),(\d?),(\d?)\]/\"$1$2$3$4$5$6$7\"/g;
    $line =~ s/\[(\d?),(\d?),(\d?)\]/\"$1$2$3\"/g;
    print $fw $line;
}
close $fh;
close $fw;
