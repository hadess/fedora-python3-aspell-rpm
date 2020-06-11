%global pypi_name aspell-python-py3

Name:           python-aspell
Version:        1.15
Release:        1%{?dist}
Summary:        Wrapper around GNU Aspell for Python 3

License:        BSD (3 clauses)
URL:            http://github.com/WojciechMula/aspell-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.bz2

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  gcc
BuildRequires:  aspell-devel

%description
aspell-python - C extension for Python 3

%package -n     python3-aspell
Summary:        %{summary}
%{?python_provide:%python_provide python3-aspell}

%description -n python3-aspell
aspell-python - C extension for Python 3

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-aspell
%doc README.rst
%{python3_sitearch}/aspell_python_py3-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/aspell.*.so

%changelog
* Thu Jun 11 2020 hadess <bnocera@redhat.com> - 1.15-1
- Initial package.
