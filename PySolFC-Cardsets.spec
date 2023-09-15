Summary:	Various cardsets for PySolFC
Name:		PySolFC-Cardsets
Version:	2.2
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/pysolfc/%{name}-%{version}.tar.bz2
# Source0-md5:	a44b410e2a3c9939fc03c298aabd8eb6
URL:		http://pysolfc.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	PySolFC
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains extras cardsets for PySolFC.

%prep
%setup -q

# Remove cardsets included in PySolFC package
%{__rm} -r cardset-2000 \
	cardset-crystal-mahjongg \
	cardset-dashavatara-ganjifa \
	cardset-dashavatara-ganjifa-xl \
	cardset-dondorf \
	cardset-gnome-mahjongg-1 \
	cardset-hanafuda-200-years \
	cardset-hexadeck \
	cardset-louie-mantia-hanafuda \
	cardset-matching \
	cardset-matching-xl \
	cardset-matrix \
	cardset-mughal-ganjifa \
	cardset-mughal-ganjifa-xl \
	cardset-neo \
	cardset-neo-hex \
	cardset-neo-tarock \
	cardset-next-matrix \
	cardset-oxymoron \
	cardset-standard \
	cardset-tuxedo \
	cardset-uni-mahjongg \
	cardset-vienna-2k

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/PySolFC/

cp -a cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/PySolFC/cardset-*
