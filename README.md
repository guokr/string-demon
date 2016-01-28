This is the string feature extracting project for later maching learning algorithms.

sample:

```
import string_demon as sd

str1 = "我住在北方，夜晚听见窗外的雨声，让我想起了南方。May the force be with you....""
print sd.spam_check(str1)
```

> (0.9047619047619048, 2.6246719160104988, 4.833333333333333, 0.7241379310344828)
return refer to: (中文重复率，中文停顿长度，英文停顿长度，中英文长度比)


```
import string_demon as sd

str2 = "我住在南方，我住在南方。"

print sd.lcs_check(str2)
```

> (2, '\xe6\x88\x91\xe4\xbd\x8f\xe5\x9c\xa8\xe5\x8d\x97\xe6\x96\xb9', 5)
> return refer to: (重复次数，LCS，LCS.length)
