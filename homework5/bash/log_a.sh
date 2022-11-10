#! /bin/bash

cur_dir="$( cd "$( dirname "$0" )" && pwd )"
log="$cur_dir"/access.log
res="$cur_dir"/res_bash.txt

echo "Total number of requests" > "$res"
cat "$log" | wc -l >> "$res"

echo -e "\nTotal number of requests by type" >> "$res"
cat "$log" | awk '{print $6}' | awk 'length($0) < 12' | sed -e 's/^.//' | sort \
| uniq -c | awk '{printf "%-4s - %d\n", $2, $1}' >> "$res"

echo -e "\nTop 10 most frequent requests" >> "$res"
cat "$log" | awk '{print $7}' | grep -Po '[^?#]*' | sort | uniq -c | sort -n -r \
| head -n 10| awk '{printf "%s\n%d\n", $2, $1}' >> "$res"

echo -e "\nTop 5 largest requests in size that ended with a client (4XX) error" >> "$res"
cat "$log" | awk '{if ($9 ~ /4../) print $7, $9, $10, $1}' | sort -nrk3 | head -n 5 \
| awk '{printf "%s\n%s\n%s\n%s\n", $1, $2, $3, $4}' >> "$res"

echo -e "\nTop 5 users by the number of requests that ended with a server (5XX) error" >> "$res"
cat "$log" | awk '{if ($9 ~ /5../) print $1}' | sort | uniq -c | sort -nr \
| head -n 5 | awk '{printf "%s\n%s\n", $2, $1}' >> "$res"
