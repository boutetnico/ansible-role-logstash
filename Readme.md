ansible-role-logstash
=====================

This role installs and configures Logstash.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| logstash_dependencies        | true     | `[apt-transport-https, gnupg]`  | list      |                                               |
| logstash_use_oss             | true     | `false`                         | bool      | Whether to use Open Source version or not.    |
| logstash_package_state       | true     | `present`                       | string    | Use `latest` to upgrade logstash.             |
| logstash_user                | true     | `logstash`                      | bool      |                                               |
| logstash_user                | true     | `logstash`                      | string    |                                               |
| logstash_group               | true     | `logstash`                      | string    |                                               |
| logstash_secondary_groups    | true     | `[]`                            | list      |                                               |
| logstash_path_data           | true     | `/var/lib/logstash`             | string    |                                               |
| logstash_path_config         | true     | `/etc/logstash/conf.d`          | string    |                                               |
| logstash_path_logs           | true     | `/var/log/logstash`             | string    |                                               |
| logstash_log_level           | true     | `info`                          | string    |                                               |
| logstash_conf_fileglob       | true     | `files/*.conf`                  | string    |                                               |
| logstash_plugins             | true     | `[]`                            | list      |                                               |
| logstash_jvm_heap_size       | true     | `1g`                            | string    |                                               |

Dependencies
------------

Java 8+ or equivalent. For testing this roles uses `default-jre-headless` package.

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-logstash

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
