menedev.docker-compose
=========

Installs binary distribution of docker-compose from GitHub releases. 

Requirements
------------

Docker is required and not installed by this role.

Role Variables
--------------

docker_compose_version: "latest" or version string (i.e. "1.17.0-rc1")

(other)
docker_compose_checksum: checksum of the binary, is set automatically
docker_compose_latest: contains latest docker-compose version string
docker_compose_checksums: contains the checksums of all binary docker-compose releases. First key is OS, second version.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: menedev.docker-compose, docker_compose_version: "1.17.0-rc1" }

License
-------

CC-BY

Author Information
------------------

You can contact/follow me at https://twitter.com/MeneDev
