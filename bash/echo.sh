#! /bin/bash
echo -n "wellcome to bash"
echo " my name is munna"

echo -e "Perl\tis\ta\tpowerful\tand\tportable\tlanguage"

# echo -E "Perl\tis\ta\tpowerful\tand\tportable\tlanguage"
printf "Perl\tis\ta\tpowerful\tand\tportable\tlanguage"

export price="\$100"
echo $price

echo "The price of this book is $price"

echo -e "Linuxhint\v is \v a \v linux \v based \v blog \v site."
echo -e "Enrich your Linux knowledge from Linuxhint\ctutorials"


string="\rPerl is a cross-platform, open-source programming language\r"
echo -e "$string"