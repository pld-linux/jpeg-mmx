# TODO
# - -progs subpackage?
# - shared library?
Summary:	libjpeg library with MMX support
Summary(pl):	Biblioteka libjpeg z obs³ug± MMX
Name:		jpeg-mmx
Version:	1.1.6
Release:	0.2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mjpeg/%{name}-0.1.6.tar.gz
# Source0-md5:	9156c429bd8c4dea65c877c50ed89e15
Patch0:		%{name}-DESTDIR.patch
# XXX: replace it with real x86_64 port or drop
#Patch1:		%{name}-x8664.patch
URL:		http://mjpeg.sourceforge.net/
BuildRequires:	gcc >= 3.0
BuildRequires:	nasm
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jpeg-mmx is a modified version of IJG libjpeg library that can use
MMX extension of x86 processors (if available).

%description -l pl
jpeg-mmx to zmodyfikowana wersja biblioteki IJG libjpeg potrafi±ca
u¿ywaæ rozszerzenia MMX procesorów x86 (je¶li jest dostêpne).

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install-prog install_real \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README usage.doc wizard.doc change.log libjpeg.doc example.c structure.doc filelist.doc coderules.doc
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libjpeg-mmx.a
%{_includedir}/*.h
%{_mandir}/man1/*
