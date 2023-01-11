<h1 class="gap">0x0D. Web stack debugging #0</h1>
<h2 class="gap">Tasks</h2>
<p>0. In this first debugging project, you will need to get <a href="https://intranet.alxswe.com/rltoken/HVGgLL51qmuulmw802M-Jg" title="Apache" target="_blank">Apache</a> to run on the container and to return a page containing <code>Hello Holberton</code> when querying the root of it.</p>

<p>Example:</p>

<pre><code>vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080-&gt;80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
</code></pre>

<p>Here we can see that after starting my Docker container, I <code>curl</code> the port <code>8080</code> mapped to the Docker container port <code>80</code>, it does not return a page but an error message. Note that you might also get the error message <code>curl: (52) Empty reply from server</code>.</p>

<pre><code>vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
</code></pre>

<p>After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains <code>Hello Holberton</code>.
Paste the command(s) you used to fix the issue in your answer file.</p>
