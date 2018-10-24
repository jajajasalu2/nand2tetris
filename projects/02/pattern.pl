$val = $ARGV[0];
$carry = $val - 1;
$string = qq{
        Xor(a=xout$val,b=yout$val,out=xxory$val);
        Xor(a=xxory$val,b=carry$carry,out=xplusy$val);
        And(a=xxory$val,b=carry$carry,out=xyand$val);
        Or(a=xyand$val,b=xandy$val,out=carry$val);
};

    print STDOUT $string;
