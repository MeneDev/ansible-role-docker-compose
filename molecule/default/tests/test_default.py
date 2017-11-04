import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    version_stdout = host.check_output('docker-compose version')
    assert "docker-compose version %s, build" % (
        os.environ['DOCKER_COMPOSE_VERSION']) in version_stdout
