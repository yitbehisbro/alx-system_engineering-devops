<h1 class=gap>0x08. Networking basics #1</h1>
<h2>Tasks</h2>
<p>0. Write a Bash script that configures an Ubuntu server with the below requirements.</p>

<p>Requirements:</p>

<ul>
<li><code>localhost</code> resolves to <code>127.0.0.2</code></li>
<li> <code>facebook.com</code> resolves to <code>8.8.8.8</code>.</li>
<li> The checker is running on Docker, so make sure to read <a href="http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/" title="this" target="_blank">this</a></li>
</ul>
<p>1. Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.</p>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
</code></pre>
 <p>100. Write a Bash script that listens on port <code>98</code> on <code>localhost</code>.</p>

<p><strong>Terminal 0</strong></p>

<p>Starting my script.</p>

<pre><code>sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
</code></pre>

<p><strong>Terminal 1</strong></p>

<p>Connecting to <code>localhost</code> on port <code>98</code> using <code>telnet</code> and typing some text.</p>

<pre><code>sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
</code></pre>

<p><strong>Terminal 0</strong></p>

<p>Receiving the text on the other side.</p>

<pre><code>sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
</code></pre>
