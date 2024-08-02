[![tests](https://github.com/boutetnico/ansible-role-logstash/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-logstash/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.logstash-blue.svg)](https://galaxy.ansible.com/boutetnico/logstash)

ansible-role-logstash
=====================

This role installs and configures [Logstash](https://www.elastic.co/guide/en/logstash/current/index.html).

Requirements
------------

Ansible 2.15 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| logstash_dependencies        | true     |                                 | list      | See `defaults/main.yml`.                      |
| logstash_package_state       | true     | `present`                       | string    | Use `latest` to upgrade logstash.             |
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
| logstash_extra_config        | true     | `{}`                            | dict      |                                               |

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
