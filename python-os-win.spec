%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-win
%global pyname os_win

%global with_doc 1

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires: git-core
BuildRequires: openstack-macros

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        Windows / Hyper-V library for OpenStack projects
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires: python3-pbr >= 2.0.0
Requires: python3-eventlet >= 0.22.0
Requires: python3-oslo-concurrency >= 3.29.0
Requires: python3-oslo-config >= 2:6.8.0
Requires: python3-oslo-log >= 3.36.0
Requires: python3-oslo-utils >= 4.7.0
Requires: python3-oslo-i18n >= 3.15.3

BuildRequires:  python3-devel
BuildRequires:  python3-pbr

BuildRequires:  python3-eventlet >= 0.18.2

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Windows / Hyper-V library for OpenStack projects - documentation
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslo-config
BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for the Windows / Hyper-V library for OpenStack projects
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
%py_req_cleanup

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{pypi_name}
%doc doc/source/readme.rst README.rst
%license LICENSE
%{python3_sitelib}/%{pyname}*

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
