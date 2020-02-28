#Change the OS configuration so that it is possible to login with user holberton
exec { 'change soft and hard limit':
  command  => "sed -i 's/holberton soft nofile 4/holberton soft nofile 10000/g'
  /etc/security/limits.conf;
  sed -i 's/holberton hard nofile 5/holberton hard nofile 30000/g'
  /etc/security/limits.conf",
  provider => 'shell',
}