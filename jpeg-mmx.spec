# TODO: cleanups, desc, summary, source (?)
Summary:	jpeg mmx
Summary(pl):	jpeg mmx
Name:		jpeg-mmx
Version:	0.1.4
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/mjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	2bd0ab82e1a87e5c0499ceef0f352759
Patch0:		%{name}-DESTDIR.patch
URL:		http://mjpeg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q 
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_libdir},%{_mandir}/man1/}

%{__make} install_real install-prog DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README usage.doc wizard.doc change.log libjpeg.doc example.c structure.doc filelist.doc coderules.doc
%{_includedir}
%attr(755,root,root)%{_bindir}
%{_libdir}
%{_mandir}/man1/
