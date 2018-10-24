$val = 0;
$z = 0;
$a = 0;
$b = 1;
$c = 2;
$d = 3;
$e = 4;
$f = 5;
$g = 6;
$h = 7;
while ($val < 16) {
    $string = qq{
    And(a=notaddress0,b=out00$val,out=and$val$z$a);
    And(a=address[0],b=out10$val,out=and$val$z$b);
    And(a=notaddress0,b=out20$val,out=and$val$z$c);
    And(a=address[0],b=out30$val,out=and$val$z$d);
    Or(a=and$val$z$a,b=and$val$z$b,out=or$val$z$b);
    Or(a=and$val$z$c,b=and$val$z$d,out=or$val$z$c);
    And(a=notaddress1,b=or$val$z$b,out=x$val$z$b);
    And(a=address[1],b=or$val$z$c,out=x$val$z$c);
    Or(a=x$val$z$b,b=x$val$z$c,out=y$val$b);

    And(a=notaddress0,b=out40$val,out=and$val$z$e);
    And(a=address[0],b=out50$val,out=and$val$z$f);
    And(a=notaddress0,b=out60$val,out=and$val$z$g);
    And(a=address[0],b=out70$val,out=and$val$z$h);
    Or(a=and$val$z$e,b=and$val$z$f,out=or$val$z$d);
    Or(a=and$val$z$g,b=and$val$z$h,out=or$val$z$e);
    And(a=notaddress1,b=or$val$z$d,out=x$val$z$d);
    And(a=address[1],b=or$val$z$e,out=x$val$z$e);
    Or(a=x$val$z$d,b=x$val$z$e,out=y$val$c);

    Nand(a=notaddress2,b=y$val$b,out=nand$val$b);
    Nand(a=address[2],b=y$val$c,out=nand$val$c);
    Nand(a=nand$val$b,b=nand$val$c,out=out[$val]);
    };
    print STDOUT $string;
    $val++;
}
