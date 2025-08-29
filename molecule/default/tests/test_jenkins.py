def test_java_installed(host):
    java = host.package("java-11-amazon-corretto")
    assert java.is_installed

def test_jenkins_package(host):
    jenkins = host.package("jenkins")
    assert jenkins.is_installed

def test_jenkins_service(host):
    jenkins = host.service("jenkins")
    assert jenkins.is_enabled
    assert jenkins.is_running

def test_jenkins_port(host):
    socket = host.socket("tcp://0.0.0.0:8080")
    assert socket.is_listening
