<h1> About Bash projects </h1>
Resources
Read or watch:

<a href="http://linuxcommand.org/lc3_lts0070.php" style = "color: red" >Shell, I/O Redirection</a><br/>
<a href="http://mywiki.wooledge.org/BashGuide/SpecialCharacters" style = "color: red"> Special Characters</a><br/>
man or help:<br/>

echo<br/>
cat<br/>
head<br/>
tail<br/>
find<br/>
wc<br/>
sort<br/>
uniq<br/>
grep<br/>
tr<br/>
rev<br/>
cut<br/>
passwd (5) (i.e. man 5 passwd)<br/>
<h2>Learning Objectives</h2>
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:<br/>

Shell, I/O Redirection<br/>
What do the commands head, tail, find, wc, sort, uniq, grep, tr do<br/>
How to redirect standard output to a file<br/>
How to get standard input from a file instead of the keyboard<br/>
How to send the output from one program to the input of another program<br/>
How to combine commands and filters with redirections<br/>
Special Characters<br/>
What are special characters<br/>
Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them<br/>
Other Man Pages<br/>
How to display a line of text<br/>
How to concatenate files and print on the standard output<br/>
How to reverse a string<br/>
How to remove sections from each line of files<br/>
What is the /etc/passwd file and what is its format<br/>
What is the /etc/shadow file and what is its format<br/>
<h3>Copyright - Plagiarism</h3>
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.<br/>
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.<br/>
You are not allowed to publish any content of this project.<br/>
Any form of plagiarism is strictly forbidden and will result in removal from the program.<br/>
<h3>Requirements</h3>
General
Allowed editors: vi, vim, emacs<br/>
All your scripts will be tested on Ubuntu 20.04 LTS<br/>
All your scripts should be exactly two lines long ($ wc -l file should print 2)<br/>
All your files should end with a new line (why?)<br/>
The first line of all your files should be exactly #!/bin/bash<br/>
A README.md file, at the root of the folder of the project, describing what each script is doing<br/>
You are not allowed to use backticks, &&, || or ;<br/>
All your files must be executable<br/>
You are not allowed to use sed or awk<br/>
<b>More Info</b><br />
Read your /etc/passwd and /etc/shadow files.<br/>

Note: You do not have to learn about fmt, pr, du, gzip, tar, lpr, sed and awk yet.<br/>

0. Write a script that prints “Hello, World”, followed by a new line to the standard output.
1. Write a script that displays a confused smiley "(Ôo)'.
2. Display the content of the /etc/passwd file.
3. Display the content of /etc/passwd and /etc/hosts
4. Display the last 10 lines of /etc/passwd
5. Display the first 10 lines of /etc/passwd
6. Write a script that displays the third line of the file iacta.
    The file iacta will be in the working directory<br/>
    You’re not allowed to use sed<br/>
7. Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
8. Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
9. Write a script that duplicates the last line of the file iacta
    The file iacta will be in the working directory<br/>
10. Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
11. Write a script that counts the number of directories and sub-directories in the current directory.
    The current and parent directories should not be taken into account
    Hidden directories should be counted
12. Create a script that displays the 10 newest files in the current directory.
    Requirements:
       One file per line<br/>
       Sorted from the newest to the oldest
13. Create a script that takes a list of words as input and prints only words that appear exactly once.
    Input format: One line, one word<br/>
    Output format: One line, one word<br/>
    Words should be sorted
14. Display lines containing the pattern “root” from the file /etc/passwd
15. Display the number of lines that contain the pattern “bin” in the file /etc/passwd
16. Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
17. Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
18. Display all lines of the file /etc/ssh/sshd_config starting with a letter.<br/>
      include capital letters as well
19. Replace all characters A and c from input to Z and e respectively.
20. Create a script that removes all letters c and C from input.
21. Write a script that reverse its input.
22. Write a script that displays all users and their home directories, sorted by users.<br/>
      Based on the the /etc/passwd file
23. Write a command that finds all empty files and directories in the current directory and all sub-directories.
      Only the names of the files and directories should be displayed (not the entire path)<br/>
      Hidden files should be listed<br/>
      One file name per line<br/>
      The listing should end with a new line<br/>
      You are not allowed to use basename, grep, egrep, fgrep or rgrep<br/>
24. Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
     Hidden files should be listed<br/>
     Only regular files (not directories) should be listed<br/>
     The names of the files should be displayed without their extensions<br/>
     The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)<br/>
     One file name per line<br/>
     The listing should end with a new line<br/>
     You are not allowed to use basename, grep, egrep, fgrep or rgrep<br/>
25. An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. <a href="https://en.wikipedia.org/wiki/Acrostic" >Read more.</a>
      Create a script that decodes acrostics that use the first letter of each line.<br/>
          The ‘decoded’ message has to end with a new line<br/>
          You are not allowed to use grep, egrep, fgrep or rgrep<br/>
