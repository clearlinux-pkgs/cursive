#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cursive
Version  : 0.2.2
Release  : 15
URL      : https://files.pythonhosted.org/packages/aa/ec/d0e802482530a0b664c910c845cada1e490bc2af568acc0c1ed55c000502/cursive-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/ec/d0e802482530a0b664c910c845cada1e490bc2af568acc0c1ed55c000502/cursive-0.2.2.tar.gz
Summary  : Cursive implements OpenStack-specific validation of digital signatures.
Group    : Development/Tools
License  : Apache-2.0
Requires: cursive-license = %{version}-%{release}
Requires: cursive-python = %{version}-%{release}
Requires: cursive-python3 = %{version}-%{release}
Requires: castellan
Requires: cryptography
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : castellan
BuildRequires : pbr

%description
cursive
        ===============================
        
        Cursive implements OpenStack-specific validation of digital signatures.
        
        As OpenStack continues to mature, robust security controls become increasingly
        critical. The cursive project contains code extracted from various OpenStack
        projects for verifying digital signatures. Additional capabilities will be
        added to this project in support of various security features.

%package license
Summary: license components for the cursive package.
Group: Default

%description license
license components for the cursive package.


%package python
Summary: python components for the cursive package.
Group: Default
Requires: cursive-python3 = %{version}-%{release}

%description python
python components for the cursive package.


%package python3
Summary: python3 components for the cursive package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cursive package.


%prep
%setup -q -n cursive-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546124079
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cursive
cp LICENSE %{buildroot}/usr/share/package-licenses/cursive/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cursive/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
