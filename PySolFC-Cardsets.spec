Summary:	Various cardsets for PySolFC
Name:		PySolFC-Cardsets
Version:	3.0
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/pysolfc/%{name}-%{version}.tar.bz2
# Source0-md5:	a9ac0984c127fc88e7d94d014ff1c6a3
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
	cardset-blaren-7x7 \
	cardset-crystal-mahjongg \
	cardset-dashavatara-ganjifa \
	cardset-dashavatara-ganjifa-xl \
	cardset-dojouji-3x3 \
	cardset-dondorf \
	cardset-gnome-mahjongg-1 \
	cardset-hanafuda-200-years \
	cardset-hexadeck \
	cardset-hokusai-6x6 \
	cardset-knave-of-hearts-4x4 \
	cardset-louie-mantia-hanafuda \
	cardset-matching \
	cardset-matching-xl \
	cardset-matrix \
	cardset-mid-winter-eve-8x8 \
	cardset-mughal-ganjifa \
	cardset-mughal-ganjifa-xl \
	cardset-neo \
	cardset-neo-hex \
	cardset-neo-tarock \
	cardset-next-matrix \
	cardset-oxymoron \
	cardset-players-trumps-10x10 \
	cardset-simple-ishido \
	cardset-simple-ishido-xl \
	cardset-standard \
	cardset-the-card-players-9x9 \
	cardset-tuxedo \
	cardset-uni-mahjongg \
	cardset-victoria-falls-5x5 \
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
