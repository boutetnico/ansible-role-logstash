import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('logstash'),
])
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('username,groupname,path', [
  ('root', 'root', '/etc/logstash/logstash.yml'),
  ('root', 'root', '/etc/logstash/log4j2.properties'),
  ('root', 'root', '/etc/logstash/jvm.options'),
])
def test_logstash_config_file(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize('name', [
  ('logstash-input-github'),
  ('logstash-filter-dissect'),
])
def test_logstash_plugin_exists(host, name):
    command = '/usr/share/logstash/bin/logstash-plugin list'
    plugins_list = host.check_output(command)
    assert name in plugins_list
