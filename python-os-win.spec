%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-win
%global pyname os_win

# There are some dependency packages without a python3 build
%if 0%{?fedora}
%global with_python3 1
%endif

%global common_desc \
This library contains Windows / Hyper-V code commonly used in the OpenStack \
projects: nova, cinder, networking-hyperv. The library can be used in any \
other OpenStack projects where it is needed.

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Windows / Hyper-V library for OpenStack projects

License:        ASL 2.0
URL:            http://www.cloudbase.it/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: git
BuildRequires: openstack-macros

%description
%{common_desc}

%package -n python2-%{pypi_name}
Summary:        Windows / Hyper-V library for OpenStack projects
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires: python-pbr >= 2.0.0
Requires: python-babel >= 2.3.4
Requires: python-eventlet >= 0.18.2
Requires: python-oslo-concurrency >= 3.8.0
Requires: python-oslo-config >= 2:4.0.0
Requires: python-oslo-log >= 3.22.0
Requires: python-oslo-utils >= 3.20.0
Requires: python-oslo-i18n >= 2.1.0

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
# FIXME(jpena): remove once a version with https://review.openstack.org/518951
# is released
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-eventlet >= 0.18.2

%description -n python2-%{pypi_name}
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Windows / Hyper-V library for OpenStack projects
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires: python3-pbr >= 2.0.0
Requires: python3-babel >= 2.3.4
Requires: python3-eventlet >= 0.18.2
Requires: python3-oslo-concurrency >= 3.8.0
Requires: python3-oslo-config >= 2:4.0.0
Requires: python3-oslo-log >= 3.22.0
Requires: python3-oslo-utils >= 3.20.0
Requires: python3-oslo-i18n >= 2.1.0

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
# FIXME(jpena): remove once a version with https://review.openstack.org/518951
# is released
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-eventlet >= 0.18.2

%description -n python3-%{pypi_name}
%{common_desc}
%endif

%package -n python-%{pypi_name}-doc
Summary:        Windows / Hyper-V library for OpenStack projects - documentation
BuildRequires: python-openstackdocstheme
BuildRequires: python-oslo-config


%description -n python-%{pypi_name}-doc
Documentation for the Windows / Hyper-V library for OpenStack projects

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
%py_req_cleanup

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{pypi_name}
%doc doc/source/readme.rst README.rst
%license LICENSE
%{python2_sitelib}/%{pyname}*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc doc/source/readme.rst README.rst
%{python3_sitelib}/%{pyname}*
%endif

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%changelog
