import pytest


@pytest.mark.parametrize("name", ["apt-transport-https", "gnupg", "python3-debian"])
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_logstash_package_installed(host):
    package = host.package("logstash")
    assert package.is_installed


def test_elastic_apt_repository_configured(host):
    """Test that Elastic APT repository is configured."""
    repo_file = host.file("/etc/apt/sources.list.d/elastic.sources")
    assert repo_file.exists
    assert repo_file.is_file
    content = repo_file.content_string
    assert "artifacts.elastic.co" in content


@pytest.mark.parametrize(
    "username,groupname,path,mode",
    [
        ("root", "root", "/etc/logstash/logstash.yml", 0o644),
        ("root", "root", "/etc/logstash/log4j2.properties", 0o644),
        ("root", "root", "/etc/logstash/jvm.options", 0o644),
    ],
)
def test_logstash_config_file(host, username, groupname, path, mode):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname
    assert config.mode == mode


def test_logstash_yml_content(host):
    """Test logstash.yml configuration content."""
    f = host.file("/etc/logstash/logstash.yml")
    content = f.content_string
    assert "path.data:" in content
    assert "path.logs:" in content


@pytest.mark.parametrize(
    "path,owner,group,mode",
    [
        ("/var/lib/logstash", "logstash", "logstash", 0o755),
        ("/var/log/logstash", "logstash", "root", 0o755),
    ],
)
def test_logstash_directories(host, path, owner, group, mode):
    d = host.file(path)
    assert d.exists
    assert d.is_directory
    assert d.user == owner
    assert d.group == group
    assert d.mode == mode


def test_logstash_user_and_group(host):
    """Test that logstash user and group exist."""
    user = host.user("logstash")
    group = host.group("logstash")
    assert user.exists
    assert group.exists
    assert user.group == "logstash"


@pytest.mark.parametrize(
    "name,version",
    [
        ("logstash-input-github", "3.0.11"),
        ("logstash-filter-dissect", None),
    ],
)
def test_logstash_plugin_exists(host, name, version):
    command = "/usr/share/logstash/bin/logstash-plugin list --verbose"
    plugins_list = host.check_output(command)
    assert name in plugins_list
    if version:
        assert version in plugins_list


def test_logstash_service(host):
    """Test that Logstash service is enabled and running."""
    service = host.service("logstash")
    assert service.is_enabled
    assert service.is_running
