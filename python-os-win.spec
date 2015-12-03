%global pypi_name os-win
%global pyname os_win

# There are some dependency packages without a python3 build
%if 0%{?fedora}
%global with_python3 0
%endif

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Windows / Hyper-V library for OpenStack projects

License:        ASL 2.0
URL:            http://www.cloudbase.it/
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 


%description
This library contains Windows / Hyper-V code commonly used in the OpenStack
projects: nova, cinder, networking-hyperv. The library can be used in any
other OpenStack projects where it is needed.

%package -n python2-%{pypi_name}
Summary:        Windows / Hyper-V library for OpenStack projects
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires: python-oslo-concurrency >= 2.3.0
Requires: python-oslo-config >= 2.3.0
Requires: python-oslo-log >= 1.8.0
Requires: python-oslo-utils >= 2.0.0
Requires: python-oslo-i18n >= 1.5.0
Requires: python-oslo-service >= 0.7.0

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

Requires: python3-oslo-concurrency >= 2.3.0
Requires: python3-oslo-config >= 2.3.0
Requires: python3-oslo-log >= 1.8.0
Requires: python3-oslo-utils >= 2.0.0
Requires: python3-oslo-i18n >= 1.5.0
Requires: python3-oslo-service >= 0.7.0

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
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python-%{pypi_name}-doc
Documentation for the Windows / Hyper-V library for OpenStack projects

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

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
