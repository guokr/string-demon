This is the string feature extracting project for later maching learning algorithms.

sample:

```
import string_demon as sd

str1 = "我住在北方，夜晚听见窗外的雨声，让我想起了南方。May the force be with you....""
str2 = "

print sd.spam_check(str1)
```

> ((0.9047619047619048, 2.6246719160104988, 4.833333333333333, 0.7241379310344828), (2, '\x97\xe6\x96\xb9', 1))

return refer to: ((中文重复率，中文每隔若干个词会停顿，英文每隔若干个词会停顿，中英文长度比), (重复次数，LCS，LCS.length))
