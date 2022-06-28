<html>

<body>
<article class="">
<h1>0x03. Shell, init files, variables and expansions</h1>
<h2>About Bash projects</h2>
<p>All the projects are auto-corrected with Ubuntu 20.04 LTS.</p>
  <div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="http://linuxcommand.org/lc3_lts0080.php" title="Expansions" target="_blank">Expansions</a> </li>
<li><a href="https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html" title="Shell Arithmetic" target="_blank">Shell Arithmetic</a> </li>
<li><a href="https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html" title="Variables" target="_blank">Variables</a> </li>
<li><a href="https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html" title="Shell initialization files" target="_blank">Shell initialization files</a> </li>
<li><a href="http://www.linfo.org/alias.html" title="The alias Command" target="_blank">The alias Command</a> </li>
<li><a href="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220628%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220628T091516Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3545d6b027220690ba395b8e84f43373917dee42564aba028d6ee9b9e006f6df" title="Technical Writing" target="_blank">Technical Writing</a></li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>printenv</code></li>
<li><code>set</code></li>
<li><code>unset</code></li>
<li><code>export</code></li>
<li><code>alias</code></li>
<li><code>unalias</code></li>
<li><code>.</code></li>
<li><code>source</code></li>
<li><code>printf</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/d8LWxAXk9_gsvpPw3ICdwQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What happens when you type <code>$ ls -l *.txt</code></li>
</ul>

<h3>Shell Initialization Files</h3>

<ul>
<li>What are the <code>/etc/profile</code> file and the <code>/etc/profile.d</code> directory</li>
<li>What is the <code>~/.bashrc</code> file</li>
</ul>

<h3>Variables</h3>

<ul>
<li>What is the difference between a local and a global variable</li>
<li>What is a reserved variable</li>
<li>How to create, update and delete shell variables</li>
<li>What are the roles of the following reserved variables: HOME, PATH, PS1</li>
<li>What are special parameters</li>
<li>What is the special parameter <code>$?</code>?</li>
</ul>

<h3>Expansions</h3>

<ul>
<li>What is expansion and how to use them</li>
<li>What is the difference between single and double quotes and how to use them properly</li>
<li>How to do command substitution with <code>$()</code> and backticks</li>
</ul>

<h3>Shell Arithmetic</h3>

<ul>
<li>How to perform arithmetic operations with the shell</li>
</ul>

<h3>The <code>alias</code> Command</h3>

<ul>
<li>How to create an alias</li>
<li>How to list aliases</li>
<li>How to temporarily disable an alias</li>
</ul>

<h3>Other <code>help</code> pages</h3>

<ul>
<li>How to execute commands from a file in the current shell</li>
</ul>

<h3>Copyright - Plagiarism</h3>

<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. </li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
<li>All your files should end with a new line (<a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">why?</a>)</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, describing what each script is doing</li>
<li>You are not allowed to use <code>&amp;&amp;</code>, <code>||</code> or <code>;</code></li>
<li>You are not allowed to use <code>bc</code>, <code>sed</code> or <code>awk</code></li>
<li>All your files must be executable</li>
</ul>

<h2>More Info</h2>

<p>Read your <code>/etc/profile</code>, <code>/etc/inputrc</code> and <code>~/.bashrc</code> files.</p>

<p>Look at some files in the <code>/etc/profile.d</code> directory.</p>

<p>Note: You do not have to learn about <code>awk</code>, <code>tar</code>, <code>bzip2</code>, <code>date</code>, <code>scp</code>, <code>ulimit</code>, <code>umask</code>, or shell scripting, yet.</p>

  </div>
</div>

0. Create a script that creates an alias.
     Name: ls <br/>
     Value: rm *<br/>
1. Create a script that prints hello user, where user is the current Linux user.
2. Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
3. Create a script that counts the number of directories in the PATH.
4. Create a script that lists environment variables.
5. Create a script that lists all local variables and environment variables, and functions.
6. Create a script that creates a new local variable.
    Name: BEST<br/>
    Value: School<br/>
7. Create a script that creates a new global variable.
    Name: BEST<br/>
    Value: School<br/>
8. Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
9. Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
<ul>
<li>POWER and DIVIDE are environment variables</li>
</ul>
10. Write a script that displays the result of BREATH to the power LOVE
<ul>
<li>BREATH and LOVE are environment variables</li>
<li>The script should display the result, followed by a new line</li>
</ul>
11. Write a script that converts a number from base 2 to base 10.

<ul>
<li>The number in base 2 is stored in the environment variable BINARY</li>
<li>The script should display the number in base 10, followed by a new line</li>
</ul>
12. Create a script that prints all possible combinations of two letters, except oo.

<ul>
<li>Letters are lower cases, from a to z</li>
<li>One combination per line</li>
<li>The output should be alpha ordered, starting with aa</li>
<li>Do not print oo</li>
<li>Your script file should contain maximum 64 characters</li>
</ul>
13. Write a script that prints a number with two decimal places, followed by a new line.<br/>
The number will be stored in the environment variable NUM.<br/>
14. Write a script that converts a number from base 10 to base 16.
<ul>
<li>The number in base 10 is stored in the environment variable DECIMAL</li>
<li>The script should display the number in base 16, followed by a new line</li>
</ul>
15. Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.
16. Write a script that prints every other line from the input, starting with the first line.
17. Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.
<ul>
<li>WATER is in base water</li>
<li>STIR is in base stir.</li>
<li>The result should be in base bestchol</li>
<ul>

</body>
</html>
