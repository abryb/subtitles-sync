Simple script to resynchronize subtitles.

Given subtitles in format as below.

> subtitles.txt
```text 
// ...
00:02:03:Lorem ipsum dolor
00:02:04:Lorem ipsum dolor
// ... 
```

```shell script
# add 10 seconds
python3 subtitle-sync.py subtitles.txt +10 > subtitles2.txt
# subtract 5 seconds
python3 subtitle-sync.py subtitles.txt -5 > subtitles2.txt
# save to same file
python3 subtitle-sync.py subtitles.txt +10 --save 
```

