<h1 class="gap">0x05. Processes and signals</h1>
<h2 class="gap">Tasks</h2>
<p>0. Write a Bash script that displays its own PID.</p>

<p>1. Write a Bash script that displays a list of currently running processes.</p>
<p>2. Using your previous exercise command, write a Bash script that displays lines containing the <code>bash</code> word, thus allowing you to easily get the PID of your Bash process.</p>
<p>3. Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word <code>bash</code>.</p>
<p>4. Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>
<p>5. We stopped our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>

<p>Write a Bash script that stops <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>kill</code></li>
</ul>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./5-dont_stop_me_now 
sylvain@ubuntu$ 
</code></pre>
<p>6. Write a Bash script that stops <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>kill</code> or <code>killall</code></li>
</ul>
<p>7. Write a Bash script that displays: </p>

<ul>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
</ul>

<p>Make a copy of your <code>6-stop_me_if_you_can</code> script, name it <code>67-stop_me_if_you_can</code>,  that kills the <code>7-highlander</code> process instead of the <code>4-to_infinity_and_beyond</code> one.</p>
<p>8. Write a Bash script that kills the process <code>7-highlander</code>.</p>
<p>100. Write a Bash script that: </p>

<ul>
<li>Creates the file <code>/var/run/myscript.pid</code> containing its PID</li>
<li>Displays <code>To infinity and beyond</code> indefinitely</li>
<li>Displays <code>I hate the kill command</code> when receiving a SIGTERM signal</li>
<li>Displays <code>Y U no love me?!</code> when receiving a SIGINT signal</li>
<li>Deletes the file <code>/var/run/myscript.pid</code> and terminates itself when receiving a SIGQUIT or SIGTERM signal</li>
</ul>
<p>101. Write a <code>manage_my_process</code> Bash script that: </p>

<ul>
<li>Indefinitely writes <code>I am alive!</code> to the file <code>/tmp/my_process</code></li>
<li>In between every <code>I am alive!</code> message, the program should pause for 2 seconds</li>
</ul>

<p>Write Bash (init) script <code>101-manage_my_process</code> that manages <code>manage_my_process</code>. (both files need to be pushed to git)</p>

<p>Requirements:</p>

<ul>
<li>When passing the argument <code>start</code>:

<ul>
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process started</code></li>
</ul></li>
<li>When passing the argument <code>stop</code>: 

<ul>
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process stopped</code></li>
</ul></li>
<li>When passing the argument <code>restart</code>

<ul>
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process restarted</code></li>
</ul></li>
<li>Displays <code>Usage: manage_my_process {start|stop|restart}</code> if any other argument or no argument is passed</li>
</ul>

<p>Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing <code>./101-manage_my_process start</code>, in our case it will simply create a new process instead of saying that it is already started.</p>
<p>102. Write a C program that creates 5 zombie processes.</p>

<p>Requirements:</p>

<ul>
<li>For every zombie process created, it displays <code>Zombie process created, PID: ZOMBIE_PID</code></li>
<li>Your code should use the Betty style. It will be checked using <code>betty-style.pl</code> and <code>betty-doc.pl</code></li>
<li>When your code is done creating the parent process and the zombies, use the function bellow</li>
</ul>

<pre><code>int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
</code></pre>
