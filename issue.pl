#!/usr/bin/env perl


$count=0;
foreach(<STDIN>){
    @list=split(/\t/,$_);
    $title = $list[7];
    $img = $list[11];
    $pm = $list[14];
    $dev = $list[15];
    $prio = $list[1];
    $tag = $list[10];

    print("$count $title\n\n");
    $filename ="/tmp/issue_$count";
    open(my $fh, '>:encoding(UTF-8)', $filename)  or die "Could not open file '$filename' $!";

    $message = "$title\n\nIMG:$img\n\nPM:$pm\n\nDEV:$dev\n\n";
    print $fh $message;
    $count = $count+1;
    close $fh;

}
