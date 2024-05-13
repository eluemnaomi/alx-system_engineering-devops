# 0-strace_is_your_friend.pp

# Define a Puppet class to manage Apache configuration
class apache_config_fix {
    
    # Ensure Apache service is installed and running
    package { 'apache2':
        ensure => 'installed',
    }

    service { 'apache2':
        ensure => 'running',
        enable => true,
    }

    # Ensure Apache configuration file is correct
    file { '/etc/apache2/apache2.conf':
        ensure  => file,
        content => template('apache/apache2.conf.erb'),
        notify  => Service['apache2'],
    }

    # Define a custom fact to check if Apache is currently running
    # This fact will be used later to trigger the strace command
    # Only necessary if the system doesn't provide a built-in fact for Apache status
    # (e.g., `service_apache_status` or similar)
    fact { 'apache_running':
        setcode => 'ps aux | grep [a]pache2',
    }

    # Define the strace command to attach to Apache process
    exec { 'strace_apache':
        command     => 'strace -p $(pgrep apache2) -o /tmp/apache_strace.log',
        refreshonly => true,
        subscribe   => Fact['apache_running'],
    }
    
}
