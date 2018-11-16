import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_haproxy_config_file(host):
    f = host.file('/etc/haproxy/haproxy.cfg')

    assert f.exists
    assert f.contains('server  vm_tango_02  127.0.0.1:8080 check')


def test_haproxy_is_installed(host):
    haproxy = host.package("haproxy")
    assert haproxy.is_installed


def test_haproxy_is_on_good_version(host):
    haproxy = host.package("haproxy")
    assert haproxy.version.startswith("1.4")


def test_server_is_started(host):
    haproxy = host.service("haproxy")
    assert haproxy.is_running


def test_server_is_enabled(host):
    haproxy = host.service("haproxy")
    assert haproxy.is_enabled
