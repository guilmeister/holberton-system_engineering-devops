#Using Puppet, create a manifest that kills a process named killmenow

exec {
    'killmenow':
    path    => '/bin:/usr/local/sbin:/usr/local/bin:
    /usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:
    /opt/vagrant_ruby/bin',
    command => 'pkill -f killmenow',
}