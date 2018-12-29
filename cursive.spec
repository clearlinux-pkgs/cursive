#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cursive
Version  : 0.2.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/aa/ec/d0e802482530a0b664c910c845cada1e490bc2af568acc0c1ed55c000502/cursive-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/ec/d0e802482530a0b664c910c845cada1e490bc2af568acc0c1ed55c000502/cursive-0.2.2.tar.gz
Summary  : Cursive implements OpenStack-specific validation of digital signatures.
Group    : Development/Tools
License  : Apache-2.0
Requires: cursive-python3
Requires: cursive-license
Requires: cursive-python
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
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

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
Requires: cursive-python3

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
export SOURCE_DATE_EPOCH=1533820133
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cursive
cp LICENSE %{buildroot}/usr/share/doc/cursive/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/cursive/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
