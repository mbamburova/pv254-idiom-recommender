cat idioms.txt | while read line
do
  printf "$line; "
  find . -type f -printf "\n%p\n" -exec cat {} \; | grep -P "$line" | wc -l
done
