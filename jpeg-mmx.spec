Summary:	libjpeg library with MMX support
Summary(pl.UTF-8):   Biblioteka libjpeg z obsługą MMX
Name:		jpeg-mmx
Version:	0.1.6
Release:	0.1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	9156c429bd8c4dea65c877c50ed89e15
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-PIC.patch
Patch2:		%{name}-gcc41.patch
# XXX: replace it with real x86_64 port or drop
#Patch1: %{name}-x8664.patch
URL:		http://mjpeg.sourceforge.net/
BuildRequires:	gcc >= 5:3.0
BuildRequires:	nasm
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/include/jpeg-mmx

%description
jpeg-mmx is a modified version of IJG libjpeg library that can use MMX
extension of x86 processors (if available).

%description -l pl.UTF-8
jpeg-mmx to zmodyfikowana wersja biblioteki IJG libjpeg potrafiąca
używać rozszerzenia MMX procesorów x86 (jeśli jest dostępne).

%package libs
Summary:	Shared jpeg-mmx library
Summary(pl.UTF-8):   Biblioteka współdzielona jpeg-mmx
Group:		Libraries

%description libs
Shared jpeg-mmx library.

%description libs -l pl.UTF-8
Biblioteka współdzielona jpeg-mmx.

%package devel
Summary:	Headers for developing programs using jpeg-mmx library
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia programów z użyciem biblioteki jpeg-mmx
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
The jpeg-mmx-devel package includes the header files necessary for
developing programs which will manipulate JPEG files using the
jpeg-mmx library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów
obrabiających pliki JPEG przy użyciu biblioteki jpeg-mmx.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%configure \
	--enable-shared \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install_real install-prog \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README usage.doc wizard.doc change.log libjpeg.doc example.c structure.doc filelist.doc coderules.doc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjpeg-mmx.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjpeg-mmx.so
%{_libdir}/libjpeg-mmx.la
%{_includedir}
