exec { 'changing ulimit':
  command  => "sed -i 's/15/1000/g' /etc/default/nginx;
  sudo service nginx restart",
  provider => 'shell',
}
