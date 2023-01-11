<h1>0x0B. SSH</h1>
<h2>Tasks</h2>
<p>0. Write a Bash script that uses <code>ssh</code> to connect to your server using the private key <code>~/.ssh/school</code> with the user <code>ubuntu</code>.</p>
    <p>1. Write a Bash script that creates an RSA key pair.</p>

<p>Requirements:</p>

<ul>
<li>Name of the created private key must be <code>school</code></li>
<li>Number of bits in the created key to be created 4096</li>
<li>The created key must be protected by the passphrase <code>betty</code></li>
</ul>
<p>2. SSH configuration connect to a server without typing a password.</p>
<p>3. Add the SSH public key below to your server so that we can connect using the <code>ubuntu</code> user.</p>

<pre><code>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
</code></pre>
<p>4. Client configuration file with <code>Puppet</code></p>
