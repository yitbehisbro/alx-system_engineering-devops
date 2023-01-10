exec { 'pkill killmenow':
  path     => '/usr/bin',
  provider => shell,
  command  => 'pkill killmenow',
  returns  => [0, 1]
}
