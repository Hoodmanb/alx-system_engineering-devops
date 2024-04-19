#puppet command that kill a process
exec {'killmenow':
path     => '/usr/bin',
command  => 'pkill killmenow',
provider => 'shell',
}
