my $page = `wget https://www.nand2tetris.org/course`;
my $fh,'<','index.html';
while ($line = <$fh>) {
if ($line =~ m/(https:\/\/docs\.wixstatic\.com\/.?\.pdf)/) {
    #my $link = $1;
    #`wget $link`;
    print $1;
}
}
