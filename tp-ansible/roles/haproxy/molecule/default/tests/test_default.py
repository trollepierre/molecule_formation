import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_haproxy_config_file(host):
    f = host.file('/etc/haproxy/haproxy.cfg')

    assert f.exists
    assert f.contains('server  vm_tango_02  127.0.0.1:8080 check')
