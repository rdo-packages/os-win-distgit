# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-win
%global pyname os_win

%global with_doc 1

%global common_desc \
This library contains Windows / Hyper-V code commonly used in the OpenStack \
projects: nova, cinder, networking-hyperv. The library can be used in any \
other OpenStack projects where it is needed.

Name:           python-%{pypi_name}
Version:        4.3.2
Release:        1%{?dist}
Summary:        Windows / Hyper-V library for OpenStack projects

License:        ASL 2.0
URL:            http://www.cloudbase.it/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: git
BuildRequires: openstack-macros

%description
%{common_desc}

%package -n python%{pyver}-%{pypi_name}
Summary:        Windows / Hyper-V library for OpenStack projects
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}

Requires: python%{pyver}-pbr >= 2.0.0
Requires: python%{pyver}-babel >= 2.3.4
Requires: python%{pyver}-eventlet >= 0.18.2
Requires: python%{pyver}-oslo-concurrency >= 3.26.0
Requires: python%{pyver}-oslo-config >= 2:5.2.0
Requires: python%{pyver}-oslo-log >= 3.36.0
Requires: python%{pyver}-oslo-utils >= 3.33.0
Requires: python%{pyver}-oslo-i18n >= 3.15.3

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr

BuildRequires:  python%{pyver}-eventlet >= 0.18.2

%description -n python%{pyver}-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Windows / Hyper-V library for OpenStack projects - documentation
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-oslo-config
BuildRequires:  python%{pyver}-sphinx

%description -n python-%{pypi_name}-doc
Documentation for the Windows / Hyper-V library for OpenStack projects
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
%py_req_cleanup

%build
%{pyver_build}

%if 0%{?with_doc}
# generate html docs
%{pyver_bin} setup.py build_sphinx -b html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyver_install}

%files -n python%{pyver}-%{pypi_name}
%doc doc/source/readme.rst README.rst
%license LICENSE
%{pyver_sitelib}/%{pyname}*

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Fri Sep 20 2019 RDO <dev@lists.rdoproject.org> 4.3.2-1
- Update to 4.3.2

