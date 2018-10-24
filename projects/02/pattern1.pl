$file = $ARGV[0];
open $fh,'<',$file or die;
while ($line = <$fh>) {
    $line =~ s/out\[(\d+)\]/outin\1/g;
    print STDOUT $line;
}
