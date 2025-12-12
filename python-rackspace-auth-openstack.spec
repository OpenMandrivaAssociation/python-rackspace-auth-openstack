Name:		python-rackspace-auth-openstack
Version:	1.3
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/rackspace-auth-openstack/rackspace-auth-openstack-%{version}.tar.gz
Summary:	Rackspace Auth Plugin for OpenStack Clients.
URL:		https://pypi.org/project/rackspace-auth-openstack/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Rackspace Auth Plugin for OpenStack Clients.

%files
%{py_sitedir}/rackspace_auth_openstack
%{py_sitedir}/rackspace_auth_openstack-*.*-info
