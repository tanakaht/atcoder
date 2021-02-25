read a b
if [ $((a-2*b)) -gt 0 ]; then
    ans=$((a-2*b))
else
    ans=0
fi
echo $ans
