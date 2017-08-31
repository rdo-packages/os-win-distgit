%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-win
%global pyname os_win

# There are some dependency packages without a python3 build
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Windows / Hyper-V library for OpenStack projects

License:        ASL 2.0
URL:            http://www.cloudbase.it/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 

%description
This library contains Windows / Hyper-V code commonly used in the OpenStack
projects: nova, cinder, networking-hyperv. The library can be used in any
other OpenStack projects where it is needed.

%package -n python2-%{pypi_name}
Summary:        Windows / Hyper-V library for OpenStack projects
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires: openstack-macros
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
BuildRequires:  python-oslo-sphinx

%description -n python2-%{pypi_name}
This library contains Windows / Hyper-V code commonly used in the OpenStack
projects: nova, cinder, networking-hyperv. The library can be used in any
other OpenStack projects where it is needed.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Windows / Hyper-V library for OpenStack projects
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires: openstack-macros
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
BuildRequires:  python3-oslo-sphinx

%description -n python3-%{pypi_name}
This library contains Windows / Hyper-V code commonly used in the OpenStack
projects: nova, cinder, networking-hyperv. The library can be used in any
other OpenStack projects where it is needed.
%endif

%package -n python-%{pypi_name}-doc
Summary:        Windows / Hyper-V library for OpenStack projects - documentation

%description -n python-%{pypi_name}-doc
Documentation for the Windows / Hyper-V library for OpenStack projects

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# let RPM handle deps
%py_req_cleanup

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


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
%doc html
%license LICENSE

%changelog
* Wed Aug 16 2017 Alfredo Moralejo <amoralej@redhat.com> 2.2.0-1
- Update to 2.2.0

