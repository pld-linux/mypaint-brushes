Summary:	Brushes to be used with the MyPaint library
Summary(pl.UTF-8):	Pędzle do używania z biblioteką MyPaint
Name:		mypaint-brushes
Version:	1.3.0
Release:	1
# According to Licenses.dep5 the files used for building/installing are GPLv2+
# but the shipped brush files are CC0
License:	CC0 v1.0
Group:		Applications/Graphics
Source0:	https://github.com/mypaint/mypaint-brushes/archive/v%{version}.tar.gz
# Source0-md5:	679190d88f67a94db57ac99017f966f5
URL:		https://github.com/mypaint/mypaint-brushes
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains brush files for use with MyPaint and other
programs.

%description -l pl.UTF-8
Ten pakiet zawiera pliki pędzli przeznaczone do używania z programem
MyPaint i innymi.

%package devel
Summary:	Files for developing with mypaint-brushes
Summary(pl.UTF-8):	Pliki do rozwijania oprogramowania korzystającego z mypaint-brushes
Group:		Development/Libraries

%description devel
This package contains a pkgconfig file which makes it easier to
develop programs using MyPaint brush files.

%description devel -l pl.UTF-8
Ten pakiet zawiera plik pkgconfig, ułatwiający tworzenie
oprogramowania wykorzystującego pliki pędzli MyPaint.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING Licenses.dep5 Licenses.md NEWS README.md
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/1.0
%{_datadir}/mypaint-data/1.0/brushes

%files devel
%defattr(644,root,root,755)
%doc COPYING Licenses.dep5 Licenses.md
%{_npkgconfigdir}/mypaint-brushes-1.0.pc
