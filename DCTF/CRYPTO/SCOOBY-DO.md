## ***SCOOBY-DOO***

```c
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in {1..22}
do
s=$(cat cipher.txt | cut -b "$i" | tr -d '\n')
  for x in {0..25}
  do
      c=${a:$x:1}
      if [[ $s == *"$c"* ]]
      then
          printf ''
      else
          printf ${a:$x:1}
      fi
   done
done
```

Flag : ***```DCTFTURINGWOULDBEPROUD```***
