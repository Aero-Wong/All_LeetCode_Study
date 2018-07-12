<<!
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
For example, assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:
the 4
is 3
sunny 2
day 1
Note:
Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.

[show hint]

Hint:
Could you write it in one-line using Unix pipes?
!

# Read from the file words.txt and output the word frequency list to stdout.

# Read from the file words.txt and output the word frequency list to stdout.
# 使用sed或者tr将文件的空空格用换行符替换 删除多余的空行
# 使用uniq对文件每行重复的字数进行统计
# 使用awk格式化输出
cat words.txt | tr -s ' ' '\n' |sort| uniq -c | sort -rn | awk '{print $2, $1}'

awk '{for(i=1;i<=NF;++i){++m[$i]}}END{for(k in m){print k, m[k}}' words.txt | sort -nr -k 2

<<! 
awk 是逐行检索文本。分为3的部分。 
BEGIN{#这里进行一些检索文本前的初始化操作} 
{#这里是对应每一行的操作}。例如这里 for(i=1;i<=NF;++i){++m[$i]}就是将每一行分隔的字段，进行词频统计。 
NF是分隔的字段数。 
$0表示整行字符串 
$1到$NF表示从分隔的第一个字符串到最后一个字符串 
awk中的数组可以用作hashtable做来词频统计。 
END{#在检索文本后的操作} 
for(k in m) k表示的就是m的key。
sort语法复习 
sort -n 将字符串转数字 
sort -r 指定顺序为从大到小 
sort -k 2 指定第二个字段作为排序判断标准

tr -s ' ' '\n' 是将所有连续的空格 空行删除并保证每一行只有一个字符串 
sort | uniq -c 通常一起用来统计重复出现的次数。
!
 